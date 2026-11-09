---
id: "financial-adt-sierra-agent"
title: "ADT：聊天拦截率 45%→60%，按结果付费的客服代理"
company: "ADT Inc."
company_hq: "US"
industry: "financial-services"
sub_industry: "security-services"
scenario: ["customer-support", "sales-enablement"]
deployment_model: "vendor-saas"
fde_involved: "vendor-embedded"
ai_tech: ["LLM", "agent", "ASR"]
vendor: ["Sierra", "Google Cloud"]
scale: "全美客服渠道（聊天 + 电话）；具体进线量未披露"
start_date: "2025"
status: "production"
evidence_grade: "A"
last_verified: "2026-11-10"
metrics:
  - name: "聊天拦截率（chat containment）"
    value: "45% → 60%"
    unit: "%"
    baseline: "2026 Q1 季内 45%"
    method: "CEO 在财报电话会披露；containment 未定义，分母未说明"
    window: "2026 Q1 ~ 2026-04 底"
    direction: "adoption"
  - name: "电话拦截率（call containment）"
    value: "16% → 25%"
    unit: "%"
    baseline: "2026 Q1 季内 16%"
    method: "同一份电话会披露；电话渠道口径未定义，且录音场景本身比文字更难被 AI 完整处理"
    window: "2026 Q1 ~ 2026-04 底"
    direction: "adoption"
sources:
  - id: "src-adt-q1-2026-call"
    type: "earnings-call"
    grade: "A"
    url: "https://equibles.com/stocks/adt/calls/2026-q1"
    publisher: "ADT Inc.（电话会转录）"
    published: "2026-04-30"
    accessed: "2026-11-10"
    note: "CEO Jim DeVries 原话给出 45%/60%（聊天）与 16%/25%（电话），并点名 Sierra 与 Google 为伙伴。"
  - id: "src-benzinga-adt-q1-2026"
    type: "media-report"
    grade: "D"
    url: "https://www.benzinga.com/insights/news/26/04/52176242/full-transcript-adt-q1-2026-earnings-call"
    publisher: "Benzinga"
    published: "2026-04"
    accessed: "2026-11-10"
    note: "同一电话会的另一份转录，用于交叉核对数字。"
  - id: "src-sierra-outcome-pricing"
    type: "company-blog"
    grade: "C"
    url: "https://sierra.ai/uk/blog/outcome-based-pricing-for-ai-agents"
    publisher: "Sierra"
    published: "2024-12-10"
    accessed: "2026-11-10"
    note: "厂商自述按结果收费：「未解决多数情况下不收费」，但保留 in most cases 的例外口子。"
tags: ["fde-model", "voice-interface", "metric-definition-war", "human-review"]
replicability: 3
human_in_loop: "escalation-only"
confidence_notes: "拦截率（containment）不等于解决率，且 ADT 未定义分母；45%→60% 是四个月内的爬坡值，不是年度均值"
---

## 1. 一句话摘要

ADT 用 Sierra 的 AI 代理接客服，2026 年一季度聊天拦截率 45%、四月底升到 60%，电话拦截率从 16% 升到 25%——这是"按结果付费"模式少见的客户方季度数据。

## 2. 业务痛点

ADT 是北美最大的安防服务商，客服结构有两个特点：

- **季节性极强**：搬家季、促销期进线量激增，临时招人成本高
- **大量低复杂度咨询**：账单、设备离线、密码重置、套餐变更占多数
- **高危场景并存**：真报警、设备故障需要人判断，不能交给机器

疫情期间 ADT 曾公开说过呼叫中心压力，之后开始系统性引入自动化。

## 3. AI 应用场景

```
输入：客户在 chat 或电话中的诉求 + 账户/设备/账单上下文
  ↓
处理：意图识别 → 自助解决（改套餐、重置密码、排查离线设备、
      预约上门）→ 无法处理时带上下文转人工
  ↓
输出：答复或已完成的动作；转人工时人工坐席直接看到上下文
  ↓
人工动作：只接例外与高风险事件；事后抽样质检
```

