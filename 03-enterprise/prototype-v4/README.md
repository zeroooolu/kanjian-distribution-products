# 星球发行·企业版 Prototype v4

本版本基于 2026-09-11 企业版评审结论，重点调整产品定价、信息架构与对外表达，不新增业务功能。

当前 `vercel.json` 中全部 `/enterprise*` 路由已指向 `prototype-v4/index.html`。

## 本轮目标

- 建立清晰的三个企业版本价格与容量梯度。
- 降低专业名词、技术术语和行业内部表达。
- 优先回答客户最关心的四个问题：产品定位、适用对象、价格与核心能力。
- 首页、Product、Solutions、Pricing 与 API 使用同一套产品语言。
- Developer / API 文档保留技术表达，但不再作为一级商业导航。

## 正式产品表达

星球发行企业版帮助发行商、唱片公司、版权公司和音乐平台，以自有品牌快速搭建音乐发行平台，或通过 API 将音乐发行能力接入现有产品。

对外只保留两个核心产品入口：

1. 自有品牌发行平台
2. 发行 API

## 平台版本

| 版本 | 价格 | 曲库规模 | 合作客户 | 主要适用阶段 |
| --- | ---: | ---: | ---: | --- |
| 基础版 | ¥12,800 / 年 | 1,000 首 | 50 个 | 小规模发行运营 |
| 专业版 | ¥59,800 / 年 | 5 万首 | 1,000 个 | 规模化多客户发行 |
| 企业版 | ¥129,800 / 年起 | 30 万首起 | 按项目配置 | 大型发行或平台级业务 |

发行使用费统一为 `¥1 / 首 / 渠道`。

发行 API 作为独立购买方式：`¥9,800 / 年起 + ¥1 / 首 / 渠道`。

## 文案规则

- Catalog → 曲库 / 音乐内容
- DSP → 音乐平台 / 目标平台
- White Label → 自有品牌发行平台
- Distribution Workflow → 发行流程
- Revenue / Settlement → 收入与结算
- Integration → 系统对接
- Migration → 历史曲库导入
- Quota → 使用额度
- Provisioning / Entitlement / Tenant 等内部产品架构词不进入销售页面
- API / DDEX / XML / SFTP 只在技术接入场景出现

页面第一层优先描述客户要完成的事情，技术架构和协议放到第二层。官网商业页面统一采用正式、专业的企业级表达，避免口语化的问答式标题和内部讨论式措辞。

## 页面

- `/enterprise`
- `/enterprise/product`
- `/enterprise/solutions`
- `/enterprise/pricing`
- `/enterprise/api`
- `/enterprise/developers`
- `/enterprise/apply`

v4 继续复用 `prototype-v2/styles.css`，并通过 `prototype-v4/styles.css` 承载企业版增量样式，不改变整体视觉系统。

## CTA 规则

- 全站通用主 CTA：`申请企业方案`
- API 场景主 CTA：`申请 API 接入`
- Pricing 版本卡：`申请基础版` / `申请专业版` / `联系商务`
- Apply 表单提交：`提交企业咨询`
- 不使用“免费试用”，除非产品实际提供无需商务审核即可进入的试用环境。

## 术语补充

- 官网产品名统一使用“自有品牌发行平台”，不与“自有品牌发行系统”混用。
- 对外商业页面优先使用“合作方 / 合作客户”，`CP` 仅允许出现在内部产品或技术语境。
- “音乐平台”用于市场与能力描述；“渠道”用于发行操作和 `¥1 / 首 / 渠道` 的计费口径。
- Developer 页面统一称“开发者指南 / 开发者中心”，不在非正式 API Reference 页面使用“正式 API 文档”的表达。

## Enterprise Visual System

商业页面优先使用产品证据而非装饰图片：

- Product Window：后台、门户、曲库、发行与收入界面
- Architecture Diagram：业务系统与发行能力的连接关系
- Flow Diagram：发行与实施流程
- Data Dashboard：规模、状态、收入与结算数据
- Code Console：API 请求、响应与开发者示例
- Event Stream：Webhook 与平台状态变化

视觉内容用于解释产品和业务流程，不使用与功能无关的音乐素材图作为主要页面装饰。
