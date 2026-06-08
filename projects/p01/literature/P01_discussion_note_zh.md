# P01 讨论后修订说明：为什么 SWOT 风速应作为主资料

> 本文档参考 P02 `literature/data_requirements.md` 的组织方式，整理 P01 在组内讨论后的科学定位、数据主次、耦合系数选择和第一阶段执行方案。README 负责英文项目卡片；本文档负责中文讨论材料。
>
> 最后更新：2026-06-08

---

## 一、讨论后的核心判断

组内修改后的科学问题更有论文潜力：从“SWOT 视角下全球风动能分布”推进到“海气耦合系数从中尺度到亚中尺度是否存在尺度依赖或 regime transition”。这个 framing 更像一个可以投稿的科学假说，而不是单纯的数据展示。

因此建议主要保留组内修改后的题目和科学逻辑，不再另起一个偏技术化的新题目。需要调整的是数据主次：**如果项目的核心卖点是 SWOT 揭示传统卫星看不到的亚中尺度海气耦合，那么 SWOT L2 sigma0-derived wind speed 应该是主风场资料，而不是 supporting dataset。**

ASCAT、ERA5、CCMP 仍然重要，但它们更适合做：

- 传统风产品对照；
- 中尺度一致性验证；
- 背景风场和天气尺度控制；
- 背景风场和传统产品对照。

它们不应替代 SWOT 风速来承担 2-10 km 或 10-25 km 亚中尺度风速响应的核心证据。

---

## 二、建议保留的科学问题

### 2.1 英文问题

Does air-sea coupling undergo a scale-dependent transition from mesoscale to submesoscale, and can SWOT wind speed, SWOT SSH, and geostationary SST reveal fine-scale wind responses that traditional wind products cannot resolve?

### 2.2 中文表述

海气耦合从中尺度进入亚中尺度时，耦合系数是否保持连续，还是会发生衰减、饱和或机制转换？SWOT 风速、SWOT SSH 和静止卫星 SST 的联合观测，能否揭示这种尺度转换发生在哪里、如何发生，以及传统散射计和再分析风场看不到的细尺度风速响应？

### 2.3 为什么这个问题比原始问题更强

原始问题强调“西边界流区域风动能强在哪里、为什么强”。这个问题很直观，但容易被理解为描述性分析。修改后的问题进一步追问：

1. 风速响应是否随尺度变化？
2. 中尺度经典 SST-wind coupling 是否能延伸到亚中尺度？
3. 是否存在一个临界尺度，使耦合斜率、相位、相干性或风动能响应发生改变？
4. SWOT 是否能看到传统风产品看不到的这部分结构？

这样科学问题更集中，也更容易形成一张核心图：**coupling coefficient as a function of scale**。

---

## 三、数据主次建议

### 3.1 核心观测三元组

| 数据 | 级别/来源 | 用途 | 优先级 |
|---|---|---|---|
| SWOT L2 sigma0-derived wind speed | SWOT / PO.DAAC | 主风场资料；计算 `U10_SWOT`、`0.5 U10_SWOT^2`、风速梯度和细尺度风速响应 | **必需，核心** |
| SWOT KaRIn L2 LR SSH | SWOT / PO.DAAC | 海洋动力结构；识别 SSH 梯度、锋面、涡旋边缘、filaments、strain 相关结构 | **必需，核心** |
| GOES-East ABI SST / NOAA ACSPO | NOAA CoastWatch / STAR | Gulf Stream 区域高频 SST 锋面；计算 SST 梯度和热力锋面结构 | **必需，核心** |
| Himawari-8/9 AHI SST | JAXA / NOAA ACSPO / GHRSST routes | Kuroshio Extension 区域高频 SST 锋面；计算 SST 梯度和热力锋面结构 | **必需，核心** |

### 3.2 辅助和对照资料

