# 按证据等级索引

写文章引用前，先确认案例在同行业中的证据等级。A=A 法定披露/同行评审；B=B 官方+数字；C=C 单方证言；D=D 二手；X=X 已回撤

> 由 `scripts/build_index.py` 自动生成，请勿手工编辑。共 20 条案例。

## A（8）

| 案例 | 企业 | 场景 | 证据 | 状态 | 交付 |
|---|---|---|---|---|---|
| [ADT：聊天拦截率 45%→60%，按结果付费的客服代理](../cases/finance/adt-sierra-agent.md) | ADT Inc. | customer-support, sales-enablement | A | production | vendor-saas |
| [摩根大通 LLM Suite：一家银行同时给出的四套数字](../cases/finance/jpmorgan-llm-suite.md) | JPMorganChase | knowledge-retrieval, software-engineering, backoffice-automation | A | scaled | platform-build |
| [Jefferson Health：5,234 名临床医生的门诊文书助手](../cases/healthcare/jefferson-abridge.md) | Jefferson Health | clinical-documentation | A | scaled | vendor-copilot |
| [Lowe's：2,500 万个问题的零售助手，转化率 3 倍](../cases/retail/lowes-mylow.md) | Lowe's Companies, Inc. | customer-support, sales-enablement, knowledge-retrieval | A | scaled | in-house |
| [英国 NHS 联邦数据平台：3.3 亿英镑买来的争议](../cases/public-sector/nhs-fdp-palantir.md) | NHS England | scheduling-optimization, data-analysis | A | production | platform-build |
| [Providence：1,547 名医生的环境录音助手，效应量只有这么点](../cases/healthcare/providence-dragon-copilot.md) | Providence | clinical-documentation | A | scaled | vendor-copilot |
| [美国国防部 Maven：13 亿美元、2 万用户的军事 AI](../cases/public-sector/dod-maven-smart-system.md) | U.S. Department of Defense (Maven Smart System) | data-analysis, risk-compliance | A | scaled | platform-build |
| [美的集团：2 万个智能体与一条对不齐的降本曲线](../cases/manufacturing/midea-agents.md) | 美的集团 | scheduling-optimization, supply-chain, manufacturing-quality | A | scaled | in-house |

## B（8）

| 案例 | 企业 | 场景 | 证据 | 状态 | 交付 |
|---|---|---|---|---|---|
| [BBVA：12 万员工全员上 ChatGPT Enterprise](../cases/finance/bbva-openai-enterprise.md) | Banco Bilbao Vizcaya Argentaria (BBVA) | knowledge-retrieval, document-processing, software-engineering | B | scaled | vendor-saas |
| [Cleveland Clinic：虚拟指挥中心，四条数字都来自厂商](../cases/healthcare/cleveland-clinic-palantir.md) | Cleveland Clinic | scheduling-optimization | B | production | platform-build |
| [Moderna：两个月造出 750 个 GPT，但没有一个可引用的效率数字](../cases/healthcare/moderna-chatgpt-enterprise.md) | Moderna | knowledge-retrieval, document-processing, data-analysis | B | scaled | vendor-saas |
| [摩根士丹利：让 98% 顾问团队用上的内部知识助手](../cases/finance/morgan-stanley-ai-assistant.md) | Morgan Stanley | knowledge-retrieval, document-processing | B | scaled | vendor-copilot |
| [North Highland：1,400 人 30 天铺开，技术交付快 50%](../cases/professional-services/north-highland-claude.md) | North Highland | document-processing, software-engineering, knowledge-retrieval | B | production | vendor-saas |
| [西门子 × 舍弗勒：被二手文章编出「35%」的工业 Copilot](../cases/manufacturing/siemens-schaeffler-copilot.md) | Schaeffler（舍弗勒） | manufacturing-quality, software-engineering | B | production | vendor-copilot |
| [T-Mobile：AI 接管 40% 客户接触，人工通话降 55%](../cases/telecom/tmobile-intentcx.md) | T-Mobile US（Deutsche Telekom 集团） | customer-support, sales-enablement | B | production | in-house |
| [Tampa General：把床位调度交给 Palantir 驻场团队](../cases/healthcare/tampa-general-palantir.md) | Tampa General Hospital | scheduling-optimization, clinical-decision | B | scaled | platform-build |

## C（3）

| 案例 | 企业 | 场景 | 证据 | 状态 | 交付 |
|---|---|---|---|---|---|
| [Intercom Fin：76% 的解决率，以及这个数字的三种口径](../cases/software/intercom-fin.md) | Intercom | customer-support | C | scaled | vendor-saas |
| [Wendy's 供应链合作社：5 分钟替代 15 人一天](../cases/retail/wendys-qscc-palantir.md) | Quality Supply Chain Co-op (QSCC) | supply-chain, scheduling-optimization | C | production | platform-build |
| [Walgreens：8 个月从 10 家店到 4,000 家店](../cases/retail/walgreens-palantir.md) | Walgreens | scheduling-optimization, supply-chain | C | scaled | platform-build |

## X（1）

| 案例 | 企业 | 场景 | 证据 | 状态 | 交付 |
|---|---|---|---|---|---|
| [Klarna：从「相当于 700 名客服」到重新招人](../cases/retracted/klarna-ai-assistant.md) | Klarna | customer-support | X | retracted | vendor-saas |
