---
id: "pharma-moderna-chatgpt-enterprise"
title: "Moderna：两个月造出 750 个 GPT，但没有一个可引用的效率数字"
company: "Moderna"
company_hq: "US"
industry: "pharma-biotech"
sub_industry: "drug-discovery"
scenario: ["knowledge-retrieval", "document-processing", "data-analysis"]
pattern: ["employee-platform"]
deployment_model: "vendor-saas"
fde_involved: "none"
ai_tech: ["LLM", "RAG"]
vendor: ["OpenAI"]
scale: "全公司数千名员工；法律部门 100% 采用"
start_date: "2023"
status: "scaled"
evidence_grade: "B"
last_verified: "2026-11-09"
metrics:
  - name: "两个月内创建的自定义 GPT 数"
    value: "750"
    unit: "count"
    baseline: "0（此前为自建 mChat）"
    method: "企业自述；口径为全公司范围内员工自行创建"
    window: "ChatGPT Enterprise 上线后 2 个月"
    direction: "adoption"
  - name: "周活跃用户中创建过 GPT 的比例"
    value: "40%"
    unit: "%"
    baseline: "未披露"
    method: "企业自述；分母为周活跃用户数，未说明如何统计「创建过」"
    window: "ChatGPT Enterprise 上线后 2 个月"
    direction: "adoption"
  - name: "人均每周对话数"
    value: "120"
    unit: "次/人/周"
    baseline: "未披露"
    method: "企业自述；120 次/周相当于每天 17 次，明显高于一般企业水平，口径存疑"
    window: "同上"
    direction: "adoption"
  - name: "法律部门采用率"
    value: "100%"
    unit: "%"
    baseline: "未披露"
    method: "企业自述；采用率定义未说明（是否有账号/是否每周使用）"
    window: "同上"
    direction: "adoption"
sources:
  - id: "src-openai-moderna"
    type: "official-case-study"
    grade: "B"
    url: "https://openai.com/index/moderna/"
    publisher: "OpenAI"
    published: "unknown"
    accessed: "2026-11-09"
    note: "官方案例：750 个 GPT、40% 周活用户创建过、人均 120 次/周对话、法律 100% 采用；全文未披露任何工时或成本节省数字"
tags: ["ai-champion-network", "internal-training", "exec-sponsorship", "novelty-decay"]
replicability: 3
human_in_loop: "review-before-send"
confidence_notes: "全部为采用率指标，无一条业务效益指标；「人均 120 次/周」与企业实际使用强度不符，疑似口径为总对话数除以创建者数"
---

## 1. 一句话摘要

Moderna 在两个月内让员工自己造出 750 个 GPT，法律部门 100% 使用——但官方案例里没有一个可引用的效率数字，这使它成为"采用率 ≠ 效益"的最佳标本。

## 2. 业务痛点

生物科技公司的知识工作特征是"专业文档密度极高、跨职能协作频繁"：

- 合同审阅、政策查询、临床方案撰写消耗大量专业人力
- 员工分散在不同职能，最佳实践难以横向流动
- 传统 IT 交付流程（提需求—排期—开发）速度远慢于业务变化
- 公司规模精简（CEO 明确表示要靠几千人完成传统上十万人的工作量）

## 3. AI 应用场景

**贯穿全职能的"自建 GPT"模式**，而非单点应用：

| GPT | 用途 |
|---|---|
| Contract Companion | 合同首轮审阅与摘要，任何职能都能拿到可读摘要 |
| Policy Bot | 内部政策问答，替代翻阅数百份文档 |
| Dose ID | 临床试验剂量分析：按标准剂量选择原则分析数据、标注引用、生成图表（仍在验证中的试点） |
| 品牌/投资者沟通类 | 准备财报电话会材料，把生物技术术语转成投资者语言 |

```
输入：合同文本 / 政策文档 / 临床数据集 / 财报素材
  ↓
处理：员工自建 GPT（基于 ChatGPT Enterprise 的高级数据分析等能力）
  ↓
输出：摘要、答复、分析图表、材料草稿
  ↓
人工动作：职能专家复核；Dose ID 明确"辅助而非替代"临床判断
```

