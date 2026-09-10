# 星球发行·企业版：产品范围与商业闭环 v1.0

> 日期：2026-09-10  
> 状态：Scope Baseline  
> 上游：企业版草稿、`business-baseline-v0.1.md`、`commercial-model-v0.1.md`

---

# 1. 产品范围正式定义

星球发行·企业版当前阶段不重新建设 Catalog、发行、DSP、收益、Tenant 管理、企业后台或下游 CP 门户。

这些能力已经存在，并可作为企业租户的实际发行系统底座。

本阶段产品边界是：

> **把看见音乐现有企业发行能力产品化，建立从产品展示、企业申请、商务签约、租户开通、套餐计费、API 接入到续费服务的完整 B2B 商业闭环。**

因此当前真正新增和需要收口的是：

```text
Commercial Layer
+
Enterprise Productization Layer
```

而不是重做 Distribution Domain。

---

# 2. 两个正式商业产品形态

企业版对外只保留两个核心产品形态。

## 2.1 品牌发行平台

定义：

> 基于现有星球发行企业能力，为企业提供可使用企业品牌运营的完整发行平台。

企业获得：

- 企业品牌；
- 独立域名 / 品牌入口；
- 企业管理后台；
- 下游 CP / 厂牌 / 音乐人发行门户；
- 多账号；
- 内容与发行；
- 看见审核；
- DSP 交付；
- 数据、报表、收益与提现；
- Tenant 基础配置；
- 可选 API 与高级接入能力。

该模式主要解决：

> 企业希望快速拥有一套完整、可运营的音乐发行平台。

---

## 2.2 模块化发行 API

定义：

> 企业保留自己的产品和 UI，通过 API 接入看见现有发行能力。

对外可以按模块开放：

```text
账号 / 基础数据
内容 / Catalog
发行
版权 / 标识
DSP / 渠道
报表 / 数据
收益 / 结算
```

企业可以只采购所需模块，而不必使用完整品牌发行平台。

该模式主要解决：

> 企业已有系统，只需要把发行、渠道、报表、收益等能力接入现有产品。

---

# 3. “企业级深度接入”不再作为第三个商业产品

DDEX、XML、Excel、SFTP、API 均为现有技术交付能力。

因此不再把 Enterprise Infrastructure 作为和“品牌发行平台 / API”平级的第三个 SKU。

正确归类为：

```text
接入 / 交付方式
├── API
├── DDEX
├── XML
├── Excel
└── SFTP
```

它们根据客户成熟度和项目需要，作为标准或定制接入能力提供。

---

# 4. 已有能力与当前建设范围

## 4.1 已有，不作为本阶段重建范围

```text
Tenant 基础管理与配置
多账号
企业管理后台
下游 CP / 厂牌门户
Artist / Album / Track
Metadata / Asset
ISRC / UPC
DSP 管理
发行任务
看见审核
DSP 交付
发行状态
报表
收益
分账
提现
DDEX / XML / Excel / SFTP / API
```

这些能力在本阶段的工作是：

- 梳理；
- 统一产品表达；
- 补充必要的 Enterprise Entitlement / Provisioning 接口；
- 用于官网与销售 Demo；
- 形成 API Developer Experience。

而不是重新设计和重做。

## 4.2 当前真正需要建设 / 收口

```text
官网与产品介绍
Pricing / Plan
企业申请
销售线索
方案与报价
合同 / KYC 状态
企业客户档案
Tenant 开通 / Provisioning
Entitlement
Quota / Usage
API Developer Center
API Credential / Sandbox / Webhook / Log
企业客户中心
账单 / 续费 / 变更
内部 Enterprise Sales / Ops
```

---

# 5. 完整商业链路

企业版的核心闭环：

```text
访问官网
  ↓
了解产品
  ↓
查看定价 / API
  ↓
申请企业版
  ↓
Enterprise Lead
  ↓
商务沟通 / 需求确认
  ↓
选择商业模式
  ├── 品牌发行平台
  └── 模块化发行 API
  ↓
报价 / 方案确认
  ↓
合同签署 + 企业 KYC
  ↓
Enterprise Account 创建
  ↓
Plan / Entitlement 配置
  ↓
Tenant 创建或关联
  ↓
品牌 / 账号 / DSP / API 初始化
  ↓
接入 / 上线
  ↓
正式使用现有发行能力
  ↓
Usage / Quota / Billing
  ↓
续费 / 升级 / 扩容 / 终止
```

该链路是当前企业版产品的核心，而不是发行后台本身。

---

# 6. 企业申请流程

官网 CTA：

```text
申请企业版
```

建议表单字段：

### 企业信息

- 企业名称；
- 企业所在地；
- 联系人；
- 手机；
- 邮箱；
- 官网 / 产品链接。

### 企业类型

- 唱片公司 / 发行商；
- 厂牌 / 版权公司；
- AI 音乐平台；
- 创作者平台；
- 音乐科技公司；
- 其他。

### 业务规模

- 当前曲库规模；
- 月新增歌曲 / 发行量；
- 下游 CP / 厂牌 / 音乐人数量；
- 主要发行地区。

### 需求

- 品牌发行平台；
- API；
- DDEX；
- XML；
- Excel；
- SFTP；
- 批量迁移；
- 报表 / 收益 / 结算。

### 计划

- 预计上线时间；
- 其他需求。

提交后生成 Enterprise Lead。

---

# 7. Lead 到 Active Tenant 状态机

建议统一状态：

