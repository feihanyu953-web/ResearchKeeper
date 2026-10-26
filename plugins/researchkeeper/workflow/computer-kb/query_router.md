# Query Router - computer_kb 融合查询协议

框架版本：v0.3-domain-routes

核心原则：

> 存储隔离，回答融合。

本文件规定计算相关问题的证据读取顺序、输出标签和冲突处理方式。它不改变论文 `kb/` 与 `wiki/` 的存储规则。

## 1. 四层证据

### 1.1 当前材料层

优先读取用户当前提供或当前任务直接相关的材料：

- 当前论文 PDF / SI / HTML / pdftotext。
- 当前计算目录。
- 输入文件：INCAR、KPOINTS、POSCAR、POTCAR、LAMMPS input、模型 config。
- 输出文件：OUTCAR、OSZICAR、vasprun.xml、log.lammps、training log。
- 报错截图或完整 error log。
- 用户明确给出的体系、目标和约束。

输出标签：

```text
【当前材料】
```

### 1.2 论文知识层

当问题涉及"论文怎么做""相似体系经验""计算设置是否合理"时读取：

- `kb/methods.md`
- `kb/relations.md`
- `kb/literature.md`
> 模块映射按当前论文 kb/INDEX.md 解析（generic-science schema: 机理/能垒/路径/描述符位于 `relations` 模块）。
- 若工作区存在 `wiki/`：`wiki/index.md`、`wiki/concepts/*.md`（概念页叙事是论文知识层的有效证据面）
- 已阅读文献中的精读笔记

输出标签：

```text
【论文知识】
```

### 1.3 计算软件层

当问题涉及软件参数、命令、报错、workflow、版本行为时读取：

- `computer_kb/INDEX.md`
- `computer_kb/SCHEMA.md`
- `computer_kb/records/*.md`
- `computer_kb/records/relations/*.md`
- `computer_kb/records/templates/*.md`
- `computer_kb/records/error_chains/*.md`
- `computer_kb/wiki/index.md`
- `computer_kb/wiki/concepts/*.md`
- `computer_kb/wiki/errors/*.md`
- `computer_kb/wiki/workflows/*.md`
- `computer_kb/sources.md`

输出标签：

```text
【软件知识】
```

### 1.4 AI 综合判断层

AI 只能在前三层证据之后给出判断。必须区分：

- 已由来源支持的事实。
- 根据事实作出的推理。
- 尚需本地验证的假设。

输出标签：

```text
【AI 判断】
```

如使用本地已跑通流程或本地 error log，使用：

```text
【本地经验】
```

## 2. 问题类型路由

### 2.1 论文精读中的计算问题

读取顺序：

```text
当前论文/PDF/SI
-> kb/methods.md
-> kb/relations.md
-> kb/literature.md
-> computer_kb/wiki/concepts
-> computer_kb/records
-> AI 判断
```

输出必须包含：

- 论文实际参数或方法。
- 相似论文经验，若有。
- 官方/软件层定义或限制。
- 是否可借鉴，以及不能直接照搬的部分。

### 2.2 设计自己的计算流程

读取顺序：

```text
用户目标和约束
-> kb/literature.md 找相似体系
-> kb/methods.md 找论文计算经验
-> kb/relations.md 找关键计算描述符/路径
-> computer_kb/wiki/workflows
-> computer_kb/wiki/concepts
-> computer_kb/wiki/errors
-> 本地 dft_models/ 或已有脚本/验证记录
-> AI 方案
```

输出必须包含：

- 目标拆解。
- 推荐 workflow。
- 需要复用的论文经验。
- 必须遵守的软件规则。
- 本地验证检查点。
- 风险和最小测试方案。

### 2.3 软件参数/命令解释

读取顺序：

