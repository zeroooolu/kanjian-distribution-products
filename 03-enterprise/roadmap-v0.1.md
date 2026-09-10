# 星球发行·企业版 Roadmap v0.1

> 日期：2026-09-10  
> 上游基线：`business-baseline-v0.1.md`  
> 目标：从官网概念 Demo 推进到可销售、可演示、可进入研发评估的企业版产品方案。

---

# 1. 当前判断

现有官网已经可以回答：

> 星球发行·企业版是什么？

但还不能完整回答企业采购时最关键的问题：

1. 企业客户拿到产品后如何管理下游 CP？
2. 一条发行任务如何从 CP 经过租户、看见到 DSP？
3. 企业如何查看审核、交付、异常和上线状态？
4. DSP 报表、待结算和可提现金额如何区分？
5. API 到底开放哪些真实能力，如何接入和调试？
6. 企业版到底怎么收费？

因此下一阶段的核心不再是首页视觉，而是构建 **Enterprise Product Demo**。

---

# 2. P0：先收口产品定义

## PR / Deliverable E00 — Product Baseline v0.2

基于真实业务基线修订此前产品定义：

### 必须修正

- White-label 对外统一改为“品牌发行平台”；
- 默认发行链路改为：

```text
CP → 租户 → 自动传输看见 → 看见审核 → DSP
```

- Own DSP Deal / Hybrid 从 P0 主能力降级为后续可选扩展；
- DDEX / XML / Excel / SFTP / API 定义为企业级接入方式，而不是第三套系统；
- 收益模型明确区分 Reported / Pending / Available / Withdrawal / Paid；
- 合同主体明确为“看见 ↔ 企业租户”；
- 下游 CP 由租户经营，不需要与看见重复签约。

### 产出

`product-definition-and-architecture-v0.2.md`

---

# 3. P1：企业管理后台 Demo

## E01 — Enterprise Console

构建真正的企业管理员视角。

建议导航：

```text
总览
客户
内容
发行
渠道
数据
收益
API
设置
```

### 总览

展示：

- 曲库规模；
- 本月发行；
- 待看见审核；
- 交付中；
- 已上线；
- 异常；
- 报表收益；
- 可提现金额。

### 客户

```text
客户 / CP 列表
├── 企业 / 厂牌名称
├── 联系人
├── 内容规模
├── 本月发行量
├── 状态
└── 账号
```

支持查看一个 CP 的：

- 用户；
- 艺人；
- 专辑；
- 歌曲；
- 发行记录；
- 收益。

### 发行

按真实状态设计：

```text
草稿
已提交租户
已传输看见
看见审核中
审核退回
待交付
交付中
部分成功
已上线
异常
更新中
下架中
已下架
```

重点展示“看见审核状态”和“DSP 交付状态”是两层状态。

### 渠道

第一版从 DSP Metadata 中抽取真实能力矩阵：

```text
平台
可发行地区
内容类型
挑选规则
交付周期
报表周期
结算周期
当前状态
```

P0 Demo 只展示“启用且允许对外展示”的渠道。

### 设置

- 企业信息；
- 品牌名称；
- Logo；
- 品牌色；
- 独立域名；
- 成员与权限；
- 下游客户入口；
- API 凭证。

---

# 4. P2：下游 CP 发行门户 Demo

## E02 — Branded Client Portal

这是企业版最容易被忽略，但最能解释产品价值的一块。

Demo 使用虚拟企业品牌，例如 `NOVA MUSIC`。

### 下游 CP 看到：

```text
首页
艺人
专辑
歌曲
发行
数据
收益
```

### 核心 Demo 场景

```text
CP 登录 NOVA MUSIC
        ↓
创建专辑 / 歌曲
        ↓
填写 Metadata
        ↓
上传音频 / 封面
        ↓
选择 DSP / 地区 / 上线时间
        ↓
提交发行
        ↓
进入 NOVA 租户
        ↓
自动传输到看见
```

提交后状态应明确展示：

> 已提交，等待发行审核

而不是让 CP 感知看见音乐作为另一个品牌。

---

# 5. P3：看见侧运营视角 Demo

## E03 — KANJIAN Operator View

企业版销售 Demo 中不一定对客户完整开放，但内部必须有这一层，才能解释供应链。

核心场景：

```text
企业租户传输任务
      ↓
看见待审核队列
      ↓
审核通过 / 驳回
      ↓
生成 DSP 交付任务
      ↓
跟踪结果
```

重点展示：

- Tenant；
- CP；
- Release；
- 来源方式；
- 审核；
- DSP 交付状态；
- 异常原因；
- 重传 / 更新 / 下架。