| 数据 | 来源 | 用途 | 优先级 |
|---|---|---|---|
| ASCAT vector winds | EUMETSAT / OSI SAF / PO.DAAC | 粗尺度传统风产品对照；中尺度一致性验证；评估传统卫星能看到什么、遗漏什么 | 推荐 |
| ERA5 10m winds / surface fields | CDS / ECMWF | 大尺度背景风、天气尺度控制、稳定度或边界层背景 | 推荐 |
| CCMP ocean surface winds | RSS / PO.DAAC | 多源融合传统风场对照，评估 SWOT 与传统 gridded wind products 的差异 | 可选 |

### 3.3 数据主次的关键理由

1. **SWOT 风速是这个项目的观测创新点。** 如果只用 ASCAT 做风场，文章会变成“ASCAT + SST 的尺度耦合，SWOT SSH 做结构标记”，与“Revealed by SWOT”的题目不完全一致。
2. **ASCAT 分辨率限制了亚中尺度证据。** ASCAT 可用于约 25 km 以上尺度的验证和矢量分解，但不能作为 2-10 km 或更细尺度风速响应的主证据。
3. **静止卫星 SST 是机制解释的关键。** GOES/Himawari 的高频 SST 可以解析西边界流锋面、filaments 和短时间变化，是解释 SWOT 风速细结构的重要热力变量。
4. **SWOT SSH 是动力结构锚点。** SSH 梯度和相关结构可以帮助判断 SST front 是否对应动态活跃的亚中尺度结构，从而解释耦合强弱的空间差异。

---

## 四、耦合系数选择

海气耦合系数并不只有一种。不同系数需要不同数据，适用尺度也不同。

### 4.1 SWOT 风速可以直接支持的系数

| 系数 | 形式 | 所需数据 | 适合本项目程度 |
|---|---|---|---|
| 风速梯度-SST 梯度耦合 | `|grad U10_SWOT| = alpha |grad SST_geo| + residual` | SWOT wind speed + GOES/Himawari SST | **最适合，主诊断** |
| 风动能梯度-SST 梯度耦合 | `|grad K10_SWOT| = beta |grad SST_geo| + residual` | `K10_SWOT = 0.5 U10_SWOT^2` + SST | **最贴近原始想法** |
| 风速异常-SST front 指标 | `U10_SWOT' = gamma SST_front_metric + residual` | SWOT wind speed + SST front metric | 推荐 |
| 谱相干 / 互谱 | coherence between `U10_SWOT` or `K10_SWOT` and `SST` / `grad SST` | SWOT wind speed + SST | **推荐，适合尺度问题** |

这些系数不需要风向，因此可以把 SWOT wind speed 放在中心。

### 4.2 暂不纳入初始核心分析的系数

风应力 curl/divergence、downwind/crosswind decomposition 等诊断需要矢量风或风应力产品。它们虽然在传统 SST-wind coupling 文献中很常见，但会把本项目的初始主线重新拉回 ASCAT/ERA5，而不是 SWOT wind speed。

因此 D0/D1 阶段建议暂不把这类诊断写成核心任务。若后续结果显示必须区分风向响应，再作为扩展分析单独设计。

---

## 五、建议的第一阶段工作流

### Phase 1：先做 Gulf Stream 个例

| 步骤 | 内容 | 产出 |
|---|---|---|
| 1 | 选择 1-3 条穿过 Gulf Stream 强 SST front 的 SWOT swath | case list |
| 2 | 下载同时间 GOES-East SST，做云筛选和时间配准 | collocated SST |
| 3 | 提取 SWOT wind speed 和 SWOT SSH | collocated SWOT fields |
| 4 | 计算 `U10_SWOT`、`K10_SWOT = 0.5 U10_SWOT^2`、`grad U10`、`grad K10`、`grad SST`、`grad SSH` | diagnostic fields |
| 5 | 做第一张图：SWOT wind speed / K10 是否沿 SST front 和 SSH gradient 组织 | pilot figure |
| 6 | 与 ASCAT / ERA5 / CCMP 同时刻对比，检查传统产品是否平滑掉细结构 | comparison figure |

