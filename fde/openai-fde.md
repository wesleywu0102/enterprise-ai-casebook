# OpenAI 的 FDE：把"驻场工程师"做成正式职级

**证据等级：A**（官方招聘页面，逐字可核）
**核实日期：2026-11-09**

---

## 一、事实

OpenAI 设有独立的 **Forward Deployed Engineering** 团队，并在多个地点按行业/职能分设岗位：

| 岗位 | 地点 | 面向 |
|---|---|---|
| Forward Deployed Engineer (FDE) | 纽约 | 通用 |
| FDE, Financial Services | 纽约 | 银行、资管、保险、私募 |
| FDE, AI Infra | 旧金山 | 半导体与 AI 基础设施 |
| FDE | 阿布扎比（UAE） | 区域市场 |

岗位共同特征：
- 要求 5 年以上工程或技术交付经验，且有客户侧负责经验
- 混合办公（每周 3 天到办公室），**出差比例最高 50%**
- 全栈能力要求：Python / JavaScript 后端 + 前端，能写生产级代码

## 二、团队定位（原文关键句）

> "OpenAI's Forward Deployed Engineering team partners with customers to turn research breakthroughs into production systems. We operate at the intersection of customer delivery and core platform development."

> "Our work turns early deployments into repeatable solution patterns, operating standards, and evaluation practices that scale across regulated financial institutions."

这句话定义了 FDE 与"实施顾问"的分野：**产出不是一次性交付，而是可复用的模式与标准。**

## 三、考核口径（最值得抄的一段）

岗位描述里对"成功"的定义：

> "You will measure success through production adoption, workflow efficiency, risk reduction, revenue impact, and evaluation-driven feedback loops that inform product, model, and GTM strategy."

拆开看是五个维度：

| 维度 | 含义 | 对应可观测指标 |
|---|---|---|
| production adoption | 真的在生产里被用 | 周活跃、留存、单日调用量 |
| workflow efficiency | 工作流变快 | 单任务时长、积压量 |
| risk reduction | 风险下降 | 误报率、人工复核率、审计发现数 |
| revenue impact | 收入影响 | 转化率、单客收入 |
| eval-driven feedback | 评测反馈回流 | 评测集扩充、模型/产品路线变更 |

**没有任何一条是"按时交付需求"。** 这是 FDE 与外包在制度层面的根本差别。

## 四、金融服务业岗位的额外要求

金融 FDE 的描述比其他岗位更严，值得单独摘出：

- 必须为受监管环境**定义上线标准**：控制措施、审计留痕、评测基准、验收阈值
- 要能在"访问控制、数据血缘、可解释性、失败模式"约束下做架构设计
- 要跑评测闭环：准确率、延迟、覆盖率、误报率
- 要把部署经验"蒸馏"成 hardened primitives、参考架构、剧本、工具

这说明一件事：**在金融业，FDE 的一半工作是合规工程，不是模型工程。**

## 五、不能从这份材料推出的结论

1. **不能说"OpenAI 有数千名 FDE"。** 招聘页不披露团队规模。
2. **不能说"OpenAI FDE 已服务多少客户"。** 未披露。
3. **不能把岗位描述当成效。** 这是"要求做什么"，不是"做到了什么"。
4. **不能假设中国区有同等配置。** 公开岗位集中在纽约、旧金山、阿布扎比。

## 六、对写作者的用法

这条材料的价值不在"OpenAI 也做 FDE"这个事实，而在它把 FDE 的**考核口径写成了公开文本**。可以据此提出一个可证伪的判断：

> 如果 FDE 真是新范式，那么未来 12 个月应能看到：模型厂商的 FDE 岗位从金融、基础设施扩展到制造、医疗；且岗位描述里出现更多"业务指标"而非"交付里程碑"。

反过来，如果一年后这些岗位消失或并入普通解决方案架构师团队，说明 FDE 只是一轮获客手段。

---

**来源**
- OpenAI Careers: *Forward Deployed Engineer (FDE) - NYC* — https://openai.com/careers/forward-deployed-engineer-(fde)-nyc-new-york-city/
- OpenAI Careers: *Forward Deployed Engineer (FDE), Financial Services - NYC* — https://openai.com/careers/forward-deployed-engineer-(fde)-financial-services-nyc-new-york-city/
- OpenAI Careers: *Forward Deployed Engineer (FDE) - AI Infra - SF*
- OpenAI Careers: *Forward Deployed Engineer - UAE*
