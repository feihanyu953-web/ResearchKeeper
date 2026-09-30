# Paper-Reader Gate Protocol

框架版本：v2.0-manual

## 设计原则

- **AI 不参与审计判定**：AI 只负责入库和同步，不生成 receipt、不比对 hash、不自行判定 PASS
- **用户手动触发审计**：通过 `/audit-all` skill 统一入口
- **三个 gate 独立**：kb/wiki、computer_kb、vector 各自独立判定，receipt 不互相替代

## 入口

`/audit-all` skill（`.claude/skills/audit-all/SKILL.md`）

## 三个 Gate

### kb/wiki gate

- 扫描范围：`kb/**/*.md` + `wiki/**/*.md`
- 排除：`kb/REVIEWER_LOG.md`、`kb/.audit/**`、`kb/INDEX.md`、`kb/SCHEMA.md`、`kb/REVIEWER.md`
- Reviewer：`kb-independent-reviewer`
- Receipt 位置：`kb/.audit/receipts/`
- Receipt schema：`kb_audit_receipt_v1`（含活动 `schema_fingerprint` 与
  coverage 在内的 content tree hash）

### computer_kb gate

- 扫描范围：`computer_kb/**/*.md`
- 排除：`computer_kb/REVIEWER_LOG.md`、`computer_kb/.audit/**`、`computer_kb/INDEX.md`、`computer_kb/REVIEWER.md`
- Reviewer：`computer-kb-independent-reviewer`（审计维度含 wiki 链接完整性检查 `check_wiki_links.py`）
- Receipt 位置：`computer_kb/.audit/receipts/`
- Receipt schema：`computer_kb_audit_receipt_v1`

### vector gate

- 审计层 1：`rsk audit-sync`（确定性校验）
- 审计层 2：`vector-retrieval-auditor` agent（检索质量 fidelity/recall）
- 审计层 2b：`vector-retrieval-auditor` agent（chain claim 覆盖：`chain_test_queries` + `--expand` 多模块验证）
- Reviewer：`vector-retrieval-auditor`
- Receipt 位置：`kb/.audit/receipts/`（与 KB receipt 共用目录）
- Receipt schema：`vector_audit_receipt_v1`（含 `schema_fingerprint` 与
  活动 vector gate hash）
- 日志：`records/vector_audit_log.jsonl`

## Tree Hash 算法

`Get-TreeHashV1`（`.claude/audit/lib/TreeHash.ps1`）：扫描指定路径的文件，按相对路径排序，计算每个文件的 SHA256，拼接后整体 SHA256。

活动 schema 为空 KB 时，只允许 schema gate PASS；content、vector sync 和
retrieval 均为 N/A。审计员必须读取活动 concrete modules，并独立核验每个
`not_applicable` 的理由与证据，不使用固定模块数量或固定 query 数量。