```text
APPLIED          已申请
QUALIFYING       需求确认中
PROPOSAL         方案 / 报价中
CONTRACTING      合同签署中
SIGNED           已签约
PROVISIONING     开通配置中
INTEGRATING      接入中
ACTIVE           已启用
SUSPENDED        已暂停
RENEWING         续费中
EXPIRED          已到期
CLOSED           已终止
```

这些状态是 Enterprise Commercial Domain，而不是发行 Domain。

---

# 8. Tenant Provisioning 的正确边界

已有 Tenant 管理基础能力，因此本阶段不做新的 Tenant 系统。

需要补的是：

> **从商业合同和套餐自动 / 半自动驱动 Tenant 开通。**

Provisioning Checklist 建议：

```text
合同已完成
企业 KYC 已完成
Enterprise Account 已创建
Tenant 已创建 / 已关联
管理员已创建
品牌配置完成
域名配置完成
DSP 范围已配置
Plan 已绑定
Entitlement 已生效
Quota 已初始化
API Credential 已创建（如需要）
Webhook 已配置（如需要）
测试完成
正式启用
```

其本质是 Orchestration，不是重新建设 Tenant CRUD。

---

# 9. Pricing / Plan / Entitlement

## 9.1 两种商业模式

### 按量模式

历史参考：

> 约 ¥0.5 / 首 / 渠道 / 次

建议主要用于：

- API；
- 弹性业务；
- 试运行客户。

主要 Meter：

```text
有效发行传输次数
= 内容 × 渠道 × 实际传输操作
```

### 年度模式

历史参考：

> 约 ¥25,000 / 年

建议主要用于：

- 品牌发行平台；
- 稳定发行规模企业。

结构：

```text
年度平台服务费
+ 包含额度
+ 超额用量
+ 可选模块 / 服务
```

正式价格需单独审批后再公开。

---

# 10. Entitlement 是产品化关键

企业签约以后，系统不能只记录一个“企业客户”。

必须能表达企业买了什么：

```text
Enterprise Plan
├── Product Mode
│   ├── Branded Platform
│   └── Modular API
├── Enabled Modules
├── DSP Scope
├── API Access
├── DDEX / XML / SFTP
├── Catalog Quota
├── Delivery Quota
├── Account Quota
├── Revenue / Settlement
├── Support Level
└── SLA
```

Plan 决定 Entitlement；Entitlement 决定现有底层能力哪些对该 Tenant 可见和可调用。

---

# 11. API Developer Center 的范围

API Developer Center 是企业版商业产品的一部分，而不是新的发行 Domain。

## 公开层

```text
API 产品介绍
能力范围
快速开始
认证说明
核心 API 文档
Webhook 说明
错误码
申请 API
```

## 登录后

```text
API Credential
Sandbox / Production
IP 白名单（如需要）
Webhook
API 调用日志
Webhook 日志
使用量
Quota
文档
技术支持
```

Developer Center 应尽量映射现有星球发行 API，而不是重新设计一套并行业务模型。

---

# 12. 企业客户中心

企业客户登录后，除了进入现有 Tenant / 发行后台，还应有一个轻量 Enterprise Account 层，查看商业关系：

```text
企业信息
当前方案
已开通能力
使用量
额度
合同
API
账单
续费 / 升级
技术支持
```

这与发行后台职责不同：

- Enterprise Account 管“和看见买了什么”；
- Tenant / Distribution Console 管“具体怎么做发行”。

---

# 13. 内部 Sales / Ops

看见内部需要一套最小 Enterprise Ops 视图：

```text
企业线索
申请记录
客户档案
方案 / 报价
合同状态
Tenant 关联
Plan / Entitlement
开通 Checklist
Usage
账单
续费
服务记录
```

P0 可以先做轻量管理，不要求替代完整 CRM / ERP。

---

# 14. 官网应该如何围绕两个商业模式重构

官网菜单维持：

```text
产品
定价
API
```

## 首页产品叙事

不再展示三个平级方案。

改为两个明确入口：

### 品牌发行平台

> 快速建立企业品牌下的完整音乐发行服务。

### 发行 API

> 将发行、渠道、数据与收益能力接入现有产品。

然后用已有能力证明：

- 多账号 / Tenant；
- 下游 CP Portal；
- 内容与发行；
- 看见审核；
- DSP 网络；
- 报表与收益；
- API / DDEX / XML / Excel / SFTP。

“深度接入”改成一段能力说明，不作为第三张产品卡。

---

# 15. 当前阶段不做什么

明确不作为当前主范围：

- 重做企业管理后台；
- 重做 CP 发行门户；
- 重做 Tenant 管理；
- 重做 Catalog；
- 重做发行工作流；
- 重做收益与提现；
- 为行业对标而强行加入 Own DSP Deal；
- 重新设计与现有系统并行的发行 API Domain；
- 构建完整 CRM；
- 构建完整财务 ERP。

---

# 16. P0 成功标准

企业版 P0 完成时，应该可以完整演示：

```text
企业从官网了解产品
↓
选择品牌发行平台或 API
↓
理解价格
↓
提交企业申请
↓
看见内部收到 Lead
↓
确认方案与报价
↓
签约 / KYC
↓
绑定 Plan
↓
创建 / 关联 Tenant
↓
自动生成对应 Entitlement / Quota
↓
完成品牌或 API 接入
↓
进入已有发行系统正式使用
↓
查看用量 / 额度 / 合同 / API
↓
续费或扩容
```

这条链打通，即代表星球发行·企业版的商业产品化闭环成立。
