---
software: VASP
category: error
status: local_verified
seed: 11
records: errors.md
---

# AIMD 温度失控与 Blowup

> 展示层页面。事实记录见 `computer_kb/records/errors.md` 的 Seed11。
> 本地验证体系: Pt(100) 3×3 + 25H₂O + Na⁺ + OH⁻ + NH₃, 109 atoms, VASP 5.4.4。

## 1. 症状

AIMD NVT 运行中温度持续上升，不收敛至 TEBEG：

| 恒温器尝试 | 典型温度 | 结果 |
|---|---|---|
| Nosé-Hoover (SMASS=-1) | ~1700-2750K 持续不降 | 未炸但不收敛 |
| Nosé-Hoover (SMASS=0.5) | ~2150-2350K | 不收敛 |
| Langevin (γ=3.0) | ~2000→3856K 加速攀升 | 即将爆炸 |
| Langevin (γ=5.0) | 首步即 ******** (97,000K) | 一瞬间爆炸 |
| **Andersen (PROB=0.2)** | **峰值 992K→13步稳定至 330K** | **成功** |

## 2. 根因

经典力场 (SPC/E) 预平衡构型在 DFT (PBE-D3) 势能面上有巨大残余力：

```
SPC/E 平衡构型 → 切换到 PBE-D3 → 每个水分子处于 PES 陡坡上
  → 初始力 RMS 10-70+ eV/Å
  → 力→原子加速→动能剧增→温度飙升
  → 恒温器无法即时响应 → blowup
```

## 3. 为什么常见恒温器失效

| 恒温器 | 机制 | 失效原因 |
|---|---|---|
| SMASS=-1 | velocity scaling | **不是恒温器**，只每步缩放速度到目标值，不产生 NVT 系综 |
| Nosé-Hoover (SMASS≥0) | 全局耦合，监测总动能 | 局部力尖峰不被感知，等全局温度上升已晚 |
| Langevin (MDALGO=3) | 每原子摩擦力 + 随机力 | 随机力分量 `√(2mγkT) η(t)` 在力场混乱时**加剧扰动** |
| **Andersen (MDALGO=1)** | **随机速度重设** | 直接打断力→动能链条，不依赖速度反馈 |

## 4. 修复：Andersen 热化级联

```
Phase 1: Andersen 热化 (200步)
  MDALGO=1, ANDERSEN_PROB=0.2
  → Andersen 每步以 20% 概率将每个原子速度重设为
    Maxwell-Boltzmann 分布，暴力切断力→动能正反馈
  → 速度不依赖力反馈 → 没有"先快后阻尼"的延迟

Phase 2: Nosé-Hoover 平衡 (500步)
  MDALGO=2, SMASS=0.5
  → 温度已稳，换确定性恒温器做 NVT 平衡

Phase 3: Nosé-Hoover 生产 (500+步)
  MDALGO=2, SMASS=0
  → 生产数据采集
```

## 5. 禁止的修复方式

| 危险做法 | 原因 |
|---|---|
| IBRION=2 CG 弛豫替代热化 | CG 在 0K 沿力梯度拉原子 → 水分子/NH₃ 化学键被拉断 |
| 加大 Langevin γ 硬压 | 随机力随 γ 增大更不稳定 |
| 延长 Nosé-Hoover 步数等收敛 | SMASS=-1 本就不产生 NVT，等再久也没用 |

## 6. 证据

- 本地验证: Pt(100) 3×3 + 25H₂O + Na⁺ + OH⁻ + NH₃, VASP 5.4.4, 56 核
- Job 32617-32623: 六轮失败 (记录在 `scf/` `aimd/` 目录下)
- Job 32624: Andersen Phase 1 成功 (记录在 `aimd/` 目录下), 200 步温度稳定
- Job 32625: Phase 2 Nosé-Hoover 平衡进行中 (`phase2_nh/`)

## 7. 适用边界

- 已知适用: 经典力场→DFT AIMD 过渡, Pt/水界面, 109 原子
- 可能需调整: 更大体系 ANDERSEN_PROB 可降至 0.1; 纯液体可降至 0.05
- 不适用: 纯 DFT 构建的平衡结构 → 直接用 Nosé-Hoover 即可

## Obsidian Links

- [[vasp_aimd_md_parameters]]
- [[vasp_md_atom_explosion]] — AIMD 离子步爆炸（相关报错，鉴别诊断）
