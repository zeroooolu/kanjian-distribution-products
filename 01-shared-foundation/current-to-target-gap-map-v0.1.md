# 当前能力 → 目标产品架构 Gap Map v0.1

> 更新时间：2026-09-09  
> 文档定位：用于把当前 SaaS / 星球发行前台已有能力，与三条产品线的目标产品架构进行对照。  
> 目的不是直接形成研发排期，而是识别哪些能力可复用、哪些需要产品化、哪些需要新增。

---

## 1. Gap 分类

- **A｜可直接复用**：当前已有较完整业务基础，目标体系继续复用；
- **B｜已有但需产品化/改造**：业务已经存在，但当前形态不足以支撑新的产品分层、白标/API 或自助化；
- **C｜需要新增**：当前没有完整产品能力，本轮必须新增；
- **D｜暂不进入本轮核心范围**：已有或可做，但不是三条产品线首阶段关键路径。

说明：本文件基于当前已知 SaaS 权限树、星球发行前台与历史材料进行产品判断，不代表完成了代码级审计。

---

## 2. 总览

| Capability | 当前基础 | Gap | 主要服务产品 | 说明 |
|---|---|---|---|---|
| Account / Login | 已有 | A | 全部 | 手机、邮箱、验证码、Google、微信等已有基础 |
| Organization / CP | 已有 | A/B | 星发、企业版 | 企业版需要进一步产品化 Tenant / Operator 关系 |
| Role / RBAC | 已有 | A | 企业版 | 当前后台已有较完整角色权限基础 |
| Branding / Site | 已有 | B | 企业版 | 需要从“建站设置”升级为标准 White-label 产品能力 |
| Artist / Label / CP Catalog | 已有 | A | 全部 | 作为共享 Catalog |
| Album / Track / MV / Composition | 已有 | A | 全部 | 作为共享内容 Domain |
| Asset / Metadata | 已有 | A/B | 全部 | 需要接入 Quota / Usage / AI 声明 |
| Bulk Import | 已有 | A/B | 星发、企业版 | 后续按 Tier / Module 开放 |
| DDEX Ingestion | 已有 | A/B | 企业版、头部星发 | 需要确定对外产品形态 |
| Contract | 已有 | A | 星发、企业版 | 合同系统可复用，模板/政策按产品区分 |
| Release Authorization | 已有业务 | A/B | 星发、企业版、AI发行 | AI发行需重新设计交易/授权关系 |
| E-sign | 已有业务 | A | 星发、企业版 | 可作为共享服务 |
| Rights Registration | 已有 | A/B | 星发、企业版、AI发行 | 需要变成 Add-on / Quota / API Module |
| Release Creation | 已有 | A | 全部 | 共享发行链路核心 |
| DSP / SP | 已有 | A | 全部 | AI产品只消费指定子集 |
| Delivery / Transmission | 已有 | A | 全部 | 核心发行底座 |
| Release Status | 已有 | A | 全部 | 前台体验可分别设计 |
| Failed Task / Exception | 已有 | A/B | 全部 | AI发行需做更标准化用户反馈 |
| Compliance | 已有 | A/B | 全部 | AI发行需要独立 AI policy |
| Metadata Update | 当前依赖人工 | B | 星发、企业版、AI发行 | 需要正式服务请求/流程化 |
| Takedown | 当前依赖人工 | B | 全部 | 星发当前用户不可自助，下架需流程化 |
| Report | 已有 | A | 全部 | 共享报表基础 |
| Royalty / Revenue | 已有 | A/B | 全部 | AI发行商业规则不同，但数据链路可复用 |
| Split | 已有 | A/B | 星发、企业版 | AI发行是否需要传统分账视商业模式决定 |
| Settlement | 已有 | A/B | 全部 | 需与新商业模型对齐 |
| Withdrawal | 已有 | A/B | 星发、AI发行 | 当前仍有后台人工审核 |
| Analytics | 已有 | A/B | 星发、企业版、AI发行 | 后续按套餐开放 |
| Product / Plan | 缺少统一模型 | C | 全部 | 三产品商业化共同基础 |
| Entitlement | 缺少统一模型 | C | 全部 | Basic/Pro/Plus、企业模块、AI套餐共同依赖 |
| Quota | 缺少统一模型 | C | 全部 | 曲库、艺人、发行量、API等核心 |
| Usage Metering | 部分存在 | B/C | 全部 | 需要统一计量口径 |
| Capacity Pack / Add-on | 未统一 | C | 星发、企业版 | 用于扩容与增值能力 |
| Order | 部分业务存在 | B/C | 企业版、AI发行、星发增值 | 需要形成统一商业订单层 |
| Payment | 有独立支付建设基础 | B | 全部 | 需与三产品商业模型衔接 |
| SLA | 线下存在 | C | 星发、企业版 | 当前服务等级更多靠人工约定 |
| Service Case | 线下存在 | C | 星发、企业版、AI发行 | 下架、改单、版权问题等需产品化 |
| Dedicated Operator | 线下存在 | B | 星发 Plus | 需要变成正式产品权益 |
| Enterprise Module Activation | 历史报价有概念 | C | 企业版 | White-label/API 模块商业开通需要统一 |
| Enterprise API Productization | 有开放 API 基础 | B | 企业版 | 需从“接口”升级为稳定产品 |
| API Credential / Scope | 待核验 | B/C | 企业版 API | 需要标准开发者能力 |
| API Usage / Rate Limit / SLA | 待核验 | B/C | 企业版 API | 商业化 API 必须补齐 |
| API Webhook / Error Contract | 待核验 | B/C | 企业版 API | 需做 API Ready 审计 |
| AI Content Declaration | 未形成独立产品能力 | C | AI发行 | AI发行审核与渠道政策的核心输入 |
| AI Music Channel Catalog | 未形成独立产品目录 | C | AI发行 | 需要维护约十余个确定 DSP |
| AI DSP Eligibility / Policy | 未形成独立产品能力 | C | AI发行 | 决定某内容是否可发某渠道 |
| Self-service Checkout | 不存在于现有星发主流程 | C | AI发行 | 新产品核心体验 |
| Service Term / Renewal | 缺少统一模型 | C | AI发行 | 新商业模式核心 |
| Subscription / Release Package | 缺少统一模型 | C | AI发行 | Phase 2 确定具体模式 |
| Promotion / 投流 | 独立产品能力 | D | 跨产品 Add-on | 不进入发行 Core |

