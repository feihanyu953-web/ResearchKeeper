# -*- coding: utf-8 -*-
"""从子 agent JSONL transcript 提取 schema_candidates YAML → JSON。

用法:
  # 从会话 subagents 目录提取（默认路径，自动检测最新会话）
  python scripts/litmind/extract_agent_yaml.py --session-dir <path/to/subagents/>

  # 从单个 agent JSONL 文件提取
  python scripts/litmind/extract_agent_yaml.py --agent-file <path/to/agent.jsonl>

  # 指定输出目录（默认 tmp/extracted/）
  python scripts/litmind/extract_agent_yaml.py --session-dir <path> --output-dir tmp/extracted/

  # 仅提取指定 paper_id（用于单篇补全）
  python scripts/litmind/extract_agent_yaml.py --session-dir <path> --filter Elena2025 Xu2021

入口文件: LITMIND.md §入库流程 → 主 AI 质量门禁 → 分批写入

关键设计决策（修改前必读）:
  - 必须用 raw_line（保留缩进）做正则匹配，不能用 line.strip()。
    YAML 行格式为 "      field_name: value"，strip 后丢失前导空格导致 ^\\s+ 失败。
    这是 v3→v5 的核心 bug 修复。
  - 续行处理: 缩进 > 8 空格且未匹配到已知字段的行视为上一字段的续行，追加到其值末尾。
  - 输出 JSON 中 record_id 固定为 "TBD-by-main"，由 batch_write_kb.py 自动分配。
"""

import argparse, json, os, re, sys, io
from pathlib import Path

import yaml

from rsk.config import PROJECT_ROOT

ALL_FIELDS = ['category', 'subject', 'metric', 'value', 'unit',
              'condition', 'source', 'confidence', 'note']
_REQUIRED_RECORD_FIELDS = ("category", "subject", "metric", "value", "source")
_PLACEHOLDERS = {"...", "…"}
_JSON_FENCE = re.compile(r"```json[ \t]*\r?\n(.*?)\r?\n```", re.DOTALL | re.IGNORECASE)


class TranscriptParseError(ValueError):
    """Raised when an explicit transcript format cannot be parsed safely."""


# ── 核心解析器 ────────────────────────────────────────────────────────

def parse_records(
    yaml_text,
    paper_id,
    *,
    module_names,
    literature_module,
):
    """从单篇论文的 YAML 片段中提取 schema_candidates 记录列表。

    参数:
      yaml_text: 从 paper_id 行到下一个 paper_id（或文末）的原始 YAML 文本。
      paper_id: 论文标识符（如 'Elena2025'）。

    返回:
      list[dict]: 每条记录包含 module 字段和 ALL_FIELDS 中的部分字段。
    """
    modules = set(module_names)
    records = []
    current_module = literature_module
    current_record = None
    in_schema = False
    last_field = None

    for raw_line in yaml_text.split('\n'):
        s = raw_line.strip()
        if not s:
            continue

        # 进入 schema_candidates 块
        if s.startswith('schema_candidates:'):
            in_schema = True
            continue

        if not in_schema:
            continue

        # 退出: 遇到非模块名的顶层 key（如 missing_data_evidence, wiki_sync_candidates）
        if not raw_line.startswith(' ') and not raw_line.startswith('-') and ':' in s:
            key = s.split(':')[0].strip()
            if key not in modules:
                if key in ('missing_data_evidence', 'wiki_sync_candidates',
                           'risk_flags', 'concepts_to_update',
                           'concepts_to_create', 'paper_stub_needed'):
                    in_schema = False
                    if current_record:
                        records.append(current_record)
                        current_record = None
                    continue

        # 活动 concrete module 头（例如 "  observations:"）
        module_candidate = s.split(':', 1)[0].strip()
        if (
            s.endswith(':')
            and module_candidate in modules
            and re.fullmatch(r'[a-z][a-z0-9_-]*', module_candidate)
        ):
            current_module = module_candidate
            continue

        # 记录起始
        if '- record_id:' in s:
            if current_record:
                records.append(current_record)
            current_record = {'module': current_module}
            last_field = None
            continue

        if not current_record:
            continue

        # 字段匹配 —— 关键: 用 raw_line（保留缩进）匹配 ^\s+field:
        matched = False
        for field in ALL_FIELDS:
            m = re.match(rf'^\s+{field}:\s*(.+?)\s*$', raw_line)
            if m:
                val = m.group(1).rstrip()
                # 去掉两侧成对引号
                if (val.startswith('"') and val.endswith('"')) or \
                   (val.startswith("'") and val.endswith("'")):
                    val = val[1:-1]
                current_record[field] = val
                last_field = field
                matched = True
                break

        # 未匹配且缩进更深 → 上一字段的续行
        if not matched and last_field and raw_line.startswith('        '):
            extra = s.strip('"').strip("'")
            prev = current_record.get(last_field, '')
            current_record[last_field] = prev + ' ' + extra

    if current_record:
        records.append(current_record)
    return records


