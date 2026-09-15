from pathlib import Path
import re

index_path = Path('03-enterprise/prototype-v4/index.html')
styles_path = Path('03-enterprise/prototype-v4/styles.css')
html = index_path.read_text()
css = styles_path.read_text()

hero = '''<section class="page" data-page="solutions">
  <section class="subhero solutions-hero solutions-hero-v2"><div class="container"><div class="solutions-hero-layout">
    <div class="solutions-hero-copy reveal"><span class="eyebrow">SOLUTIONS</span><h1>面向不同业务模式的<br>企业发行解决方案</h1><p>企业可选择自有品牌发行平台，或通过发行 API 接入现有产品与系统。根据客户协作方式、曲库规模和系统集成需求组合发行能力。</p></div>
    <div class="solutions-mode-map reveal" aria-label="企业发行产品形态"><div class="solution-mode-card"><span class="mode-no">01</span><small>BRANDED PLATFORM</small><b>自有品牌发行平台</b><p>适合直接服务音乐人、厂牌和版权客户。</p></div><div class="solution-mode-card api"><span class="mode-no">02</span><small>DISTRIBUTION API</small><b>发行 API</b><p>适合接入现有网站、App 或内部系统。</p></div><div class="solution-mode-core"><span>星球发行企业能力</span><i>→</i><b>国内外音乐平台</b></div></div>
  </div></div></section>
  <nav class="solutions-subnav" aria-label="解决方案页章节"><div class="container"><a href="#solution-selector">方案选择</a><a href="#solution-fit">适配判断</a><a href="#solution-implementation">实施上线</a></div></nav>'''

html, n = re.subn(r'<section class="page" data-page="solutions">\s*<section class="subhero solutions-hero">.*?</section>', hero, html, count=1, flags=re.S)
assert n == 1, f'hero replacement count={n}'

