# 海外音乐发行产品商业模式研究（2026-09）

> 目的：为星球发行 Basic / Professional / Plus 重构，以及后续 AI 自助发行商业模式设计提供参考。
> 
> 研究重点不是功能穷举，而是观察海外发行产品如何处理：长尾客户、艺人数量、发行数量、持续存储/在架成本、人工服务成本、续费、增值服务和 AI 音乐风险。

## 一、结论先行

海外主流独立发行产品并不存在一种统一模式，但有几个高度稳定的商业规律：

1. **低门槛产品普遍把“艺人数量”作为核心分层单位，而不是把 ISRC / UPC 单独卖成主要收入来源。**
2. **“无限发行”通常建立在年度订阅、低人工服务和续费机制之上**；如果取消订阅，部分平台会下架内容，或者要求为“永久保留”额外付费。
3. **按发行付费仍然广泛存在**，适合低频用户，也天然可以覆盖每次发行产生的审核、交付和长期维护成本。
4. **头部客户通常不是简单购买更贵套餐，而是进入精选/邀请制合作层**，获得专属客户经理、DSP 营销、预付/Advance、定制分成等服务。
5. **客服 SLA 是非常典型的版本差异。**低档以工单和标准响应为主，高档提供 1 个工作日甚至专属客户经理。
6. **Add-on 是重要利润结构。**永久保留、封面授权、Content ID、Dolby Atmos、母带、推广等均可独立收费。
7. **AI 音乐的行业方向不是简单“允许/禁止”，而是：披露 + 风险审核 + 渠道差异 + 反垃圾上传。**无限 AI 上传风险正在明显上升。

对星球发行最关键的一点是：**不能直接复制 DistroKid / Ditto 的“无限发行”。星球发行当前本身没有年度订阅来覆盖长尾客户的持续存储和运营成本，因此必须增加资源配额和超额商业化。**

---

## 二、主要竞品模式

### 1. DistroKid

**模式：年度订阅 + 无限发行 + 按艺人数量分层 + 大量 Add-on。**

当前产品主要分为 Musician、Musician Plus、Ultimate。所有版本均可无限上传，但：

- Musician：1 个艺人/乐队；
- Musician Plus：2 个艺人/乐队；
- Ultimate：可扩展到更多艺人（当前官网展示最高可到 100）；
- 高版本增加定时发行、Label Name、进阶数据、音频替换等能力。

ISRC 和 UPC 在正常上传发行时自动生成且免费，并不是核心收费项。

DistroKid 一个非常重要的成本机制是：**如果用户停止支付年度订阅，作品可能从 DSP 下架。**用户可以针对单个发行购买 Leave a Legacy Add-on，让作品在订阅终止后仍长期保留。当前公开价格中 Leave a Legacy 为单曲和专辑分别收费。

#### 对星球发行的启发

- 艺人数量非常适合作为“客户规模”的简单外显指标；
- 但真正解决长期成本的是**年度续费/长期托管机制**；
- “继续在架”本身也可以成为一种持续服务，而不是默认永久免费。

---

### 2. Ditto Music

**模式：年度订阅 + 无限发行 + 按艺人数分层。**

当前结构：

- Starter：1 个艺人；
- Pro：2 个艺人；
- Labels：3 个以上艺人并继续随艺人数量增长计价；
- 所有版本强调无限发行、100% streaming royalties；
- Pro 开始增加 Sync、Publishing、YouTube Content ID、Priority Support 等能力。

Ditto 允许订阅费从版税余额中自动扣除，是一个值得注意的续费设计。

#### 对星球发行的启发

Ditto 最值得参考的不是“无限发行”，而是：

> **把账号管理的艺人数作为厂牌/个人的规模分界，再把高级商业服务放到高版本。**

这与星球发行当前个人音乐人、中小厂牌、大型厂牌/发行商并存的客户结构高度吻合。

---

### 3. TuneCore

**模式：年度 Unlimited Plan + Pay-per-release 双轨。**

当前年度计划包括 Rising Artist、Breakout Artist、Professional；同时仍保留单曲/专辑按发行收费模式。

非常值得参考的是其版本差异：

- 基础发行能力各版本基本一致；
- 客服响应明确分为约 3 / 2 / 1 个工作日；
- Professional 才强调多艺人管理、Label Name 等厂牌能力；
- Professional 新增艺人 Profile 可单独付费扩容。

#### 对星球发行的启发

这说明成熟发行产品通常不会通过“低版本不能正常发行”来分层，而更多用：

- 客户规模；
- SLA；
- 数据/分析；
- 高级管理能力；
- 扩容收费；

来完成商业分层。

---

### 4. Amuse

**模式：年度订阅 + Unlimited Distribution + 艺人数 + 服务等级。**

当前 Artist / Artist Plus / Professional 大致对应 1 / 2 / 3+ Artist Profiles，并设置不同支持速度，Professional 提供 Priority Support。

值得关注的两个机制：

1. 官网明确强调即使降级，音乐仍可保持上线；
2. 当前 Terms 规定，在没有有效 Base Subscription 的完整月份中，会对版税收取一定比例 Commission。

