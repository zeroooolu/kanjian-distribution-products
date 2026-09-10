# 企业音乐发行基础设施竞品研究（White-label / API）

> 日期：2026-09-10  
> 状态：Research baseline v1.0  
> 目的：为「星球发行·企业版」产品定义、商业模式、产品形态与 Roadmap 提供行业事实基线。  
> 范围：不研究 DistroKid / TuneCore 等面向音乐人的零售发行产品，重点研究“帮助企业搭建自己的音乐发行业务”的 B2B 基础设施产品。

---

# 1. 结论先行

当前海外 B2B 音乐发行基础设施已经形成较稳定的产品范式：

> **基础设施供应商不只是替企业发行音乐，而是把“经营一家音乐发行商所需要的技术与供应链能力”作为产品出售。**

典型客户包括：

- 独立发行商；
- 唱片公司 / 厂牌集团；
- 艺人服务公司；
- 音乐 SaaS / 创作工具；
- 流媒体、内容平台、社区产品；
- 希望增加音乐发行能力的其他企业。

行业普遍存在两种基础接入形态：

```text
White-label SaaS
企业不自行开发发行系统，直接使用供应商提供的品牌化发行平台

API / Headless Infrastructure
企业保留自己的产品和前台，通过 API / DDEX / XML / Webhook 等接入发行供应链
```

成熟厂商会继续向下提供：

```text
Catalog / Metadata
→ QC / Validation
→ Distribution / Delivery
→ DSP Status / Update / Takedown
→ Analytics / Reporting
→ Royalty Accounting
→ Payment / Payout
```

但不同厂商覆盖深度不同。

---

# 2. 行业产品可以分成四类

## 2.1 Turnkey White-label Distribution

代表：SonoSuite、EVEARA、Revelator White Label。

核心卖点：

> 企业不用自建发行系统，就可以用自己的品牌、域名、客户关系与定价运营一个发行平台。

典型能力：

- 自定义域名；
- Logo / 色彩 / 登录页；
- 企业自己的 End User / Label / Artist；
- 用户自行创建 Release；
- 企业管理员审核；
- 发行到 DSP；
- 查看数据与收益；
- 企业配置用户价格、分成或服务规则。

White-label 的成熟形态并不等于“换 Logo”，而是完整的 **Distributor Operating Console + Client Portal**。

---

## 2.2 Headless Distribution API / Digital Supply Chain

代表：AudioSalad、FUGA、LabelGrid Engine、Revelator API。

核心卖点：

> 企业已经有自己的产品或内部系统，只需要采购发行供应链能力。

典型 API 生命周期：

```text
Client / Organization
→ Artist / Label
→ Track / Release
→ Asset Upload
→ Metadata Validation
→ Submit / Approve
→ DSP Selection
→ Deliver
→ Delivery Status
→ Update / Redelivery
→ Takedown
→ Report / Revenue
```

成熟 API 通常还包括：

- Sandbox；
- API Token / OAuth；
- Webhook；
- Delivery Log；
- Metadata Validation；
- 幂等 / 状态管理；
- DDEX / XML 批量或企业级通道。

---

## 2.3 Enterprise Delivery Infrastructure

代表：FUGA、AudioSalad。

与普通“发行 API”相比，更重要的是允许客户：

- 使用平台已有 DSP 发行关系；
- 或使用客户自己的 DSP Direct Deals；
- 按 DSP / Territory / Release 设置不同交付策略；
- 使用 DDEX / XML 等行业标准接入；
- 管理大规模 Catalog 和复杂供应链。

这一层的核心不是 UI，而是 **Distribution Deal 与 Delivery Technology 解耦**。

---

## 2.4 Music Business OS

代表：Revelator，以及部分 Label Management 产品。

在发行之外继续覆盖：

- Contract；
- Revenue Split；
- Royalty Processing；
- Statement；
- Recoupment；
- Balance；
- Payment / Payout；
- Rights；
- Publishing 等。

这一类产品更完整，但建设成本和业务复杂度显著高于单纯 Distribution Infrastructure。

---

# 3. 核心竞品矩阵