selector = '''
  <section class="section solutions-selector-section" id="solution-selector"><div class="container">
    <div class="section-head reveal"><span class="eyebrow">CHOOSE YOUR BUSINESS</span><h2>从业务模式出发，确定发行方案</h2><p>不同企业的差异主要在客户协作方式、现有产品形态和系统集成深度。选择业务类型后，可直接查看推荐产品组合与系统连接方式。</p></div>
    <div class="solution-role-tabs reveal" role="tablist" aria-label="企业类型"><button class="active" type="button" role="tab" aria-selected="true" data-solution-role="distributor"><b>01</b><span>发行商</span></button><button type="button" role="tab" aria-selected="false" data-solution-role="label"><b>02</b><span>唱片 / 版权</span></button><button type="button" role="tab" aria-selected="false" data-solution-role="ai"><b>03</b><span>AI 音乐平台</span></button><button type="button" role="tab" aria-selected="false" data-solution-role="system"><b>04</b><span>音乐科技 / 内容平台</span></button></div>
    <div class="solution-role-stage reveal" data-solution-stage>
      <article class="solution-role-panel active" data-solution-panel="distributor"><div class="solution-role-copy"><span class="solution-role-kicker">发行商</span><h3>建立自有品牌发行服务</h3><p>面向多个厂牌、版权方和音乐人提供发行服务，客户可提交内容、查看发行状态、数据和收入，发行运营统一管理。</p><div class="solution-recommend"><small>推荐组合</small><div><span>自有品牌发行平台</span><span class="secondary">发行 API 可选</span></div></div><div class="solution-capabilities"><span>客户门户</span><span>多客户运营</span><span>曲库管理</span><span>审核发行</span><span>数据与收入</span></div><a class="text-link" href="/enterprise/product" data-route>查看产品能力 →</a></div><div class="solution-architecture"><div class="solution-flow-label">BUSINESS FLOW</div><div class="solution-flow"><div class="flow-node source"><small>CLIENTS</small><b>音乐人 · 厂牌 · 版权方</b></div><i>→</i><div class="flow-node primary"><small>YOUR BRAND</small><b>自有品牌发行门户</b><span>提交 · 状态 · 数据 · 收入</span></div><i>→</i><div class="flow-node core"><small>OPERATIONS</small><b>企业发行运营</b><span>审核 · 曲库 · 发行 · 结算</span></div><i>→</i><div class="flow-node output"><small>DSP NETWORK</small><b>国内外音乐平台</b></div></div></div></article>
      <article class="solution-role-panel" data-solution-panel="label" hidden><div class="solution-role-copy"><span class="solution-role-kicker">唱片公司 / 版权公司</span><h3>统一管理曲库与发行运营</h3><p>集中管理艺人、专辑、歌曲和发行数据，支持历史曲库迁移、批量发行、平台状态跟踪和收入结算。</p><div class="solution-recommend"><small>推荐组合</small><div><span>自有品牌发行平台</span><span class="secondary">系统集成可选</span></div></div><div class="solution-capabilities"><span>曲库管理</span><span>批量导入</span><span>审核发行</span><span>平台状态</span><span>数据与结算</span></div><a class="text-link" href="/enterprise/product#product-catalog" data-route>查看曲库与发行能力 →</a></div><div class="solution-architecture"><div class="solution-flow-label">BUSINESS FLOW</div><div class="solution-flow"><div class="flow-node source"><small>CATALOG</small><b>曲库 · DAM · 历史数据</b></div><i>→</i><div class="flow-node core"><small>ENTERPRISE</small><b>曲库与发行运营</b><span>导入 · 审核 · 发行</span></div><i>→</i><div class="flow-node output"><small>DISTRIBUTION</small><b>国内外音乐平台</b></div><i>→</i><div class="flow-node source"><small>FINANCE</small><b>数据 · 收入 · 结算</b></div></div></div></article>
      <article class="solution-role-panel" data-solution-panel="ai" hidden><div class="solution-role-copy"><span class="solution-role-kicker">AI 音乐 / 创作平台</span><h3>把发行能力接入现有创作产品</h3><p>保留原有账号与创作体验，通过发行 API 提交作品、配置目标平台，并持续接收审核、发行和上线状态。</p><div class="solution-recommend"><small>推荐组合</small><div><span>发行 API</span><span class="secondary">企业发行能力</span></div></div><div class="solution-capabilities"><span>内容接口</span><span>发行接口</span><span>状态回传</span><span>全球发行</span><span>数据与收入</span></div><a class="text-link" href="/enterprise/api" data-route>了解发行 API →</a></div><div class="solution-architecture"><div class="solution-flow-label">API FLOW</div><div class="solution-flow"><div class="flow-node source"><small>PRODUCT</small><b>AI Music App / SaaS</b></div><i>API</i><div class="flow-node primary"><small>DISTRIBUTION API</small><b>标准发行接口</b><span>内容 · 发行 · 状态 · 报表</span></div><i>→</i><div class="flow-node core"><small>OPERATIONS</small><b>审核与渠道交付</b></div><i>→</i><div class="flow-node output"><small>DSP NETWORK</small><b>国内外音乐平台</b></div></div></div></article>
      <article class="solution-role-panel" data-solution-panel="system" hidden><div class="solution-role-copy"><span class="solution-role-kicker">音乐科技 / 内容平台</span><h3>把发行能力接入现有业务系统</h3><p>通过 API、SFTP、XML 或 DDEX 连接现有内容与业务流程，按业务规模组合发行、数据和系统集成能力。</p><div class="solution-recommend"><small>推荐组合</small><div><span>发行 API</span><span class="secondary">企业级系统集成</span></div></div><div class="solution-capabilities"><span>发行 API</span><span>SFTP / XML</span><span>DDEX</span><span>平台状态</span><span>数据报表</span></div><a class="text-link" href="/enterprise/api" data-route>查看系统接入方式 →</a></div><div class="solution-architecture"><div class="solution-flow-label">SYSTEM FLOW</div><div class="solution-flow"><div class="flow-node source"><small>INTERNAL SYSTEM</small><b>CRM · CMS · DAM · ERP</b></div><i>↔</i><div class="flow-node primary"><small>INTEGRATION</small><b>API · SFTP · XML · DDEX</b></div><i>↔</i><div class="flow-node core"><small>ENTERPRISE</small><b>发行基础设施</b><span>统一业务对象与状态</span></div><i>→</i><div class="flow-node output"><small>CHANNELS</small><b>发行渠道与数据</b></div></div></div></article>
    </div>
  </div></section>
'''