也就是说，Amuse 用“订阅费”和“无订阅情况下的分成”完成两种成本回收路径。

#### AI 相关

Amuse 2026 年公开规则允许 AI-generated music，但明确：

- 某些平台会被排除（其帮助中心目前举例包括 Qobuz、Meta、YouTube Content ID）；
- 模仿知名艺人、AI Cover 会拒绝；
- Terms 对 AI Release 的短期大量上传设有速度限制（rolling period upload limit）。

#### 对星球发行的启发

这对未来 AI 自助发行尤其重要：**不要做真正意义上的无限 AI 发行。**即使做订阅，也应有月度/周期发行额度和反滥用机制。

---

### 5. CD Baby

**模式：一次性按 Release 收费 + 收益抽成。**

当前没有维持账号所需的年度订阅费：

- Single 按次收费；
- Album 按次收费；
- Streaming / Download 等收益继续按一定比例抽成；
- FastForward 等优先审核、优先支持为独立 Add-on。

#### 对星球发行的启发

这是 AI 自助发行非常值得参考的一类模式：

> **每一个新发行天然产生一笔确定收入，因此不容易出现“用户无限制造内容，但平台永远无法收回成本”的问题。**

对于高频 AI 内容尤其有价值。

---

### 6. RouteNote

**模式：Free Revenue Share + Premium Pay-per-release + 后续年度维护。**

当前：

- Free：无前置费用，平台保留一部分发行收益；
- Premium：按 Single / EP / Album 类型支付首年费用并保留 100% streaming/download revenue；
- Premium 后续需要年度维护费用；如果不再付费，可切回 Free 模式。

这是典型的“低价值用户按分成、高价值用户付费买断分成”的混合结构。

#### 对星球发行的启发

RouteNote 给出的最大启发是：**Revenue Share 与付费发行并不互斥，可以允许用户在生命周期中切换。**

---

### 7. UnitedMasters

**模式：订阅层 + 邀请制高端合作层。**

当前公开层级包括 DEBUT+、SELECT、PARTNER：

- 低档年度订阅；
- SELECT 提供更高级分析、品牌/Sync 等机会；
- PARTNER 为邀请制，提供 dedicated artist relations、全球营销、品牌/Sync、Advance 等，商务条款可定制。

#### 对星球发行的启发

UnitedMasters 的结构与星球发行未来非常接近：

> **大多数用户使用标准化产品；真正头部客户进入邀请制服务层，而不是单纯“买最贵会员”。**

Plus 应更接近 Partnership Tier，而不是零售会员。

---

### 8. Symphonic

**模式：Starter 订阅 + Partner 申请制分成。**

当前：

- Starter 面向新艺人，按 Primary Artist 收年度费用，发行数量基本不限；
- Partner 面向成熟艺人/厂牌和 Volume-heavy Account，按申请进入，采用定制 Revenue Share；
- Partner 可以获得更深入的 Client Support 和 DSP Marketing。

这是另一个非常典型的“双产品经济模型”：

- 长尾：付固定费，平台不参与/少参与收益；
- 头部：不一定收固定费，而通过分成与客户共同增长。

---

### 9. LANDR

LANDR 当前提供 Distribution Basic / Pro 年度订阅，同时把发行作为更大创作工具套件 LANDR Studio 的组成部分。

LANDR 的参考价值主要在于：发行本身可以成为生态入口，然后通过 Mastering、Plugins、Collaboration 等周边服务提升 ARPU，而不是全部利润都压在发行费本身。

---

## 三、海外产品实际用了哪些“成本控制阀门”

综合上述产品，可以看到实际有以下几类：

### A. 艺人 Profile 数量

非常普遍：

- 1 Artist → 独立音乐人；
- 2-5 Artists → 小团队/小厂牌；
- 更多 Artists → Label / Enterprise。

**这是客户规模指标，不是存储成本指标。**

### B. 年度订阅

用于覆盖持续服务、维护和内容在线成本。

### C. 按 Release 收费

让每次新入库和发行直接产生收入，是最强的边际成本回收方式。

### D. 内容在架/长期托管

DistroKid 的 Leave a Legacy 说明“长期保持作品在线”本身可以产品化收费。

### E. 人工服务与 SLA

低档：知识库/工单；
高档：优先客服；
头部：Dedicated Manager。

### F. Add-on

常见收费内容：

- Cover Licensing；
- Content ID；
- Dolby Atmos；
- Mastering；
- Release Protection；
- Sync / Publishing；
- Promotion；
- 永久在架/长期托管。

---

## 四、对星球发行的直接判断

### 4.1 不建议直接复制“年度订阅 + 无限发行”

星球发行目前核心商业关系仍然是合作发行 / Revenue Share。

如果 Basic 同时满足：

- 不收固定费用；
- 无限艺人；
- 无限曲库；
- 无限新发行；
- 无限 ISRC/UPC；
- 持续存储；
- 人工客服；

那么对低收入 CP 来说，平台存在结构性亏损。

因此星球发行必须增加 **Entitlement / Quota / Add-on**。

---

### 4.2 真正应该控制的是“资源”，不是单独控制代码

建议未来资源维度优先级：