## 4. 落地方式

- **选型过程**：对比测试自建 mChat、Microsoft Copilot、ChatGPT Enterprise 三者，以 NPS 为准全面转向后者
- **推广机制**（这部分比技术更值得抄）：
  - 目标：6 个月内让所有能访问数字工具的员工实现 100% 采用与熟练
  - 内部 AI 论坛每周约 2,000 名活跃参与者
  - 提示词大赛选出前 100 名重度用户，组成内部"生成式 AI 冠军"团队
  - 领导层赞助 + 引导式培训 + 办公时间（office hours）
- **前置条件**：十年积累的数据平台与 mChat 阶段 80%+ 的员工采用率
- **交付方**：无厂商 FDE 驻场

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 自定义 GPT 数 | 750（2 个月内） | 企业自述 | OpenAI 案例 |
| 周活用户创建率 | 40% | 企业自述 | 同上 |
| 人均周对话 | 120 次 | 企业自述，口径存疑 | 同上 |
| 法律部门采用率 | 100% | 企业自述 | 同上 |
| 工时/成本节省 | **未披露** | — | 同上 |

## 6. 不可验证或存疑之处

1. **没有一条业务效益指标。** 全部是采用率、创建数、对话数。这三个都是"投入侧"指标，不能证明产出。
2. **"人均 120 次/周"很可疑。** 每天 17 次对话，对一个需要深度工作的科研人员来说不现实。更可能是"总对话数 ÷ 周活用户数"，其中少数重度用户拉高了均值，或把 API 调用算进了对话数。
3. **750 个 GPT 里有多少还在被使用？** 未披露。企业自建 GPT 的典型生命周期是"建完用两周，然后遗忘"。没有留存率数据，750 这个数字的信息量很低。
4. **Dose ID 仍是"开发与验证中的试点"。** 官方措辞明确，不能当作已落地的临床决策应用引用。
5. **CEO 的"十万人 vs 几千人"是假设，不是结果。** 那是"如果不这么做会需要多少人"的反事实推演，不是"已经省了多少人"。
6. **先有条件被忽略。** Moderna 在 ChatGPT Enterprise 之前已有 mChat 和 80%+ 的员工采用率，以及十年数据平台积累。把"两个月 750 个 GPT"当成可复制的速度，会严重误判。

## 7. 可复用要点

1. **让员工自己造工具，而不是 IT 统一开发。** 这是唯一能跟上业务变化速度的方式。
2. **配套机制比工具重要**：冠军网络、办公时间、内部论坛、提示词大赛——四件套缺一不可。
3. **先做"人人都要用"的高频场景**（合同摘要、政策问答），再碰专业场景（剂量分析）。
4. **注意前提**：需要已统一的数据平台和较高的数字工具渗透率。没有这个前提，"全员自建"会变成"全员乱建"。
5. **不要用采用率向上汇报效益。** 采用率是过程指标，汇报时会被追问"所以省了多少钱"。

## 8. 引用边界

✅ 可以说：
- "Moderna 在采用 ChatGPT Enterprise 后两个月内，员工创建了约 750 个自定义 GPT，40% 的周活跃用户创建过至少一个"
- "其法律部门达到 100% 使用率，主要用于合同首轮审阅"
- "官方材料未披露任何工时或成本节省数据"

❌ 不能说：
- "Moderna 用 AI 把研发周期从 X 缩短到 Y"（官方无此数据；"42 天"之类的数字来自二手文章）
- "750 个 GPT 带来了显著效率提升"（无对应指标）
- "AI 让 Moderna 用几千人干十万人活"（是反事实假设，非已实现结果）
- "每个员工每周用 120 次"（口径不明，且与企业实际不符）

## 9. 来源

- OpenAI 客户案例：*Moderna：a few thousand people can have the impact of a hundred thousand*（标题大意），https://openai.com/index/moderna/
  关键事实：750 个 GPT、40% 周活用户创建、120 次/周/人、法律 100%、内部论坛 2,000 人/周、mChat 80%+ 前置采用
  重要缺口：全文无工时/成本节省数字