| 产品 | 核心定位 | White-label | API / Headless | 子客户 / 多厂牌 | Own DSP Deal | QC / Delivery Lifecycle | Royalty | Payment | 公开计费信号 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| AudioSalad | Digital Supply Chain / Delivery Infrastructure | ✅ | ✅ | ✅ 用户协作 | ✅ | ✅ | 报表为主 | 未见核心能力 | 月 SaaS License，按 Assets Under Management 分档 |
| FUGA | Enterprise Music Distribution Infrastructure | ✅ | ✅ REST / XML / DDEX | ✅ Sub-account | ✅ Direct Deals / FUGA Deals | ✅✅ | Analytics / 部分商业能力 | 非核心公开卖点 | Enterprise 合同制 |
| Revelator | Music Distribution & Business OS | ✅✅ | ✅✅ | ✅ Organization / Client | ✅ | ✅✅ | ✅✅ | ✅ | Enterprise / API 合同制 |
| SonoSuite | White-label Distribution SaaS | ✅✅ | ✅ Distribution API | ✅ End User / Label | ✅ Direct / SonoSuite / Merlin | ✅✅ | ✅ | 出款动作主要在平台外完成 | 企业报价，容量 / 用户 /发行服务相关 |
| LabelGrid | Distribution Platform + Developer API | Imprint | ✅✅ Engine | ✅ Label Portal | 有企业能力 | ✅ | ✅ | Imprint 强调 Artist Payout | API 按 Tracks / Labels / Monthly Royalties / SLA 分档 |
| EVEARA | Turnkey White-label DIY Distribution | ✅✅ | ✅ | ✅ | 以平台 DSP agreements 为主 | ✅ | ✅ Reporting | ✅ Payout 能力 | 企业定制报价 |
| ampsuite | Label Management + Distribution + Accounting | 品牌化业务系统 | 未见其把 API 作为核心公开卖点 | ✅ Label / Licensor | 可与发行服务结合 | ✅ | ✅✅ | 当前帮助中心说明实际支付需平台外完成 | Distribution Revenue Share 或 Label Services Subscription |
| Label Engine | Distribution + Label Accounting / Promotion | 有品牌化 Label Services，但非典型平台级白标 | 未见公开完整 Distribution API 产品 | 多 Label | 非核心 | ✅ | ✅✅ | 支持处理应付但产品定位偏 Label Ops | 发行抽成；Label Services 固定订阅 |

> 注：矩阵只记录截至 2026-09-10 能从官方公开资料确认或较可靠推断的能力。未公开不等于产品一定不支持。

---

# 4. AudioSalad

## 4.1 产品定位

AudioSalad 更接近 **Digital Supply Chain / Delivery Infrastructure**，产品公开结构包括：

- Catalog Management；
- Distribution；
- Delivery；
- API；
- Analytics；
- White Label。

其核心优势是把音乐内容管理与全球 DSP 交付做成基础设施，而不是仅提供面向艺人的发行前台。

## 4.2 Delivery 与 Distribution 分离

这是最值得星球发行企业版参考的设计之一。

AudioSalad 明确支持两种客户：

```text
客户已有 DSP Direct Deals
→ 只使用 AudioSalad Delivery Technology

客户没有 Direct Deals
→ 使用 AudioSalad Distribution Service / Deals
```

说明：

> **发行代理关系（Deal）和技术交付（Delivery）是两个独立产品能力。**

这使其既能服务普通厂牌，也能服务已经拥有 DSP 直签关系的大型发行商。

## 4.3 API

公开 API 能力包括：

- Headless Content Management；
- Metadata / Media Retrieval；
- Remote Ingestion；
- Trigger Delivery；
- Return Delivery Status。

## 4.4 White Label

公开能力包括：

- Logo；
- Color Scheme；
- Custom Domain；
- Branded Dashboard；
- 邀请客户和团队进入平台；
- 客户可在品牌化 Dashboard 中管理内容和交付。

## 4.5 DDEX 与计费

AudioSalad 官方 FAQ 明确表示支持 DDEX，并列出了多个 ERN 版本。

计费结构公开为：

> Monthly SaaS software license fee + pricing tiers based on number of assets under management。

这说明大型发行基础设施的计费单位通常与 **Catalog Scale** 绑定，而不是单纯按照 API Request 次数。

### 对星球发行的启发

