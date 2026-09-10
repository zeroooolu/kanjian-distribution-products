# 星球发行·企业版 Roadmap v0.2

> 日期：2026-09-10  
> 状态：Commercial Productization Roadmap  
> 上游：`product-scope-and-commercial-loop-v1.0.md`

---

# 1. Roadmap 调整原则

v0.1 中将“企业管理后台 Demo、CP 品牌发行门户 Demo”等列为核心建设项。

基于最新确认，这些能力已经存在，并可完整提供给企业租户，因此 v0.2 正式调整：

> **企业版当前阶段不重建发行系统，而是补齐商业获取、申请签约、套餐计费、开通编排、Developer Center 与客户生命周期。**

---

# 2. 新的产品范围

当前要建设的是：

```text
官网 / Product Marketing
Pricing / Plan
Enterprise Application
Lead / Sales Ops
Contract / KYC Status
Enterprise Account
Tenant Provisioning
Entitlement / Quota / Usage
API Developer Center
Billing / Renewal
```

已有并直接复用：

```text
Tenant Management
Enterprise Console
CP Portal
Catalog
Distribution
DSP
Review
Delivery
Report
Revenue
Withdrawal
DDEX / XML / Excel / SFTP / API
```

---

# 3. PR / 阶段规划

## EE00 — 产品范围与对象模型收口

目标：把 Commercial Domain 和现有 Distribution Domain 分开。

产出：

- Enterprise Account；
- Lead；
- Application；
- Plan；
- Entitlement；
- Quota；
- Usage；
- Contract Status；
- Provisioning；
- Billing；
- Renewal；
- Tenant Link。

同时将两个商业产品确定为：

1. 品牌发行平台；
2. 模块化发行 API。

完成标准：产品对象、状态、关系全部明确。

---

## EE01 — 官网 v2 信息架构与产品叙事

目标：让官网真正围绕两个商业模式销售，而不是围绕基础能力堆模块。

菜单保持：

```text
产品
定价
API
```

首页核心结构：

1. Hero；
2. 两种产品模式；
3. 已有发行平台能力证明；
4. 真实发行链路；
5. DSP 网络；
6. 数据、收益与结算；
7. API / DDEX / XML / Excel / SFTP；
8. Pricing；
9. 企业申请 CTA。

关键调整：

- 删除“企业级深度接入”第三个产品卡；
- 品牌发行平台与发行 API 成为唯一两个产品入口；
- 已有后台 / CP Portal 用真实截图或高保真界面证明；
- 官网不重新解释底层所有功能细节。

---

## EE02 — Pricing / Plan

目标：把历史商业报价变成正式产品结构。

需要设计：

### 按量合作

- 核心计量：有效发行传输；
- 历史锚点：约 ¥0.5 / 首 / 渠道 / 次；
- 适合 API / 试运行 / 弹性客户。

### 年度合作

- 历史锚点：约 ¥25,000 / 年；
- 年度平台费；
- 包含额度；
- 超额规则；
- 可选模块 / 服务。

### Plan Schema

```text
Plan
├── Product Mode
├── Enabled Modules
├── DSP Scope
├── Delivery Quota
├── Catalog Quota
├── Account Quota
├── API Access
├── Integration Methods
├── Revenue / Settlement
├── Support
└── SLA
```

完成标准：官网 Pricing 和内部报价使用同一套产品逻辑。

---

## EE03 — Enterprise Application

目标：官网流量进入可管理的企业销售线索。

范围：

- 企业申请页；
- 企业信息；
- 客户类型；
- 业务规模；
- 需求模块；
- 预计上线时间；
- 联系方式；
- 申请成功页。

状态：

```text
已申请
需求确认中
方案 / 报价中
合同中
已签约
```

完成标准：官网 CTA 不再只是商务邮箱或假按钮。

---

## EE04 — Enterprise Sales / Ops

目标：看见内部可以接住申请并完成商业流转。

最小后台：

