# 看见音乐发行产品体系：产品能力架构矩阵 v0.1

> 更新时间：2026-09-09  
> 文档定位：Phase 1 产品架构阶段的核心产出之一。用于明确三条产品线与共享发行能力之间的边界，作为后续商业模式、具体产品形态、官网包装和 Roadmap 的共同基础。  
> 本文讨论的是**产品能力架构**，不是最终技术微服务拆分，也不代表当前所有能力都已达到可直接商业售卖或标准 API Ready 状态。

---

## 1. 架构目标

本轮拆分的核心不是建设三套发行系统，而是形成：

> **一套共享发行能力底座 + 三条差异化商业产品线。**

三条产品线分别是：

1. **星球发行**：看见音乐运营的合作发行产品，升级为 Basic / Professional / Plus；
2. **星球发行·企业版**：面向企业客户的 White-label SaaS / API 产品；
3. **AI 音乐发行**：专门面向 AI 音乐流通场景的付费自助发行产品，复用现有发行底座，但拥有独立的渠道目录、审核策略与收费模式。

关键原则：

- 三条产品共享稳定的 Catalog / Release / Delivery / Rights / Reporting 等核心 Domain；
- 产品差异主要由 Product Policy、Entitlement、Quota、Operator、Channel Policy、Commercial Model 和 UX 决定；
- 共享能力不代表三个产品前台形态相同；
- 共享底层不代表所有代码必须放在一个系统或仓库；
- 一个能力在当前 SaaS 权限树中存在，不代表它已经是标准化、可售卖的 Enterprise API。

---

## 2. 产品架构总图

```text
                             Distribution Capability Platform
                                         │
             ┌───────────────────────────┼───────────────────────────┐
             │                           │                           │
             ▼                           ▼                           ▼
        星球发行                    星球发行·企业版                 AI 音乐发行
 Managed Distribution             Distribution OS               AI Distribution
             │                           │                           │
    Kanjian-operated Portal      White-label SaaS / API      Self-service Portal
             │                           │                           │
 Basic / Pro / Plus            Enterprise Operator          AI-focused Channel Set
             │                           │                           │
 Revenue Share + Add-on      SaaS/API Commercial Model      Paid Distribution Model
             └───────────────────────────┴───────────────────────────┘
                                         │
              Identity / Catalog / Rights / Release / Delivery /
             Compliance / Reporting / Royalty / Settlement / Billing
```

---

## 3. 产品层与共享能力层的分工

### 3.1 共享发行能力层负责“发行这件事本身”

例如：

- 一个 Artist 是什么；
- 一个 Track / Album / Release 是什么；
- 一份授权关系如何关联作品；
- 一次发行请求如何进入审核；
- 内容如何交付到 DSP；
- 发行状态如何回传；
- 报表如何对应作品和 CP；
- 收益如何计算、分账、结算。

### 3.2 产品层负责“以什么规则卖给谁”

例如：

- 星球发行用户属于 Basic、Professional 还是 Plus；
- Basic 每年可以管理多少内容、多少艺人；
- Plus 是否获得专属运营与更高 SLA；
- 企业版购买哪些 SaaS 模块、开通哪些 API；
- 企业客户使用自己的品牌还是看见品牌；
- AI 音乐发行支持哪十余个 DSP；
- AI 音乐发行按歌曲、渠道、服务期限还是订阅收费；
- 某个 AI 内容是否满足某个 DSP 的发行条件。

因此不应该为了套餐、品牌和收费差异复制 Catalog、Release、Delivery 等底层模型。

---

## 4. Operator 模型

三个产品最重要的差异之一是“谁在运营发行关系”。

```text
Platform
  ↓
Operator
  ↓
CP / Organization
  ↓
Artist / Catalog
  ↓
Release
```

| 产品 | Operator | 主要服务对象 | 运营方式 |
|---|---|---|---|
| 星球发行 | 看见音乐 | 音乐人 / 厂牌 / 版权公司 / CP | 看见运营 + 用户前台自助 |
| 企业版 White-label | 企业客户 | 企业自己的音乐人 / 厂牌 / CP | 企业客户运营自己的发行平台 |
| 企业版 API | 企业客户 | 企业自己的最终用户 | 企业自有产品通过 API 调用看见能力 |
| AI 音乐发行 | 看见音乐 / 自动化系统 | AI 音乐创作者及相关用户 | 高度标准化、自助化、付费发行 |

