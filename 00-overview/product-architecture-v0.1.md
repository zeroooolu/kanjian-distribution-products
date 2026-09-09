# 看见音乐发行产品体系架构 v0.1

> 日期：2026-09-09  
> 状态：产品架构基线（用于进入后续商业模式设计）  
> 目标：先冻结“整个发行产品体系如何组成、三条产品线如何共享底层、各自边界是什么”，暂不在本文确定具体价格、额度、版本权益数字或页面原型。

---

## 1. 架构结论

看见音乐未来不是维护三套独立发行系统，而是建立：

> **一套统一发行能力底座 + 三条面向不同客户关系与商业模式的产品线。**

三条产品线分别是：

1. **星球发行**：看见音乐运营的合作发行产品；
2. **星球发行·企业版**：向企业输出发行系统与发行能力；
3. **AI 音乐发行**：专门面向 AI 音乐流通场景的付费自助发行产品。

三条产品共享内容、发行、渠道、合同、报表、收益等核心能力，但在运营主体、客户关系、渠道范围、收费模式、服务等级、产品体验上分别独立。

---

## 2. 总体产品架构

```text
                           看见音乐发行产品体系
                                    │
                 ┌──────────────────┴──────────────────┐
                 │      Shared Distribution Platform   │
                 │        统一发行能力与业务数据层       │
                 └──────────────────┬──────────────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
          星球发行             星球发行·企业版          AI 音乐发行
     Managed Distribution     Distribution OS       Paid Self-service
              │                     │                     │
      看见运营的发行前台       White-label / API      独立自助发行前台
              │                     │                     │
     Basic / Pro / Plus     企业自己开展发行业务     AI 音乐为核心商品
```

核心原则：

- **共享 Domain，不共享商业模式。**
- **共享发行能力，不强制共享同一套 UI。**
- **三条产品线不能各自维护独立的歌曲、专辑、发行、渠道、报表和收益主数据。**
- **产品差异由产品层、策略层、权益层和运营层表达，而不是复制底层系统。**

---

## 3. 五层产品架构

### Layer 1：品牌与商业产品层

直接面向市场定义“客户买的是什么”。

```text
星球发行
星球发行·企业版
AI 音乐发行
```

这一层负责：

- 产品定位；
- 客户类型；
- 商业关系；
- 套餐 / 合作等级；
- 价格；
- 官网与市场表达。

### Layer 2：体验与操作端层

```text
星球发行 Portal

企业版：
├── Enterprise Management Console
├── White-label CP / Creator Portal
└── Open API

AI 音乐发行：
└── Self-service Distribution Portal
```

现有关系：

- 当前 SaaS 权限体系对应企业级 **Management Console**；
- 当前 `star.kanjian.com` 对应看见自己运营的 **CP / Creator Portal**；
- 企业白标可以复用上述两类端能力；
- AI 音乐发行应复用底层发行能力，但采用独立、自助、付费优先的产品体验，不应被迫套用当前星发 UI。

### Layer 3：产品策略与权益层

这是未来三个产品产生差异的关键层。

包括：

- Product / Plan；
- Entitlement；
- Quota；
- Usage Meter；
- Channel Policy；
- Service Level / SLA；
- Pricing Policy；
- Contract Policy；
- Approval Policy；
- Operator Policy。

这一层负责回答：

> 同一个底层发行能力，为什么在不同产品、不同套餐、不同客户中表现不同？

例如：

- 星球发行 Basic 与 Plus 都能发行，但可管理曲库量、人工支持和商务条件不同；
- 企业版不同客户可以开通不同模块；
- AI 音乐发行只开放确定的一组 AI 音乐可发行 DSP，而不是共享全部星发渠道；
- 自助发行需要先支付，再进入发行流程。

### Layer 4：统一发行 Domain / Capability 层

未来产品架构的稳定核心。

#### Identity / Organization

- User
- Account
- Organization
- Tenant
- Role / Permission
- Operator

#### Catalog / Asset

- Artist
- Label
- CP / Content Provider
- Album / Release
- Track
- Music Video
- Composition
- Metadata
- Audio / Video / Artwork / File

#### Rights / Contract

- Master Agreement
- Release Authorization
- Rights
- Rights Scope
- Contract Party
- Electronic Signing
- Copyright Registration

#### Distribution

- Distribution Request
- Release Review
- Channel Selection
- Delivery / Transmission
- DSP / SP
- Delivery Route
- Delivery Status
- Takedown / Update
- Failure / Retry / Exception

#### Compliance

- Content Review
- Rights Review
- AI-related Declaration
- DSP Policy Check
- Blacklist / Risk Rule

#### Reporting / Royalty / Settlement

- DSP Report
- Royalty Report
- Revenue
- Split
- Receivable
- Receipt
- Withdrawal
- Settlement

#### Commercial Infrastructure