该 Demo 可以直接复用星球发行现有内部能力的真实结构。

---

# 6. P4：API Developer Product

## E04 — Developer Center

菜单中的 API 不再只链接首页一张卡，而是进入独立开发者页面。

建议信息架构：

```text
API 概览
快速开始
鉴权
内容接口
发行接口
DSP / 基础数据
文件上传
ISRC / UPC
状态查询
Webhook
错误码
使用记录
```

### 原则

不重新发明一套 API Resource Model。

首先完成：

```text
现有后台 API
      ↓ Endpoint Mapping
Enterprise External API
      ↓
企业开发者文档
```

### Developer Experience P0

- API Key；
- 测试环境 / Sandbox；
- Bearer Token 或现有鉴权方案标准化；
- Request / Response 示例；
- Error Code；
- API Log；
- Webhook；
- Webhook 重试 / 日志；
- 使用量 / Quota。

### 竞品基准

LabelGrid 当前 API 产品已经公开提供：

- Public Docs；
- API Token；
- IP Whitelist；
- Sandbox；
- Webhook；
- Delivery Logs；
- 明确 API Pricing。

因此星球发行 API Demo 至少要达到“可被技术负责人评估”的程度，而不是营销说明页。

---

# 7. P5：收益与结算 Demo

## E05 — Revenue & Withdrawal

按照真实业务规则设计。

### 企业 / CP 收益页至少展示

```text
累计报表收益
待结算
可提现
提现处理中
已提现
```

### 一条 DSP 收益的生命周期

```text
DSP 报表导入
      ↓
形成报表收益
      ↓
看见分账至租户 / CP
      ↓
等待 DSP 实际结算到账
      ↓
转为可提现
      ↓
提现申请
      ↓
看见打款
```

必须避免把“报表收入”和“现金余额”混成一个金额。

### API 对应状态

后续 API 至少需要能够表达：

- reported；
- pending_settlement；
- available；
- withdrawal_processing；
- paid。

---

# 8. P6：定价页正式化

## E06 — Pricing

目前已有两种历史商业模式：

### 按量合作

```text
约 ¥0.5 / 首 / 渠道 / 次
```

### 年度合作

```text
约 ¥25,000 / 年
```

正式企业版应保留“按量”和“年度”两种购买逻辑，但把计费对象定义清楚：

- 传输次数；
- 曲库规模；
- 下游账号 / CP 数量；
- API / 品牌平台；
- 高级接入方式；
- 服务与 SLA。

详见 `commercial-model-v0.1.md`。

---

# 9. P7：官网 v2

只有在 E01–E06 的产品内容已经成形后，再重构官网。

官网菜单保持：

```text
产品
定价
API
```

官网重点不再堆能力词，而是直接展示真实产品：

### 首页

- 企业发行平台 Hero；
- 企业 Console 截图；
- CP Portal 截图；
- 真实发行链路；
- DSP 网络；
- 收益闭环；
- API；
- Pricing；
- CTA。

### 产品

独立页面：

- 品牌发行平台；
- 企业后台；
- CP 门户；
- 发行流程；
- 渠道；
- 数据与收益。

### API

Developer Product 页面。

### 定价

正式商业模型。

---

# 10. 推荐执行顺序

```text
E00 产品定义 v0.2
        ↓
E01 企业管理后台 Demo
        ↓
E02 CP 品牌发行门户 Demo
        ↓
E03 看见运营 / 审核链路 Demo
        ↓
E04 API Developer Center
        ↓
E05 收益与提现 Demo
        ↓
E06 商业模式 / 定价
        ↓
E07 官网 v2
```

不建议继续先打磨官网视觉。

原因是：

> E01–E06 做完后，官网中每一屏都会有真实产品可以展示，销售表达会自然成立。

---

# 11. P0 完成标准

企业版第一轮产品设计完成时，应该可以用一个完整 Demo 回答：

```text
一家企业如何开通企业版？
↓
如何配置自己的发行品牌？
↓
如何创建下游 CP 账号？
↓
CP 如何提交一张专辑？
↓
内容如何自动传到看见？
↓
看见如何审核？
↓
如何发送到 DSP？
↓
如何查看上线 / 异常？
↓
DSP 报表回来后如何分账？
↓
什么时候变成可提现？
↓
API 客户如何完成同一条链路？
↓
最终怎么收费？
```

只要这条链路能够完整演示，星球发行·企业版就从“概念官网”进入了真正可以销售和研发评估的产品阶段。