Operator 是产品架构层概念，用于描述业务责任与产品关系。是否需要在后续技术实现中成为独立实体，由工程架构阶段进一步决定。

---

## 5. Capability Map 总矩阵

标记说明：

- **Core**：应属于共享发行能力层；
- **Policy**：复用共享能力，但该产品需要独立规则/权益；
- **Experience**：主要是该产品自己的前台/后台体验；
- **Exclusive**：该产品线特有能力；
- **Optional**：是否开放由套餐、模块或客户需求决定；
- **—**：不是该产品的主要能力。

| 能力域 | 共享底座 | 星球发行 | 企业版 White-label | 企业版 API | AI 音乐发行 |
|---|---|---|---|---|---|
| Identity / Account | Core | Experience | Experience + Policy | Core API | Experience |
| Organization / CP | Core | Policy | Experience + Policy | Core API | 简化使用 |
| Role / RBAC | Core | 简化 | Experience + Policy | Optional API | 简化 |
| Branding / Site | 基础能力 | 看见品牌 | **Exclusive/核心卖点** | — | 独立品牌体验 |
| Artist / Label / CP Catalog | Core | Policy | Core | Core API | Core + 简化 |
| Album / Release | Core | Policy | Core | Core API | Core + Policy |
| Track | Core | Policy | Core | Core API | Core + Policy |
| MV | Core | Policy | Optional | Optional API | 首期可选 |
| Composition | Core | Policy | Optional | Optional API | 首期可选 |
| File / Asset / Metadata | Core | Policy / Quota | Core / Quota | Core API | Core / Quota |
| Playlist / Content Collection | Shared capability | Optional | Optional | Optional API | — |
| 页面上传 | Core | Experience | Experience | — | Experience |
| 批量导入 | Core | Tier Policy | Core | Import API | 视套餐开放 |
| DDEX 入库 | Core | 高阶/特定客户 | Optional | DDEX/API | — |
| 总协议 / Master Agreement | Core | Product Policy | Tenant Policy | Optional API | 新商业协议 |
| 专辑授权书 / Release Authorization | Core | Product Policy | Tenant Policy | Optional API | 按交易协议设计 |
| E-sign | Shared service | Core | Optional | Optional | 可选 |
| 权利登记 | Shared capability | Add-on / Quota | Optional Module | Optional API | Add-on |
| Release Creation | Core | Experience | Core | Core API | Experience |
| Channel Selection | Core | Product Policy | Tenant/DSP Policy | API Policy | **AI Channel Policy** |
| Metadata Validation | Core | Core | Core | Core API | Core + AI Rule |
| Compliance Review | Core | Product Policy | Tenant Policy | Optional API | **AI-specific Policy** |
| Delivery / Transmission | Core | Core | Core | Core API | Core |
| DSP / SP Management | Core | 看见维护 | Enterprise Admin | API/配置能力 | 只消费 AI DSP Catalog |
| Transmission Route | Core | 看见维护 | Enterprise Admin | Optional API | 系统维护 |
| Release Status | Core | Experience | Core | Core API | Experience |
| Failed Task / Exception | Core | 内部运营处理为主 | Enterprise Admin | Webhook/API | 系统运营处理 |
| Metadata Update | Core | Service Request | Enterprise Workflow | API | Self-service/Rule-based |
| Takedown | Core | Service Request，当前不可用户自助 | Enterprise Workflow | API | Product Policy |
| Report Ingestion | Core | 看见后台 | Enterprise Admin | API | 看见后台 |
| Revenue / Royalty | Core | Core | Optional Module | API | Core |
| Split | Core | 看见政策 | Optional Module | API | 新商业规则 |
| Settlement | Core | Core | Optional Module | API | Core |
| Withdrawal | Core | Experience + 后台审核 | Optional | Optional API | Experience |
| Sales / Catalog Analytics | Shared capability | Tier Policy | Optional Module | Optional API | 基础分析 |
| Product / Plan | Commercial Core | **Basic/Pro/Plus** | Module/Package | API Product | Package/Subscription |
| Entitlement | Commercial Core | **核心** | **核心** | API Scope | **核心** |
| Quota | Commercial Core | **核心** | **核心** | Usage Limit | **核心** |
| Usage Metering | Commercial Core | 内容/服务用量 | SaaS/API 用量 | API Usage | 发行/渠道/期限用量 |
| Order | Commercial Core | Add-on/扩容 | 企业合同/订单 | API 商业合同 | **核心购买路径** |
| Payment | Shared commercial service | Add-on/扩容 | 企业收款 | 企业收款 | **核心购买路径** |
| SLA | Service Core | Tier Policy | Enterprise Contract | API SLA | Standard SLA |
| Service Case | Service Core | 核心，需产品化 | Enterprise Workflow | Support API 可选 | 标准客服 |
| 专属运营 | Service capability | Pro/Plus Policy | 企业自有运营 | — | — |
| 版权/法务 Case | Service capability | Tier Policy | Optional Service | — | Standard/付费支持 |
| AI Content Declaration | Shared metadata capability | 如 DSP 需要则使用 | 如客户需要 | API Field | **核心** |
| AI DSP Catalog | Channel policy capability | — | Optional | Optional | **Exclusive/核心** |
| AI DSP Eligibility | Policy engine | — | Optional | Optional API | **Exclusive/核心** |
| Self-service Checkout | Shared commerce | Add-on 可用 | — | — | **Exclusive/核心体验** |
| Service Term / Renewal | Commercial capability | 非核心 | 合同周期 | API contract | **核心** |

