---
id: "financial-jpmorgan-llm-suite"
title: "摩根大通 LLM Suite：一家银行同时给出的四套数字"
company: "JPMorganChase"
company_hq: "US"
industry: "financial-services"
sub_industry: "banking"
scenario: ["knowledge-retrieval", "software-engineering", "backoffice-automation"]
pattern: ["employee-platform"]
deployment_model: "platform-build"
fde_involved: "in-house"
ai_tech: ["LLM", "RAG", "agent"]
vendor: ["Microsoft Azure", "OpenAI", "Anthropic"]
scale: "20 万–32 万名员工（口径见第 6 节）；200+ 个基于平台构建的应用"
start_date: "2024"
status: "scaled"
evidence_grade: "A"
last_verified: "2026-11-09"
metrics:
  - name: "LLM Suite 覆盖员工数"
    value: "20 万 / 32 万（两个口径并存）"
    unit: "人"
    baseline: "不适用"
    method: "20 万：2025 年投资者日与 2026 年多个公开场合；32 万：Forrester 2026 奖项材料（企业提交）"
    window: "2025-05 ~ 2026-10"
    direction: "adoption"
  - name: "周留存率"
    value: "85%"
    unit: "%"
    baseline: "未披露"
    method: "Forrester 2026 技术战略影响奖材料，基于企业提交数据"
    direction: "adoption"
  - name: "用户满意度"
    value: "89"
    unit: "score"
    baseline: "未披露"
    method: "同上，未说明量表与样本"
    direction: "quality-up"
  - name: "KYC 单案成本"
    value: "-40%"
    unit: "%"
    baseline: "2022 年水平"
    method: "2025 年投资者日披露；未说明是否剔除业务量变化"
    window: "2022 ~ 2025"
    direction: "cost-down"
  - name: "年度 AI 支出"
    value: "约 7 亿美元（2026-10 修正）"
    unit: "USD"
    baseline: "此前公开表述为约 20 亿美元/年"
    method: "CFO Jeremy Barnum 在 2026 Q3 电话会上的修正口径；未说明两者统计范围差异"
    window: "2026"
    direction: "cost-down"
sources:
  - id: "src-jpm-investor-day-2025"
    type: "earnings-call"
    grade: "A"
    url: "https://www.jpmorganchase.com/ir"
    publisher: "JPMorganChase Investor Day"
    published: "2025-05-19"
    accessed: "2026-11-09"
    note: "投资者日材料：LLM Suite 覆盖 20 万+ 员工；商业与投资银行条线 175+ 个用例在生产；KYC 单案成本较 2022 年降 40%"
  - id: "src-forrester-2026"
    type: "media-report"
    grade: "B"
    url: "https://www.forrester.com/blogs/forresters-2026-technology-strategy-impact-and-enterprise-architecture-awards-winners-for-na/"
    publisher: "Forrester"
    published: "2026"
    accessed: "2026-11-09"
    note: "奖项材料由企业提交、Forrester 评审：约 32 万员工、80+ 数据源连接、85% 周留存、89 分满意度"
  - id: "src-ciodive-jpm-2026"
    type: "media-report"
    grade: "C"
    url: "https://tech.yahoo.com/cybersecurity/articles/jpmorgan-chase-goldman-sachs-underscore-201500310.html"
    publisher: "CIO Dive（经 Yahoo 转载）"
    published: "2026-10"
    accessed: "2026-11-09"
    note: "全球 CIO Lori Beer 在 Evident AI Symposium 发言：支持 1,000 个业务应用；编码助手占 token 支出主要部分"
  - id: "src-jpm-q3-2026"
    type: "earnings-call"
    grade: "A"
    url: "https://www.bankingnewsai.com/banks/jpmorgan-chase/ai-strategy"
    publisher: "JPMorganChase Q3 2026 电话会（经行业数据库汇编）"
    published: "2026-10-13"
    accessed: "2026-11-09"
    note: "汇编页按日期整理了高管公开表述；原始逐字记录需以公司 IR 归档为准"
tags: ["regulated-industry", "center-of-excellence", "metric-definition-war", "internal-training", "agent-orchestration"]
replicability: 1
human_in_loop: "review-before-send"
confidence_notes: "同一家公司在不同场合给出的员工数、用例数、支出额互相矛盾，是'大企业 AI 数字不可直接引用'的最佳样本"
---

## 1. 一句话摘要

摩根大通把内部大模型平台做成了企业级基础设施，但它在不同场合给出的四个核心数字（员工数、用例数、支出额、效益）彼此矛盾——这条案例的价值，恰在于教你**不要**怎么引用大企业的 AI 数据。

## 2. 业务痛点

一家 30 万人规模的银行，AI 落地面临三个结构性障碍：

- **不能碰公开模型**：2022 年因数据外泄风险封禁 ChatGPT
- **不能各自采购**：各业务线自建工具会导致合规、成本、数据边界失控
- **不能只做 Demo**：投行、风控、KYC、研发的流程差异极大，通用聊天机器人无法直接产生业务结果

## 3. AI 应用场景

