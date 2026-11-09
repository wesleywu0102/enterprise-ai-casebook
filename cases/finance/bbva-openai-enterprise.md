---
id: "financial-bbva-openai-enterprise"
title: "BBVA：12 万员工全员上 ChatGPT Enterprise"
company: "Banco Bilbao Vizcaya Argentaria (BBVA)"
company_hq: "ES"
industry: "financial-services"
sub_industry: "banking"
scenario: ["knowledge-retrieval", "document-processing", "software-engineering"]
deployment_model: "vendor-saas"
fde_involved: "unknown"
ai_tech: ["LLM", "RAG", "agent"]
vendor: ["OpenAI"]
scale: "12 万员工（2025-12 宣布全员扩展）；此前阶段 11,000 人；2 万+ 自建 GPT"
start_date: "2024"
status: "scaled"
evidence_grade: "B"
last_verified: "2026-11-10"
metrics:
  - name: "员工规模"
    value: "120,000+"
    unit: "人"
    baseline: "2024-05 起 3,300 个账号 → 11,000 人"
    method: "BBVA 官方新闻稿；宣布扩展规模，不等于已完成激活"
    window: "2025-12-12"
    direction: "adoption"
  - name: "每日使用比例"
    value: "80%"
    unit: "%"
    baseline: "未披露"
    method: "BBVA 官方稿，内部统计；分母为已开通用户"
    window: "2025-12"
    direction: "adoption"
  - name: "每周节省时间（员工自报）"
    value: "约 3 小时"
    unit: "小时/人/周"
    baseline: "未披露（自报，非系统计时）"
    method: "BBVA 内部测量 + 员工自报；同一稿另称特定任务节省超过 76%"
    window: "2025-12"
    direction: "time-down"
  - name: "特定任务耗时节省"
    value: "超过 76%"
    unit: "%"
    baseline: "未披露"
    method: "BBVA 称为 internal measurements，但未说明是哪些任务、样本多大"
    window: "2025-12"
    direction: "time-down"
  - name: "自建 GPT 数量"
    value: "2 万+"
    unit: "个"
    baseline: "不适用"
    method: "BBVA 官方稿；另有 4,000 多个被标为高频使用"
    window: "2025-12"
    direction: "adoption"
sources:
  - id: "src-bbva-openai-2025"
    type: "official-press-release"
    grade: "B"
    url: "https://www.bbva.com/en/innovation/bbva-and-openai-seal-a-strategic-alliance-to-redefine-banking-with-artificial-intelligence/"
    publisher: "BBVA"
    published: "2025-12-12"
    accessed: "2026-11-10"
    note: "客户方官方稿（英文）：12 万员工、80% 日活、每周约 3 小时。数字由客户自己发布，这是本案例最有价值的地方。"
  - id: "src-bbva-the-eight-es"
    type: "official-press-release"
    grade: "B"
    url: "https://www.bbva.com/es/innovacion/bbva-impulsa-the-eight-su-estrategia-para-transformar-la-experiencia-financiera-con-ia/"
    publisher: "BBVA（西班牙语原稿）"
    published: "2025-12-12"
    accessed: "2026-11-10"
    note: "西语原稿补充：特定任务节省超过 76%、2 万多个 GPT、4,000 多个高频使用。"
  - id: "src-openai-fde-page"
    type: "official-case-study"
    grade: "C"
    url: "https://openai.com/business/forward-deployed-engineering"
    publisher: "OpenAI"
    published: "unknown"
    accessed: "2026-11-10"
    note: "供应商页声称 BBVA 信用风险系统准确率 80%；BBVA 官方稿中找不到此数字，不可作为客户成效引用。"
tags: ["fde-model", "co-delivery", "regulated-industry", "vendor-sourced-number", "exec-sponsorship"]
replicability: 4
human_in_loop: "review-before-send"
confidence_notes: "规模与采用率有客户方官方口径，但「每周省 3 小时」是员工自报、「省 76%」只适用特定任务；OpenAI 页面上的 80% 准确率客户从未确认"
---

## 1. 一句话摘要

BBVA 把 ChatGPT Enterprise 从 3,300 个试点账号扩到全行 12 万人，80% 用户每天用、自报每周省 3 小时——这是欧洲银行业少见的、由客户自己发布数字的案例。

## 2. 业务痛点

一家横跨西班牙、墨西哥、土耳其、南美的银行，内部知识极度碎片化：

- 集团层面有海量制度、产品条款、监管文件，多语言、多司法辖区
- 客户经理回答问题要靠找专家、翻内部网、发邮件问合规
- 信贷、风控、软件开发的文档处理量巨大
- 受监管行业不能把客户数据随意送进公共模型，只能走企业版

BBVA 的选择是"从上往下铺"：不挑几个场景做试点，而是先给全员一个通用助手，再让业务部门自己长出用例。

## 3. AI 应用场景