1. 必须把 Delivery 与 Distribution Deal 分开建模；
2. Catalog / Asset Volume 是合理计费锚点；
3. API 应覆盖完整供应链状态，而不是只有“创建发行”；
4. DDEX 是进入真正 Enterprise 客户层级的重要能力。

---

# 5. FUGA

## 5.1 产品定位

FUGA 是本轮最接近“Enterprise Distribution Infrastructure 天花板”的参考对象。

当前公开核心包括：

- Catalog Management；
- Music Distribution；
- Analytics；
- White Label；
- API；
- XML / DDEX；
- Webhook；
- Direct Deal / FUGA Deal 体系。

## 5.2 White Label 是组织与审核模型

FUGA White Label 不只是视觉品牌化。

典型结构：

```text
Primary Distributor Account
│
├── Sub-label Account
├── Artist Account
└── Other Sub-account
```

子账号可以：

- 上传内容；
- 创建 Release；
- 提交到 Distributor 主目录。

Distributor 可以：

- Review；
- Edit；
- Reject；
- Accept / Approve；
- 控制发行日期；
- 控制 Delivery Setting；
- 控制 Delivery Partner。

所以真正的 White Label 核心是：

> **客户经营自己的下游发行网络，而基础设施供应商在后面提供 Supply Chain。**

## 5.3 API / XML / DDEX / Webhook

FUGA 允许企业通过程序化方式执行：

- 指定 DSP；
- 设置 Release Schedule；
- Trigger Delivery；
- Update；
- Redelivery；
- Takedown；
- 获取 Trends / Analytics。

2026 年官方帮助中心还明确提供 Catalog & Distribution API 的 OAuth Client ID / Client Secret 管理。

Webhook 可用于监听 Product 状态变化，在 White Label 场景通知 Distributor 有新的下游产品提交审核或被拒绝。

## 5.4 Direct Deals

FUGA 条款明确区分：

- 客户自己的 DSP Direct Deals；
- FUGA / IIP 的 Aggregation Deals。

说明 Deal Policy 是 Enterprise Distribution 的一等配置对象。

### 对星球发行的启发

1. Enterprise 要建立 Primary Operator / Sub-account 层级；
2. Review Gate 必须处在子客户和实际 DSP Delivery 之间；
3. API、White Label、DDEX 不应是三套独立业务，而应共享同一个 Distribution Domain；
4. Webhook 是 API 产品的基础能力，不是后期附加功能；
5. Own Deal / Platform Deal 是大客户必然需求。

---

# 6. Revelator

## 6.1 产品定位

Revelator 已经从发行工具扩展为较完整的 **Music Business OS**。

其 API 当前公开覆盖：

```text
Digital Supply Chain
+ Analytics
+ Royalty Processing
+ Payment Distribution
```

## 6.2 API

官方描述的 API 能力包括：

- Release / Track / Metadata / Rights；
- Release Scheduling；
- Delivery Status；
- Webhook；
- Streaming / Revenue Analytics；
- Contract；
- Split；
- Recoupable；
- DSP Statement；
- Royalty Statement；
- Payment Status。

同时支持：

- 使用 Revelator DSP agreements；
- 或使用客户自己的 DSP agreements。

## 6.3 组织模型

Revelator API 明确存在两级：

```text
Organization
└── Client
    ├── Releases
    ├── Tracks
    ├── Artists
    └── Labels
```

Organization 管理一个或多个 Client，并负责部分行政操作、Release inspection 和 DSP configuration。

这与企业发行平台需要的 Operator → Client 层级高度一致。

## 6.4 White Label

公开能力包括：

- Custom Domain / Subdomain；
- Logo / Color；
- Login / Signup Page；
- Branded Email；
- DKIM / SPF；
- Support URL；
- Distribution / Privacy Policy；
- 多语言（官方当前宣传 19 languages）；
- Label / Artist Portal；
- Client Feature Management。

### 对星球发行的启发

Revelator 很适合作为长期能力地图参考，但不适合一期完整复制。

其 Contract → Royalty → Payment 已经进入另外一个复杂领域。如果星球发行企业版一期目标是快速验证 Distribution Infrastructure，应该优先完成发行供应链，而不是立即复制完整 Music Business OS。

---

# 7. SonoSuite

