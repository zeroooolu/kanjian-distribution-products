# 星球发行·企业版官网原型 v1.1

> 日期：2026-09-10  
> 状态：官网初稿 / 可视化产品讨论稿

## 目的

基于：

- `03-enterprise/product-definition-and-architecture-v0.1.md`
- `06-research/enterprise-white-label-api-competitor-research-2026.md`
- 企业版方向草稿
- 星球发行与 AI 音乐发行现有品牌视觉

建立企业版官网原型，用于继续讨论产品定位、接入方式、功能架构、商业模式与对外表达。

## v1.1 调整

- 全局移除面向访问者的人称表达；
- 对照 AudioSalad、FUGA、LabelGrid、SonoSuite、Revelator 简化产品文案；
- Hero 改为结果型表达：`让企业拥有专属音乐发行平台`；
- White-label 与 Distribution API 作为两个主要标准接入入口；
- Enterprise Infrastructure 改为横向深度方案，降低与标准产品入口的视觉竞争；
- Distribution Engine 改为横向生命周期 Pipeline；
- Core Capabilities 改为更克制的基础设施能力矩阵；
- White-label 控制区改为 `品牌独立 / 业务独立运营`；
- 减少冗余英文辅助标签、重复解释、重阴影和卡片堆叠。

## 当前页面结构

1. Hero：让企业拥有专属音乐发行平台
2. 接入方式
   - White-label
   - Distribution API
   - Enterprise Infrastructure
3. 发行引擎：完整发行生命周期
4. 核心能力：企业发行基础能力
5. White-label Control：品牌与业务配置
6. 发行网络：中国与全球 DSP
7. 适用业务
8. Enterprise CTA

## 视觉原则

- 延续星球发行产品家族蓝色主色；
- 复用 `/assets/star-logo.png`；
- 复用 `music-promotion` 仓库中的 DSP 彩色 Logo；
- B2B / Infrastructure 气质高于普通音乐人产品；
- 以产品控制台、API、发行 Pipeline 与品牌配置界面作为主要视觉；
- 信息层级优先于装饰，减少无意义卡片化与营销性视觉；
- 当前为纯 HTML + CSS 原型，便于快速迭代。

## Preview

Vercel 路由：`/enterprise`

## 当前未定

- 最终产品命名；
- 正式商务联系方式；
- Pricing 是否公开；
- 白标可配置项最终范围；
- API v1 最终资源模型；
- Own DSP Deal / Platform Deal 的商业和技术边界；
- Revenue / Royalty / Settlement 一期开放深度。