- Product
- Plan
- Entitlement
- Quota
- Usage
- Order
- Payment
- Invoice / Billing Reference

#### Operations / Service

- Customer Service Case
- Manual Review
- Change Request
- Takedown Request
- Legal / Copyright Case
- Service Priority / SLA

---

## 4. 三条产品线的产品边界

## 4.1 星球发行

### 产品本质

由看见音乐直接运营的 **Managed Distribution / 合作发行服务**。

客户主要包括：

- 独立音乐人；
- 厂牌；
- 版权公司；
- 聚合发行商及其他 CP。

### 操作端

继续以现有星球发行前台为主要用户产品，升级为：

- Basic
- Professional
- Plus

### 产品责任

星球发行负责：

- 看见与客户的合作发行关系；
- 总协议及单次发行授权；
- 发行审核、交付与状态；
- 月度报表、版税与提现；
- 客服、运营、法务等合作服务；
- 不同合作等级的服务、资源和商业条件。

### 不属于星球发行核心产品的内容

宣发推广不作为核心发行权益的一部分。

它可以：

- 作为独立音乐营销 / 投流产品售卖；
- 对 Professional / Plus 提供跨产品优惠或战略权益；
- 不应重新混入发行核心能力定义。

---

## 4.2 星球发行·企业版

### 产品本质

向希望自己开展音乐发行业务的企业客户输出 **Distribution OS / Distribution Infrastructure**。

### 两种交付方式

#### White-label SaaS

完整白标发行平台，应包含两类端：

```text
客户品牌
   │
   ├── 企业运营管理后台
   │     ├── 用户 / CP
   │     ├── 内容
   │     ├── 合同
   │     ├── 发行 / DSP
   │     ├── 审核 / 合规
   │     ├── 报表 / 分账
   │     └── 系统设置
   │
   └── 客户自己的发行前台
         ├── 注册 / 认证
         ├── 签约
         ├── 艺人 / 内容
         ├── 提交发行
         ├── 状态查询
         ├── 报表 / 收益
         └── 提现 / 用户服务
```

#### API

客户保留自己的产品，只调用看见的发行能力。

企业版后续应逐步形成标准能力 API 目录，而不是把内部 API 权限直接等同于对外 API 产品。

### 企业版的核心产品属性

- Operator 是企业客户；
- 看见提供底层系统、发行能力和渠道基础设施；
- 企业自己管理其音乐人、厂牌、CP 和业务规则；
- White-label 与 API 可以共享底层能力，但定价和交付方式不同。

---

## 4.3 AI 音乐发行

### 产品本质

一条**专门为 AI 音乐流通服务建立的付费自助发行产品线**。

核心流通商品是 AI 音乐，主要解决 AI 时代大量创作者希望快速、标准化、按服务付费发行音乐的问题。

### 关于“支持普通音乐”的准确边界

产品允许：

- AI 生成音乐；
- AI 辅助创作音乐；
- 普通音乐。

但产品的市场定位、渠道设计、审核规则和商业模型围绕 **AI 音乐发行场景**构建。

系统底层不人为维护“AI 音乐发行系统”和“普通音乐发行系统”两套 Domain；AI 相关信息作为作品、声明、审核与渠道策略属性存在。

### 渠道边界

AI 音乐发行不是星球发行全部 DSP 能力的缩小版。

首期只开放已经明确可承接 AI 音乐的一组固定 DSP（当前业务判断约十余个），形成独立 Channel Catalog：

```text
AI Music Distribution Channel Catalog
├── DSP A
├── DSP B
├── DSP C
└── ...
```

这组渠道由产品运营维护，不向用户暴露全部看见发行渠道。

### 核心流程

```text
注册 / 登录
   ↓
创建作品 / 上传文件
   ↓
填写 Metadata 与 AI 相关声明
   ↓
选择可发行 DSP
   ↓
选择服务方式 / 服务期限
   ↓
付款
   ↓
审核
   ↓
发行交付
   ↓
查看审核 / 上线状态
   ↓
报表与收益管理
```

### 与星球发行的根本区别

- 不以传统版税分成作为核心收费模式；
- 主要收入来自发行服务费 / 订阅 / 渠道 / 服务期等收费；
- 以自助、标准化、规模化为主要运营目标；
- 复用现有发行能力，但产品前台、订单、计费和渠道策略独立。

---

## 5. Operator：统一架构里的关键角色

三条产品的一个核心差异是“谁在经营这套发行关系”。

建议在产品架构中明确 **Operator（发行运营主体）** 概念。

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

对应关系：

| 产品 | Operator |
|---|---|
| 星球发行 | 看见音乐 |
| 企业版 White-label | 企业客户 |
| 企业版 API | 企业客户 |
| AI 音乐发行 | 看见音乐 / 自助系统运营 |

Operator 决定或关联：

