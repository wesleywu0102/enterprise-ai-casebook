---
id: "retail-lowes-mylow"
title: "Lowe's：2,500 万个问题的零售助手，转化率 3 倍"
company: "Lowe's Companies, Inc."
company_hq: "US"
industry: "retail"
sub_industry: "home-improvement"
scenario: ["customer-support", "sales-enablement", "knowledge-retrieval"]
pattern: ["retrieval-knowledge"]
deployment_model: "in-house"
fde_involved: "unknown"
ai_tech: ["LLM", "RAG", "agent"]
vendor: ["OpenAI"]
scale: "1,700+ 家门店（店员端 Mylow Companion）；线上渠道全量"
start_date: "2025"
status: "scaled"
evidence_grade: "A"
last_verified: "2026-11-10"
metrics:
  - name: "累计处理问题数"
    value: "2,500 万+"
    unit: "次"
    baseline: "不适用"
    method: "Lowe's 财报电话会披露；累计值，含顾客与店员两侧"
    window: "截至 2026-07-31"
    direction: "adoption"
  - name: "使用助手的线上顾客转化率"
    value: "3 倍"
    unit: "倍"
    baseline: "不使用 Mylow 的线上顾客"
    method: "公司财报电话会口径；未做对照实验，存在自选择偏差"
    window: "FY2026 Q2"
    direction: "revenue-up"
  - name: "店员端部署门店数"
    value: "1,700+"
    unit: "家"
    baseline: "不适用"
    method: "官方新闻稿；只给范围，无成效数字"
    window: "2025-05-05"
    direction: "adoption"
sources:
  - id: "src-lowes-q2fy26-call"
    type: "earnings-call"
    grade: "A"
    url: "https://corporate.lowes.com/sites/lowes-corp/files/low-usq-transcript-2026-08-19.pdf"
    publisher: "Lowe's Companies, Inc."
    published: "2026-08-19"
    accessed: "2026-11-10"
    note: "FY2026 Q2 电话会逐字稿：2,500 万问题、3 倍转化率。财报电话会陈述可被追责，属 A 级来源。"
  - id: "src-lowes-pr-2025-05"
    type: "official-press-release"
    grade: "B"
    url: "https://corporate.lowes.com/generation/pdf/document-file.pdf?path=/newsroom/press-releases/lowes-deploys-first-scale-ai-assistant-retail-associates-05-05-25"
    publisher: "Lowe's"
    published: "2025-05-05"
    accessed: "2026-11-10"
    note: "部署范围稿（1,700+ 门店），全文无任何成效数字。不能当成效来源用。"
tags: ["fde-model", "co-delivery", "floor-raising", "human-review"]
replicability: 4
human_in_loop: "review-before-send"
confidence_notes: "3 倍转化率是相关性而非因果，Lowe's 未做对照实验；且「2,500 万问题」是累计值，不能当活跃度"
---

## 1. 一句话摘要

Lowe's 与 OpenAI 联合开发了两个 Mylow：一个给顾客做家装规划，一个给 1,700 多家门店的店员回答问题。累计处理 2,500 万个问题，用助手的线上顾客转化率是不用者的 3 倍。

## 2. 业务痛点

家居家装的零售场景有两个特殊难点：

- **决策复杂度高**：一个装修项目涉及测量、材料、工具、施工顺序，顾客往往不知道自己缺什么
- **店员知识门槛高**：水管、电气、木材、园艺跨多个专业，新员工很难在短期内掌握
- **线上转化低**：大件商品客单价高、决策周期长，线上顾问缺位导致流失

Lowe's 的解法是"两个助手"：一个面向顾客做项目规划，一个面向店员做内部知识问答。

## 3. AI 应用场景