pattern = r'\n  <section class="section"><div class="container"><div class="section-head reveal"><span class="eyebrow">SOLUTION SCENARIOS</span>.*?(?=\n  <section class="section"><div class="container"><div class="section-head reveal"><span class="eyebrow">SOLUTION FIT</span>)'
html, n = re.subn(pattern, selector, html, count=1, flags=re.S)
assert n == 1, f'selector replacement count={n}'

fit = '''
  <section class="section solutions-fit-section" id="solution-fit"><div class="container"><div class="section-head split reveal"><div><span class="eyebrow">SOLUTION FIT</span><h2>从关键业务条件判断合适的方案</h2></div><p>客户协作方式、现有产品、业务规模和系统集成要求，决定产品形态与版本组合。</p></div><div class="solution-fit-matrix reveal"><div class="fit-matrix-head"><span>业务条件</span><span>典型需求</span><span>推荐方式</span></div><div class="fit-matrix-row"><b>客户协作</b><span>客户需要直接提交内容、查询发行状态和数据</span><strong>自有品牌发行平台</strong></div><div class="fit-matrix-row"><b>现有产品</b><span>已有网站、App 或 SaaS，希望保留原有体验</span><strong>发行 API</strong></div><div class="fit-matrix-row"><b>业务规模</b><span>多客户、大曲库、批量发行与分账结算</span><strong>专业版 / 企业版</strong></div><div class="fit-matrix-row"><b>系统集成</b><span>需要 API、SFTP、XML、DDEX 等标准化对接</span><strong>企业级集成</strong></div></div><div class="fit-matrix-action reveal"><span>版本差异主要体现在容量、分账、集成深度与服务等级。</span><a class="text-link" href="/enterprise/pricing" data-route>查看版本与价格 →</a></div></div></section>
'''
pattern = r'\n  <section class="section"><div class="container"><div class="section-head reveal"><span class="eyebrow">SOLUTION FIT</span>.*?(?=\n  <section class="section soft"><div class="container"><div class="section-head split reveal"><div><span class="eyebrow">IMPLEMENTATION & LAUNCH</span>)'
html, n = re.subn(pattern, fit, html, count=1, flags=re.S)
assert n == 1, f'fit replacement count={n}'

implementation = '''
  <section class="section soft solutions-implementation" id="solution-implementation"><div class="container"><div class="section-head split reveal"><div><span class="eyebrow">IMPLEMENTATION & LAUNCH</span><h2>标准化实施流程，支持平稳上线</h2></div><p>根据业务规模、曲库结构和系统集成需求，确定实施范围、接入方式与上线计划。</p></div><div class="solutions-timeline reveal"><article><b>01</b><h3>业务评估</h3><p>确认曲库规模、客户体系、发行量与目标平台。</p></article><article><b>02</b><h3>方案设计</h3><p>确定产品版本、系统边界与接入方式。</p></article><article><b>03</b><h3>数据准备</h3><p>准备曲库、账号、元数据和接口数据。</p></article><article><b>04</b><h3>联调验证</h3><p>验证账号权限、发行渠道与真实发行链路。</p></article><article><b>05</b><h3>正式上线</h3><p>进入持续发行运营与企业服务。</p></article></div></div></section>
'''
pattern = r'\n  <section class="section soft"><div class="container"><div class="section-head split reveal"><div><span class="eyebrow">IMPLEMENTATION & LAUNCH</span>.*?(?=\n\n  <section class="enterprise-contact-cta">)'
html, n = re.subn(pattern, implementation, html, count=1, flags=re.S)
assert n == 1, f'implementation replacement count={n}'

