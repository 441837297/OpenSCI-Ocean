# P01 数据源说明

本文档列出 D0 可行性检查所需的候选公开数据。原始数据不应提交到仓库；仓库中只保留下载脚本、访问说明、质量控制说明和处理后的图表结果。

## 一、核心观测数据

### 1.1 SWOT L2 sigma0-derived wind speed

- 来源：SWOT / PO.DAAC
- 用途：主风场资料；用于计算近海面风速、风速梯度、风速动能代理量和细尺度风速响应。
- 关键变量：wind speed / sigma0-derived wind speed、质量标记、swath 坐标、时间。
- 派生量：`K10_SWOT = 0.5 * U10_SWOT^2`，可选 `E10_SWOT = 0.5 * rho_air * U10_SWOT^2`。
- 注意事项：SWOT wind speed 是风速大小，不是完整矢量风；不能单独计算 wind stress curl/divergence 或 oceanic wind work。
- 优先级：**必需，核心**

### 1.2 SWOT KaRIn L2 Low Rate SSH

- 来源：NASA PO.DAAC / CNES / SWOT mission
- 候选产品：`SWOT_L2_LR_SSH_D` 及 Basic、Expert、WindWave、Unsmoothed 等相关子产品。
- 用途：海洋动力结构；用于识别 SSH 梯度、fronts、eddies、filaments、strain 相关结构，并作为耦合 regime boundary 的动力锚点。
- 关键变量：sea surface height、sea surface height anomaly、quality flags、swath coordinates。
- 注意事项：SSH 梯度可用于刻画细尺度动力结构，但亚中尺度解释需要滤波、误差控制和质量标记筛选。
- 官方入口：https://podaac.jpl.nasa.gov/dataset/SWOT_L2_LR_SSH_D
- 优先级：**必需，核心**

### 1.3 GOES ABI SST / NOAA ACSPO

- 来源：NOAA CoastWatch / NOAA STAR
- 候选产品：ACSPO Global SST from ABI，包括 GOES-East 和 GOES-West。
- 区域：美洲及邻近海域，重点服务 Gulf Stream。
- 用途：高频 SST front；计算 SST 梯度、front 方向和热力锋面强度。
- 关键变量：SST、quality flags、clear-sky mask、SSES uncertainty。
- 注意事项：高时间分辨率是机制检验的关键，但需要处理云、降雨和日变化偏差。
- 官方入口：
  - https://coastwatch.noaa.gov/cwn/processing-algorithms/acspo.html
  - https://coastwatch.noaa.gov/cwn/products/acspo-global-sst-abi.html
- 优先级：**必需，核心**

### 1.4 Himawari-8/9 AHI SST

- 来源：JAXA P-Tree / JAXA Himawari Monitor，也可通过 GHRSST/ACSPO 相关公开入口获取。
- 区域：西北太平洋，重点服务 Kuroshio Extension。
- 用途：高频 SST front；与 SWOT pass 配准，解释 Kuroshio Extension 区域风速动能增强是否与亚中尺度 SST-front coupling 有关。
- 关键变量：SST、quality flags、cloud mask。
- 注意事项：需要评估云筛选、晴空采样偏差和日变化影响。
- 官方入口：https://earth.jaxa.jp/en/data/2529/index.html
- 优先级：**必需，核心**

## 二、辅助与对照风场

### 2.1 ASCAT ocean vector winds

- 来源：EUMETSAT OSI SAF / KNMI / PO.DAAC
- 候选产品：MetOp-B/C ASCAT L2 winds；MEaSUREs-OSVW wind vectors and wind stress。
- 用途：传统卫星风场对照；中尺度一致性验证；提供矢量风用于 downwind/crosswind 分解。
- 注意事项：ASCAT 原生分辨率和有效分辨率会平滑很多 SWOT 可见的亚中尺度结构，因此不应作为 2-10 km 细尺度风速响应的主证据。
- 官方入口：
  - https://podaac.jpl.nasa.gov/dataset/ASCATC-L2-25km
  - https://podaac.jpl.nasa.gov/MEaSUREs-OSVW
- 优先级：推荐

### 2.2 ERA5

- 来源：Copernicus Climate Data Store / ECMWF
- 用途：大尺度背景风、天气尺度控制、边界层背景、稳定度和敏感性检验。
- 关键变量：10 m wind speed / components、surface fluxes、boundary-layer diagnostics。
- 注意事项：有效分辨率不足以支撑真正亚中尺度风速梯度结论。
- 官方入口：https://cds.climate.copernicus.eu/
- 优先级：推荐

### 2.3 CCMP ocean surface winds

- 来源：Remote Sensing Systems / NASA MEaSUREs / PO.DAAC
- 用途：多源融合传统风产品对照；提供背景风场和大尺度风速结构。
- 注意事项：网格化融合会平滑最细尺度结构，主要用于评估 SWOT 与传统产品的差异。
- 官方入口：https://podaac.jpl.nasa.gov/MEaSUREs-CCMP
- 优先级：可选

## 三、试验区域

### 3.1 Gulf Stream

- 参考范围：30-45 N, 80-40 W
- 数据组合：SWOT wind speed + SWOT KaRIn SSH + GOES-East/West ABI SST + ASCAT/ERA5/CCMP 对照风场。
- 科学价值：强 SST front、强海气边界层响应、活跃中尺度/亚中尺度过程。

### 3.2 Kuroshio Extension

- 参考范围：28-45 N, 135-170 E
- 数据组合：SWOT wind speed + SWOT KaRIn SSH + Himawari AHI SST + ASCAT/ERA5/CCMP 对照风场。
- 科学价值：典型西边界流延伸体，具有强 SST 梯度和活跃的涡-平均流相互作用。

## 四、D0 待回答的数据可行性问题

1. SWOT wind speed 在 Gulf Stream 和 Kuroshio Extension 强锋面区域的质量是否足以支持亚中尺度诊断？
2. SWOT wind speed 与 GOES/Himawari SST 的最佳时间配准窗口是多少？
3. SWOT wind-speed kinetic energy 与 ASCAT/ERA5/CCMP 在西边界流区域的差异主要来自真实细结构，还是采样/质量控制差异？
4. 西边界流区域更强的风速动能异常是否与更强的静止卫星 SST 耦合系数统计相关？
5. 不同区域应该使用哪个尺度范围定义“亚中尺度”？
6. 耦合系数对云筛选、日变化、降雨污染和 SWOT 质量标记有多敏感？