---

## 6. Shared Core：必须保持统一的数据与业务语义

以下能力不应因为三个产品而建立三套数据模型。

### 6.1 Identity & Organization

稳定对象：

- User
- Account
- Organization
- CP / Partner
- Role / Permission

产品差异：

- 星球发行以看见作为 Operator；
- 企业版允许企业管理自己的组织、团队、CP 和角色；
- AI 音乐发行应简化组织模型，优先优化个人/小团队自助体验。

### 6.2 Catalog & Asset

稳定对象：

- Artist
- Label
- Album / Release
- Track
- MV
- Composition
- File / Asset
- Metadata

原则：

> AI 音乐不是另一套 Track / Album 数据模型。

AI 相关属性应作为内容声明、来源、审核与渠道策略的一部分存在，例如：

- AI-generated / AI-assisted 声明；
- AI voice / synthetic voice 信息；
- 模型/工具相关声明（仅在业务或渠道需要时）；
- AI policy review status。

### 6.3 Rights & Contract

稳定能力：

- 总协议；
- Release/Album 授权；
- 权利信息；
- 合同主体；
- E-sign；
- 权利登记。

产品差异主要体现在合同模板和商业关系，而不是重新建设合同系统。

### 6.4 Distribution

稳定能力：

```text
Release Request
    ↓
Validation
    ↓
Compliance / Review
    ↓
Channel Selection
    ↓
Delivery
    ↓
DSP Status
    ↓
Update / Takedown / Exception
```

三个产品应尽量共享这条执行链路。

### 6.5 Reporting / Royalty / Settlement

稳定能力：

- 渠道报表接收；
- 作品收入匹配；
- 收益计算；
- 分账；
- 结算；
- 提现。

产品商业模式不同，但底层收入与作品的关联关系仍应统一。

---

## 7. 星球发行专属产品能力

星球发行不是 SaaS 套餐，而是由看见运营的**合作发行产品**。

其真正产品化重点是：

### 7.1 Partnership Tier

```text
Basic
Professional
Plus
```

Tier 未来负责表达：

- 准入等级；
- 合作深度；
- 分成政策；
- 服务等级；
- SLA；
- 资源与系统权益。

### 7.2 Entitlement / Quota

候选计量维度：

- 托管歌曲/Track 数量；
- 年度新增发行量；
- 艺人数量；
- 专辑/Release 数量；
- 文件/存储规模；
- ISRC / UPC；
- 批量工具；
- 改单/下架等人工服务次数；
- 版权登记等增值服务数量。

商业模式阶段再确定最终使用哪些指标和具体数字。

### 7.3 Service Operations

