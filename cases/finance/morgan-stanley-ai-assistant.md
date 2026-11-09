---
id: "financial-morganstanley-ai-assistant"
title: "摩根士丹利：让 98% 顾问团队用上的内部知识助手"
company: "Morgan Stanley"
company_hq: "US"
industry: "financial-services"
sub_industry: "wealth-management"
scenario: ["knowledge-retrieval", "document-processing"]
deployment_model: "vendor-copilot"
fde_involved: "unknown"
ai_tech: ["LLM", "RAG", "ASR"]
vendor: ["OpenAI", "Microsoft Azure"]
scale: "财富管理条线全部顾问团队；约 10 万份研究文档与内部文件语料"
start_date: "2023"
status: "scaled"
evidence_grade: "B"
last_verified: "2026-11-09"
metrics:
  - name: "顾问团队使用率"
    value: ">98%"
    unit: "%"
    baseline: "未披露"
    method: "企业自述；以「顾问团队」为分母，非个人比例；统计方式未公开"
    direction: "adoption"
  - name: "文档可达率"
    value: "20% → 80%"
    unit: "%"
    baseline: "系统上线前可被检索到的文档占比"
    method: "企业自述，原文为 access to documents，未定义统计口径与分母"
    direction: "quality-up"
  - name: "可问答的语料规模"
    value: "7,000 个问题 → 10 万份文档"
    unit: "count"
    baseline: "上线前可覆盖的问题集合"
    method: "企业自述；两个数字单位不同（问题数 vs 文档数），不构成倍数关系"
    direction: "quality-up"
sources:
  - id: "src-openai-morgan-stanley"
    type: "official-case-study"
    grade: "B"
    url: "https://openai.com/index/morgan-stanley/"
    publisher: "OpenAI"
    published: "unknown"
    accessed: "2026-11-09"
    note: "官方案例页，客户高管具名引语；页面未标注发布日期与上线时间，数字均为双方自述，无第三方审计"
tags: ["RAG", "regulated-industry", "zero-data-retention", "evals-in-production", "exec-sponsorship"]
replicability: 3
human_in_loop: "review-before-send"
confidence_notes: "全部数字为企业与厂商共同自述，无第三方核验；上线时间未能从一手页面确认"
---

## 1. 一句话摘要

把 10 万份研究报告和内部文件做成只能"引用公司自有内容"的问答系统，让财富管理顾问查资料从数天缩到数小时——这条案例真正的价值不在模型，而在它上线前的那套评测流程。

## 2. 业务痛点

财富管理顾问每天要回答客户关于税务、遗产规划、产品条款、市场观点的问题，答案散落在：

- 研究报告库（数万份，跨年份、跨资产类别）
- 合规与产品文档
- 内部专家邮件与会议记录
- 客户自身的持仓与沟通历史

痛点不是"没有资料"，而是**找不到、找不全、找到了不敢用**。顾问为了一个合规口径的问题可能要打三个电话。此外，客户会议后的记录整理和 CRM 录入是纯手工，跟进邮件常常延后数天才发出。

## 3. AI 应用场景

**场景 A：AI @ Morgan Stanley Assistant（知识问答）**

```
输入：顾问的自然语言问题
  ↓
处理：在 10 万份内部文档上做检索增强生成（RAG），答案附带原文出处
  ↓
输出：带引用的回答
  ↓
人工动作：顾问核对引用后使用；不得直接对客户原文转发
```

**场景 B：AI @ Morgan Stanley Debrief（会议纪要）**

```
输入：经客户同意的 Zoom 会议录音
  ↓
处理：Whisper 转写 → GPT-4 生成客户纪要 → 自动写入 CRM
  ↓
输出：会议纪要 + 跟进邮件草稿
  ↓
人工动作：顾问审阅修改后发送
```

关键设计：**答案只能从公司自有内容生成**，不使用公开版 ChatGPT 的知识。这是金融合规场景的硬约束。

## 4. 落地方式

- **技术栈**：Azure 上的 OpenAI 模型 + 零数据保留（zero data retention）协议，公司数据不用于训练公开模型
- **评测机制（最值得学的部分）**：
  - 每个用例上线前必须过评测框架
  - 摘要类任务由顾问和提示工程师对准确性与连贯性打分
  - 为 Debrief 构建了覆盖不同会议类型的评测数据集
  - 每日用样本问题跑回归测试，发现薄弱环节
  - 发现准确率不足时，与 OpenAI 一起回调检索方法，而不是换模型
- **组织**：设 Firmwide AI 负责人（Jeff McMillan）统一牵头，产品与架构、生成式 AI 解决方案各有专职负责人
- **交付方**：公开信息未说明是否有厂商 FDE 驻场，标注为 unknown

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 顾问团队使用率 | >98% | 企业自述，分母为"顾问团队" | OpenAI 案例页 |
| 文档可达率 | 20% → 80% | "access to documents"，口径未定义 | 同上 |
| 语料规模 | 10 万份文档 | 企业自述 | 同上 |
| 跟进时效 | "数天 → 数小时" | 定性描述，无具体分布 | 同上（Kaitlin Elliott 引语） |

## 6. 不可验证或存疑之处

1. **"98%"没有分母定义。** 是团队数还是人数？"使用过"还是"每周使用"？官方页面都没说。写成"98% 的员工每天在用"是错的。
2. **"7,000 → 100,000" 不是 14 倍增长。** 前者是问题数量，后者是文档数量，单位不同。这是本案例被转述时最高频的错误。
3. **"数天 → 数小时"是定性表述。** 没有中位数、没有分布，无法量化。
4. **没有成本数据。** 也没有 ROI 数字。任何"摩根士丹利因此节省 X 亿美元"的说法都是外部估算，不是公司披露。
5. **上线时间不明。** 官方页面未给日期；公开报道普遍指向 2023 年随 GPT-4 上线、2024 年扩展 Debrief，但本库未取得可直接引用的一手时间声明。

## 7. 可复用要点

1. **先建评测集，再上线。** 每个用例配一套"真实用户问题 + 标准答案"，这是金融场景能过合规的前提。
2. **答案必须带出处。** 不是为了好看，是为了让顾问能承担合规责任。
3. **宁可回调检索，不要先换模型。** 案例里准确率不足时的第一动作是改检索方法。
4. **零数据保留是采购门槛，不是加分项。** 受监管行业谈不下来这条，项目基本无法启动。
5. **从一个可度量的小场景切入**（研究摘要、会议纪要），而不是"给全公司一个 ChatGPT"。

## 8. 引用边界

✅ 可以说：
- "摩根士丹利称超过 98% 的财富管理顾问团队使用内部 AI 助手（OpenAI 客户案例，企业自述）"
- "其系统把可检索文档比例从 20% 提升到 80%（口径未公开）"
- "上线前建立了每日回归测试与人工评分机制"

❌ 不能说：
- "98% 的员工每天使用"（分母与频次均未披露）
- "知识覆盖提升了 14 倍"（单位不同，不可比）
- "节省了数亿美元"（公司未披露成本或收益）
- "这是 RAG 在金融业的最佳实践"（单案例不足以称最佳）

## 9. 来源

- OpenAI 客户案例：*Morgan Stanley uses AI evals to shape the future of financial services*，https://openai.com/index/morgan-stanley/
  关键引语（David Wu）："We went from being able to answer 7,000 questions to a place where we can now effectively answer any question from a corpus of 100,000 documents."
  关键引语（Kaitlin Elliott）："follow-ups that used to take days now happen within hours."
- 补充背景（D 级，仅作线索）：多方媒体报道其 2023 年起向顾问推广、2024 年扩展 Debrief 工具
