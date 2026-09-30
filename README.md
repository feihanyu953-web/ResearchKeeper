# ResearchKeeper

**File-first academic knowledge management with reproducible semantic retrieval.**
（文件优先的学术知识管理 + 可复现语义检索）

ResearchKeeper 是一个 **Python 3.11 工具 + Claude Code 插件**，用于构建「**可审计的论文知识库**」：在显式工作区实例化经批准的 schema，每条论文记录都可溯源到源证据，并可建立本地 bge-m3 向量索引做语义检索。

## 核心理念

- **七角色 schema**：知识按 `literature / entities / methods / conditions / results / relations / claims` 七个角色组织，每个模块声明 file/role/trigger_keywords/extract_rules/audit_focus
- **覆盖度审计语义**：每篇论文对每个活跃模块显式声明 `covered` / `not_applicable`（需理由 + 可检验的原文/SI 证据）/ `missing`，由独立审查员验证——不允许"看起来写完了"
- **fail-closed**：schema 提案经 JSON Schema 校验 + 冲突检测；字节相同的提案仅对同一空 KB 幂等；含真实记录的 KB 拒绝重复提案
- **独立审计**：kb / vector / computer-kb 三类审计由独立 agent 执行（事实型 prompt 模板），主 AI 无法注入覆盖率预测，审计结果生成 receipt
- **Provider Protocol v1**：`rsk provider query`（只读）与 `write-candidate`（shadow 副本干跑）都不授予写权限——写记录永远需要用户显式批准

## 功能模块

**7 个 skills**

| Skill | 用途 |
|---|---|
| `/researchkeeper:setup` | 初始化：Python/依赖检查 → 选工作区 → 配 schema → 初始化 Compute KB → 模型下载（需单独同意） |
| `researchkeeper` | 主 skill：论文阅读、知识检索、kb/wiki 维护、向量搜索、VASP/LAMMPS 计算知识路由 |
| `/researchkeeper:configure-schema` | 空 KB 的七角色 schema 配置流程（提案 → 验证 → 预览 → 显式批准） |
| `audit-all` | 全流程审计（kb/wiki gate + vector gate）并生成 receipt |
| `post-kb-audit` / `post-vector-audit` / `post-computer-kb-audit` | 分层审计（对应 kb 修改、向量同步、计算知识库修改后触发） |

**3 个独立审计 agents**：kb-independent-reviewer · vector-retrieval-auditor · computer-kb-independent-reviewer

**`rsk` CLI**：`cli / config / doctor / schema / kb / wiki / vector / provider / workflow / zotero / experiment / parser / setup / install_state`

## 内置模板

- `generic-science` — 通用科学论文
- `electrocatalysis` — 电催化领域（含 claims/conditions/results 等模块的领域定制）
- 自定义模板通过 `configure-schema` 流程提案（`schemas/schema-proposal.schema.json`）

## 安装

```powershell
claude plugin marketplace add "<本地路径>\ResearchKeeper-v0.2.0-local-marketplace-cb62811"
claude plugin install researchkeeper@researchkeeper-local --scope user
```

然后在工作区目录运行 `/researchkeeper:setup`。也可以不用插件、直接安装 Python CLI 入口（`rsk setup`）。**完整安装/配置说明见 [README-安装使用.md](README-安装使用.md)。**

## 系统要求

| 项目 | 要求 |
|---|---|
| Claude Code | 插件宿主 |
| Python | **3.11.x**（`>=3.11,<3.12`） |
| 向量模型 | bge-m3，约 **2.2 GB**（存平台级用户缓存，首次下载需单独同意） |
| 计算 | CPU 为默认且完整支持；CUDA 仅在用户明确选择后使用 |
| 依赖 | 首次初始化可联网安装锁定依赖（`requirements.lock` / `requirements.cuda.lock`），venv 与激活态在 `${CLAUDE_PLUGIN_DATA}` |

## 验证环境

v0.2.0（正式提交 `cb62811a0325c1846643f1024939f7afb308bbb8`，196 文件 / ~2.99 MB，sha256 见 `DELIVERY-METADATA.json`）；已在 Claude Code 2.1.220 + Python 3.11.9 上通过 marketplace / plugin / CLI / bootstrap / 计算初始化全套验证。

**发布范围**：框架 + 论文工作流材料 + generic-science 与 electrocatalysis 模板 + 基础 VASP/LAMMPS 计算参考资料。**不含**用户知识库数据、向量索引、模型缓存与私有集群材料。

## 文档地图

| 文档 | 内容 |
|---|---|
| [README-安装使用.md](README-安装使用.md) | 交付说明：安装、初始化、配置（中文） |
| [plugins/researchkeeper/README.md](plugins/researchkeeper/README.md)（[中文版](plugins/researchkeeper/README_CN.md)） | 插件主文档 |
| `plugins/researchkeeper/docs/` | architecture · getting-started · installation · customization · schema-customization · provider-protocol · contributing |
| [plugins/researchkeeper/skills/researchkeeper/references/RSK-DETAILED-GUIDE.md](plugins/researchkeeper/skills/researchkeeper/references/RSK-DETAILED-GUIDE.md) | 主 skill 的完整使用指南（检索流程、入库流程、执行顺序） |

## License

- 代码：MIT
- 原创知识与解释性内容：CC BY 4.0（见 [plugins/researchkeeper/CONTENT_LICENSE](plugins/researchkeeper/CONTENT_LICENSE)）
- 第三方依赖：[THIRD_PARTY_NOTICES.md](plugins/researchkeeper/THIRD_PARTY_NOTICES.md)