## 7.1 产品定位

SonoSuite 是最典型的 **Turnkey White-label Music Distribution SaaS**。

目标是让企业不需要自建技术基础设施，就能以自己的品牌和域名开展数字发行业务。

核心公开产品包括：

- Catalog；
- Distribution；
- QC；
- Royalty Management；
- Reports / Analytics；
- White Label；
- Distribution API。

## 7.2 发行策略

SonoSuite 当前明确提供：

- Direct Deals；
- SonoSuite Partnerships；
- Merlin；

不同 Distribution Strategy。

这再次证明：

> **“走谁的 DSP Deal”必须从 Delivery Engine 中独立出来。**

## 7.3 QC Workflow

其典型流程为：

```text
End User Creates Release
→ Request Distribution
→ Delivery Pipeline
→ SonoSuite QC
→ Approved / Rejected
→ DSP Delivery
```

高级支持等级还会影响 QC 出错后的服务方式。

## 7.4 企业自己控制用户商业规则

SonoSuite 的管理端支持给不同 End User 配置不同 Pricing。

其公开 Pricing 字段包括：

- Price per release；
- UPC；
- ISRC；
- Delivery per track / channel；
- QC；
- Takedown；
- Update；
- Upload 等。

这一点非常重要：White Label 的企业客户不是系统使用者，而是 **面向下游用户的发行服务经营者**。

## 7.5 规模单位

官网当前展示的起始容量信号包括：

- 5,000 tracks；
- 500 user accounts；
- 3 admin accounts；
- Bulk upload；
- Dedicated account manager；
- own deals setup。

这类容量比“多少 API Calls”更接近发行企业实际业务规模。

### 对星球发行的启发

1. White Label 必须支持企业自主管理 End User；
2. 企业应能配置对下游客户的商业规则，而不只是看见对企业的收费；
3. Track / User / Admin / Delivery Volume 都可作为企业套餐计量项；
4. QC 和 Support SLA 可以商业化分层。

---

# 8. LabelGrid

## 8.1 产品拆分值得重点参考

LabelGrid 当前把 B2B 产品明确拆为：

```text
Engine
= Distribution API / Developer Infrastructure

Imprint
= Hosted White-label Portal
```

这个拆法比简单叫“API版 / 白标版”更接近两个独立产品形态。

## 8.2 Engine API

公开能力包括：

- Catalog read；
- Create / update release；
- Upload audio / artwork；
- Artist / Contributor；
- Webhook；
- Submit for distribution；
- Sandbox；
- Bearer Token；
- Public API Docs。

## 8.3 API 公开定价

截至 2026-09，公开 API 计划为：

| Plan | 月价（年付） | Tracks | Labels | Monthly Royalties | SLA |
|---|---:|---:|---:|---:|---|
| Starter API | $139 | 3,000 | 5 | $35k | 48h |
| Growth API | $389 | 10,000 | 25 | $115k | 48h |
| Scale API | $879 | 25,000 | 100 | $350k | Dedicated TAM / 24h |
| Custom API | $2,149+ | Bespoke | Unlimited | Custom / Unlimited | Custom |

最值得关注的不是具体价格，而是它的 **计费维度**：

```text
Catalog Size
+ Number of Labels
+ Monthly Royalties Processed
+ Support SLA
```

即：按照客户的发行生意规模收费，而不是按照 HTTP API 调用次数收费。

## 8.4 Imprint White Label

当前公开说明：

- 企业自己的 Brand / Domain；
- 企业自己定义 Plan / Price；
- 用户向企业付款；
- 支持 Artist Payout；
- LabelGrid 在后台提供发行基础设施。

### 对星球发行的启发

1. Enterprise 产品可拆成 Hosted 和 Headless 两种清晰形态；
2. API 必须提供 Sandbox / Docs / Webhook / Logs；
3. 商业计量应面向 Tracks / Labels / Revenue / SLA；
4. White Label 的终局是让客户经营自己的 SKU、Price、User、Payout，而不是简单租用后台。

---

# 9. EVEARA

EVEARA 是典型的 B2B SaaS White-label DIY Distribution。

公开能力包括：