电话渠道比聊天难得多——口音、噪音、老年用户，所以电话拦截率（25%）明显低于聊天（60%）。

## 4. 落地方式

- **供应商**：Sierra（AI 代理）+ Google Cloud（基础设施/模型）；ADT 在电话会里点名称赞了两家伙伴
- **收费模式**：按结果计费。Sierra 官方说法是"解决的对话才收费，未解决多数情况不收费"，但保留 "in most cases" 的例外；也承认路由类交互更适合按次计费
- **交付形态：厂商工程团队深度陪跑。** Sierra 公开描述部署初期会与其 agent 工程师逐轮迭代，但无合同条款证明"驻场"。本库按 `vendor-embedded` 记录
- **上线节奏**：2025 年起推进，2026 Q1 开始披露量化指标

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 聊天拦截率 | 45% → 60% | 2026 Q1 均值 vs 4 月底；分母未定义 | ADT Q1 2026 电话会 |
| 电话拦截率 | 16% → 25% | 同上 | 同上 |

这是本库唯一"客户方在财报场合给出季度爬坡曲线"的客服 AI 案例，证据等级优于任何厂商 case study。

## 6. 不可验证或存疑之处

1. **containment ≠ resolution。** 拦截率只表示"没有转人工就结束了"，不代表问题真被解决。客户可能放弃、可能稍后再来。
2. **分母未定义。** 是全部进线，还是只算进入 AI 队列的会话？是否剔除了"本来就不该由 AI 接"的流量？ADT 没说。
3. **四个月爬坡值不等于稳态。** 45%→60% 很可能是上线初期调优带来的快速提升，长期能否维持未知。
4. **没有 2025 年同期基线。** 无法判断是否本来就有季节性改善。
5. **同一场电话会另有更宽的口径。** ADT 称"今年大部分呼叫中心来电将由 AI 处理"，那是路由/分流目标，与 25% 的实际拦截率不是一回事，二手转述常混用。
6. **Sierra 的"按结果收费"有例外。** 官方原文是 "in most cases, there's no charge"，不是绝对承诺。

## 7. 可复用要点

1. **聊天先上、电话后上。** 文字渠道的容错率高，电话涉及口音与实时性，拦截率天然低一半以上。
2. **转人工必须带上下文。** 否则拦截率提升会被人工作业量抵消。
3. **用季度曲线看进展，不用单点看结论。** 45%→60% 这种四个月的变化，比"平均 60%"更有信息量。
4. **按结果付费适合高重复、可判定的场景。** 如果"是否解决"难以判定（如安防咨询），计费争议会很多。

## 8. 引用边界

✅ 可以说：
- "ADT 在 2026 年一季度财报电话会披露，其聊天渠道 AI 拦截率为 45%，到 4 月底升至 60%；电话渠道从 16% 升至 25%"
- "ADT 将 Sierra 与 Google 列为该项目的合作伙伴"
- "Sierra 采用按结果计费模式，未解决的对话多数情况下不收费"

❌ 不能说：
- "AI 解决了 ADT 60% 的客服问题"（拦截率不是解决率）
- "ADT 因此减少了 45% 的客服人力"（未披露人力数据）
- "电话渠道也有 60% 由 AI 处理"（电话是 25%）
- "Sierra 对所有未解决对话都不收费"（原文是 in most cases）

## 9. 来源

- ADT Inc., *Q1 2026 Earnings Call Transcript*, 2026-04-30
  关键句："Our chat containment in Q1 was 45%, and at the end of April, it's 60%. Call containment was 16% for the first quarter. By the end of April, it was 25%."
- Sierra, *Outcome-based pricing for AI agents*, 2024-12-10
  关键句："If the conversation is unresolved, in most cases, there's no charge."