当前大量真实服务发生在线下沟通中，应逐步产品化：

- 修改资料申请；
- 下架申请；
- 版权争议 Case；
- 客服 Case；
- 专属运营；
- SLA / 优先级；
- 服务记录。

Plus 的核心价值不应只是更多菜单，而应包括更深入的服务关系。

### 7.4 Cross-product Promotion

宣发/投流不属于星球发行 Core Distribution。

但可作为：

- Add-on；
- 会员权益；
- Plus 战略客户权益；
- 跨产品入口。

---

## 8. 企业版专属产品能力

企业版的本质不是“把后台开放给客户”，而是：

> **让客户可以运营自己的音乐发行业务。**

### 8.1 White-label SaaS

完整产品由两端组成：

```text
企业品牌
  │
  ├── Management Console
  │     企业运营团队使用
  │
  └── CP / Creator Portal
        企业自己的音乐人、厂牌、CP 使用
```

企业版专属重点能力：

- Branding / Site；
- 企业组织与角色；
- 企业自己的 CP 管理；
- 企业自己的合同模板与签约规则；
- DSP/传输配置；
- 企业运营后台；
- 模块开通与权限；
- Tenant-level Entitlement / Quota；
- 客户服务与 SLA。

### 8.2 Open API

API 不是把内部接口文档公开，而需要产品化成稳定 Capability Contract。

建议未来对外按业务能力包装：

- Identity / Organization API
- Catalog API
- Artist / Label / CP API
- Ingestion API
- Release API
- Delivery / DSP API
- Contract / Rights API
- Reporting API
- Royalty / Split / Settlement API
- Copyright Registration API

并配套：

- API Key / Credential；
- Scope；
- Version；
- Usage Metering；
- Rate Limit；
- Webhook；
- Error Contract；
- SLA；
- Developer Documentation。

当前已有 Apifox 开放 API 作为现状输入，但后续需要单独完成 API Ready 审计。

---

## 9. AI 音乐发行专属产品能力

### 9.1 产品边界

AI 音乐发行是一条**专门为 AI 音乐流通建立的新商业产品线**。

核心服务商品是：

> **把符合要求的 AI 音乐，以标准化、自助、付费方式发行到看见已经确认支持 AI 音乐的指定 DSP 集合。**

虽然产品允许普通音乐使用，但产品定位、渠道设计、审核逻辑和商业包装均围绕 AI 音乐发行建立。

### 9.2 AI Channel Catalog

AI 音乐发行不开放星球发行的完整 DSP 网络。

需要建立一套独立的产品渠道目录：

```text
AI Music Channel Catalog
├── DSP A
├── DSP B
├── DSP C
└── ...约十余个确定渠道
```

该目录由产品运营统一维护，是该产品的核心 SKU 组成部分。

### 9.3 AI Channel Policy

每个 AI DSP 至少需要描述：

- 是否允许 AI-generated；
- 是否允许 AI-assisted；
- 是否有额外声明字段；
- 是否涉及 AI voice / imitation 限制；
- 是否需要额外人工审核；
- 支持哪些发行类型；
- 上线/下架相关特殊规则。

由于渠道集合本身是确定的，产品形态可以直接面向用户展示“当前支持发行到哪些 AI 渠道”，而不是抽象成无限 DSP Policy Engine 后才上线。

### 9.4 Paid Self-service Commerce

AI 音乐发行必须拥有完整的购买链路：

```text
上传内容
  ↓
AI/版权声明与审核
  ↓
选择渠道 / 服务方案
  ↓
确认价格
  ↓
支付
  ↓
提交发行
  ↓
状态追踪
  ↓
收益与报表
```

核心商业能力：

- SKU / Package；
- Release Unit；
- Channel Package；
- Service Term；
- Order；
- Payment；
- Entitlement；
- Quota；
- Renewal。

具体采用按首、按专辑、按渠道、按期限、订阅或混合模式，在 Phase 2 商业模式阶段决定。

---

## 10. Commercial Infrastructure 应成为共享能力

虽然三条产品收费方式完全不同，但建议产品架构层统一商业基础能力。

```text
Product
  ↓
Plan / SKU
  ↓
Entitlement
  ↓
Quota
  ↓
Usage
  ↓
Order / Contract
  ↓
Payment / Settlement
```