1. **有效/托管音轨数量（Active Catalog Units）**：最接近长期存储与维护成本；
2. **年度新增音轨或发行额度**：最接近新增审核、交付、存储成本；
3. **Primary Artist 数量**：最适合作为音乐人与厂牌规模分层；
4. **源文件/扩展资产存储空间**；
5. **人工服务次数 / 服务 SLA**；
6. ISRC / UPC：作为发行额度的附属权益，而不是主要成本指标。

不建议用“专辑数量”作为唯一资源单位，因为单曲和 30 首专辑的成本差异很大。

---

### 4.3 ISRC / UPC 建议作为“发行额度”的一部分

海外多数主流产品正常发行时会免费分配 ISRC / UPC。

因此更自然的产品表达不是：

> 购买 100 个 ISRC。

而是：

> Basic 每年包含 X 个新发行音轨额度；在发行额度内，所需 ISRC / UPC 自动分配。

如果用户需要：

- 非发行用途批量申请；
- 独立提前申请；
- 超出发行额度；

再作为增购项收费。

这样用户感知更合理，也更接近真实成本。

---

### 4.4 星发应采用“双层商业结构”

建议明确区分：

#### Tier（合作等级）

由看见根据客户价值评定：

- Basic
- Professional
- Plus

客户不能简单通过付款购买 Plus。

#### Add-on / Capacity Pack（资源增购）

客户即使没有达到 Professional / Plus 准入标准，也可以因为业务量较大而购买：

- 曲库扩容包；
- 艺人扩容包；
- 年度发行额度包；
- 文件托管空间；
- 高级服务包；
- 特殊版权/发行服务。

这能够解决“**规模大但收入低**”客户的问题，同时保持合作等级本身的价值。

---

## 五、AI 音乐产品的初步研究结论

AI 音乐不能照搬普通音乐的 Unlimited Subscription。

### 市场正在出现三个明确变化

1. DSP 越来越强调 AI disclosure；
2. 大规模、重复、低质量上传被视为 spam 风险；
3. 不同 DSP / UGC 平台对 AI 内容接受度不同。

Spotify 目前支持 AI Credits / DDEX 方向的 AI contribution disclosure，并持续加强 impersonation 与 spam enforcement。

DistroKid 当前上传流程已经要求用户披露 AI 是否参与 lyrics / music / audio，并支持 AI Persona 信息。

Amuse 当前允许 AI-generated music，但会根据渠道规则排除部分平台，并限制短周期大量 AI Release。

### 对看见 AI 音乐发行的建议

首期优先：

> **Pay-per-release 或“订阅 + 月度有限额度”，不要 Unlimited AI Release。**

原因：

- 每条内容都能覆盖审核和交付成本；
- 抑制内容农场；
- 更容易按不同 DSP 风险定价；
- 未来可以增加 AI 审核、版权风险检查等增值服务。

AI 产品还需要单独维护一个 `Channel Eligibility Matrix`：

- 可正常发行；
- 可发行但不支持 UGC / Content ID；
- 需要 AI disclosure；
- 不接受 AI Generated；
- 仅特定权利证明后接受。

最终渠道矩阵必须以**看见自己的 DSP 合同和实际传输规则**为准，公开网络规则只能作为外部参考。

---

## 六、下一步建议

基于本轮研究，下一步不需要继续扩大竞品数量，应该进入星球发行商业结构设计：

1. 定义 Basic / Professional / Plus 的合作定位；
2. 定义资源计量单位；
3. 定义每个 Tier 的 Entitlement；
4. 定义 Add-on / Capacity Pack；
5. 定义现有用户迁移与 Grandfathering；
6. 再和运营、财务核算出具体额度和价格。

---

## 七、主要公开来源（研究日期：2026-09-09）

- DistroKid Pricing: https://distrokid.com/pricing/
- DistroKid Subscription / Leave a Legacy: https://support.distrokid.com/hc/en-us/articles/360013649233-If-I-Don-t-Renew-My-DistroKid-Subscription-Will-My-Music-Stay-Live-in-Streaming-Services
- DistroKid AI Credits: https://support.distrokid.com/hc/en-us/articles/50784709021971-How-to-Fill-Out-AI-Credits
- Ditto Pricing: https://dittomusic.com/en/pricing
- TuneCore Pricing: https://www.tunecore.com/pricing
- Amuse Pricing: https://www.amuse.io/en/pricing/
- Amuse AI content policy: https://support.amuse.io/en/articles/131081-content-not-approved-on-amuse
- CD Baby Pricing: https://support.cdbaby.com/hc/en-us/articles/213125406-How-much-does-CD-Baby-cost
- RouteNote Pricing: https://support.routenote.com/kb-article/how-much-does-routenote-cost/
- UnitedMasters Pricing: https://comms.unitedmasters.com/en/pricing
- Symphonic Pricing: https://symphonic.com/pricing/
- LANDR Distribution Pricing: https://support.landr.com/hc/en-us/articles/31618416509975-How-much-does-it-cost-to-distribute-music-with-LANDR
- Spotify AI policy direction: https://newsroom.spotify.com/2025-09-25/spotify-strengthens-ai-protections/
