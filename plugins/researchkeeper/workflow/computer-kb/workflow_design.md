# workflow_design · 计算 workflow 设计原则

框架版本：v0.1

本文件规定如何从论文经验、软件规则和本地验证记录设计计算 workflow。

## 设计输入

- 用户目标：体系、反应、尺度、软件约束、时间/资源限制。
- 论文经验：`kb/methods.md`、`kb/relations.md`、`kb/literature.md`。
- 软件规则：`computer_kb/records/`、`computer_kb/wiki/concepts/`。
- 报错和失败路径：`computer_kb/wiki/errors/`。
- 本地经验：用户本地计算目录中可追溯的输入/输出/日志。

## 输出结构

任何 workflow 方案应至少包含：

1. 目标和边界。
2. 输入文件或前置条件。
3. 推荐步骤。
4. 每步检查点。
5. 常见失败路径和回退策略。
6. 需要本地小测试验证的参数。
7. 证据标签：论文知识、软件知识、本地经验、AI 判断。

## 不允许

- 不允许只给“照论文做”的流程。
- 不允许只给官方教程而忽略用户的具体研究场景。
- 不允许把未验证的 AI 推测写成 `local_verified`。
