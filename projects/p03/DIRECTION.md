# P03 研究方向（DIRECTION.md）

> 立项种子（v0.2）。**写完即冻结**——后续所有方向调整通过 README.md 迭代。
> 本文档是 P03 "做什么" 的 single source of truth。

## 1. 主题与工作标题

- **工作标题（EN）**: Eddy-Periphery Fine-Scale Strain Enhancement Revealed by SWOT Altimetry
- **中文一句话**: SWOT 揭示已编目中尺度涡旋外围的细尺度应变增强
- **核心科学问题**: 传统高度计已编目的中尺度涡旋，其外围是否存在 SWOT 才能解析的细尺度应变增强？这种增强是否独立预测 SST 和 Chl-a 示踪物响应？
- **差异化（vs 前人）**:
  - vs Archer 2025（SWOT 全球 fine-scale SSH）：不做全场景 activity map，聚焦 eddy-centric periphery
  - vs Dong 2025（Lofoten warm ring）：不做单 basin + 模型机制，用 SWOT 实测做跨海盆统计检验；不把 warm ring 当主假说
  - vs Zhang 2019（strain → Chl）：继承 strain predictor 框架，但用 SWOT 替换 AVISO，从全场 strain 转为 eddy-centric peripheral strain
  - vs Liu 2026（SWOT Lagrangian network）：不做 network，不做全场 connectivity
  - vs Chen & Chen 2025（DUACS polarity）：互补——我们依赖 DUACS 极性可靠性做 AE/CE 分层

## 2. 硬约束

| 项 | 值 |
|---|---|
| 投稿目标 / venue | Nature Communications 或 Science Advances（取决于 Stage 2 跨区域 tracer 证据强度） |
| 篇幅上限 | NC 无严格限制；计划 ~5000 词 + 5 主图 |
| Deadline | 无硬性截止；Stage 2 原型目标 2–4 周 |
| 算力 | HPC（/slurm/zhangzs/Eddy_SWOT/），MATLAB R2025a + Python |
| 数据 | 全部公开数据（SWOT / DUACS / SST / Ocean Color） |
| 研究区域 | 第一阶段 Kuroshio Extension；跨区域扩展 Gulf Stream / Agulhas Return Current |

## 3. 科学问题演化（P03 连续性）

```
原始 P03 D0（2026-06-05）:
  "SWOT-resolved rim 是否比传统 eddy-core 更好地组织 tracer anomalies?"
  H2: rim-radius offset (R_SWOT − R_DUACS)

Stage 1 结果（2026-06-13）:
  16 Kuroshio prototype cases, v2 修正.
  5 clean cases 的 ΔR 符号混合（+32, −4, +34, −4, −2 km）.
  样本量不足以精确估计总体，但足以排除原半径偏移假说.
  → 排除了低层解释: SWOT 不简单改写边界半径.

文献深化（2026-06-14）:
  阅读 Zhang 2019 NC + Dong 2025 NC + Archer 2025 Nature.
  → 方向从 "radius offset" 升级为 "peripheral strain enhancement."

当前 P03（v0.2）:
  "已编目中尺度涡旋外围是否存在 SWOT 才能解析的细尺度应变增强?"
```

## 4. 核心假说

> **H1（主假说 — physical organization）**: Catalogued mesoscale eddies show statistically significant excess fine-scale strain around their peripheries, relative to matched controls, as observed by SWOT.

> **H2（tracer response — gated on H1）**: The peripheral strain enhancement predicts independent SST and Chl-a responses: eddies with stronger peripheral strain show stronger surface thermal and biological signatures.

## 5. 方法框架

### 5.1 两层框架

```
第一层（predictor，纯 SWOT SSH，lock-box）:
  检验 eddy periphery 是否存在 excess fine-scale strain.
  不碰 SST/Chl-a.

第二层（response，打开 lock-box）:
  检验 peripheral strain enhancement 是否预测 tracer response.
```

### 5.2 主 predictor

| 变量 | 定义 | 物理含义 |
|------|------|---------|
| E_e(ρ) | P_e(ρ) − C_e(ρ) | **核心**: excess strain（超出 matched control 的 peripheral strain） |
| F_edge | annulus 内 S_app > control P90 的面积比例 | 外围应变空间覆盖度 |
| S_app | SWOT SSH-derived apparent geostrophic strain rate proxy | 表观地转应变率（Zhang 2019 定义） |
| A_∇_HP | median(|∇η_SWOT^HP|) in annulus | 稳健性替代指标（避免二阶导数噪声） |

