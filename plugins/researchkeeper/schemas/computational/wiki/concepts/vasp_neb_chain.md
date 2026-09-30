---
software: VASP
category: concept
status: seed
seed: "P2"
records:
  - relations/vasp_neb_chain.md
  - templates/vasp_neb_ci.md
---

# VASP NEB/CI-NEB 参数链

> 事实追溯到 `computer_kb/records/relations/vasp_neb_chain.md` 和 `computer_kb/records/templates/vasp_neb_ci.md`。

## NEB 参数关系

| 参数 | 角色 | 推荐值 | 与谁联动 |
|---|---|---|---|
| IMAGES | 路径分辨率 | 5-7 | SPRING/EDIFFG |
| SPRING | 插点间距均匀性 | -5.0 | IMAGES |
| EDIFFG | 力收敛标准 | -0.03 | IMAGES/LCLIMB |
| LCLIMB | CI-NEB 精确鞍点 | .TRUE. | EDIFFG 需紧 |
| IBRION | NEB 模式 | 1 (VTST 用 3) | — |

## 快速启动

```bash
nebmake.pl IS/POSCAR FS/POSCAR 5   # 生成 5 张插值
# INCAR: IMAGES=5 SPRING=-5.0 LCLIMB=.TRUE. IBRION=1 EDIFFG=-0.03
```

## 关联资源

- [[vasp_scf_accuracy_chain]] — SCF 精度链 (NEB 的 SCF 保底)
