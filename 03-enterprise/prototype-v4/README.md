# 星球发行·企业版 Prototype v4

本版本基于 2026-09-11 企业版评审结论，重点调整产品定价、信息架构与对外表达，不新增业务功能。

当前 `vercel.json` 中全部 `/enterprise*` 路由已指向 `prototype-v4/index.html`。

## 本轮目标

- 拉开三个平台版本的价格梯度。
- 降低专业名词、技术术语和行业内部表达。
- 优先回答客户最关心的四个问题：这是什么、适合谁、多少钱、能解决什么问题。
- 首页、Product、Solutions、Pricing 与 API 使用同一套产品语言。
- Developer / API 文档保留技术表达，但不再作为一级商业导航。

## 正式产品表达

星球发行企业版帮助发行商、唱片公司、版权公司和音乐平台，用自己的品牌快速搭建音乐发行系统，或通过 API 将音乐发行能力接入现有产品。

对外只保留两个核心产品入口：

1. 自有品牌发行系统
2. 发行 API

## 平台版本

| 版本 | 价格 | 主要适用阶段 |
| --- | ---: | --- |
| 基础版 | ¥19,800 / 年 | 刚开始做发行业务 |
| 专业版 | ¥59,800 / 年 | 有稳定客户和曲库，长期经营 |
| 企业版 | ¥129,800 / 年起 | 大规模业务或复杂系统接入 |

发行使用费统一为 `¥1 / 首 / 渠道`。

发行 API 作为独立购买方式：`¥9,800 / 年起 + ¥1 / 首 / 渠道`。

## 文案规则

- Catalog → 曲库 / 音乐内容
- DSP → 音乐平台 / 目标平台
- White Label → 自有品牌
- Distribution Workflow → 发行流程
- Revenue / Settlement → 收入与结算
- Integration → 系统对接
- Migration → 历史曲库导入
- Quota → 使用额度
- Provisioning / Entitlement / Tenant 等内部产品架构词不进入销售页面
- API / DDEX / XML / SFTP 只在技术接入场景出现

页面第一层优先描述客户要完成的事情，技术架构和协议放到第二层。

## 页面

- `/enterprise`
- `/enterprise/product`
- `/enterprise/solutions`
- `/enterprise/pricing`
- `/enterprise/api`
- `/enterprise/developers`
- `/enterprise/apply`

v4 继续复用 `prototype-v2/styles.css`，只增加极少量移动端导航覆盖样式，不改变整体视觉系统。
