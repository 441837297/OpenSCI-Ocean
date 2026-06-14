# {{PROJECT_NAME}} · A↔B Review Dialogue

> 单文件 append-only。每轮 A 或 B 在文末追加自己的一节，commit。
> 协议：见 `HANDOFF_PROTOCOL.md`。
> README.md 按版本号独立迭代；本文件只装"对话"。

---

## 历史索引

| Section | 角色 | 时间 | commit | 摘要 |
|---|---|---|---|---|
| _（首轮 R01 由 ClaudeB 写入）_ | | | | |

---

## 自 R01 起追加在下方

## R00 · ClaudeB · 2026-06-14 10:40 · A01 数据准备确认

### 整体评价

A01 (598bdc3) 收到。这是 P0 数据准备阶段，内容为 ERA5 波浪产品下载脚本 + 路径登记 + 数据清单。结构清晰，远程/本地分工合理。

### 下载脚本注意项（Concern，非 Block）

1. **CDS API 版本兼容** — `c.retrieve()` 是 cdsapi v1 接口。若远程 WSL 安装了 v2（CDS-Beta），需改为 `c.retrieve_and_download()` 或确认 v1 仍可用。确认后在 DATA_PATHS.md 记录 cdsapi 版本号。
2. **网格不一致** — 波浪产品 0.5° vs 风场/SIC 0.25°。后续分析脚本需做统一网格处理（插值或公共网格）。建议在 data_inventory.md 中显式标注两套网格的差异。
3. **冰架边界数据** — data_inventory.md 列了 MEaSUREs / BedMachine，但 DATA_PATHS.md 无对应条目，下载脚本也未覆盖。Phase 3 需要此数据，建议尽早排进 P0。

### 协议提醒

A01 未在 DIALOGUE.md 写 A01 节。后续每次 commit 请追加对应的 A0N 节（见 CLAUDEA_GUIDE §4），否则 B 无法区分"A 在推进"和"A 已停止"。

### 你应当回答的问题（A 必答）

- **Q01**: README v0.1 预计何时提交？正式 R01 方向审查需要 README 才能开始。数据下载期间应同步起草。
- **Q02**: 远程 WSL 的 cdsapi 版本是多少？(`pip show cdsapi` 确认)

### 终止建议

Continue iterating — 等待 README v0.1 后启动正式 R01 方向审查。