```
【顾客侧 Mylow】
输入：自然语言需求（"我要翻新一个 10 平米的浴室"）+ 商品目录与库存
  ↓
处理：理解项目意图 → 拆解所需材料与工具 → 检索可售 SKU 与替代品
  ↓
输出：采购清单 + 施工步骤 + 商品链接
  ↓
人工动作：顾客自行确认；复杂项目转门店设计顾问

【店员侧 Mylow Companion】
输入：店员提问（产品参数、库存位置、跨部门流程）
  ↓
输出：答复 + 系统内操作入口
  ↓
人工动作：店员核对后回复顾客
```

两个助手共用同一套模型能力，但面向的对象、知识库和风险等级不同。

## 4. 落地方式

- **形态**：与 OpenAI 联合开发，Lowe's 自建（in-house），基于 OpenAI 模型
- **是否 FDE 驻场：未披露。** OpenAI 的 FDE 业务页把 Lowe's 列为案例，但 Lowe's 的官方稿与电话会都没有描述交付形态。本库按 `unknown`
- **推广节奏**：线上 Mylow 先行；店员端 Mylow Companion 于 2025-05-05 宣布铺到 1,700 多家门店
- **组织配套**：门店端做了培训与话术改造，把"查手册"变成"问助手 + 核对"

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 累计回答问题 | 2,500 万+ | 累计，含顾客与店员；截至 2026-07-31 | Lowe's Q2 FY2026 电话会 |
| 线上转化率 | 3 倍 | 对比不使用 Mylow 的线上顾客 | 同上 |
| 店员端覆盖 | 1,700+ 门店 | 部署范围，无成效数字 | Lowe's 2025-05-05 新闻稿 |

这是本库少数由**财报电话会**支撑的零售 AI 案例，来源等级最高。

## 6. 不可验证或存疑之处

1. **3 倍是相关性，不是因果。** 愿意用助手的顾客本身购买意向更强（自选择）。Lowe's 没有做对照实验（如随机分流），所以"用助手导致转化率提升 3 倍"无法成立。
2. **2,500 万是累计值。** 不反映当前活跃度，也无法换算成人均使用。它与"每周多少次"完全是两回事。
3. **部署稿没有成效数字。** 2025-05-05 的官方新闻稿只有范围，很多二手文章把"1,700 家门店"当成成效。
4. **OpenAI 页面上的两个数字客户未确认。** 供应商页称店员使用后"顾客满意度提升 200 个基点"、以及某些效率指标，Lowe's 的一手材料里找不到。
5. **成本与人力影响未披露。** 无法判断是否减少了门店人手或培训时长。

## 7. 可复用要点

1. **两个助手、一个模型。** 顾客侧与员工侧分开做产品，但共享能力层，比"一个通用聊天窗"有效得多。
2. **员工侧要接系统，不只接知识。** 能直接查到"这家店 3 号货架有没有货"，比会背产品手册有用。
3. **转化率类指标必须做分流实验。** 否则永远会被质疑自选择，也永远算不出真实增量。
4. **累计问题数适合对外讲规模，不适合对内做验收。** 验收要看每个店的解决时长与会话重开率。

## 8. 引用边界

✅ 可以说：
- "Lowe's 在 FY2026 Q2 财报电话会披露，其 AI 助手 Mylow 累计处理 2,500 万个问题，使用该助手的线上顾客转化率是不使用者的 3 倍（未做对照实验）"
- "店员端 Mylow Companion 于 2025 年 5 月铺到 1,700 多家门店"

❌ 不能说：
- "AI 助手让 Lowe's 线上转化率提升 200%"（3 倍是组间对比，不是提升幅度，也不是因果）
- "Mylow 每天有 2,500 万次使用"（是累计值）
- "这是 OpenAI FDE 驻场交付的"（交付形态未披露）
- "顾客满意度提升 200 个基点"（仅供应商口径，客户未确认）

## 9. 来源

- Lowe's, *Q2 2026 Earnings Call Transcript*, 2026-08-19
  关键句："MyLow … has supported over 25 million questions from customers and associates" / "the conversion rate for online customers who use MyLow is triple that of customers who do not use the tool."
- Lowe's, *Lowe's Deploys First At-Scale AI Assistant for Retail Associates*, 2025-05-05（仅部署范围）