LLM Suite 是一个**模型无关的中间层**，不是单一应用：

```
底层：多家模型（OpenAI / Anthropic 等）经私有云接入
  ↓
中间层：统一的权限、数据连接（80+ 内部系统）、审计、成本计量
  ↓
上层：各业务线自建应用（研究摘要、文档分析、KYC、编码助手、客户经理助手）
```

人机分工因场景而异，但统一要求是**人工复核后才进入客户流程**（2026 年 10 月起明确禁止外部 agent 在客户账户内操作）。

## 4. 落地方式

- **形态**：平台自建（platform-build），从服务约 1,000 人的聊天机器人起步，扩展为企业平台
- **交付方**：内部团队（in-house），公开信息未见厂商 FDE 驻场
- **治理**：集中式平台 + 分散式创新；设认证项目把业务人员训练成"AI 方案构建者"
- **规模管理**：从统计"用例数量"转向"50 个由业务方负责的战略举措"
- **成本**：编码助手消耗了大部分 token 预算，成为成本治理重点

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 覆盖员工 | 20 万+（2025 投资者日） / 约 32 万（Forrester 2026） | 两个口径并存，差异未解释 | A / B |
| 周留存率 | 85% | Forrester 奖项材料 | B |
| 用户满意度 | 89 分 | 量表与样本未披露 | B |
| KYC 单案成本 | -40%（对比 2022） | 投资者日披露，未剔除业务量影响 | A |
| 生产用例 | 175+（2025）→ 450（2026 年中）→ 目标 1,000（2026 年底） | 不同时间点，不可并列 | A / C |
| 年度 AI 支出 | 约 7 亿美元（2026-10）vs 约 20 亿美元（此前） | CFO 修正，统计范围差异未说明 | A |

## 6. 不可验证或存疑之处

**这一节是本案例的核心，请优先读。**

1. **员工数矛盾：20 万 vs 32 万。** 前者出自投资者日与高管公开发言，后者出自 Forrester 奖项材料。可能是"有账号"与"已接入"的区别，也可能是提交材料时把范围扩大了。**公司未解释。**
2. **支出额矛盾：20 亿 vs 7 亿。** 2026 年 10 月 CFO 把年度 AI 支出表述改为"接近 7 亿美元"，而非一年前引用的 20 亿美元。同一时期还有"AI 投入已回本"的说法。三个数字无法同时成立，除非统计口径不同（如是否含算力折旧、是否含人力）。
3. **"效益尚未体现在业绩中"。** 同一次电话会里，CFO 明确表示 AI 的收益还没有在整体业绩中显现。这与"20 亿投入已收回 20 亿节省"的流传说法直接冲突。
4. **用例数不是成果。** 175 → 450 → 1,000 的增长衡量的是内部立项数量，不是业务价值。公司自己也已把考核口径从用例数改成 50 个战略举措。
5. **"部分部门减员 30%–40%" 无法归因。** CEO 的说法是某些部门人数下降 30%–40%，但同时存在自然流失（年流失率约 10%）与业务重组。

## 7. 可复用要点

1. **做平台，不做应用集合。** 统一权限、数据连接、审计、成本计量，是规模化前提。
2. **模型无关是风险控制手段**，不只是采购策略。
3. **把"用例数"换成"业务方负责的战略举措数"。** 前者激励堆数量，后者要求有人对结果负责。
4. **成本要按场景归集。** 编码助手吃掉大部分 token 预算这件事，只有做了归集才看得见。
5. **不要用这家公司的数字做行业基准。** 它的口径连自己都没统一。

## 8. 引用边界

✅ 可以说：
- "摩根大通的内部 LLM 平台覆盖 20 万以上员工（2025 年投资者日披露）"
- "该行 2026 年 10 月将年度 AI 支出表述修正为接近 7 亿美元，并称效益尚未体现在业绩中"
- "该行公开的员工数、用例数、支出额在不同场合存在不一致"

❌ 不能说：
- "摩根大通 AI 投入 20 亿美元已全部回本"（与 2026-10 的 CFO 表述冲突）
- "32 万员工每天都在用"（覆盖数≠活跃数；周留存 85% 是另一指标）
- "AI 让摩根大通减员 40%"（是部分部门、且无法归因）
- 把任何单一年份的数字当作"行业平均水平"

## 9. 来源

- JPMorganChase Investor Day 2025（2025-05-19）：LLM Suite 覆盖 20 万+ 员工，175+ 用例在生产，KYC 单案成本较 2022 年降 40%
- Forrester, *2026 Technology Strategy Impact Awards*：约 32 万员工、80+ 数据源、85% 周留存、89 分满意度
- CIO Dive（2026-10，Evident AI Symposium）：CIO Lori Beer 称支持 1,000 个业务应用，编码助手占 token 支出主要部分
- Q3 2026 电话会（2026-10-13）：AI 支出修正为接近 7 亿美元；效益尚未体现在业绩中；禁止外部 agent 操作客户账户
- Q2 2026 电话会（2026-07-14）：近 1,000 个用例，约 50 个"真正重要"；部分部门人数下降 30%–40%