---

## 3. 星球发行：最大的 Gap 不在发行链路，而在“分层经营”

### 当前已经有

- 注册/认证；
- 总协议签约；
- 艺人管理；
- 专辑/歌曲/MV 创建；
- 内容上传；
- 专辑授权；
- 发行；
- 状态查看；
- 月度报表与版税；
- 提现申请；
- 客服/运营人工服务。

### 真正缺少

```text
Customer Tier
  ↓
Entitlement
  ↓
Quota
  ↓
Usage
  ↓
Service Level
  ↓
Commercial Policy
```

因此星球发行升级的核心并不是“重做发行”，而是把当前一刀切的合作方式变成可经营、可计量、可分级的产品。

### P0 Gap

1. Basic / Professional / Plus 的正式 Tier 模型；
2. 曲库/艺人/发行量等 Quota；
3. 超额后的 Capacity Pack / Add-on；
4. 服务等级和 SLA；
5. 下架/改单/版权问题的 Service Request；
6. 老用户迁移与重新评级机制。

---

## 4. 企业版：最大的 Gap 是“从已有 SaaS 变成标准产品”

当前 SaaS 已经有大量功能，不需要从零建设企业发行系统。

真正缺口是：

### 4.1 White-label Productization

当前已有：

- 管理后台；
- 用户/组织/角色；
- 建站设置；
- CP、艺人、厂牌；
- 合同；
- 发行；
- DSP；
- 报表；
- 分账。

需要补齐：

- White-label 标准交付边界；
- 品牌可配置项；
- 客户自己的发行前台标准模板；
- 模块开通；
- Tenant Entitlement；
- Capacity / Usage；
- 企业套餐与合同；
- SLA / Support Package。

### 4.2 API Productization

当前已知存在对外 Apifox 文档和大量内部 API 权限，但当前不能直接得出“所有模块均可作为标准 API 售卖”。

需要完成：

```text
Current API Inventory
      ↓
Capability Grouping
      ↓
API Ready Audit
      ↓
Stable Contract
      ↓
Credential / Scope
      ↓
Usage / Rate Limit
      ↓
Webhook / Error Contract
      ↓
Pricing / SLA
```