- Fully customizable White Label UI；
- Full API Capabilities；
- DSP Agreements；
- Distribution；
- Music ID；
- Fingerprinting；
- Analytics；
- Marketing Tools；
- Reporting；
- Payout；
- Multiple Languages；
- Native iOS / Android 能力。

其商业叙事非常明确：

> 企业通过接入 EVEARA，在自己的品牌中增加一条可持续收费的音乐发行业务，而 EVEARA 作为“invisible partner”存在。

### 对星球发行的启发

企业版的客户价值不能只写“减少技术开发成本”，还应该写：

- 增加新的业务线；
- 获得新的经常性收入；
- 增强原有客户粘性；
- 获取更多音乐内容与业务数据。

---

# 10. ampsuite / Label Engine：补充参考

这两家公司不是本轮最核心的 Headless Distribution Infrastructure 对标，但对“发行商内部经营系统”有参考价值。

## ampsuite

产品从 Label Operations 出发，把：

- Release；
- Distribution；
- Promotion；
- Contract；
- Accounting；
- Licensor；
- Publishing；

放进一个业务系统。

值得注意的是：其 Accounting 能生成艺人 / Licensor Statement，但官方当前帮助中心明确说明实际支付动作仍需企业在平台外通过银行、PayPal 等方式完成。

说明 **Royalty Accounting 与 Payment Rail 可以分阶段建设**。

## Label Engine

以：

- Distribution；
- Accounting；
- Promotion；
- Demo Management；

为核心。

它展示了另一种商业模式：发行可以采用 Revenue Share，而独立 Label Services 也可以固定订阅收费。

---

# 11. 行业已经形成的“标配”与“进阶能力”

## 11.1 White-label 最低标配

```text
Custom Domain
Logo / Color / Brand
Login / Signup
Email Branding
End User / Label Management
Catalog / Release Creation
Distribution Request
Report / Revenue View
Support Contact
```

只做到这些，只能算基础 White-label。

## 11.2 真正拉开差距的能力

### A. Multi-tenant / Hierarchy

```text
Infrastructure Provider
└── Distributor / Enterprise Operator
    ├── Label
    ├── Sub-label
    ├── Artist
    └── Client
```

### B. Deal Configuration

```text
Platform DSP Deal
Own DSP Direct Deal
Hybrid Deal by DSP / Territory
```

### C. Supply Chain Control

```text
Validate
→ Submit
→ Review
→ Approve / Reject
→ Schedule
→ Deliver
→ Delivery Status
→ Redelivery / Update
→ Takedown
```

### D. Developer Infrastructure

```text
REST API
DDEX / XML
Sandbox
API Credential
Webhook
Delivery Log
Audit Log
```

### E. Revenue Infrastructure

```text
DSP Statement
→ Revenue
→ Split
→ Royalty Statement
→ Balance
→ Payout Request / Payment
```

### F. Enterprise Control Plane

企业管理员能够配置：

- Brand；
- Client；
- Feature；
- DSP；
- Deal；
- Pricing；
- Contract / Revenue Share；
- QC Policy；
- Quota；
- SLA；
- API Credential。

---

# 12. 商业模式的行业规律

综合本轮竞品，企业发行基础设施的收费大致围绕以下结构展开：

```text
Base Platform / License Fee
+
Capacity / Usage
+
Optional Modules
+
Support / SLA
+
Distribution Economics（如适用）
```

常见计量单位：

- Tracks / Assets Under Management；
- Labels / Clients；
- End User Accounts；
- Admin Accounts；
- Release / Delivery Volume；
- Monthly Royalties Processed；
- Storage / Media；
- DSP / Channel；
- API / DDEX 能力等级；
- Support SLA。

行业信号非常明确：

> **API Call 次数不是音乐发行基础设施最好的主计费单位。Catalog 和业务规模更能反映长期成本与客户价值。**

---

# 13. 对「星球发行·企业版」最重要的行业结论

## 13.1 产品本质

星球发行企业版不应该被定义为“星球发行的大客户版本”。

更准确的是：

> **向企业输出音乐发行基础设施，让企业以自己的品牌、客户关系和商业模式开展音乐发行业务。**

## 13.2 White-label 和 API 必须共用同一底座

White-label 是看见提供 UI；API 是客户提供 UI。

两者下面应该是同一套：

