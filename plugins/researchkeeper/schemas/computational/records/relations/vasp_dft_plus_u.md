# VASP DFT+U 参数选择指南

> record_type: relation | scope: single_software | software: [VASP]

~~~yaml
record_id: rel-vasp-dft-plus-u-0003
record_type: relation
scope: single_software
software:
  - VASP
topic: "DFT+U 参数联动: LDAU/LDAUTYPE/LDAUL/LDAUU/LDAUJ"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/LDAU"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: >
  DFT+U 用于校正 3d/4f 电子的强关联自相互作用误差。
  LDAU 激活 +U; LDAUTYPE 选择双重计数方式; LDAUL/LDAUU/LDAUJ 指定轨道和 U/J 值。
evidence_level: should
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_dft_plus_u_guide.md
related_records:
  - vasp-param-ldau-0223
  - vasp-param-ldautype-0227
  - vasp-param-ldaul-0225
  - vasp-param-ldauu-0228
  - vasp-param-ldauj-0224
note: "U 值选取没有通用标准——不同泛函/价态/配位环境的有效 U 不同。这里给的是领域常用参考值。"
last_checked: 2026-05-24

relation_type: overrides
relation_basis:
  - domain_knowledge
  - official_cross_ref

parameters:
  - name: LDAU
    role: "DFT+U 总开关"
    constraint: ".TRUE. 激活"
    record: vasp-param-ldau-0223
  - name: LDAUTYPE
    role: "双重计数修正方式"
    constraint: "2 = Dudarev (最常用); 1 = Liechtenstein"
    record: vasp-param-ldautype-0227
  - name: LDAUL
    role: "每个原子种类的轨道量子数"
    constraint: "2=d; 3=f; -1=不加U"
    record: vasp-param-ldaul-0225
  - name: LDAUU
    role: "每个原子种类的 U 值 (eV)"
    constraint: "有效 U 值; 元素/价态/泛函依赖"
    record: vasp-param-ldauu-0228
  - name: LDAUJ
    role: "每个原子种类的 J 值 (eV)"
    constraint: "Dudarev (LDAUTYPE=2) 只用 U_eff=U-J; J≈1.0 eV 默认"
    record: vasp-param-ldauj-0224

relation_rules:
  - id: R1
    type: requires_companion
    from: LDAU=.TRUE.
    to: "LDAUL/LDAUU/LDAUJ 必须全部指定"
    detail: "只设 LDAU=.TRUE. 不设 LDAUL/LDAUU → 所有元素 U=0 → +U 无效果"
    decision: "LDAU=.TRUE. + LDAUL=2 2 -1 + LDAUU=3.5 3.5 0 + LDAUJ=1.0 1.0 0"
    consequence: "只设 LDAU=.TRUE. 不设 LDAUL/LDAUU → U=0 → +U 无效果"

  - id: R2
    type: overrides
    from: LDAUTYPE
    to: LDAUJ 的解释
    detail: "LDAUTYPE=2 (Dudarev): U_eff = U - J → J 值对结果影响小"
    decision: "Dudarev 时 LDAUJ 可设 1.0 (默认)，主要靠 LDAUU 调 U_eff"
    consequence: "LDAUTYPE=2 下 U_eff=U−J，J 影响小；改用 LDAUTYPE=1 时 J 重新起作用"

  - id: R3
    type: requires_companion
    from: "U_eff 选取"
    to: "元素/价态"
    detail: "领域常用 U 值参考 (Dudarev, PBE)"
    decision: |
      Ni: U_eff = 3.5-6.0 eV (价态/配位依赖)
      Co: U_eff = 3.0-4.0 eV
      Fe: U_eff = 4.0-5.0 eV
      Mn: U_eff = 3.5-5.0 eV
      Cu: U_eff = 4.0-6.0 eV (CuO 需, 金属 Cu 可不加)
      Cr: U_eff = 3.0-3.5 eV
    note: "以上为文献常见范围，具体值需针对体系做 U 扫描验证"
    consequence: "U 值不当 → 电子结构定性错误（金属/绝缘体误判）；需按体系做 U 收敛测试"

failure_signatures:
  - symptom: "加 U 后带隙反而变小或金属化"
    likely: "U 值过大"
  - symptom: "加 U 与不加 U 能量几乎相同"
    likely: "LDAUL 未正确设置对应元素轨道"
  - symptom: "不同 U 值吸附能变化 > 0.3 eV"
    likely: "U 对化学描述符敏感 → 需要 U 收敛测试"
~~~
