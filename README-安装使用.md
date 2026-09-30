# ResearchKeeper v0.2.0 本地插件市场包

本目录可直接作为 Claude Code 的本地插件市场。它来自正式产品源码提交
`cb62811a0325c1846643f1024939f7afb308bbb8`，不包含 Git 历史、测试、构建目录、
wheel、egg-info、Python 缓存、模型、虚拟环境或用户工作区数据。

源码根部的 `CLAUDE.md` 不会被 Claude Code 当作插件上下文自动加载，因此交付包
没有把它原样放在插件根部。其完整内容已保存在
`plugins/researchkeeper/skills/researchkeeper/references/RSK-DETAILED-GUIDE.md`，
并由 `researchkeeper` skill 明确要求在相关任务前读取。这样详细操作说明仍会
参与实际使用，同时插件清单可以通过严格校验。

## 压缩和解压

压缩时请压缩整个
`ResearchKeeper-v0.2.0-local-marketplace-cb62811` 文件夹。用户解压后，
应能在该文件夹根部直接看到 `.claude-plugin` 和 `plugins` 两个目录。
不要只压缩 `plugins/researchkeeper`。

## 用户安装

前置条件：

- 已安装 Claude Code；
- 已安装 Python 3.11.x；
- 初始化时可以联网安装锁定的 Python 依赖；后续模型设置还需要约 2.2 GB
  的 bge-m3 下载空间。

在 PowerShell 中，把下面的路径替换为用户实际解压路径：

```powershell
claude plugin marketplace add "D:\实际路径\ResearchKeeper-v0.2.0-local-marketplace-cb62811"
claude plugin install researchkeeper@researchkeeper-local --scope user
```

也可以在 Claude Code 的 `/plugin` 界面中添加这个本地市场目录，然后安装
`researchkeeper@researchkeeper-local`。

安装完成后重新打开 Claude Code，在需要作为 ResearchKeeper 工作区的目录中
运行：

```text
/researchkeeper:setup
```

setup 会先检查 Python 3.11、插件数据目录、CPU/CUDA 选择和依赖锁，再征求同意
创建隔离环境。CPU 是默认且完整支持的选项；CUDA 只应在用户明确选择后使用。
依赖安装完成后，setup 会继续引导选择明确的工作区、配置 schema、初始化
Compute KB，并在再次获得同意后下载或复用模型。

## 目录完整性

市场入口：

```text
.claude-plugin/marketplace.json
```

插件入口：

```text
plugins/researchkeeper/.claude-plugin/plugin.json
```

交付来源、文件数和插件树摘要记录在 `DELIVERY-METADATA.json`。
