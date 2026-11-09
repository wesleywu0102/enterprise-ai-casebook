# Anthropic 的 Applied AI / FDE：仍在组建期，且与 Palantir 的合作被普遍误读

**证据等级：A（招聘 JD、官方公告）/ 无（客户落地成效）**
**核实日期：2026-11-10**

---

## 一、Anthropic 有没有 FDE

有，但组织形态与 OpenAI 不同：**Anthropic 没有单独发布一篇"FDE 是什么"的官方博文**，最接近官方定义的是 Applied AI 团队下的招聘 JD。原文：

> "As a member of the Applied AI team at Anthropic, you will be a Forward Deployed Engineer (FDE) who embeds directly with our most strategic customers to drive transformational AI adoption."

> "You will sit at the frontier of enterprise AI deployments and serve as **one of our founding FDEs** who helps to shape our forward-deployed motion."

> "Work within customer systems to build production applications with Claude models, ensuring that these products meet customer requirements."

> "Provide white glove deployment support for Anthropic products in enterprise environments."

岗位：Forward Deployed Engineer，伦敦，£225,000–£255,000，出差 25–50%。

**"one of our founding FDEs" 这句话很关键**：它说明这个岗位在招聘时仍处于**组建期**。把 Anthropic 写成"已有成熟 FDE 交付体系"是没有依据的——这与 Palantir 二十年的 FDE 建制、OpenAI 已按行业分设岗位，不是同一阶段。

## 二、Anthropic × Palantir：三件事被混成了一件

中文自媒体里流传最广的说法是"2025 年 11 月 Claude 成为首个部署在五角大楼的商业大模型"。核实后，这是把三个不同时间、不同性质的事件压缩成了一句。

| 日期 | 事件 | 性质 |
|---|---|---|
| 2024-11-07 | Anthropic + Palantir + AWS：Claude 3/3.5 进入 Palantir AIP，跑在 AWS 支持的 IL6 环境 | **能力上线**，非项目落地 |
| 2025-04-17 | Anthropic 加入 Palantir FedStart，Claude 以 FedRAMP High / DoD IL5 供给联邦政府 | **合规通道**，非项目落地 |
| 2025-11-18 | Palantir 发布自家产品 "AI FDE" | **与 Anthropic 无关** |

2024-11-07 联合公告原文：

> "This partnership allows for an integrated suite of technology to operationalize the use of Claude within Palantir's AI Platform (AIP) [...] hosted on Palantir's Impact Level 6 (IL6) accredited environment, supported by AWS."

> "Claude became accessible within Palantir AIP on AWS earlier this month."

注意措辞是 "became accessible"——**可用**，不是**已用于某个政府项目**。

## 三、有没有可核验的政府客户成效

**没有。**

- 公告里唯一的量化表述是 Palantir CTO 举的一个**不具名商业客户**例子：某美国保险公司用 78 个 AI agent 把承保流程从两周压到三小时。厂商高管口述、客户匿名、无基线细节，且不是政府项目
- FedStart 公告里的 "millions of federal government employees" 是**未来目标**（原文用 "will be able to start offering... in the coming months"），不是已落地用户数
- 没有任何政府部门公开确认使用 Claude 的具体项目或成效

**另一个取证细节**：Anthropic 官网没有这条合作的独立新闻稿（`anthropic.com/news/anthropic-palantir` 返回 404），联合稿由 Palantir 经 Business Wire 发布。写"Anthropic 官方新闻稿宣布"是不准确的，应写"双方联合公告，Palantir 发布"。

## 四、Anthropic 客户里唯一"客户自己发布数字"的一个

在核实的 9 家候选客户里，绝大多数数字由 Anthropic 撰写（Rakuten 79%、GitLab 98% 满意度、Intercom 86% 上限）。唯一由**客户自己**在自家网站发布的量化案例是 North Highland：

> "our AI Driven Delivery framework, built with Claude Code as it's engine, now delivers our technical work roughly 50% faster than the way we used to work."

已收录为独立案例：[`../cases/professional-services/north-highland-claude.md`](../cases/professional-services/north-highland-claude.md)。但注意：**没有任何证据表明这是 Anthropic FDE 驻场交付的**，该公司是自行采购 + 自建交付框架。

## 五、结论：这个专题里最容易被夸大的三处

1. **把"能力可用"写成"已落地"。** Claude 进入 IL6 环境 ≠ 某个国防项目在用。
2. **把"组建期"写成"成熟体系"。** JD 原文 "founding FDEs" 是最直接的证据。
3. **把"厂商撰写的客户案例"写成"客户验证"。** Rakuten 的 79% 没有任何 Rakuten 官方渠道确认。

---

**来源**
- Anthropic Careers, *Forward Deployed Engineer*（伦敦）— https://www.anthropic.com/careers/jobs/5423029008
- Business Wire, *Anthropic and Palantir Partner to Bring Claude AI Models to AWS for U.S. Government Intelligence and Defense Operations*, 2024-11-07 — https://www.businesswire.com/news/home/20241107699415/en/
- Palantir IR, *Anthropic Joins Palantir's FedStart Program to Deploy Claude Application*, 2025-04-17 — https://investors.palantir.com/news-details/2025/Anthropic-Joins-Palantirs-FedStart-Program-to-Deploy-Claude-Application/
- Anthropic, *Claude for Government*（无日期）— https://www.anthropic.com/solutions/government
- 相关：[`anthropic-goldman-jv.md`](anthropic-goldman-jv.md)（FDE 被资本化）、[`../cases/professional-services/north-highland-claude.md`](../cases/professional-services/north-highland-claude.md)