因此企业版本轮最重要的不是多开发几个页面，而是把已有能力变成清晰、稳定、可报价、可交付的标准产品。

---

## 5. AI 音乐发行：最大的 Gap 是“商业产品层和渠道政策层”

AI 音乐发行不需要重新建设完整发行底座。

可复用：

- User；
- Artist；
- Album / Track；
- Metadata；
- Asset；
- Release；
- Review；
- Delivery；
- DSP Status；
- Report；
- Revenue；
- Withdrawal。

需要新增的核心能力：

### 5.1 AI 内容声明

用户提交时需要形成结构化 AI 内容信息，用于审核和渠道判断。

### 5.2 AI Music Channel Catalog

维护本产品可售卖的约十余个 DSP，而不是直接展示看见全部发行渠道。

### 5.3 AI Channel Eligibility

依据内容声明和渠道规则判断：

> 这首作品能否发这个 DSP。

### 5.4 付费发行 Commerce

```text
Package / SKU
  ↓
Channel Selection
  ↓
Service Term
  ↓
Price
  ↓
Order
  ↓
Payment
  ↓
Entitlement
  ↓
Release
```

### 5.5 Renewal / Expiration

如果最终商业模式包含服务期限，则必须定义：

- 到期后如何续费；
- 不续费作品如何处理；
- 渠道是否需要下架；
- 收益如何结算。

这部分是现有星球发行商业关系中基本不存在的新问题。

---

## 6. Shared Commercial Core：建议作为三产品共同新能力

目前最大的共性新增，不是发行，而是商业化基础设施。

建议目标模型：

```text
Product
├── STAR_RELEASE
├── ENTERPRISE
└── AI_DISTRIBUTION

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
Payment
```

三产品分别使用不同规则，但不分别建设三套套餐、权益、计量逻辑。

### 星球发行使用它解决

- Basic / Pro / Plus；
- 曲库/艺人/发行额度；
- 扩容包；
- Add-on。

### 企业版使用它解决

- SaaS 模块；
- API 模块；
- 租户容量；
- 月费；
- API Usage。

### AI 音乐发行使用它解决

- 单次发行；
- 渠道套餐；
- 服务期限；
- 订阅；
- 每月发行额度。

---

## 7. Shared Service Core：另一个容易被忽略的共同缺口

建议把当前人工处理的事务逐步统一为 Service Case：

```text
Service Case
├── Metadata Update
├── Takedown
├── Copyright Issue
├── Finance / Withdrawal Issue
├── Delivery Exception
└── General Support
```

每个 Case 有：

- CP；
- Release；
- Type；
- Priority；
- SLA；
- Assigned Operator；
- Status；
- Resolution。

### 对星球发行的意义

可以真正区分 Basic / Pro / Plus 的服务等级和运营成本。

### 对企业版的意义

White-label 客户可以获得一套可复制的发行运营工作环境。

### 对 AI 音乐发行的意义

把少量无法自助解决的问题纳入标准客服，而不是重新回到微信群式服务。

---

## 8. 从产品角度的优先级

### Phase 1 继续完成产品架构

P0：

1. 三产品关键业务流关系图；
2. 产品架构 ADR / 决策记录；
3. 当前 Gap Map 评审与冻结。

### Phase 2 商业模式

优先顺序建议：

1. 星球发行 Basic / Pro / Plus；
2. 企业版 SaaS / API；
3. AI 音乐发行。

原因不是重要性不同，而是星球发行的分层规则会反过来帮助明确：

- 哪些能力是合作发行权益；
- 哪些能力应该成为付费 Add-on；
- 哪些能力更适合放入企业版；
- 哪些自助化能力可直接复用到 AI 音乐发行。

---

## 9. 当前结论

现有系统的核心问题不是“发行能力不够”，而是：

> **已有很多能力，但没有被统一组织成面向三种商业模式的产品架构。**

真正需要本轮新增的重心是：

```text
Productization
+ Tier / Plan
+ Entitlement
+ Quota
+ Usage
+ Commerce
+ Service Operations
+ Enterprise API Productization
+ AI Channel Productization
```

因此后续 Roadmap 应以这些差距为核心，而不是重新建设 Catalog / Release / DSP / Royalty 等已经存在的基础业务系统。
