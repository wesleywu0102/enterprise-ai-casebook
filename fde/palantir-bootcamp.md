# Palantir 的 Bootcamp：FDE 的原始形态，与一组互相矛盾的数字

**证据等级：B（模式与官方表述）/ 无（转化率，溯源失败）**
**核实日期：2026-11-10（本节已按一手来源重写，修正了此前版本的三处错误）**

---

## 一、Bootcamp 是什么

AIP Bootcamp 是 Palantir 的获客与交付合一机制，官方描述是：

> "From 0 to use case in 5 days."
>
> "Run a five-day AIP Bootcamp to: 1 / Understand how to apply AI to mission-critical operations 2 / Develop initial use cases in the software 3 / Onboard and train users for rollout in operations"

早期官方博客的口径更宽（2023-10-12）："participants can expect to go from zero to use case in just one to five days"。

流程大致是：

```
潜在客户报名 → 3–5 天驻场工作坊（用客户自己的真实数据）
  → 现场搭出可运行的 AI 工作流 → 当场判断值不值得买
  → 转化：签小额合同 → 扩展为平台 license + 长期驻场
```

关键设计：**不先讲 PPT，先让客户用自己的数据跑一遍。**

## 二、FDE 在其中的角色

Palantir 的 FDE 是这套机制的劳动力基础：驻场工程师直接写代码、接数据、建本体（Ontology）模型，交付物是"可复制的编排逻辑"而非一次性系统。这也是 Palantir 能把服务当获客成本、靠后续 license 回收的结构性原因。

## 三、转化率：溯源失败，不引用任何单一数字

**这是本文最重要的一节。我在此前的版本里写下了"Q1 2026 转化率 70%+""21%→34%"等数字，均来自二手转述。2026-11-10 的复核结论是：这些数字一个都追不到官方原文，且互相矛盾。**

检索到的所有"转化率"来源均为二手站点，给出的数字互斥：

| 流传说法 | 声称的来源 | 复核结果 |
|---|---|---|
| 约 70%（680+ 场） | "Karp 在财报电话会" | 官方致股东信、官网、官方博客中均无对应表述 |
| 约 30–40%（1,300+ 场） | 二手分析 | 同上，无法溯源 |
| 约 75%（2024 年 915 场） | 二手媒体 | 同上；且 915 与 680 两个场次数也互斥 |

**判定：转化率溯源失败。本库禁止引用任何单一转化率。**

另外，我此前写的"2025 年初约 200 场""Q1 2026 已举办 680 场以上"也站不住。**官方唯一给过的硬数字是 Q1 2024 致股东信里的这句话：**

> "In the last quarter alone, we conducted **more than 660 bootcamps** with organizations across industries and sectors."

注意这是**单季举办场次**，不是累计客户数，更不是转化率。把它写成"累计服务 660 家客户"是错的。

## 四、可验证的部分

| 事实 | 数值 / 表述 | 来源 | 等级 |
|---|---|---|---|
| 单场时长 | 5 天（官方页）；早期口径 1–5 天 | Palantir 官网 / 官方博客 2023-10-12 | B |
| 单季场次 | 2024 年 Q1 超过 660 场 | Palantir Q1 2024 致股东信 | A |
| 官方三步目标 | 理解场景 → 在软件里搭出用例 → 培训用户准备推广 | Palantir 官网 | B |
| 转化率 | **无官方披露** | — | 无 |

**最常见的升格表述**：把"5 天出一个 use case"写成"5 天交付生产级 AI 系统"。官方三步目标里没有任何一步是"上生产"。

## 五、"AI FDE"：FDE 自己被自动化？

Palantir CTO 的公开表述是，其 **AI forward-deployed engineer**（一个能执行复杂软件迁移任务的 agent）已能在两周内完成 SAP ERP 从 ECC 到 S/4HANA 的迁移，而这类项目"通常要数年、花费数千万美元"。

这是本专题里最值得追踪、也最需要警惕的一条：

- **值得追踪**：如果成立，FDE 的产能瓶颈（人力）会被打破，整个交付经济学改写
- **需要警惕**：目前只有高管口述，无客户案例、无第三方验证、无失败率数据。ERP 迁移的难点在数据清洗与业务规则映射，不在代码转换——"两周"很可能指某个特定环节

**写作建议**：写成"一个待验证的宣称"，并给出验证条件（是否公布具体客户、迁移后账务一致性如何验证）。不要写成"AI 已经能两周迁移 SAP"。

## 六、可复用要点

1. **把 POC 压缩成工作坊，是 B2B AI 最有效的销售创新之一。** 客户用自己的数据看到结果，比任何 demo 有说服力。
2. **驻场工程师的产出必须是"可复制的编排"，不是"能跑的 demo"。** 否则第二个客户要重新做一遍。
3. **服务毛利低不是问题，前提是能转化为 license。** 转不了，就是纯外包。
4. **警惕任何没有原文的转化率。** 连场次数都能出现 660/680/915/1,300 四个版本，转化率更不可信。

## 七、引用边界

✅ 可以说：
- "Palantir 的 AIP Bootcamp 官方定位是'5 天从 0 到一个用例'，包含理解场景、搭建初步用例、培训用户三步，官方没有承诺 5 天上线生产"
- "据其 2024 年 Q1 致股东信，单季举办了超过 660 场 bootcamp"
- "关于 bootcamp 转化率，公开转述有 30–40%、70%、75% 等多个互斥版本，均无法追到官方原文"

❌ 不能说：
- "Palantir bootcamp 转化率 70%/75%"（溯源失败）
- "Palantir 累计服务 660 家客户"（是单季场次）
- "AI 已能两周完成 SAP 迁移"（仅高管宣称，无验证）
- "bootcamp 模式适用于所有企业软件"（它依赖一个能承载客户真实数据的平台底座）

---

**来源**
- Palantir, *AIP Bootcamp*（官网，无日期）— https://www.palantir.com/platforms/aip/bootcamp
  关键句："From 0 to use case in 5 days."
- Palantir Blog, *Deploying Full Spectrum AI in Days: How AIP Bootcamps Work*, 2023-10-12 — https://blog.palantir.com/deploying-full-spectrum-ai-in-days-how-aip-bootcamps-work-21829ec8d560
- Palantir, *Letter to Shareholders (Q1 2024)* — https://www.palantir.com/q1-2024-letter/en
  关键句："In the last quarter alone, we conducted more than 660 bootcamps"
- 关联案例（Palantir FDE 在客户侧的实际交付）：[`../cases/healthcare/tampa-general-palantir.md`](../cases/healthcare/tampa-general-palantir.md)、[`../cases/healthcare/cleveland-clinic-palantir.md`](../cases/healthcare/cleveland-clinic-palantir.md)、[`../cases/public-sector/nhs-fdp-palantir.md`](../cases/public-sector/nhs-fdp-palantir.md)、[`../cases/retail/wendys-qscc-palantir.md`](../cases/retail/wendys-qscc-palantir.md)