html = html.replace("document.querySelectorAll('.product-subnav,.api-subnav')", "document.querySelectorAll('.product-subnav,.api-subnav,.solutions-subnav')")
needle = "const arch=e.target.closest('[data-arch-tab]');"
insert = "const solutionRole=e.target.closest('[data-solution-role]');if(solutionRole){const stage=document.querySelector('[data-solution-stage]'),key=solutionRole.dataset.solutionRole;document.querySelectorAll('[data-solution-role]').forEach(btn=>{const active=btn===solutionRole;btn.classList.toggle('active',active);btn.setAttribute('aria-selected',String(active))});stage?.querySelectorAll('[data-solution-panel]').forEach(panel=>{const active=panel.dataset.solutionPanel===key;panel.classList.toggle('active',active);panel.hidden=!active});return}"
assert needle in html
html = html.replace(needle, insert + needle, 1)

marker = '/* Enterprise Solutions v2: decision-led page */'
assert marker not in css
css += r'''

/* Enterprise Solutions v2: decision-led page */
[data-page="solutions"]{--sol-blue:#315ff4;--sol-blue2:#2149d8;--sol-ink:#172238;--sol-muted:#6f7b8e;--sol-line:#dfe5ef;--sol-soft:#f6f8fc}
[data-page="solutions"] .solutions-hero-v2{padding:88px 0 78px;background:radial-gradient(circle at 86% 18%,rgba(49,95,244,.11),transparent 29%),linear-gradient(180deg,#fff 0%,#f7f9ff 100%)}
[data-page="solutions"] .solutions-hero-v2:after{display:none}
[data-page="solutions"] .solutions-hero-layout{display:grid;grid-template-columns:minmax(0,.88fr) minmax(470px,1.12fr);gap:64px;align-items:center}
[data-page="solutions"] .solutions-hero-copy h1{max-width:720px;margin:10px 0 22px;font-size:58px;line-height:1.06;letter-spacing:-.05em}
[data-page="solutions"] .solutions-hero-copy p{max-width:660px;margin:0;color:#687487;font-size:16px;line-height:1.78}
[data-page="solutions"] .solutions-mode-map{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:16px;border:1px solid #dce4f1;border-radius:24px;background:rgba(255,255,255,.86);box-shadow:0 22px 58px rgba(27,45,87,.08)}
[data-page="solutions"] .solution-mode-card{position:relative;min-height:185px;padding:25px 23px;border:1px solid #e2e7f0;border-radius:17px;background:linear-gradient(180deg,#fff,#fbfcff)}
[data-page="solutions"] .solution-mode-card.api{background:linear-gradient(180deg,#f6f8ff,#fff)}
[data-page="solutions"] .mode-no{display:grid;place-items:center;width:30px;height:30px;margin-bottom:25px;border-radius:9px;background:#eaf0ff;color:var(--sol-blue);font-size:9px;font-weight:900}
[data-page="solutions"] .solution-mode-card small{display:block;color:#8795aa;font-size:9px;font-weight:850;letter-spacing:.08em}
[data-page="solutions"] .solution-mode-card b{display:block;margin:8px 0 8px;color:#1c2941;font-size:18px}
[data-page="solutions"] .solution-mode-card p{margin:0;color:#7b8798;font-size:11px;line-height:1.62}
[data-page="solutions"] .solution-mode-core{grid-column:1/-1;display:flex;align-items:center;justify-content:center;gap:14px;padding:13px 16px;border-radius:13px;background:#17233a;color:#fff;font-size:11px}
[data-page="solutions"] .solution-mode-core span{color:#b9c6dd;font-weight:700}[data-page="solutions"] .solution-mode-core i{color:#6f8cff;font-style:normal}[data-page="solutions"] .solution-mode-core b{font-size:11px}
[data-page="solutions"] .solutions-subnav{position:sticky;top:72px;z-index:42;border-bottom:1px solid #e6eaf1;background:rgba(255,255,255,.94);backdrop-filter:blur(16px)}
[data-page="solutions"] .solutions-subnav .container{display:flex;gap:30px;overflow:auto;scrollbar-width:none}
[data-page="solutions"] .solutions-subnav a{flex:none;padding:15px 0;border-bottom:2px solid transparent;color:#7a8698;font-size:12px;font-weight:760;white-space:nowrap}
[data-page="solutions"] .solutions-subnav a.active{color:var(--sol-blue2);border-bottom-color:var(--sol-blue)}
[data-page="solutions"] .section[id]{scroll-margin-top:126px}
[data-page="solutions"] .solutions-selector-section{padding-top:94px;padding-bottom:104px}
[data-page="solutions"] .solutions-selector-section .section-head{max-width:850px;margin-bottom:34px}
[data-page="solutions"] .solution-role-tabs{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border-top:1px solid var(--sol-line);border-bottom:1px solid var(--sol-line)}
[data-page="solutions"] .solution-role-tabs button{display:flex;align-items:center;gap:12px;min-height:66px;padding:0 18px;border:0;border-right:1px solid var(--sol-line);background:transparent;color:#798598;text-align:left;cursor:pointer}
[data-page="solutions"] .solution-role-tabs button:last-child{border-right:0}
[data-page="solutions"] .solution-role-tabs button b{color:#a1adbf;font-size:9px;letter-spacing:.08em}
[data-page="solutions"] .solution-role-tabs button span{font-size:12px;font-weight:800}
[data-page="solutions"] .solution-role-tabs button:hover{background:#fafbfe;color:#40506a}
[data-page="solutions"] .solution-role-tabs button.active{background:#f3f6ff;color:#2449c9;box-shadow:inset 0 -2px 0 var(--sol-blue)}
[data-page="solutions"] .solution-role-tabs button.active b{color:#6682e6}
[data-page="solutions"] .solution-role-stage{margin-top:28px}
[data-page="solutions"] .solution-role-panel{display:grid;grid-template-columns:minmax(300px,.72fr) minmax(0,1.28fr);gap:42px;align-items:stretch}
[data-page="solutions"] .solution-role-panel[hidden]{display:none}
[data-page="solutions"] .solution-role-copy{padding:28px 4px 20px 0}
[data-page="solutions"] .solution-role-kicker{display:block;margin-bottom:13px;color:#6179c5;font-size:10px;font-weight:850;letter-spacing:.06em}
[data-page="solutions"] .solution-role-copy h3{max-width:470px;margin:0 0 15px;color:var(--sol-ink);font-size:32px;line-height:1.18;letter-spacing:-.035em}
[data-page="solutions"] .solution-role-copy>p{max-width:520px;margin:0;color:var(--sol-muted);font-size:13px;line-height:1.75}
[data-page="solutions"] .solution-recommend{margin-top:28px;padding-top:19px;border-top:1px solid var(--sol-line)}
[data-page="solutions"] .solution-recommend small{display:block;margin-bottom:10px;color:#929dac;font-size:9px;font-weight:850;letter-spacing:.08em}
[data-page="solutions"] .solution-recommend>div{display:flex;flex-wrap:wrap;gap:8px}
[data-page="solutions"] .solution-recommend span{display:inline-flex;padding:8px 10px;border-radius:9px;background:#315ff4;color:#fff;font-size:10px;font-weight:800}
[data-page="solutions"] .solution-recommend span.secondary{border:1px solid #d9e2f5;background:#fff;color:#53657f}
[data-page="solutions"] .solution-capabilities{display:flex;flex-wrap:wrap;gap:7px;margin:17px 0 20px}
[data-page="solutions"] .solution-capabilities span{padding:6px 8px;border:1px solid #e1e6ee;border-radius:8px;background:#fff;color:#6c788a;font-size:9px;font-weight:700}
[data-page="solutions"] .solution-role-copy .text-link{font-size:11px}
[data-page="solutions"] .solution-architecture{position:relative;overflow:hidden;min-height:390px;padding:25px;border:1px solid #dbe3ef;border-radius:22px;background:linear-gradient(rgba(238,242,248,.8) 1px,transparent 1px),linear-gradient(90deg,rgba(238,242,248,.8) 1px,transparent 1px),linear-gradient(180deg,#fbfcff,#f6f8fc);background-size:34px 34px;box-shadow:0 22px 58px rgba(28,45,84,.07)}
[data-page="solutions"] .solution-flow-label{margin-bottom:48px;color:#98a4b6;font-size:9px;font-weight:850;letter-spacing:.12em}
[data-page="solutions"] .solution-flow{display:flex;align-items:center;justify-content:center;gap:10px;min-height:210px}
[data-page="solutions"] .flow-node{display:flex;flex:1;min-width:0;min-height:128px;flex-direction:column;justify-content:center;padding:18px 16px;border:1px solid #dce3ed;border-radius:14px;background:rgba(255,255,255,.94);box-shadow:0 8px 24px rgba(28,45,84,.04)}
[data-page="solutions"] .flow-node small{color:#8b98aa;font-size:8px;font-weight:900;letter-spacing:.08em}
[data-page="solutions"] .flow-node b{margin-top:9px;color:#26344d;font-size:11px;line-height:1.42}
[data-page="solutions"] .flow-node span{margin-top:7px;color:#8a95a5;font-size:8px;line-height:1.45}
[data-page="solutions"] .flow-node.primary{border-color:#9eb3ff;background:#f4f7ff}.flow-node.primary b{color:#294dcc}
[data-page="solutions"] .flow-node.core{border-color:#c9d6f2;background:#fff;box-shadow:inset 0 3px 0 #315ff4,0 10px 26px rgba(49,95,244,.07)}
[data-page="solutions"] .solution-flow>i{flex:none;color:#6d85d8;font-style:normal;font-size:11px;font-weight:850}
[data-page="solutions"] .solutions-fit-section{padding-top:92px;padding-bottom:96px;background:#f8faff}
[data-page="solutions"] .solutions-fit-section .section-head{max-width:none;margin-bottom:30px}
[data-page="solutions"] .solution-fit-matrix{border-top:1px solid #dce3ed;border-bottom:1px solid #dce3ed;background:#fff}
[data-page="solutions"] .fit-matrix-head,[data-page="solutions"] .fit-matrix-row{display:grid;grid-template-columns:.5fr 1.45fr .75fr;gap:28px;align-items:center;padding:0 22px}
[data-page="solutions"] .fit-matrix-head{min-height:46px;background:#f6f8fc;color:#98a3b3;font-size:9px;font-weight:850;letter-spacing:.07em}
[data-page="solutions"] .fit-matrix-row{min-height:76px;border-top:1px solid #e7ebf1}
[data-page="solutions"] .fit-matrix-row b{color:#35425a;font-size:12px}.fit-matrix-row span{color:#778396;font-size:11px;line-height:1.55}.fit-matrix-row strong{color:#3157d5;font-size:11px}
[data-page="solutions"] .fit-matrix-action{display:flex;align-items:center;justify-content:space-between;gap:24px;margin-top:20px;color:#8490a1;font-size:11px}
[data-page="solutions"] .solutions-implementation{padding-top:88px;padding-bottom:92px}
[data-page="solutions"] .solutions-implementation .section-head{max-width:none;margin-bottom:42px}
[data-page="solutions"] .solutions-timeline{position:relative;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:0;border-top:1px solid #d6deea}
[data-page="solutions"] .solutions-timeline article{position:relative;padding:28px 28px 0 0;background:transparent;border:0;box-shadow:none}
[data-page="solutions"] .solutions-timeline article:before{content:"";position:absolute;top:-5px;left:0;width:9px;height:9px;border-radius:50%;background:#315ff4;box-shadow:0 0 0 4px #e8eeff}
[data-page="solutions"] .solutions-timeline b{color:#7b91df;font-size:9px;letter-spacing:.08em}
[data-page="solutions"] .solutions-timeline h3{margin:15px 0 8px;color:#26344c;font-size:15px}
[data-page="solutions"] .solutions-timeline p{max-width:185px;margin:0;color:#7d899a;font-size:10px;line-height:1.62}
@media(max-width:1050px){[data-page="solutions"] .solutions-hero-layout{grid-template-columns:1fr;gap:38px}[data-page="solutions"] .solutions-mode-map{max-width:820px}[data-page="solutions"] .solution-role-panel{grid-template-columns:1fr;gap:28px}[data-page="solutions"] .solution-role-copy{max-width:760px;padding-bottom:0}}
@media(max-width:820px){[data-page="solutions"] .solutions-hero-v2{padding:70px 0 64px}[data-page="solutions"] .solutions-hero-copy h1{font-size:48px}[data-page="solutions"] .solutions-subnav{top:64px}[data-page="solutions"] .section[id]{scroll-margin-top:116px}[data-page="solutions"] .solution-role-tabs{grid-template-columns:repeat(2,1fr)}[data-page="solutions"] .solution-role-tabs button:nth-child(2){border-right:0}[data-page="solutions"] .solution-role-tabs button:nth-child(-n+2){border-bottom:1px solid var(--sol-line)}[data-page="solutions"] .solution-flow{align-items:stretch;flex-direction:column;gap:8px}[data-page="solutions"] .solution-flow>i{align-self:center;transform:rotate(90deg)}[data-page="solutions"] .flow-node{flex:none;width:100%;min-height:90px}[data-page="solutions"] .solution-flow-label{margin-bottom:20px}[data-page="solutions"] .solution-architecture{min-height:0}[data-page="solutions"] .solutions-timeline{grid-template-columns:repeat(3,1fr);row-gap:34px;border-top:0}[data-page="solutions"] .solutions-timeline article{padding-top:20px;border-top:1px solid #d6deea}[data-page="solutions"] .solutions-timeline article:before{top:-5px}}
@media(max-width:620px){[data-page="solutions"] .solutions-hero-v2{padding-top:56px}[data-page="solutions"] .solutions-hero-copy h1{font-size:40px;line-height:1.1}[data-page="solutions"] .solutions-hero-copy p{font-size:14px}[data-page="solutions"] .solutions-mode-map{grid-template-columns:1fr;padding:11px;border-radius:19px}[data-page="solutions"] .solution-mode-card{min-height:0;padding:21px}[data-page="solutions"] .solution-mode-core{grid-column:1}[data-page="solutions"] .solutions-selector-section{padding-top:72px;padding-bottom:78px}[data-page="solutions"] .solution-role-tabs{grid-template-columns:1fr}[data-page="solutions"] .solution-role-tabs button{border-right:0;border-bottom:1px solid var(--sol-line)!important}[data-page="solutions"] .solution-role-tabs button:last-child{border-bottom:0!important}[data-page="solutions"] .solution-role-copy h3{font-size:28px}[data-page="solutions"] .solution-architecture{padding:18px;border-radius:18px}[data-page="solutions"] .fit-matrix-head{display:none}[data-page="solutions"] .fit-matrix-row{grid-template-columns:1fr;gap:6px;min-height:0;padding:18px 17px}[data-page="solutions"] .fit-matrix-row strong{margin-top:3px}[data-page="solutions"] .fit-matrix-action{align-items:flex-start;flex-direction:column}[data-page="solutions"] .solutions-timeline{grid-template-columns:1fr;gap:0;border-left:1px solid #d6deea;margin-left:5px}[data-page="solutions"] .solutions-timeline article{padding:10px 0 24px 24px;border-top:0}[data-page="solutions"] .solutions-timeline article:before{top:14px;left:-5px}[data-page="solutions"] .solutions-timeline p{max-width:none}}
'''

index_path.write_text(html)
styles_path.write_text(css)
print('solutions page redesigned')