### 5.3 四类 Matched Controls

| Control | 方法 | 排除的混淆 |
|---------|------|-----------|
| A: Same-swath random | 同 swath、同纬度、同覆盖率随机中心 | Swath geometry + 观测噪声 |
| B: Local displaced | eddy center 平移 3–5R | 大尺度流系 + 区域 EKE |
| C: Background-strain matched | 按低通 DUACS strain/EKE 分层匹配 | "涡旋偏好高应变区" |
| D: Isolated-eddy subset | 排除邻近 eddy < 3R | Eddy-eddy interaction / saddle 误判 |

### 5.4 五实验路线

| Exp | 问题 | 输出 |
|-----|------|------|
| 1 | 是否存在 excess peripheral strain? | radial profile E(r/R), composite maps |
| 2 | 空间范围和滤波尺度敏感性? | heatmap(filter × r/R), regional profiles |
| 3 | 伪影排除（四类 controls）? | control summary, retained effect size |
| 4 | 是否预测 SST/Chl-a response? | F_edge vs tracer response |
| 5 | F_edge 分布形态（连续 vs 分群）? | distribution, dip test |

## 6. 关键口径（已定）

1. **不声称"边界比涡核重要"**: 说 core mode（垂向泵浦）和 peripheral strain mode（侧向应变/前生化）并存。
2. **不声称 genesis**: 第一阶段不声称涡旋生成了 strain；只主张 matched controls 后的 eddy-associated peripheral strain excess。
3. **不把 warm ring 当主假说**: Dong 2025 是机制支撑，不是我们直接检验的对象。
4. **术语保守化**: 主文用 "eddy-periphery fine-scale strain enhancement"。"halo" 仅在数据证实 annular continuity + radial localization + azimuthal coverage 后作为 shorthand。
5. **Predictor-response 分离**: 先证明物理 organization，再检验 tracer response。不用 tracer 定义物理状态。
6. **PET 作 registry，不作 boundary-definer**: AVISO detect → SWOT measure。

## 7. 风险

- **最大风险**: excess strain 完全由 background fronts 解释（matched controls 无法区分）
- **Swath edge 污染**: SWOT swath 边缘噪声可能伪装成 fine-scale strain
- **滤波尺度敏感**: 如果 signal 只在单一尺度出现
- **SST 数据分辨率**: Dong 2025 的 warm ring 是 1–10 km / ~0.4°C，需要高分辨率 SST 才能分辨
- **F_edge 可能单峰分布**: 如果是连续谱，不能强行分 "rich vs poor"

## 8. 参考文献（核心 6 篇）

1. **Zhang et al. 2019** — Nature Communications. 地转应变作为 ageostrophic motion 和 Chl 的组织变量。Strain predictor 框架来源。
2. **Dong et al. 2025** — Nature Communications. Lofoten Basin 涡旋边缘应变 → warm ring。机制支撑。
3. **Archer et al. 2025** — Nature. SWOT 全球 1–100 km fine-scale SSH。数据能力基础。
4. **De Marez et al. 2026** — Ocean Science. 首次在 SWOT swath 上跑 py-eddy-tracker。P03 pipeline 直接参考。
5. **Carli et al. 2025** — JGR Oceans. SwotDiag 拟合核方法。梯度计算核心代码。
6. **Han et al. 2026** — NSR. SWOT Antarctic eddy activity。论文结构模板（surface activity → hidden process）。

## 9. 与 Zhang 2019 的定位关系（2026-06-16 新增）

Zhang 2019 证明了 **strain 是海洋细尺度过程的关键组织变量**——全场 S_g 越高，ageostrophic KE 和 Chl 越强。但 Zhang 2019 不问"strain 围着涡旋组织吗？"

P03 的增量：
1. **从全场 → eddy-centric**：Zhang 2019 按 S_g quantile 分 bin，P03 按涡旋中心做 annulus composite
2. **从无 control → control-subtracted**：Zhang 2019 不需要 control（strain 是自变量），P03 引入 displaced control 分离 eddy-associated 信号
3. **涡核-外围二分**：Zhang 2019 不区分，P03 发现涡核 strain 显著低于背景（新发现）
4. **SWOT 分辨率**：2 km vs 0.25°，直接验证低分数据推断的 fine-scale structure
5. **互补而非替代**：Zhang 2019 的 strain→tracer 框架是 P03 Exp 4 的理论基础

---

*冻结日期: 2026-06-14 | 版本: v0.2*