- 品牌；
- 客户归属；
- 合同主体；
- 产品与套餐；
- 可用渠道；
- 审核策略；
- 服务策略；
- 报表与结算关系。

---

## 6. 三条产品应该共享什么

必须尽量共享：

- 用户与组织基础能力；
- 艺人 / 厂牌 / CP 主体模型；
- 专辑 / 歌曲 / MV / 词曲等 Catalog；
- 文件与 Metadata；
- 合同和授权数据模型；
- Release / Distribution Job；
- DSP 与传输能力；
- 审核 / 合规能力；
- 报表、收入与收益数据；
- Order / Payment 基础能力；
- Entitlement / Quota 基础能力。

共享的是：

> **能力、主数据、状态和业务规则基础设施。**

不要求共享：

- 官网；
- 前台 UI；
- 产品导航；
- 品牌；
- 价格；
- 套餐；
- 渠道组合；
- 客服入口；
- 具体运营流程。

---

## 7. 三条产品必须保持独立的部分

| 维度 | 星球发行 | 企业版 | AI 音乐发行 |
|---|---|---|---|
| 运营主体 | 看见 | 企业客户 | 看见 / 自助系统 |
| 主要客户 | 音乐人/厂牌/CP | 发行企业 | AI 音乐创作者/团队 |
| 核心商业关系 | 合作发行 | SaaS / API | 付费自助发行 |
| 渠道范围 | 看见合作发行渠道 | 客户合同/产品配置决定 | 固定 AI DSP Catalog |
| 产品体验 | 合作发行 Portal | Console + White-label Portal / API | 独立 Self-service Portal |
| 服务模式 | 客服/运营/专属服务 | 企业自己运营 + 看见企业支持 | 标准化自助服务 |
| 核心收费逻辑 | 分成 + 增值项 | 部署/模块/月费/Usage | 按发行/渠道/期限/订阅等 |

具体收费模型在下一阶段单独设计，本文只冻结结构。

---

## 8. 当前系统能力与未来架构的对应关系

### 当前 SaaS 管理后台

主要承接未来：

- Enterprise Management Console；
- Shared Distribution Platform 的后台操作能力；
- 看见内部运营能力。

### 当前星球发行前台

主要承接未来：

- 星球发行 Basic / Professional / Plus；
- 作为 White-label CP Portal 的重要能力来源。

### 当前开放 API

主要承接未来：

- 企业版 API 的基础；
- 但必须重新形成标准化、版本化、可计费、可授权的 API Product，而不是直接暴露内部接口。

### 当前支付能力

未来统一支撑：

- 企业版费用；
- AI 音乐发行订单；
- 星球发行 Add-on / 扩容 / 增值服务。

---

## 9. 产品架构阶段暂不解决的问题

以下问题进入下一阶段“商业模式设计”：

### 星球发行

- Basic / Professional / Plus 准入；
- 版税分成；
- ISRC / UPC；
- 艺人数；
- 曲库 / 存储；
- 发行量；
- 服务 SLA；
- 扩容包与 Add-on；
- 老用户迁移。

### 企业版

- White-label 报价；
- API 模块报价；
- Deployment / Setup Fee；
- 月费 / 年费；
- Usage Meter；
- 哪些当前能力可立即售卖。

### AI 音乐发行

- 按首 / 按专辑 / 按渠道 / 按期限；
- 订阅档位；
- 每月发行额度；
- DSP 组合；
- 服务期限；
- 收益结算方式；
- 增值服务。

---

## 10. 项目推进顺序

本项目后续统一按以下顺序推进：

### Phase 1：产品架构

目标：明确一套发行产品体系、三条产品线、共享底座和产品边界。

**当前文档即 Phase 1 的第一版基线。**

### Phase 2：商业模式

分别设计：

1. 星球发行 Basic / Professional / Plus；
2. 星球发行·企业版 White-label / API；
3. AI 音乐发行付费模型。

### Phase 3：具体产品形态

明确每条产品：

- 功能范围；
- 信息架构；
- 用户流程；
- 页面与操作端；
- 套餐展示；
- 购买 / 签约 / 结算体验。

### Phase 4：官网与市场包装

产出：

- 总发行产品体系对外表达；
- 三条产品官网结构；
- 企业版对外销售页；
- 套餐与价格页；
- 产品介绍与销售材料。

### Phase 5：产品原型与实施 Roadmap

产出：

- 核心页面原型；
- 改造项；
- 复用项；
- 新建项；
- 工程实施优先级；
- 分阶段上线 Roadmap。

---

## 11. 当前架构的一句话定义

> **看见音乐建立一套统一的音乐发行基础设施，并以“合作发行、企业发行基础设施、AI 音乐付费自助发行”三种产品形态面向不同客户；三者共享发行能力和业务数据，但拥有独立的运营主体、商业规则、渠道策略和产品体验。**