```text
申请列表
企业客户
联系人
需求
方案
报价
合同状态
租户关联
Plan
开通状态
续费日期
```

P0 不做完整 CRM；只服务企业版商业闭环。

---

## EE05 — Tenant Provisioning / Entitlement

目标：解决“签约后如何把已经存在的 Tenant 能力正确开给客户”。

不重新做 Tenant 管理，而是增加 Provisioning Orchestration。

流程：

```text
Signed Contract
↓
Enterprise Account
↓
Plan
↓
Tenant Create / Link
↓
Entitlement
↓
Quota
↓
Brand / DSP / API Config
↓
Active
```

Checklist：

- 企业账号；
- Tenant；
- 管理员；
- 品牌；
- 域名；
- DSP；
- API；
- Quota；
- 测试；
- 上线。

完成标准：商务合同能够映射成系统权限和能力。

---

## EE06 — API Developer Center

目标：把现有发行 API 真正包装成企业可采购的 Developer Product。

### Public

```text
API 概览
能力范围
快速开始
鉴权
API 文档
Webhook
错误码
申请接入
```

### Authenticated

```text
API Key
Sandbox / Production
Webhook
调用日志
Webhook 日志
Usage
Quota
技术支持
```

执行原则：

1. 先对现有 API 做 Endpoint Mapping；
2. 复用真实接口；
3. 补企业鉴权、隔离、日志、Quota 和文档；
4. 不另造一套发行 Domain。

---

## EE07 — Enterprise Customer Center

目标：让企业客户管理“与看见的商业关系”，而不是管理发行内容。

客户中心范围：

```text
企业信息
当前方案
已开通能力
使用量 / Quota
合同
API
账单
续费
升级 / 扩容
服务支持
```

与已有发行后台分工：

```text
Enterprise Customer Center
= 买了什么 / 用了多少 / 合同和服务

Existing Distribution Console
= 内容如何发行
```

---

## EE08 — Billing / Renewal

目标：打通持续经营闭环。

P0 范围：

- 年度到期日期；
- 使用量；
- 超额量；
- 账单状态；
- 续费提醒；
- 续约；
- Plan 升级；
- Quota 扩容；
- 暂停 / 到期。

不要求一期建设复杂自动支付；可以继续由商务 / 财务线下收款，但系统必须能记录商业状态。

---

## EE09 — 完整 Enterprise Sales Demo

最终演示脚本：

```text
打开企业版官网
↓
了解品牌发行平台 / API
↓
查看 Pricing
↓
打开 Developer Docs
↓
提交企业申请
↓
内部收到 Lead
↓
选择方案 / 报价
↓
合同完成
↓
开通 Enterprise Account
↓
创建 / 关联已有 Tenant
↓
生效 Entitlement / Quota
↓
进入现有品牌发行平台
或
创建 API Credential
↓
正式发行
↓
客户中心查看 Usage / Contract / Renewal
```

到这一阶段，Enterprise Product Demo 才算完整。

---

# 4. 当前优先级

## 第一优先级

```text
EE00 产品对象与商业状态
EE02 Pricing / Plan
EE03 企业申请
```

原因：这是整个商业闭环的骨架。

## 第二优先级

```text
EE01 官网 v2
EE04 Sales / Ops
EE05 Provisioning / Entitlement
```

原因：把销售和现有 Tenant 能力接起来。

## 第三优先级

```text
EE06 Developer Center
EE07 Customer Center
EE08 Renewal
```

原因：让 API 客户和存量企业长期可运营。

---

# 5. 下一步立即执行

下一轮建议不再继续抽象讨论，直接完成三件事：

1. **EE00：定义 Enterprise Commercial Domain 对象和状态机；**
2. **EE02：把按量 / 年度两种模式收口成可展示 Pricing；**
3. **EE03：设计企业申请 → 商务 → 签约 → 开通完整原型。**

完成这三项后，再基于真实商业链重构当前官网 v2。