### 星球发行

主要用于：

- Basic / Professional / Plus 权益；
- 扩容包；
- Add-on；
- 部分付费服务。

### 企业版

主要用于：

- Setup / Deployment；
- Module Activation；
- Subscription；
- API Usage；
- Storage / Capacity Usage。

### AI 音乐发行

主要用于：

- 单次购买；
- 渠道组合；
- 服务期限；
- 订阅套餐；
- 发行额度。

这样可以避免三个产品分别建设一套权益与计费系统。

---

## 11. Operations / Service 应作为正式产品能力

当前星球发行已经存在大量人工工作：

- 下架；
- 修改资料；
- 客服问题；
- 版权争议；
- 法务协调；
- 提现审核；
- 大客户专属运营。

如果这些能力继续只存在于微信、邮件、微信群和人工记忆中，则：

- 无法准确区分 Basic / Pro / Plus 服务等级；
- 无法测量服务成本；
- 无法建立 SLA；
- 无法让企业版复制完整运营能力；
- 无法进一步让 AI / Agent 参与工作。

因此共享能力层应逐步引入：

```text
Service Request / Case
├── Type
├── Priority
├── SLA
├── Operator
├── Status
├── Related CP
├── Related Release
└── Resolution
```

这属于架构方向，本阶段不要求立即重做客服系统。

---

## 12. Capability 的现状成熟度分类

根据目前已知 SaaS 权限与业务现状，可以先粗分三类。

### A. 已存在较成熟业务基础

- Account / Organization / Role；
- Album / Track / MV / Composition；
- Artist / Label / CP；
- 批量导入；
- DDEX；
- Contract；
- Distribution；
- DSP / Transmission；
- Compliance；
- Report；
- Royalty / Split；
- Withdrawal；
- Rights Registration；
- Branding / Site；
- Data Dashboard。

### B. 已有业务但需要重新产品化

- 修改资料流程；
- 下架流程；
- 客服与运营 Case；
- SLA；
- 专属运营服务记录；
- API 产品化；
- Tenant / Module 商业开通；
- 各产品统一 Usage Metering。

### C. 本轮拆分需要新增或重点建设的产品能力

- Product / Plan；
- Entitlement；
- Quota；
- Commercial Usage；
- Capacity Pack；
- Basic / Pro / Plus Tier Engine；
- AI Music Channel Catalog；
- AI Channel Policy；
- AI Self-service Checkout；
- AI Service Term / Renewal；
- Enterprise API Product / Scope / Usage Model。

---

## 13. 本阶段明确不做的事

产品架构阶段暂不确定：

- Basic / Professional / Plus 具体价格；
- 各 Tier 具体歌曲、艺人、ISRC、UPC 数量；
- Enterprise SaaS / API 具体价格；
- AI 音乐发行具体单曲/专辑价格；
- AI 音乐发行最终订阅档位；
- 三条产品最终官网页面；
- 最终 UI 原型；
- 底层微服务和数据库物理拆分。

这些分别属于后续商业模式、产品形态、原型和工程 Roadmap 阶段。

---

## 14. Phase 1 产品架构完成标准

在进入三个产品商业模式设计前，应至少完成以下产出：

- [x] 产品体系总体架构 v0.1
- [x] 三产品 Capability Map v0.1
- [x] Shared Distribution Domain 初版边界
- [x] Operator 模型初版
- [x] AI 音乐发行渠道边界原则
- [ ] 当前能力 → 目标能力 Gap Map
- [ ] 三产品关键业务流关系图
- [ ] 产品架构阶段关键 ADR / 决策清单

完成最后三项后，Phase 1 可以收口，正式进入 Phase 2：三个产品的商业模式设计。

---

## 15. 下一步

下一步优先产出：

### `current-to-target-gap-map-v0.1.md`

把本文件定义的目标能力，与当前实际系统进行对照，区分：

1. 已经存在、可直接复用；
2. 已存在但需要产品化/改造；
3. 需要新增；
4. 暂不需要。

该文档的目的不是立即排技术开发，而是确认：

> **为了支撑三条产品线，现有 SaaS/星发能力距离目标产品架构到底还差什么。**
