---
id: "retail-wendys-qscc-palantir"
title: "Wendy's 供应链合作社：5 分钟替代 15 人一天"
company: "Quality Supply Chain Co-op (QSCC)"
company_hq: "US"
industry: "retail"
sub_industry: "restaurant-supply-chain"
scenario: ["supply-chain", "scheduling-optimization"]
deployment_model: "platform-build"
fde_involved: "unknown"
ai_tech: ["digital-twin", "agent"]
vendor: ["Palantir"]
scale: "服务美国与加拿大 6,400+ 家门店；34 个配送中心、250+ 发货点、3,500 辆运输资产"
start_date: "2024"
status: "production"
evidence_grade: "C"
last_verified: "2026-11-10"
metrics:
  - name: "单次糖浆短缺的处理耗时"
    value: "5 分钟"
    unit: "分钟"
    baseline: "一年前需 15 人一整天（约 120 人时）"
    method: "合作社总裁兼 CEO 在 Palantir 客户大会上的口述；n=1 单次事件，非统计期均值"
    window: "2024 ~ 2025-04"
    direction: "time-down"
  - name: "预警时点（反事实）"
    value: "提前 48–72 小时"
    unit: "小时"
    baseline: "假设无系统时的发现时点"
    method: "客户高管口述的反事实假设，不是实测对比；不可作为实测成效"
    window: "2025"
    direction: "time-down"
  - name: "投资回报（前瞻估计）"
    value: "8–10 倍"
    unit: "倍"
    baseline: "未披露"
    method: "客户高管对媒体的预估，明确用词是 over time；非实测、非审计"
    window: "2025-03"
    direction: "cost-down"
sources:
  - id: "src-palantir-wendys-2024"
    type: "official-press-release"
    grade: "B"
    url: "https://investors.palantir.com/news-details/2024/From-the-Farm-to-the-Frosty-Palantir-and-Wendys-Partner-on-AI-and-Supply-Chain-Digitalization/"
    publisher: "Palantir / Business Wire（QSCC 联合署名）"
    published: "2024-08-07"
    accessed: "2026-11-10"
    note: "合作公告。原文用将来时 will be moving onto AIP，常被媒体写成「已上线见效」。"
  - id: "src-pymnts-palantir-2025"
    type: "media-report"
    grade: "D"
    url: "https://www.pymnts.com/news/artificial-intelligence/2025/palantir-reinvents-wendys-supply-chain-network-walgreens-operations/"
    publisher: "PYMNTS"
    published: "2025-04-29"
    accessed: "2026-11-10"
    note: "转述 QSCC CEO 在 Palantir 客户大会的演讲：5 分钟 vs 15 人一天、6,450 家门店等网络规模。"
tags: ["fde-model", "vendor-sourced-number", "co-delivery"]
replicability: 3
human_in_loop: "escalation-only"
confidence_notes: "核心数字来自供应商大会舞台上的客户口述，n=1，无审计、无门店级对照；且签约主体是合作社 QSCC 而非 Wendy's 公司"
---

## 1. 一句话摘要

Wendy's 体系的供应链合作社把运输、配送中心、门店库存做成一张实时数字孪生图，一次糖浆短缺从"15 人打一天电话"变成"5 分钟处理完"——但这是供应商大会上讲的一个故事，不是统计结果。

## 2. 业务痛点

快餐连锁的供应链有两层复杂度：

- **门店层**：6,400+ 家门店，多数是加盟店，订货行为分散且受促销剧烈影响
- **网络层**：34 个配送中心、250+ 发货点、3,500 辆运输资产，任何一环延误都会在几天后变成门店缺货

Wendy's 的特殊之处是采购由独立的合作社 QSCC 统一负责，因此它的痛点是**跨组织的信息延迟**：门店发现缺货 → 报给加盟商 → 报给合作社 → 合作社问配送中心 → 配送中心查库存 → 再回传。每一跳都是电话和邮件。

## 3. AI 应用场景

```
输入：配送中心库存、在途运输、门店订货与销售、促销计划
  ↓
处理：AIP 上搭建供应链数字孪生 → 实时比对"应有库存 vs 实际库存"
      → 识别异常缺口并生成调拨方案
  ↓
输出：缺货预警 + 建议调拨路径（哪个仓、调多少、走哪条线）
  ↓
人工动作：供应链团队确认方案并执行，与供应商/承运商沟通
```

官方举的例子是 2024 年一次糖浆短缺（Frosty 用糖浆，与 Thin Mints 联名促销相关）：系统在缺口扩散前定位到具体批次和仓库。