```
输入：员工提问 + 企业内部知识（制度、产品条款、代码库）
  ↓
处理：ChatGPT Enterprise（含企业数据边界）→ 检索/生成/代码补全
  ↓
输出：答复、文档草稿、代码、分析脚本
  ↓
人工动作：员工核对后使用；涉及客户决策的仍走原有审批
```

三类用法占比最高：文档处理与摘要、软件开发、信贷风险分析。另有面向客户的对话助手 Blue（独立产品线）。

## 4. 落地方式

- **形态**：ChatGPT Enterprise 席位 + OpenAI API；BBVA 称双方团队"共同工作、联合投资"
- **是否 FDE 驻场：未披露。** BBVA 的官方稿没有使用前置部署工程师这一说法，OpenAI 的 FDE 页面也没有把 BBVA 列为 FDE 项目。本库按 `unknown` 处理，不臆测
- **推广路径**：2024-05 起 3,300 个账号 → 11,000 人 → 2025-12 宣布扩展到 12 万人
- **组织配套**：设"AI 采纳"专职团队、按部门培训、内部 GPT 市场（员工自建 2 万多个，4,000 多个被标为高频使用）
- **合规**：企业版数据边界 + 不用于模型训练；受监管业务保留人工审批

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 覆盖员工 | 12 万+ | 宣布扩展规模，非激活数 | BBVA 2025-12-12 |
| 每日使用比例 | 80% | 客户内部统计，分母为已开通用户 | 同上 |
| 每周节省时间 | 约 3 小时 | 员工自报 + 内部测量 | 同上 |
| 特定任务耗时 | -76% 以上 | 客户称 internal measurements，未列任务清单 | BBVA 西语稿 |
| 自建 GPT | 2 万+（4,000+ 高频） | 客户官方 | 同上 |
| 信用风险准确率 | 80% | **仅见于 OpenAI 页面，客户未确认** | OpenAI FDE 页 |

## 6. 不可验证或存疑之处

1. **"每周 3 小时"是自报。** 不是系统计时，也不是工时审计。自报时间节省在文献里普遍高估（人们倾向于回报符合期待的数字）。
2. **"76%" 只适用特定任务。** 同一份稿里，全员口径是"约 3 小时/周"，特定任务是"超过 76%"。把 76% 写成"全员效率提升 76%"是最常见的错误转述。
3. **12 万是"宣布扩展"，不是"已激活"。** 企业级席位部署通常分季度完成。
4. **80% 信用风险准确率来源可疑。** 这个数字只出现在 OpenAI 的 FDE 业务页，BBVA 的中英文官方稿里都没有。按本库规则，它只能标为"供应商口径，客户未确认"。
5. **无对照组。** 没有"同样一批员工不用 AI 时每周花多少时间在例行任务上"的测量。
6. **FDE 参与度不明。** 这是本案例与 OpenAI 官方 FDE 叙事之间最大的空隙——BBVA 是"最大规模部署之一"，但没有任何一方说这是 FDE 交付的。

## 7. 可复用要点

1. **先给全员，再挑场景。** 与"选 3 个高价值场景做深"相反，BBVA 走的是广覆盖路线，靠员工自建 GPT 长出长尾用例（2 万个里 4,000 个高频，命中率约 20%）。
2. **员工自建是低成本的需求发现机制。** 但要接受 80% 的自建品没人用。
3. **数据边界是受监管行业的前置条件。** 没有"不用于训练 + 企业隔离"，合规直接否掉。
4. **不要用自报时间做 ROI。** 立项时用自报可以，结项时必须换系统侧指标（工单时长、代码合并周期、审批通过时间）。

## 8. 引用边界

✅ 可以说：
- "BBVA 于 2025 年 12 月宣布把 ChatGPT Enterprise 扩展到全行 12 万名员工，此前为 11,000 人"
- "BBVA 称 80% 的用户每日使用，员工自报每周在例行任务上节省约 3 小时"
- "BBVA 称其内部测量显示特定任务耗时节省超过 76%，并已自建 2 万个以上 GPT"

❌ 不能说：
- "BBVA 全员效率提升 76%"（76% 只适用特定任务）
- "AI 为 BBVA 每年节省 XX 万工时"（3 小时是自报，且未披露基数）
- "BBVA 的信用风险模型准确率 80%"（客户从未确认）
- "这是 OpenAI FDE 团队交付的项目"（无任何一方如此表述）

## 9. 来源

- BBVA, *BBVA and OpenAI Seal a Strategic Alliance to Redefine Banking with Artificial Intelligence*, 2025-12-12
  关键句："BBVA will extend the use of ChatGPT Enterprise to its more than 120,000 employees" / "Eighty percent of users access the assistant daily and report saving an average of three hours per week on routine tasks."
- BBVA（西语）, *BBVA impulsa 'The Eight'…*, 2025-12-12
  关键句："ahorros de tiempo superiores al 76% en determinadas tareas"
- OpenAI, *Forward Deployed Engineering*（业务页，无日期）：80% 信用风险准确率的唯一出处