```text
computer_kb/wiki/concepts/ 下与参数相关的概念页
  - VASP SCF 参数 → vasp_scf_accuracy_chain.md
  - VASP AIMD/MD 参数 → vasp_aimd_md_parameters.md
  - VASP NEB 参数 → vasp_neb_chain.md
  - VASP 吸附能/自由能 → vasp_adsorption_energy_chain.md
  - VASP 电子结构（DOS/PDOS/d-band/Bader）→ vasp_electronic_structure_chain.md
  - VASP DFT+U → vasp_dft_plus_u_guide.md
  - VASP thermostat 选择 → vasp_md_thermostat_guide.md
  - VASPsol 隐式溶剂 → vasp_vaspsol_implicit_solvent.md
  - LAMMPS 命令索引 → lammps_command_index.md
  - LAMMPS MD 基础 → lammps_md_basics.md
  - LAMMPS 前置命令链 → lammps_md_setup_chain.md
  - LAMMPS thermostat/integration 链 → lammps_md_fix_thermostat_chain.md
  - LAMMPS MACE pair → lammps_mace_pair_chain.md
  - LAMMPS 温度统计与冻结原子 → lammps_temp_frozen_atoms.md
  - MACE 训练 → mace_training_basics.md
  - MACE CLI 参数 → mace_cli_parameters.md
  - MACE in LAMMPS → mace_in_lammps.md
  - MACE batch/VRAM → mace_batch_vram_hardware.md
  - MACE loss 权重 → mace_training_loss_balance.md
  - DeePMD/DPA4C 训练微调冻结压缩 → deepmd_dpa4c_basics.md
  - DPA4C → LAMMPS MD 管线 → aimd_to_dpa4c_to_lammps.md
  - MLFF 建集读哪个 VASP 输出文件 → vasp_output_for_mlff_dataset.md
  - AIMD 轨迹的氢键环境-势垒理论分析（Q_pre/n̄_ww/P_z → ΔG‡）→ cv_hbond_pt_framework.md
  - 跨软件参数流 → cross_software_parameter_flow.md
-> computer_kb/records
-> computer_kb/sources.md
-> 如涉及论文复现，再读取 kb/methods.md
-> AI 解释
```

输出必须包含：

- 官方定义。
- 常见用法。
- 适用范围和误区。
- 与当前研究体系的关系。
- 如涉及论文，标出论文用法只是案例，不是软件标准。

### 2.4 报错排查

读取顺序：

```text
完整 error log / 当前输出文件
-> computer_kb/wiki/errors/ 下与报错相关的错误页
  - VASP SCF 不收敛 → vasp_scf_not_converge.md
  - VASP AIMD 原子爆炸 → vasp_md_atom_explosion.md
  - VASP 温度失控 → aimd_temperature_runaway.md
  - VASP NEB 不收敛 → vasp_neb_not_converge.md
  - VASP Γ-only 金属 slab 电子态翻转（E0 跳变）→ vasp_gamma_state_flip.md
  - VASP 吸附能异常 → vasp_adsorption_energy_abnormal.md
  - VASP DOS/d-band 异常 → vasp_dos_dband_abnormal.md
  - VASP 带电 slab ZBRENT → vasp_charged_slab_zbrent.md
  - VASP 频率 NPAR 冲突 → vasp_freq_npar_kpoints.md
  - LAMMPS 能量 NaN → lammps_md_energy_nan.md
  - LAMMPS 丢失原子 → lammps_lost_atoms.md
  - LAMMPS 数值不稳定 → lammps_non_numeric_instability.md
  - LAMMPS out-of-range atoms → lammps_out_of_range_atoms.md
  - LAMMPS unrecognized style/package → lammps_unrecognized_style_package.md
  - LAMMPS energy/stress not tallied → lammps_energy_stress_not_tallied.md
  - LAMMPS pair mace 未识别 → lammps_mace_pair_not_found.md
  - LAMMPS PLUMED 未加载 → lammps_plumed_lib_not_loaded.md
  - MACE CUDA OOM → mace_cuda_out_of_memory.md
  - MACE 数据加载 initial loss → mace_data_loading_initial_loss.md
  - MACE E0s 误差 → mace_e0s_large_energy_error.md
  - MACE 数据集质量（高能 force）→ mace_dataset_quality_high_energy_forces.md
  - MACE GPU 过热降频 → mace_gpu_thermal_throttle.md
  - MACE 多 GPU checkpoint → mace_multigpu_checkpoint.md
  - MACE Kokkos/newton 冲突 → mace_kokkos_newton_conflict.md
  - MACE 2GPU domain decomp → mace_domain_decomp_2gpu.md
  - MACE 微调 best 退回 epoch-0 → mace_finetune_best_checkpoint_epoch0.md
  - POSCAR/POTCAR 元素顺序错配（无报错静默出错）→ poscar_potcar_order_mismatch.md
  - deepmd Kokkos neigh full 冲突 → deepmd_kokkos_newton_conflict.md
-> computer_kb/records/errors.md        # 通用错误事实入口
-> computer_kb/records/error_chains/    # 本地/任务特化诊断链
-> computer_kb/wiki/workflows
-> 官方 issue/doc
-> 当前输入文件和本地目录
-> AI 排查
```

输出必须包含：

- 报错原文或关键行。
- 最可能原因排序。
- 逐步排查步骤。
- 不建议直接做的危险修复。
- 需要用户或 AI 继续检查的文件。

### 2.5 参数关系查询

读取顺序：

