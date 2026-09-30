# ResearchKeeper (`rsk`)

ResearchKeeper v0.2.0 是面向可审计论文知识库的 Python 3.11 工具和 Claude Code plugin：它在显式 workspace 中物化经批准的 schema，保留记录到原文证据的可追溯性，并可建立本地 bge-m3 向量索引。

[English](README.md) · [安装](docs/installation.md) · [Schema 定制](docs/schema-customization.md) · [Provider Protocol v1](docs/provider-protocol.md)

## 公开范围

公开发行版包含框架、论文工作流资料、generic-science 与 electrocatalysis 模板，以及 VASP/LAMMPS 的基础计算参考资料；**不**包含用户个人 KB、向量、模型缓存、私有集群资料，或项目特定的耦合与机器学习势内容。

## 安装与首次使用

支持两个入口，且均要求 Python **3.11.x**（`>=3.11,<3.12`）。

- **Standalone CLI：** 使用 Python 3.11 安装包，选择显式 workspace，创建/验证七角色 schema proposal，获得 apply 批准后，再单独确认模型下载并运行 `rsk setup`。
- **Claude Code plugin：** 安装 plugin 后调用 `/researchkeeper:setup`。依赖 bootstrap 使用 `${CLAUDE_PLUGIN_DATA}`；空 workspace 的首次 schema 必须调用 `/researchkeeper:configure-schema`。

首次 setup 会下载或复用 BAAI/bge-m3，下载量约 2.2 GB（实际传输量可随主机和 revision 变化）。模型不放在项目 `models/` 目录：standalone 与 plugin runtime 都使用平台的 ResearchKeeper 用户缓存 `models/` 位置；plugin dependency venv 和 active-install state 则位于 `${CLAUDE_PLUGIN_DATA}`。`doctor --json` 会报告实际解析路径。GPU/CUDA 仅为可选加速，CPU 是完整 fallback；检测到 GPU 不等于用户同意使用 GPU，下载也需单独确认。

模型下载为 **Hugging Face 优先 → ModelScope 兜底**（`huggingface.co` 不可达时使用，如大陆无代理环境）。两条路径都固定 immutable commit hash 以保证快照可审计。ModelScope 兜底默认通过 `git ls-remote` **自动解析** master commit hash；仅当解析失败（无 git 或远端不可达）时才会报错，错误信息会给出手动解析指引：

```powershell
git ls-remote https://www.modelscope.cn/BAAI/bge-m3.git HEAD   # → 40 位 hex commit hash
$env:RSK_BGE_MODELSCOPE_REVISION = "<40-hex commit hash>"       # 设置后覆盖自动解析
rsk setup --workspace <ws> --device cpu --non-interactive --yes --json
```

命令和确认边界见[安装说明](docs/installation.md)。旧的 `generic` 三模块模板已移除；v0.2.0 首次安装请用 `generic-science` 或 `electrocatalysis`（经 `configure-schema`），不要沿用交互式 `rsk init` 流程。

## 空 KB schema 流程

`/researchkeeper:configure-schema` 会检查 `schema status --json`，列出 `generic-science` 与 `electrocatalysis`，在 KB 之外准备 proposal，验证并预览 module→file 和 role 映射；只有显式批准后才执行 `schema apply --yes --json`。它不安装依赖、不下载模型、不创建 embedding 或 vector index。

内置和 custom proposal 都必须覆盖七种语义角色：`literature`、`entities`、`methods`、`conditions`、`results`、`relations`、`claims`。每个 module 声明 `name`、`display`、`file`、`role`、`description`、`trigger_keywords`、`extract_rules`、`audit_focus`；proposal 还包含 `template_id`、`template_version`、`schema_version` 和按 role 指定的 `vector_gate_queries`。见 [Schema 定制](docs/schema-customization.md)。

Schema 修改采用 fail-closed：同一空 KB 中 byte-identical proposal 可 idempotent 重复 apply；冲突 proposal 或含真实记录的 KB 都会被拒绝。v0.2.0 不提供非空 KB 自动迁移、schema generation、替换或 rollback。

## 覆盖声明与审计

每篇论文必须将每个活动 module 声明为 `covered`、`not_applicable` 或 `missing`。`not_applicable` 必须给出理由和可核对的论文/SI 原文证据，并由独立 reviewer 核验。

已配置的空 KB 可以通过结构 schema validation，但没有论文内容、向量或检索结果。因此 content、vector、retrieval audit 都是 **N/A**，不是 PASS，直到对应输入存在。

## Provider Protocol v1

`rsk provider` 提供 read-oriented `query` 与 dry-run `write-candidate`。`query` 写入经验证的结果 artifact；`write-candidate` 在 shadow copy 中验证，并在 formal KB 外写入审阅 artifact。二者都不授予写入记录权限；用户须审阅 candidate，并显式批准正常 KB write workflow。严格的 request、artifact 与 stdout/stderr 合同见 [Provider Protocol v1](docs/provider-protocol.md)。

## 许可证

ResearchKeeper 代码采用 [MIT](LICENSE)；原创知识和说明内容采用 [CC BY 4.0](CONTENT_LICENSE)。直接 runtime dependency 和 BAAI/bge-m3 见[第三方声明](THIRD_PARTY_NOTICES.md)；ResearchKeeper 不会重新许可它们。
