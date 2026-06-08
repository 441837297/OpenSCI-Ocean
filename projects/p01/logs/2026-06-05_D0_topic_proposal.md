# AI 交互日志

- 日期：2026-06-05 至 2026-06-08
- 阶段：D0
- 模型：GPT-5 / Codex
- 任务：将用户的研究想法整理为 OpenSCI-Ocean P01 D0 提案，并在组内讨论后修订数据主次和科学问题表述

## Prompt 摘要

用户提出使用 SWOT 和静止卫星 SST 揭示亚中尺度海气耦合，重点区域为 Gulf Stream 和 Kuroshio Extension。用户强调数据全部公开、代码可复现，核心资料包括 SWOT KaRIn、SWOT wind speed、GOES SST、Himawari SST。研究重点包括：

- SWOT 视角下全球或区域近海面风速动能分布；
- 西边界流区域风速动能为何更强；
- 是否可以通过静止卫星 SST 计算海气耦合系数来解释这种增强；
- 传统风产品是否因分辨率和平滑处理而看不到亚中尺度风速响应；
- SWOT wind speed 应作为主风场资料，而不是仅作为辅助检查。

组内讨论后，科学问题被提升为“海气耦合从中尺度到亚中尺度是否存在尺度依赖或 regime transition”。用户认可这个科学问题更好，但认为 SWOT wind speed 的主资料地位必须保留。

## 关键输出

在 `projects/p01/` 下形成并更新 D0 工作包：

- `README.md`：英文项目卡片，保留新版科学问题，同时明确 SWOT wind speed 为 primary atmospheric response field。
- `analysis/analysis_plan.md`：中文分析计划，说明配准、滤波、SWOT 风速动能、耦合系数和谱分析路线。
- `analysis/data_sources.md`：中文数据源说明，明确核心观测三元组和辅助对照数据。
- `literature/literature_seed.md`：中文文献种子清单，保留英文文献信息以便 DOI 核验。
- `literature/P01_discussion_note_zh.md`：中文讨论材料，解释为什么 README 可采用新版科学问题，但 SWOT wind speed 仍应作为主风场资料。
- `logs/2026-06-05_D0_topic_proposal.md`：本 AI 交互日志。

## 人工判断

这个项目最有力的叙事不是简单绘制风速动能分布，而是：

1. 使用新版 scale-dependent regime-transition 问题提升科学高度；
2. 使用 SWOT wind speed 作为细尺度风速响应的核心观测；
3. 使用 GOES/Himawari SST 解释西边界流区域风速动能增强是否与亚中尺度 SST-front coupling 有关；
4. 使用 ASCAT/ERA5/CCMP 作为传统产品对照，说明传统风产品可能平滑或遗漏哪些结构；
5. 使用 SWOT SSH 作为动力结构锚点，判断 SSH gradients、fronts、filaments 和 wind-speed response 是否空间协同。

## 主要风险

- SWOT wind speed 质量需要单独核查，包括降雨污染、海况影响、sigma0 retrieval uncertainty、swath-edge effects 和陆地污染。
- SWOT wind speed 是风速大小，不是矢量风；初始阶段不纳入 wind stress curl/divergence 或 downwind/crosswind 分解。
- ASCAT/ERA5/CCMP 可以辅助机制解释，但不应替代 SWOT 支撑 2-10 km 亚中尺度风速响应。
- 西边界流区域风速动能增强可能同时受到大尺度大气强迫和海洋锋面诱导耦合影响，机制必须检验而不能预设。
- AI 推荐文献必须人工核验后再引用。
