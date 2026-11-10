---
id: "software-intercom-fin"
title: "Intercom Fin：76% 的解决率，以及这个数字的三种口径"
company: "Intercom"
company_hq: "US"
industry: "software-internet"
sub_industry: "saas"
scenario: ["customer-support"]
pattern: ["deflection-agent"]
deployment_model: "vendor-saas"
fde_involved: "none"
ai_tech: ["LLM", "RAG", "agent"]
vendor: ["Intercom（自研 Fin Apex 模型）"]
scale: "12,000+ 客户（官网口径）；单个大客户如 Anthropic 月解决 56 万次"
start_date: "2023"
status: "scaled"
evidence_grade: "C"
last_verified: "2026-11-09"
metrics:
  - name: "平均解决率（resolution rate）"
    value: "76%（官网）/ 65%（自有学习中心）"
    unit: "%"
    baseline: "未披露（无对照组）"
    method: "厂商自算，基于其平台上客户的对话；「解决」的定义由厂商制定，未公开审计方法与抽样规则"
    window: "2026"
    direction: "quality-up"
  - name: "解决率的时间序列"
    value: "51% → 66% → 76%"
    unit: "%"
    baseline: "2024-10 的 51%（当时称 out of the box）"
    method: "厂商逐年披露：2024-10 为 51%（数千客户、数百万对话），2025-10 为 66%（6,000+ 客户），2026-09 起为 76%（12,000+ 客户）"
    window: "2024-10 ~ 2026-11"
    direction: "quality-up"
  - name: "分母口径变更（关键）"
    value: "Resolution Rate: Will increase"
    unit: "口径"
    baseline: "变更前分母含 Fin Constrained（Fin 在场但没机会回答）的会话"
    method: "厂商帮助中心 2026-08-31 公告，自行宣布把 Fin Constrained 移出分母；官方举例：1,000 会话中解决 250，旧口径 250÷750=33%，新口径 250÷500=50%"
    window: "2026-08-31 起"
    direction: "quality-up"
  - name: "客户规模"
    value: "12,000+ / 8,000+"
    unit: "家"
    baseline: "不适用"
    method: "同一厂商不同页面给出两个数字，时点不同"
    direction: "adoption"
  - name: "Anthropic 单月解决量"
    value: "约 56 万次，解决率约 79%"
    unit: "次/月"
    baseline: "未披露"
    method: "Anthropic 支持负责人 Isabel Larrow 在 Intercom 客户页的引语；单方证言"
    direction: "volume-up"
sources:
  - id: "src-intercom-home-2026"
    type: "official-case-study"
    grade: "C"
    url: "https://www.intercom.com/"
    publisher: "Intercom"
    published: "2026"
    accessed: "2026-11-09"
    note: "官网：Fin 平均解决率 76%，覆盖 12,000+ 客户，部分超过 85%"
  - id: "src-intercom-pricing-2026"
    type: "official-case-study"
    grade: "C"
    url: "https://www.intercom.com/learning-center/ai-customer-service-agent-pricing-comparison"
    publisher: "Intercom"
    published: "2026"
    accessed: "2026-11-09"
    note: "定价页：8,000+ 客户平均 76%，每月约提升 1 个百分点；$0.99/解决；25 万次/月以上客户可获 65% 解决率保证，未达标赔付 100 万美元"
  - id: "src-fin-ai-accuracy"
    type: "official-case-study"
    grade: "C"
    url: "https://fin.ai/learn/ai-customer-service-agent-accuracy"
    publisher: "Fin（Intercom 旗下）"
    published: "2026"
    accessed: "2026-11-09"
    note: "同一厂商的学习中心页写「65% avg, up to 93%」，并称行业真实解决率区间为 60–86%，高于此应怀疑定义"
  - id: "src-intercom-metrics-update"
    type: "official-case-study"
    grade: "C"
    url: "https://www.intercom.com/help/en/articles/15599377-update-to-fin-performance-metrics"
    publisher: "Intercom Help"
    published: "2026-08-31"
    accessed: "2026-11-10"
    note: "厂商自行公告改变分母：把 Fin Constrained 移出解决率计算，并明写 Resolution Rate: Will increase。本库最重要的口径证据。"
  - id: "src-intercom-fin-outcomes"
    type: "official-case-study"
    grade: "C"
    url: "https://www.intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes"
    publisher: "Intercom Help"
    published: "2026-09-23"
    accessed: "2026-11-10"
    note: "定义「解决」= 客户确认满意（confirmed）或直接关闭对话未再求助（assumed）；后者也算解决并计费。"
  - id: "src-fin-blog-2024"
    type: "company-blog"
    grade: "C"
    url: "https://www.intercom.com/blog/fin-2-powered-by-anthropic-claude-llm/"
    publisher: "Intercom（Des Traynor）"
    published: "2024-10-10"
    accessed: "2026-11-10"
    note: "51% 的原始出处；同篇承认其他厂商可通过挑选客户与行业给出更高数字。"
  - id: "src-fin-blog-2025"
    type: "company-blog"
    grade: "C"
    url: "https://www.intercom.com/blog/whats-new-with-fin-3"
    publisher: "Intercom（Declan Ivory）"
    published: "2025-10-15"
    accessed: "2026-11-10"
    note: "66% 的原始出处；同篇自我提醒「66% 的解决率不等于替你做了 66% 的工作」。"
  - id: "src-salesforce-acquires-fin"
    type: "official-press-release"
    grade: "A"
    url: "https://salesforce.com/news/press-releases/2026/09/10/salesforce-completes-acquisition-of-fin"
    publisher: "Salesforce"
    published: "2026-09-10"
    accessed: "2026-11-10"
    note: "收购完成（约 36 亿美元）。此后 Fin 的指标口径并入 Salesforce 披露体系，不再独立。"