# ── Agent JSONL 处理 ───────────────────────────────────────────────────

def extract_yaml_blocks_from_jsonl(fpath):
    """读取 agent JSONL 文件，提取所有 assistant 消息中的 ```yaml``` 块。

    返回:
      list[str]: 每个元素为一个完整的 YAML 块（可能含多篇论文，以 --- 分隔）。
    """
    all_text = []
    with open(fpath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                msg = json.loads(line)
            except json.JSONDecodeError:
                continue
            if msg.get('type') != 'assistant':
                continue
            content = msg.get('message', {}).get('content', [])
            if isinstance(content, str):
                all_text.append(content)
            elif isinstance(content, list):
                for block in content:
                    if isinstance(block, dict) and block.get('type') == 'text':
                        all_text.append(block.get('text', ''))

    combined = '\n'.join(all_text)
    return re.findall(r'```yaml\n(.*?)```', combined, re.DOTALL)


def split_by_paper(block):
    """将一个 YAML 块按 paper_id 拆分，返回 {paper_id: sub_yaml_text}。

    支持单块内含多篇论文（以 --- 或相邻 paper_id 行为界）。
    """
    pids_raw = re.findall(r'paper_id:\s*["\']?(\w+)', block)
    pids = list(dict.fromkeys(pids_raw))  # dedup, preserve order
    result = {}

    for pid in pids:
        # 定位此 paper_id 的位置
        pos = None
        for pattern in [f'paper_id: "{pid}"', f"paper_id: '{pid}'",
                        f'paper_id: {pid}']:
            pos = block.find(pattern)
            if pos != -1:
                break
        if pos is None:
            continue

        # 找下一个 paper_id 或 --- 分隔符
        next_pos = float('inf')
        for other in pids:
            if other == pid:
                continue
            for pattern in [f'paper_id: "{other}"', f"paper_id: '{other}'",
                            f'paper_id: {other}']:
                p = block.find(pattern, pos + 20)
                if p != -1 and p < next_pos:
                    next_pos = p

        sep = block.find('\n---\n', pos + 20)
        if sep != -1 and sep < next_pos:
            next_pos = sep

        sub = block[pos:next_pos] if next_pos != float('inf') else block[pos:]
        result[pid] = sub

    return result


def records_to_json_entries(records, paper_id):
    """将 parse_records 输出转为 batch_write_kb.py 兼容的 JSON 记录列表。

    确保 13 个 schema_v1 字段齐全，缺失的用默认值填充。
    """
    clean = []
    for r in records:
        entry = {
            'record_id': 'TBD-by-main',
            'schema_version': 'schema_v1',
            'paper_id': paper_id,
            'module': r.get('module', 'literature'),
            'category': r.get('category', ''),
            'subject': r.get('subject', ''),
            'metric': r.get('metric', ''),
            'value': r.get('value', ''),
            'unit': r.get('unit', '无'),
            'condition': r.get('condition', ''),
            'source': r.get('source', f'[{paper_id}]'),
            'confidence': r.get('confidence', 'single_source'),
            'note': r.get('note', ''),
        }
        clean.append(entry)
    return clean


def parse_module_coverage(yaml_text):
    """Extract structured coverage without inventing missing evidence."""
    try:
        payload = yaml.safe_load(yaml_text) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid agent YAML: {exc}") from exc
    coverage = payload.get("module_coverage")
    if not isinstance(coverage, dict):
        raise ValueError("agent YAML requires structured module_coverage")
    return coverage


def records_to_ingest_envelope(records, paper_id, module_coverage):
    candidates = {}
    for entry in records_to_json_entries(records, paper_id):
        candidates.setdefault(entry["module"], []).append(entry)
    return {
        "paper_id": paper_id,
        "schema_candidates": candidates,
        "module_coverage": module_coverage,
    }


def _normalize_envelope_payload(
    payload,
    *,
    module_names,
    literature_module,
    expected_paper_id=None,
):
    if not isinstance(payload, dict):
        raise TranscriptParseError("paper envelope must be an object")
    paper_id = str(payload.get("paper_id", "")).strip()
    if not paper_id:
        raise TranscriptParseError("paper envelope requires paper_id")
    if expected_paper_id is not None and paper_id != expected_paper_id:
        raise TranscriptParseError(
            f"paper_id mismatch: expected {expected_paper_id}, got {paper_id}"
        )
    modules = tuple(str(item) for item in module_names)
    if literature_module not in modules:
        raise TranscriptParseError(
            "literature_module must be one of the active modules"
        )

    bibliography = payload.get("bibliography", {})
    if not isinstance(bibliography, dict):
        raise TranscriptParseError("bibliography must be an object")
    raw_candidates = payload.get("schema_candidates")
    raw_records = payload.get("records")
    records = []
    if raw_candidates is not None:
        if not isinstance(raw_candidates, dict):
            raise TranscriptParseError("schema_candidates must be an object")
        for module, items in raw_candidates.items():
            if module not in modules:
                raise TranscriptParseError(
                    f"unknown active module {module!r}"
                )
            if not isinstance(items, list):
                raise TranscriptParseError(
                    f"schema_candidates.{module} must be a list"
                )
            for raw in items:
                if not isinstance(raw, dict):
                    raise TranscriptParseError(
                        f"schema_candidates.{module} entries must be objects"
                    )
                record = dict(raw)
                record["module"] = module
                records.append(record)
    elif raw_records is not None:
        if not isinstance(raw_records, list):
            raise TranscriptParseError("records must be a list")
        if not all(isinstance(item, dict) for item in raw_records):
            raise TranscriptParseError("record entries must be objects")
        records = [dict(item) for item in raw_records]
    else:
        raise TranscriptParseError(
            "paper envelope requires records or schema_candidates"
        )

    candidates = {}
    for index, raw in enumerate(records):
        module = str(raw.get("module", "")).strip()
        if module not in modules:
            raise TranscriptParseError(
                f"record[{index}] has unknown module {module!r}"
            )
        record_paper_id = str(raw.get("paper_id", paper_id)).strip()
        if record_paper_id != paper_id:
            raise TranscriptParseError(
                f"record[{index}] paper_id does not match envelope"
            )
        record = {
            "record_id": str(
                raw.get("record_id", "TBD-by-main")
            ).strip()
            or "TBD-by-main",
            "schema_version": str(
                raw.get("schema_version", "schema_v1")
            ).strip()
            or "schema_v1",
            "paper_id": paper_id,
            "module": module,
            "category": raw.get("category", ""),
            "subject": raw.get("subject", ""),
            "metric": raw.get("metric", ""),
            "value": raw.get("value", ""),
            "unit": raw.get("unit", "无"),
            "condition": raw.get("condition", ""),
            "source": raw.get("source", ""),
            "confidence": raw.get("confidence", "single_source"),
            "note": raw.get("note", ""),
        }
        for field in _REQUIRED_RECORD_FIELDS:
            value = record[field]
            if value is None or (isinstance(value, str) and not value.strip()):
                raise TranscriptParseError(
                    f"record[{index}] missing required field {field!r}"
                )
            if isinstance(value, str) and value.strip() in _PLACEHOLDERS:
                raise TranscriptParseError(
                    f"record[{index}] contains placeholder field {field!r}"
                )
        candidates.setdefault(module, []).append(record)

    coverage = payload.get("coverage", payload.get("module_coverage"))
    if not isinstance(coverage, dict):
        raise TranscriptParseError(
            "paper envelope requires coverage or module_coverage"
        )
    if set(coverage) != set(modules):
        missing = sorted(set(modules) - set(coverage))
        extra = sorted(set(coverage) - set(modules))
        details = []
        if missing:
            details.append("missing coverage: " + ", ".join(missing))
        if extra:
            details.append("unknown coverage: " + ", ".join(extra))
        raise TranscriptParseError("; ".join(details))
    return {
        "paper_id": paper_id,
        "bibliography": dict(bibliography),
        "schema_candidates": candidates,
        "module_coverage": dict(coverage),
    }


def parse_paper_envelope(
    transcript_text,
    *,
    module_names,
    literature_module,
    expected_paper_id=None,
):
    """Parse one JSON-first paper envelope with YAML compatibility."""
    text = str(transcript_text)
    fenced = _JSON_FENCE.findall(text)
    if re.search(r"```json\b", text, re.IGNORECASE):
        if len(fenced) != 1:
            raise TranscriptParseError(
                "invalid fenced JSON: expected one complete JSON block"
            )
        try:
            payload = json.loads(fenced[0])
        except json.JSONDecodeError as exc:
            raise TranscriptParseError(
                f"invalid fenced JSON: {exc.msg}"
            ) from exc
    elif text.lstrip().startswith("{"):
        try:
            payload = json.loads(text)
        except json.JSONDecodeError as exc:
            raise TranscriptParseError(
                f"invalid bare JSON: {exc.msg}"
            ) from exc
    else:
        try:
            payload = yaml.safe_load(text)
        except yaml.YAMLError as exc:
            raise TranscriptParseError(f"invalid agent YAML: {exc}") from exc
    return _normalize_envelope_payload(
        payload,
        module_names=module_names,
        literature_module=literature_module,
        expected_paper_id=expected_paper_id,
    )


def _message_text(message):
    payload = message.get("message", message)
    if not isinstance(payload, dict):
        return ""
    content = payload.get("content", "")
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    return "\n".join(
        str(item.get("text", ""))
        for item in content
        if isinstance(item, dict) and item.get("type") in (None, "text")
    )


def extract_envelopes_from_jsonl(
    path,
    *,
    module_names,
    literature_module,
):
    """Collect paper envelopes from all assistant messages in a JSONL file."""
    envelopes = []
    seen = set()
    with Path(path).open(encoding="utf-8") as handle:
        messages = []
        for line in handle:
            try:
                messages.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    for message in messages:
        if message.get("type") != "assistant":
            continue
        text = _message_text(message)
        candidates = []
        json_blocks = _JSON_FENCE.findall(text)
        if re.search(r"```json\b", text, re.IGNORECASE):
            if not json_blocks:
                raise TranscriptParseError(
                    "invalid fenced JSON: incomplete JSON block"
                )
            candidates.extend(
                f"```json\n{block}\n```" for block in json_blocks
            )
        else:
            yaml_blocks = re.findall(
                r"```ya?ml[ \t]*\r?\n(.*?)\r?\n```",
                text,
                re.DOTALL | re.IGNORECASE,
            )
            if yaml_blocks:
                for block in yaml_blocks:
                    split = split_by_paper(block)
                    candidates.extend(split.values() or [block])
            elif text.lstrip().startswith("{"):
                candidates.append(text)
            elif (
                "paper_id:" in text
                and (
                    "schema_candidates:" in text
                    or "\nrecords:" in text
                )
                and (
                    "module_coverage:" in text
                    or "\ncoverage:" in text
                )
            ):
                split = split_by_paper(text)
                candidates.extend(split.values() or [text])
        for candidate in candidates:
            envelope = parse_paper_envelope(
                candidate,
                module_names=module_names,
                literature_module=literature_module,
            )
            paper_id = envelope["paper_id"]
            if paper_id in seen:
                raise TranscriptParseError(
                    f"duplicate paper envelope: {paper_id}"
                )
            seen.add(paper_id)
            envelopes.append(envelope)
    return envelopes


# ── 主入口 ─────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(
        description='从子 agent JSONL transcript 提取 schema_v1 记录为 JSON')
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument('--session-dir',
                     help='会话 subagents 目录（包含 agent-*.jsonl 文件）')
    src.add_argument('--agent-file',
                     help='单个 agent JSONL 文件路径')
    p.add_argument('--output-dir', default=str(PROJECT_ROOT / 'tmp' / 'extracted'),
                   help='JSON 输出目录（默认: tmp/extracted/）')
    p.add_argument('--filter', nargs='*',
                   help='仅提取指定 paper_id（空格分隔），省略则提取全部')
    args = p.parse_args()
    from rsk.kb.coverage import active_modules

    configured_modules = active_modules(PROJECT_ROOT)
    module_names = tuple(
        str(module["name"]) for module in configured_modules
    )
    literature_modules = [
        str(module["name"])
        for module in configured_modules
        if str(module.get("role", "")) == "literature"
    ]
    if len(literature_modules) != 1:
        raise ValueError("active schema requires exactly one literature module")
    literature_module = literature_modules[0]

    # 确定源文件列表
    if args.agent_file:
        agent_files = [args.agent_file]
    else:
        agent_dir = args.session_dir
        agent_files = sorted(
            os.path.join(agent_dir, f)
            for f in os.listdir(agent_dir)
            if f.startswith('agent-') and f.endswith('.jsonl')
        )
        if not agent_files:
            print(f"错误: {agent_dir} 中未找到 agent-*.jsonl 文件")
            sys.exit(1)

    filter_set = set(args.filter) if args.filter else None
    os.makedirs(args.output_dir, exist_ok=True)

    total_papers = 0
    total_records = 0

    for agent_fpath in agent_files:
        agent_name = os.path.basename(agent_fpath)
        try:
            envelopes = extract_envelopes_from_jsonl(
                agent_fpath,
                module_names=module_names,
                literature_module=literature_module,
            )
        except (OSError, TranscriptParseError) as exc:
            print(f"FAIL {agent_name}: {exc}")
            continue

        found = 0
        for envelope in envelopes:
            pid = envelope["paper_id"]
            if filter_set and pid not in filter_set:
                continue
            entries = [
                entry
                for items in envelope["schema_candidates"].values()
                for entry in items
            ]

            out_path = os.path.join(args.output_dir, f'{pid}.json')
            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump(envelope, f, ensure_ascii=False, indent=2)

            mods = sorted(set(r['module'] for r in entries))
            lit_ok = any(len(r.get('subject', '')) > 5
                         for r in entries
                         if r['module'] == literature_module)
            print(f'  {pid}: {len(entries)} recs ({",".join(mods)}) '
                  f'lit_ok={lit_ok}')
            found += 1
            total_papers += 1
            total_records += len(entries)

        if found:
            print(f'  ← {agent_name} ({found} papers)')

    print(f'\n{"=" * 50}')
    print(f'Total: {total_papers} papers, {total_records} records')
    print(f'Output: {args.output_dir}')


if __name__ == '__main__':
    main()
