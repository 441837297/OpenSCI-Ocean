# D0 分析计划

## 工作标题

SWOT 揭示的亚中尺度海气耦合尺度依赖 regime transition

## 核心科学问题

海气耦合从中尺度进入亚中尺度时，是否存在尺度依赖、衰减、饱和或 regime transition？SWOT 风速是否能揭示传统风产品被平滑或遗漏的细尺度风速响应？

## 核心原则

科学问题应主要沿用组内修改后的“尺度依赖 / regime transition”框架。这里的主要修订不是重写科学逻辑，而是调整资料主次：主风场资料应当是 SWOT L2 wind speed。ASCAT、ERA5 和 CCMP 应作为对照、验证、背景场和矢量风辅助资料，而不是替代 SWOT 来支撑亚中尺度风速响应。

## 变量

- SWOT L2 风速：`U10_SWOT`
- SWOT 风速动能代理量：`K10_SWOT = 0.5 * U10_SWOT^2`
- SWOT KaRIn SSH / SLA
- Gulf Stream 区域 GOES-East ABI SST
- Kuroshio Extension 区域 Himawari-8/9 AHI SST
- ASCAT、ERA5、CCMP 的对照风场
- SST 梯度强度与 SST front 方向
- SWOT SSH 梯度及可选的动力锋面强度指标
- `U10_SWOT`、`K10_SWOT`、SST、SSH 的不同尺度滤波异常

## 候选诊断

### 1. 数据配准与质量控制

构建 Gulf Stream 和 Kuroshio Extension 区域的 SWOT 风速 / SWOT SSH / 静止卫星 SST 匹配样本。

- 以 SWOT swath 时间和空间坐标为基准。
- 从同一条 SWOT 轨道中提取 wind speed 与 SSH。
- 在候选时间窗内匹配 GOES/Himawari 晴空 SST，例如 `±30 min`、`±1 h`、`±3 h`。
- ASCAT、ERA5、CCMP 只作为对照产品和矢量风参考。
- 保留 SWOT 质量标记、SST 云掩膜、降雨标记、陆地掩膜和 swath edge 指标。

### 2. 多尺度分解

对 SWOT 风速、静止卫星 SST 和 SWOT SSH 做空间滤波。

- 中尺度候选范围：100-500 km。
- 过渡尺度候选范围：25-100 km。
- SWOT 可解析的亚中尺度候选范围：2-25 km，具体取决于 SWOT 风速质量、噪声水平和有效分辨率。
- 对滤波窗口、截止波长、沿轨/跨轨采样方式做敏感性检验。

对照产品不应定义本研究的最小尺度。ASCAT 可以支持它能够解析的尺度，而 SWOT wind speed 应承担细尺度风速响应的核心证据。

### 3. SWOT 风速动能代理量

从 SWOT wind speed 估算近海面风速动能代理量：

```text
K10_SWOT = 0.5 * U10_SWOT^2
```

如果需要带空气密度的能量密度形式：

```text
E10_SWOT = 0.5 * rho_air * U10_SWOT^2
```

本项目初始阶段不估算海洋风功输入 `tau dot u_o`。目标变量是 SWOT 观测到的近海面风速大小、风速动能及其细尺度结构。

### 4. 尺度依赖耦合系数

主诊断使用 SWOT 风速：

```text
|grad U10_SWOT| = alpha(lambda) |grad SST_geo| + residual
|grad K10_SWOT| = beta(lambda) |grad SST_geo| + residual
K10_SWOT' = gamma(lambda) SST_front_metric + residual
```

其中 `lambda` 表示空间尺度或滤波截止波长。核心检验是 `alpha(lambda)`、`beta(lambda)`、相干性或相位是否从中尺度到亚中尺度发生 break、plateau、decay 或 phase shift。

辅助矢量风诊断可在 ASCAT 或 ERA5 可解析尺度上进行：

```text
curl(tau) = a crosswind_grad(SST) + residual
div(tau) = b downwind_grad(SST) + residual
```

这些诊断有助于机制解释，但不应被表述为 SWOT 2-10 km 尺度风速响应的直接证据。

### 5. 谱分析与相干分析

计算以下变量之间的互谱、相干和相位：

- `U10_SWOT` 或 `K10_SWOT` 与静止卫星 SST。
- `grad U10_SWOT` 或 `grad K10_SWOT` 与 `grad SST_geo`。
- `K10_SWOT` 异常与 SWOT SSH 梯度。
- SWOT wind speed 与 ASCAT/ERA5/CCMP 风场，用于量化传统产品平滑或遗漏的结构。

核心图应展示耦合系数或相干曲线是否在亚中尺度出现转折、平台、衰减或相位变化。

## 试验工作流

1. 选择 1 条或多条穿过 Gulf Stream 强 SST front 的 SWOT swath。
2. 配准 SWOT wind speed、SWOT SSH 和 GOES-East SST。
3. 绘制第一个个例图：`U10_SWOT`、`K10_SWOT`、SST front 和 SSH gradient。
4. 与 ASCAT、ERA5、CCMP 对比，展示传统产品能解析什么、遗漏什么。
5. 基于 SWOT wind speed 和 GOES SST 计算多尺度耦合系数。
6. 在 Kuroshio Extension 区域使用 Himawari SST 重复分析。
7. 加入弱锋面控制区，检验信号是否特异于西边界流区域。
8. 根据结果决定 D1 稿件侧重 regime transition、scale-dependent weakening，还是 SWOT-observed fine-scale wind response。

## 图件计划

1. Gulf Stream 和 Kuroshio Extension 区域 SWOT swath 与 SST front 覆盖图。
2. SWOT wind speed / `K10_SWOT`、静止卫星 SST front 和 SWOT SSH gradient 的个例图。
3. SWOT 与 ASCAT/ERA5/CCMP 对比图，突出传统产品的平滑效应。
4. 基于 SWOT wind speed 和静止卫星 SST 的尺度依赖耦合系数曲线。
5. SWOT wind speed、SST front 与 SWOT SSH gradient 的相干和相位谱。
6. Gulf Stream 与 Kuroshio Extension 的对比图。
7. 弱锋面控制区结果。

## 人工审查重点

- 核查 SWOT wind speed 质量、降雨污染、海况影响和 swath edge artifacts。
- 细尺度结论必须以 SWOT wind speed 为主风场证据。
- ASCAT、ERA5、CCMP 只能在其可辩护尺度内使用。
- 区分风速动能与海洋风功输入。
- 把 regime transition 作为待检验假说，而不是预设结论。
- AI 建议的所有参考文献必须人工核验后再引用。