tags: ["metric-definition-war", "vendor-sourced-number", "human-review"]
replicability: 2
human_in_loop: "escalation-only"
confidence_notes: "全部数字由厂商定义并自算，「解决率」无行业统一口径；同一厂商不同页面给出 65% 与 76% 两个均值"
---

## 1. 一句话摘要

Intercom 的 Fin 是客服 AI 里公开数据最多的产品，也是最值得研究"指标如何被定义"的样本：同一家公司，三个页面，给出了 65%、76%、93% 三个解决率。

## 2. 业务痛点

SaaS 公司的客服成本随客户数线性增长：

- 一线咨询高度重复（退款、账单、账号、订单状态）
- 多语言、多时区导致人力排班困难
- 人工解决时长以十分钟计，客户等待时间长
- 外包客服质量不稳定，品牌风险高

## 3. AI 应用场景

```
输入：客户在 chat/email/phone/Slack 的咨询 + 企业知识库与流程文档
  ↓
处理：检索企业知识 → 多阶段校验（检索—重排—对照原文验证）→ 生成答复；
      必要时调用工具执行动作（改地址、退单、查物流）
  ↓
输出：答复或已完成的动作
  ↓
人工动作：超出置信度或涉及例外时转人工；企业侧做抽样质检
```

人机分工是"AI 处理标准流程，人工只接例外"——这决定了它的成本结构。

## 4. 落地方式

- **形态**：SaaS，按"解决"（outcome）计费，$0.99/次；可与 Zendesk、Salesforce、HubSpot 等既有工单系统共存
- **交付方**：无 FDE 驻场，标准产品 + 客户自助配置（Simulations 用于上线前压测）
- **厂商的风险承诺**：月对话量 25 万次以上的客户，若解决率未达 65%，赔付 100 万美元——这是本库少见"厂商为指标下注"的情况，值得单独记一笔
- **扩散方式**：平台内客户互相参照（Anthropic、Clay、Lightspeed 等作为背书客户）

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 平均解决率 | 76% | 厂商自算，无对照，定义未公开 | 官网 / 定价页 |
| 平均解决率（另一页） | 65%，最高 93% | 同上 | fin.ai 学习中心 |
| 客户数 | 12,000+ / 8,000+ | 两个页面不一致 | 官网 / 定价页 |
| Anthropic 用量 | 约 56 万次/月，约 79% | 客户高管引语 | Intercom 客户页 |
| 厂商承诺线 | 65%（未达标赔 100 万美元） | 仅适用 25 万次/月以上客户 | 定价页 |

### 解决率的三年时间线，以及中间的换尺子

| 时间 | 数字 | 原文 | 口径 |
|---|---|---|---|
| 2024-10-10 | **51%** | "an average resolution rate of 51% across thousands of Intercom customers and millions of conversations" | 全体客户平均，称 out of the box（未调优） |
| 2025-10-15 | **66%** | "its average resolution rate has continued to climb to 66% across our 6,000+ customers. Over 20% of our customers are getting above 80%" | 全体客户平均 |
| **2026-08-31** | **换尺子** | "Resolution Rate: Will increase, because Fin Constrained conversations are no longer counted in the denominator" | 分母剔除"Fin 在场但没机会回答"的会话 |
| 2026-09-10 | **76%** | "achieving an industry-leading average resolution rate of 76%" | Salesforce 收购完成稿照搬 |
| 2026-11（当前） | **76%** | "Fin customers average a 76% resolution rate, across 12,000+ businesses" | 全体客户平均 |

