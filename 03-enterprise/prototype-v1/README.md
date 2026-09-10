# 星球发行·企业版官网原型 v2.0

> 日期：2026-09-10  
> 状态：Enterprise Commercial Website / Product Demo Scaffold

## 本轮目标

企业版不再以“再设计一套发行后台”为目标，而是围绕已经存在的 Tenant、企业后台、下游 CP 门户、发行、DSP、报表、分账和提现能力，搭建完整的企业商业产品链路。

本轮依据：

- `03-enterprise/product-scope-and-commercial-loop-v1.0.md`
- `03-enterprise/business-baseline-v0.1.md`
- `03-enterprise/commercial-model-v0.1.md`
- `06-research/enterprise-white-label-api-competitor-research-2026.md`
- `SAAS0102(2).pdf` 中已有音乐资产、发行、分账、合规和 API 能力介绍
- AudioSalad、FUGA、SonoSuite、LabelGrid、Revelator、EVEARA 当前企业产品官网结构

## 产品结构

对外正式保留两个核心商业产品：

1. **品牌发行平台**：以企业品牌、独立域名和客户体系运营完整发行服务；
2. **发行 API**：将内容、发行、渠道、报表与收益能力接入现有产品。

DDEX / XML / Excel / SFTP 不再作为第三个产品，统一归入企业技术接入与交付能力。

## 顶层导航

继续遵循三主菜单：

```text
产品
├── 产品总览
└── 解决方案

定价

API
├── 发行 API
└── 开发者中心
```

右侧提供：

- 开发者中心快捷入口；
- 申请企业版。

## 当前页面 / 路由

- `/enterprise`：企业版首页
- `/enterprise/product`：产品总览 / 品牌发行平台 / API 能力
- `/enterprise/solutions`：发行商、版权公司、AI 音乐平台、音乐科技平台解决方案
- `/enterprise/pricing`：年度合作 + 按量合作
- `/enterprise/api`：发行 API 产品页
- `/enterprise/developers`：Developer Center 信息架构 Demo
- `/enterprise/apply`：企业申请与入驻流程 Demo

当前使用同一 HTML 根据 clean route 渲染不同页面，方便在产品设计阶段快速迭代；后续研发实现时可拆为真实路由和组件。

## 首页商业叙事

首页已经从纯能力展示改成完整 B2B 商业链：

```text
产品定位
↓
品牌发行平台 / 发行 API
↓
真实发行链路
CP → 企业租户 → 看见审核 → DSP
↓
已有发行能力证明
↓
全球发行网络
↓
企业申请 / 评估 / 报价 / 签约 / 开通 / 上线
↓
申请企业版
```

## PPT 能力继承

旧 SaaS 介绍中保留并重新产品化表达的能力：

- 元数据与资产集中管理；
- 多平台发行；
- 报表解析与多维度版税分账；
- 资产传输；
- 合同 / 合规基础能力；
- API 与多种企业交付方式。

不沿用旧 PPT 的视觉样式和“音乐基建云服务平台”泛化定位。

## 竞品结构参考

- AudioSalad：服务能力短表达 + API / White Label 独立入口；
- FUGA：Distribution 为主产品，Custom-branded distribution 与 API 作为企业扩展；
- SonoSuite：面向 Distributor 的明确白标价值 + 业务规模申请表；
- LabelGrid：One Engine / Two Ways In + Pricing + Developer Hub；
- Revelator：White Label 与 API 独立产品页，API 覆盖供应链、数据和收益；
- EVEARA：企业申请 / Onboarding 作为完整购买链的一部分。

## 定价策略

当前官网只公开商业模型，不公开未经重新审批的历史固定价格：

- 年度合作：年度平台服务 + 约定发行额度 + 超额使用；
- 按量合作：按歌曲 × 渠道 × 实际传输计费。

历史 `¥25,000 / 年` 与 `约 ¥0.5 / 首 / 渠道 / 次` 继续作为内部商业模型基线。

## Developer Center

当前为结构 Demo，已包含：

- 快速开始；
- 鉴权；
- 内容 API；
- 发行 API；
- 基础数据；
- Webhook；
- 日志与错误码；
- 用量与配额。

示例 Endpoint 仅用于说明 Developer Experience，不代表最终生产接口。下一阶段需要基于现有真实后台 API 完成 Endpoint Mapping。

## 企业申请

申请页已经包含：

- 企业基本信息；
- 企业类型；
- 品牌发行平台 / 发行 API 选择；
- 曲库规模；
- 月发行量；
- 下游 CP / 厂牌数量；
- API / DDEX / XML / SFTP / Excel 技术需求；
- 企业入驻流程。

当前表单为 Demo，不提交真实 Lead 数据。

## 下一步

1. 根据真实 API 文档完成 Developer Center Endpoint Mapping；
2. 将企业申请表接到 Enterprise Lead；
3. 设计内部 Lead → Proposal → Contract → Provisioning 流程；
4. 设计 Plan / Entitlement / Quota / Usage；
5. 确认公开 Pricing 数字后完成定价页 v1.0；
6. 用现有真实企业后台 / CP 门户截图替换部分示意界面。