```text
目标参数
-> computer_kb/records/relations/      # 查该参数参与的关系图
-> 关联参数的 records
-> computer_kb/wiki/concepts           # 查看叙事化解释
-> 官方交叉引用
-> AI 给出联动修改建议
```

输出必须包含：

- 该参数与哪些参数存在什么类型的关系。
- 修改此参数时哪些参数必须同步调整。
- 关系推导依据是什么（official / physical_constraint / domain_knowledge）。

### 2.6 任务参数设计

读取顺序：

```text
用户目标、体系、硬件约束
-> computer_kb/records/templates/      # 匹配任务域模板
-> 模板中每个参数的 records
-> 本地硬件验证证据
-> 官方文档交叉验证
-> AI 生成参数组合
```

输出必须包含：

- 匹配到的模板及适用条件。
- 每个参数的推荐值、理由和来源。
- 当前体系与模板适用条件的差异（如有）。
- 需要本地小测试验证的边界。

### 2.7 Workflow 复用/修改

已跑通的 workflow 路由（页面存在时优先直达）：

```text
- VASP ASE→MACE 数据集构建 → vasp_ase_to_mace_dataset.md
- MACE 训练-评估-LAMMPS 冒烟测试 → mace_train_eval_lammps_smoke_test.md
- 电催化界面水 AIMD+MLFF 主线 → electrocatalysis_interface_water_aimd_mlff.md
- AIMD→MACE→LAMMPS 管线 → aimd_to_mace_to_lammps.md
- AIMD→DPA4C→LAMMPS 管线 → aimd_to_dpa4c_to_lammps.md
- VASP 大体系两步 SCF → vasp_two_step_scf_large_system.md
- MLFF 建集的 VASP 输出选取 → vasp_output_for_mlff_dataset.md
```

> 上述领域路由仅在当前工作区 `computer_kb/wiki/workflows/` 实际含有对应页面时
> 生效；页面不存在时跳过该直达项，走下方通用流程（其他领域路由表同理——
> 路由是工作区扩充项，不是插件内置数据）。

读取顺序：

```text
computer_kb/wiki/workflows/目标workflow
-> linked concepts/errors
-> records/workflows.md
-> 当前材料
-> 论文 kb 中相似体系
-> AI 修改建议
```

输出必须包含：

- 原 workflow 的适用范围。
- 当前任务与原 workflow 的差异。
- 哪些步骤可复用。
- 哪些步骤必须重做验证。
- 修改后的 workflow 草案。

## 3. 证据标签输出

默认格式：

```markdown
【当前材料】
...

【论文知识】
...

【软件知识】
...

【本地经验】
...

【AI 判断】
...
```

如果某一层没有可用证据，必须写：

```text
【论文知识】未检索到相关已入库论文经验。
```

不得把未检索到的内容写成"没有相关文献"。

## 4. 冲突处理

### 4.1 当前论文 vs 官方软件文档

- 当前论文说明作者怎么做。
- 官方文档说明软件行为和参数定义。
- 若两者冲突，不直接判论文错误，先考虑版本、体系、近似和作者经验。
- 给用户建议时必须标注"可借鉴"和"需本地测试"的边界。

### 4.2 论文 kb vs computer_kb

- `kb/` 记录论文事实，不负责软件最佳实践。
- `computer_kb/` 记录软件事实，不代表某篇论文实际采用。
- 回答中并列展示二者，最终由 AI 给出适用性判断。

### 4.3 本地经验 vs 官方文档

- 官方文档优先解释软件定义。
- 本地经验优先解释当前机器/当前体系下是否跑通。
- 本地经验不得覆盖官方定义，但可以形成"本地推荐流程"。

### 4.4 AI 推理边界

AI 不得把推理写成事实。必须使用以下表述之一：

- "我推测"
- "更可能"
- "需要用小测试验证"
- "当前证据不足"
- "原文/官方文档未说明"

## 5. integration/ 自洽性

维护 `workflow/computer-kb/` 时必须检查：

- `query_router.md` 的路由规则是否覆盖 `computer_kb/INDEX.md` 列出的问题类型。
- `paper_to_compute.md` 的跨库引用是否正确，指向的 `kb/` 文件是否存在。
- `workflow_design.md` 引用的 `computer_kb` records/concepts 是否存在。
- 路由规则中提到的资源路径（如本地计算目录）是否实际存在。
- integration 规则是否坚持"存储隔离，回答融合"。

## 6. 最小回答要求

任何计算相关回答至少满足：

- 明确回答问题本身。
- 标出使用了哪些证据层。
- 若给参数建议，说明来源和适用范围。
- 若给 workflow，包含检查点和失败回退。
- 若排查报错，先要完整 error log；没有 log 时只能给初步排查路径。