厂商自己在帮助中心给出的算例最清楚：1,000 个会话里 Fin 解决了 250 个，旧口径分母 750 → **33%**；新口径分母 500 → **50%**。同一批对话，换分母，数字涨 17 个百分点。

**第二重换尺子：什么算"解决"。** 帮助中心的定义是：客户在 Fin 最后一次回答后（a）确认满意，或（b）**直接关掉对话、没再求助**——后者叫 "Assumed Resolution"，同样算解决并计费。也就是说，客户什么反应都没有，也可能被算作"已解决"。

**第三重：厂商自己早就警告过。** 2025-10 的博客里写着："if Fin is resolving 66% of your queries, it isn't yet doing 66% of the work for you." 2024 年 Fin 2 发布时更直白："we too can selectively sample certain customers or certain verticals and give you a far higher number."

**一个必须知道的事实**：Salesforce 已于 **2026-09-10** 完成对 Fin 的收购（约 36 亿美元），Intercom 改名 Fin。当前主推的 76% 出现在收购完成前后，此后该指标并入 Salesforce 的披露体系，不再有独立第三方视角。

## 6. 不可验证或存疑之处

1. **"解决率"没有行业统一定义。** 同一段对话，算"AI 答复且客户未再追问"、"AI 关闭工单"、还是"客户确认解决"，结果能差 20 个百分点。厂商自己也在学习中心里承认："高于 86% 的数字应被审视其定义。"
2. **65% 与 76% 同时存在。** 可能是不同时点（每月提升 1 个百分点）、不同客户口径（8,000 vs 12,000），也可能一个是"平均"一个是"承诺下限"。厂商未解释。
3. **无对照组。** 没有"同一批客户不用 AI 时的解决率"作比较。部分对话本来就会被自助帮助中心解决，AI 只是接手了这部分。
4. **样本自选择。** 愿意接入 AI 客服的客户，本身工单结构更标准化。
5. **客户证言不可核。** Anthropic 的 79% 由客户支持负责人给出，无内部数据佐证。
6. **成本对比缺失。** $0.99/解决 与人工单次成本的对比未披露。若人工单次成本是 $5，AI 看起来极便宜；若人工单次是 $1.2（低成本地区外包），账就不一样了。

## 7. 可复用要点

1. **先定义"解决"，再谈解决率。** 建议同时看：客户是否在 48 小时内重复联系、CSAT、工单重开率。
2. **用厂商承诺线当压测目标。** 65% 的赔付门槛，比 76% 的宣传均值更适合做立项假设。
3. **把"能执行动作"作为分水岭。** 只能回答的机器人与能改地址、能退单的机器人，价值差一个量级。
4. **抽样质检不能省。**  escalation-only 模式下，错误答复会直接触达客户。
5. **注意规模门槛。** 赔付保证只对月对话量 25 万次以上的客户开放，中小企业拿不到这个承诺。

## 8. 引用边界

✅ 可以说：
- "Intercom 称其 AI 客服 Fin 的平均解决率为 76%，覆盖约 8,000–12,000 家客户（厂商自算，无第三方审计）"
- "该公司对月对话量 25 万次以上的客户承诺 65% 解决率，未达标赔付 100 万美元"
- "Anthropic 的支持负责人称其每月由 Fin 解决约 56 万次咨询，解决率约 79%"

❌ 不能说：
- "AI 客服平均能解决 76% 的咨询"（这是单一厂商客户群的数据，不是行业均值）
- "客服成本因此下降 76%"（解决率不等于成本下降比例）
- "Anthropic 裁掉了客服团队"（无任何证据）
- 把 93% 当行业上限引用（那是厂商自述的单客户峰值）

## 9. 来源

- Intercom 官网首页（2026 访问）：Fin 平均解决率 76%，12,000+ 客户
- Intercom 学习中心《AI Agent Pricing》（2026）：8,000+ 客户平均 76%，每月 +1pp；$0.99/outcome；65% 保证
- fin.ai《AI Customer Service Agent Accuracy》（2026）：65% avg, up to 93%；行业真实区间 60–86%
- Intercom 客户页：Anthropic 案例引语（Isabel Larrow, Head of AI Support）