### Phase 2：尺度依赖分析

| 步骤 | 内容 | 产出 |
|---|---|---|
| 1 | 对 SWOT wind speed、SST、SSH 做多尺度滤波 | scale bands |
| 2 | 计算不同尺度下 `|grad U10|` vs `|grad SST|` 的回归斜率 | alpha(lambda) |
| 3 | 计算 `|grad K10|` vs `|grad SST|` 的回归斜率 | beta(lambda) |
| 4 | 做互谱、相干和相位分析 | coherence / phase curves |
| 5 | 检查是否存在 coupling coefficient 的 break、plateau、decay 或 phase shift | regime evidence |

### Phase 3：Kuroshio Extension 和控制区

| 步骤 | 内容 | 产出 |
|---|---|---|
| 1 | 用 Himawari SST 重复 Kuroshio Extension 分析 | basin comparison |
| 2 | 选择弱 SST front 控制区 | control samples |
| 3 | 比较西边界流和控制区的 coupling coefficient 曲线 | mechanism test |
| 4 | 判断是否支持 regime transition 或只是 scale-dependent weakening | paper framing |

---

## 六、关键风险和表述边界

### 6.1 SWOT 风速质量

SWOT 风速虽然是 L2 产品，并且已有 GRL 文章使用 SWOT 风速讨论亚中尺度海气相互作用，但仍需要在本项目中做质量控制。尤其要注意 rain contamination、sea state、sigma0 retrieval uncertainty、swath-edge effects 和 land contamination。

### 6.2 风速不是矢量风

SWOT wind speed 是风速大小，不是完整矢量风。因此：

- 可以做 `U10`、`K10`、`grad U10`、`grad K10`；
- 可以做 SST-front 与 wind-speed response 的耦合；
- 初始阶段不做 wind stress curl/divergence 或 downwind/crosswind 分解。

### 6.3 机制不能直接假设

西边界流区域风动能较强，可能来自：

1. 大尺度大气强迫；
2. 海洋锋面诱导的大气边界层响应；
3. 两者共同作用；
4. 采样、天气过程或云筛选带来的偏差。

因此论文中要把“为什么更强”写成待检验机制，而不是先验结论。

### 6.4 传统产品看不到，不等于传统产品错误

ASCAT/ERA5/CCMP 看不到细结构，主要是因为分辨率、采样和反演/融合方法限制。更稳妥的说法是：

> Traditional products may smooth or under-resolve fine-scale wind responses that SWOT can observe.

---

## 七、建议和组内沟通表述

可以这样和组里沟通：

> 我同意把科学问题提升为 scale-dependent regime transition，这比单纯讨论风动能分布更有论文潜力。但我建议把 SWOT L2 sigma0-derived wind speed 从 supporting dataset 提升为 primary atmospheric response field。因为如果核心论点是 SWOT 揭示了传统卫星看不到的亚中尺度海气耦合，那么风速响应本身应该主要来自 SWOT。ASCAT 很重要，但更适合作为 coarse-scale benchmark 和传统产品对照，不能替代 SWOT 来支撑 2-10 km 亚中尺度风场响应。

更简短地说：**题目和科学逻辑沿用组内版本，资料主次改为 SWOT wind speed 主导。**

---

## 八、待核验文献方向

- SWOT-derived wind speed / sigma0 wind speed 的产品说明和质量评估。
- 使用 SWOT wind speed 研究 submesoscale air-sea interactions 的 GRL 文章。
- Chelton / Small / O'Neill 系列 mesoscale SST-wind coupling 框架。
- coupling coefficient 的尺度依赖研究。
- ASCAT effective resolution 与 scatterometer wind response to SST fronts 的文献。
- GOES / Himawari high-frequency SST fronts 与 western boundary current air-sea coupling 研究。