## 4. 落地方式

- **供应商**：Palantir，AIP 平台
- **分两阶段**：第一阶段做供应链网络可视化与决策，第二阶段做动态库存管理、门店差异化信息和需求偏差分配
- **交付形态：未明确为 FDE。** 官方材料没有出现 "forward deployed" 表述；英国《泰晤士报》的报道写法是 "Palantir's engineers helped Wendy's to organise its data"，属工程师深度参与，但不足以判定为 FDE 驻场。本库按 `unknown` 处理
- **时间线需要注意**：2024-08 的联合稿用的是将来时（"will be moving onto AIP"）；到 2025-04，客户高管已经在描述运行中的系统和实时告警。**没有任何一方给出正式的 go-live 日期**

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 糖浆短缺处理耗时 | 5 分钟 | 客户高管口述，单次事件；对比"一年前 15 人一天" | PYMNTS 2025-04-29 |
| 网络覆盖 | 6,450 家门店 / 34 个 DC / 3,500 辆运输资产 | 客户高管给出的规模，非成效 | 同上 |
| 预警提前量 | 48–72 小时 | 反事实假设，非实测 | 同上 |
| 投资回报 | 8–10 倍（over time） | 前瞻预估，非实测 | 泰晤士报专访（2025-03） |

严格说，这里**只有一个可引用的成效数字**，就是一个 n=1 的案例耗时。其余都是规模或预估。

## 6. 不可验证或存疑之处

1. **主体错位。** 签约方是 Quality Supply Chain Co-op（QSCC），是 Wendy's 体系内独立运营的采购合作社，不是 The Wendy's Company。写"Wendy's 与 Palantir 合作"在严格意义上不准确；我也没找到 Wendy's 公司层面的投资者关系稿。
2. **全部成效来自供应商大会舞台。** 没有客户官网案例页、没有财报披露、没有第三方审计。"5 分钟 vs 一天"是同一事件的人工/系统前后对比，不能外推为整体库存周转改善。
3. **"提前 48–72 小时"是反事实。** 客户的原话是"如果没有这套系统，我们会晚这么久才发现"，这属于假设性推断，不是测量值。
4. **阶段被混淆。** 2024-08 的公告是"将迁移到 AIP"，中文转述里大量出现"已上线并降本 XX%"。实际上到 2025 年 4 月才有运行中的证据。
5. **ROI 8–10 倍没有算法。** 既没说分母（投入多少），也没说分子包含哪些项（缺货损失？库存占用？人工时？）。

## 7. 可复用要点

1. **从"一次具体事故"开始做案例。** 这个项目最有说服力的地方不是百分比，而是"某天某款糖浆差点断供，系统 5 分钟定位"。讲故事比讲均值有效，但要标明这是单个案例。
2. **数字孪生先解决"看得见"，再解决"算得准"。** 第一阶段只做可视化与告警，就已经产生价值。
3. **跨组织流程是主要障碍。** 合作社、加盟商、配送中心、供应商四方数据口径不一致，比模型难得多。
4. **别把"迁移公告"当"上线公告"。** 这是本库反复拦下的一类错误。

## 8. 引用边界

✅ 可以说：
- "Wendy's 体系的供应链合作社 QSCC 用 Palantir AIP 搭建供应链数字孪生，其总裁在 2025 年 4 月的 Palantir 客户大会上称，一次糖浆短缺的处理时间从'15 人一整天'降到 5 分钟"
- "该网络覆盖约 6,400 家门店、34 个配送中心、3,500 辆运输资产"

❌ 不能说：
- "Wendy's 用 AI 把供应链效率提升了 XX%"（无此类数字）
- "Palantir 帮 Wendy's 省了 X 百万美元"（ROI 只有 8–10 倍的定性预估）
- "这是 FDE 驻场的成功案例"（官方无 FDE 表述，本库按 unknown 处理）
- "提前 48–72 小时预测缺货"（这是反事实，不是预测精度）

## 9. 来源

- Palantir IR / Business Wire, *From the Farm to the Frosty: Palantir and Wendy's Partner on AI and Supply Chain Digitalization*, 2024-08-07
  原文用将来时："will be moving onto Palantir's AIP"
- PYMNTS, *Palantir Reinvents Wendy's Supply Chain Network, Walgreens' Operations*, 2025-04-29
  关键引语："It took Wendy's five minutes to manage the syrup supply issue. A year ago, it would have taken 15 people a full day."
- 注：Business Wire 原始稿当前返回 Page Unavailable，引用以 Palantir IR 转载版为准