```text
Organization / Client
Catalog
Rights
QC
Release
DSP
Delivery
Report
Royalty
```

不能形成两套业务逻辑。

## 13.3 White-label 不只是 Branding

真正需要的是：

> **Operator Control Plane。**

企业客户必须能够经营自己的：

- 用户；
- 厂牌；
- 内容；
- 发行规则；
- DSP；
- 审核；
- 商业规则；
- 报表和收益。

## 13.4 Delivery 与 Deal 必须解耦

目标模型应支持：

```text
看见 DSP Deal
客户 Own Deal
Hybrid Deal
```

一期可以只开放看见 Deal，但 Domain Model 不应把两者写死。

## 13.5 一期不要直接复制完整 Revelator

建议先把 Distribution Infrastructure 做完整：

```text
Tenant / Client
+ Catalog
+ QC
+ Delivery
+ DSP
+ Status
+ Reporting
+ White Label
+ API
```

Royalty Accounting / Contract / Global Payment 可以逐步扩展。

---

# 14. 后续还需要继续确认的问题

以下问题需要进入星球发行企业版正式产品设计阶段：

1. 首批真实客户是谁；
2. 客户更偏 White-label 还是 API；
3. 客户是否已有 DSP Direct Deal；
4. 看见是否允许不同企业使用不同 DSP 合同主体 / Deal；
5. 企业的下游客户层级需要做到几级；
6. QC 是看见统一执行、企业执行，还是混合；
7. Revenue / Royalty 由看见算到企业，还是继续算到企业下游客户；
8. 企业是否能配置自己的发行价格和 Revenue Share；
9. 是否在一期提供真实 Payout；
10. 企业版如何与现有星球发行客户、合同和 Catalog 隔离；
11. API 的第一批具体 Use Case；
12. DDEX / Own Deal 放在哪一个阶段。

---

# 15. 官方研究来源

以下均为本轮优先采用的官方公开资料，访问日期 2026-09-10：

## AudioSalad

- https://audiosalad.com/services/
- https://audiosalad.com/faq/

## FUGA

- https://fuga.com/products-services/music-distribution/
- https://fuga.com/products-services/old-music-distribution/
- https://support.fuga.com/hc/en-us/articles/50684825679252-Managing-your-FUGA-API-credentials
- https://support.fuga.com/hc/en-us/articles/28485420930324-FUGA-Webhooks-User-Guide
- https://legal.fuga.com/7689e3743b9172f1/

## Revelator

- https://revelator.com/features/api
- https://revelator.com/features/white-label
- https://revelator.com/product/revelator-api
- https://api-docs.revelator.com/v2/en/getting-started/
- https://api-docs.revelator.com/en/distribution

## SonoSuite

- https://sonosuite.com/
- https://sonosuite.com/features
- https://sonosuite.com/distributors
- https://support.sonosuite.com/hc/en-us/articles/228897648-What-is-SonoSuite
- https://support.sonosuite.com/hc/en-us/articles/4404704187666-Pricing-Tab
- https://support.sonosuite.com/hc/en-us/articles/4405649848978-Can-I-set-different-pricing-for-a-specific-End-User

## LabelGrid

- https://labelgrid.com/features/white-label-and-api/
- https://labelgrid.com/features/music-distribution-api/
- https://labelgrid.com/pricing/
- https://help.labelgrid.com/en/developers/api-overview/

## EVEARA

- https://eveara.com/
- https://eveara.com/features/
- https://eveara.com/diy-distribution/

## ampsuite

- https://support.ampsuite.com/hc/en-us
- https://support.ampsuite.com/hc/en-us/articles/8488851014164-Introduction-to-Accounting
- https://support.ampsuite.com/hc/en-us/articles/17740710611860-How-do-I-pay-my-artists

## Label Engine

- https://label-engine.com/
- https://metrics.label-engine.com/pricing.php
- https://help.label-engine.com/en/collections/2663000-accounting

---

# 16. 本文使用方式

本文只负责回答：

> **这个行业当前是怎么做企业音乐发行基础设施的？**

星球发行企业版自己的定位、架构、一期边界和 Roadmap 不在本文中直接定案，统一进入：

`03-enterprise/product-definition-and-architecture-v0.1.md`
