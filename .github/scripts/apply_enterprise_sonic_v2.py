from pathlib import Path

root = Path(__file__).resolve().parents[2]
html_path = root / '03-enterprise/prototype-v4/index.html'
css_path = root / '03-enterprise/prototype-v4/styles.css'
html = html_path.read_text()
css = css_path.read_text()

old_cap = '''  <section class="section soft home-capabilities"><div class="container"><div class="section-head reveal"><span class="eyebrow">WHAT IT DOES</span><h2>把发行业务集中到一套系统</h2><p>从客户、曲库和审核发行，到上线进度、平台数据和收入结算，减少表格、邮件和多套工具之间的重复操作。</p></div><div class="feature-grid reveal"><article><b>01</b><h3>客户管理</h3><p>客户、厂牌和内部账号统一管理，减少分散维护。</p></article><article><b>02</b><h3>曲库管理</h3><p>艺人、专辑、歌曲、音频、封面和发行资料集中管理。</p></article><article><b>03</b><h3>审核与发行</h3><p>从提交、审核到选择目标平台和正式发行，流程连续可追踪。</p></article><article><b>04</b><h3>上线进度</h3><p>统一查看各平台处理中、已上线、失败及后续处理状态。</p></article><article><b>05</b><h3>数据报表</h3><p>发行结果和平台数据集中查看，减少人工汇总。</p></article><article><b>06</b><h3>收入与结算</h3><p>收入、分账、待结算、可提现和提现记录统一管理。</p></article></div></div></section>'''
new_cap = '''  <section class="section soft home-capabilities"><div class="container"><div class="section-head split reveal"><div><span class="eyebrow">WHAT IT DOES</span><h2>把发行业务集中到一套系统</h2></div><p>把客户、曲库、审核发行、上线状态、数据与收入放进同一个工作空间，让复杂业务通过可视化状态和统一操作完成。</p></div><div class="capability-showcase reveal">
    <article class="capability-card"><div class="capability-art art-clients"><div class="avatar-stack"><i>N</i><i>B</i><i>C</i></div><div class="mini-lines"><span></span><span></span><span></span></div><em>128 CLIENTS</em></div><div class="capability-meta"><span class="capability-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="8" cy="8" r="3"></circle><circle cx="17" cy="9" r="2.5"></circle><path d="M3.5 19c.7-3.2 2.5-4.8 5-4.8s4.3 1.6 5 4.8M14 18c.4-2.3 1.7-3.5 3.8-3.5 1.5 0 2.6.6 3.2 1.8"></path></svg></span><b>01</b></div><h3>客户管理</h3><p>客户、厂牌和内部账号统一管理，业务关系和内容归属保持清晰。</p></article>
    <article class="capability-card"><div class="capability-art art-catalog"><div class="mini-cover"></div><div class="catalog-lines"><span><b>Midnight Signals</b><i>12 tracks</i></span><span><b>Neon Summer</b><i>Single</i></span><span><b>After Rain</b><i>EP</i></span></div></div><div class="capability-meta"><span class="capability-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M4 6h16v12H4z"></path><path d="M8 3v3M16 3v3M8 10h8M8 14h5"></path></svg></span><b>02</b></div><h3>曲库管理</h3><p>艺人、专辑、歌曲、音频、封面和发行资料集中沉淀，并保持关联。</p></article>
    <article class="capability-card"><div class="capability-art art-review"><div class="review-track"><span class="done">提交</span><i></i><span class="active">审核</span><i></i><span>发行</span></div><small>24 ITEMS TO REVIEW</small></div><div class="capability-meta"><span class="capability-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 4h14v16H5z"></path><path d="M8 9l2 2 5-5M8 15h8"></path></svg></span><b>03</b></div><h3>审核与发行</h3><p>从资料校验、内容审核到目标平台提交，完整流程持续可追踪。</p></article>
    <article class="capability-card"><div class="capability-art art-status"><span class="dsp ok">Spotify <b>LIVE</b></span><span class="dsp pending">Apple <b>PROCESSING</b></span><span class="dsp ok">QQ Music <b>LIVE</b></span></div><div class="capability-meta"><span class="capability-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M4 12h4l2-5 4 10 2-5h4"></path><path d="M4 4v16h16"></path></svg></span><b>04</b></div><h3>上线进度</h3><p>集中查看不同平台处理中、已上线和异常状态，并继续完成后续维护。</p></article>
    <article class="capability-card"><div class="capability-art art-data"><div class="bar-chart"><i style="height:34%"></i><i style="height:58%"></i><i style="height:44%"></i><i style="height:76%"></i><i style="height:92%"></i><i style="height:68%"></i></div><em>+18.4%</em></div><div class="capability-meta"><span class="capability-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 19V9M10 19V5M15 19v-7M20 19V3"></path></svg></span><b>05</b></div><h3>数据报表</h3><p>发行结果和平台数据集中查看，为运营分析和内部数据处理提供统一入口。</p></article>
    <article class="capability-card"><div class="capability-art art-revenue"><div class="revenue-total"><span>AVAILABLE</span><strong>¥428,620</strong></div><div class="split-bars"><i></i><i></i><i></i></div><em>3 SETTLEMENT GROUPS</em></div><div class="capability-meta"><span class="capability-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"></circle><path d="M8.5 9.5h7M8.5 14.5h7M12 7v10"></path></svg></span><b>06</b></div><h3>收入与结算</h3><p>收入、分账、待结算、可提现和提现记录在统一业务视图中管理。</p></article>
  </div></div></section>'''
if old_cap not in html:
    raise SystemExit('home capabilities block not found')
html = html.replace(old_cap, new_cap, 1)

old_audience = '''  <section class="section home-audience-section"><div class="container"><div class="section-head split reveal"><div><span class="eyebrow">WHO IT IS FOR</span><h2>为不同类型的音乐企业，提供合适的发行方式</h2></div><a class="text-link home-section-head-link" href="/enterprise/solutions" data-route>查看企业解决方案 →</a></div><div class="solution-preview home-use-cases reveal"><article><span class="case-no">01 · DISTRIBUTOR</span><span>发行商</span><h3>建立自有发行品牌和客户平台</h3><p>用一个后台服务多个厂牌、版权方和音乐人。</p></article><article><span class="case-no">02 · LABEL & RIGHTS</span><span>唱片公司 / 版权公司</span><h3>统一管理曲库、发行、数据与收入</h3><p>减少 Excel、人工汇总和分散的发行操作。</p></article><article><span class="case-no">03 · PLATFORM & AI</span><span>音乐平台 / AI 音乐产品</span><h3>在现有产品中增加音乐发行服务</h3><p>保留原有产品体验，通过 API 接入发行流程。</p></article></div></div></section>'''
new_audience = '''  <section class="section home-audience-section"><div class="container"><div class="section-head split reveal"><div><span class="eyebrow">WHO IT IS FOR</span><h2>为不同类型的音乐企业，提供合适的发行方式</h2></div><a class="text-link home-section-head-link" href="/enterprise/solutions" data-route>查看企业解决方案 →</a></div><div class="solution-preview home-use-cases reveal"><article><span class="case-glyph" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="5" cy="6" r="2"></circle><circle cx="19" cy="6" r="2"></circle><circle cx="12" cy="18" r="2"></circle><path d="M7 7.2l4 8M17 7.2l-4 8M7 6h10"></path></svg></span><span class="case-no">01 · DISTRIBUTOR</span><span>发行商</span><h3>建立自有发行品牌和客户平台</h3><p>用一个后台服务多个厂牌、版权方和音乐人。</p></article><article><span class="case-glyph" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M4 7l8-3 8 3-8 3-8-3zM4 12l8 3 8-3M4 17l8 3 8-3"></path></svg></span><span class="case-no">02 · LABEL & RIGHTS</span><span>唱片公司 / 版权公司</span><h3>统一管理曲库、发行、数据与收入</h3><p>减少 Excel、人工汇总和分散的发行操作。</p></article><article><span class="case-glyph" aria-hidden="true"><svg viewBox="0 0 24 24"><rect x="3" y="5" width="7" height="6" rx="1.5"></rect><rect x="14" y="13" width="7" height="6" rx="1.5"></rect><path d="M10 8h3a4 4 0 014 4v1M14 16h-3a4 4 0 01-4-4v-1"></path></svg></span><span class="case-no">03 · PLATFORM & AI</span><span>音乐平台 / AI 音乐产品</span><h3>在现有产品中增加音乐发行服务</h3><p>保留原有产品体验，通过 API 接入发行流程。</p></article></div></div></section>'''
if old_audience not in html:
    raise SystemExit('home audience block not found')
html = html.replace(old_audience, new_audience, 1)

old_scenarios = '''  <section class="section"><div class="container"><div class="section-head reveal"><span class="eyebrow">SOLUTION SCENARIOS</span><h2>从业务场景出发，选择合适的发行能力</h2><p>围绕品牌建设、曲库管理、产品集成与系统对接四类典型场景，组合适合企业现状的发行方案。</p></div><div class="scenario-card-grid reveal"><article class="scenario-card"><span class="scenario-kicker">建设自有品牌发行平台</span><h3>自有品牌发行平台</h3><p>以企业自有品牌开展发行业务，统一提供客户门户、发行运营、数据与收入管理能力。</p></article><article class="scenario-card"><span class="scenario-kicker">管理规模化曲库</span><h3>统一曲库与发行运营</h3><p>集中管理内容资产、批量发行、平台状态、业务数据和收入，支撑持续增长的发行规模。</p></article><article class="scenario-card"><span class="scenario-kicker">嵌入现有网站或 App</span><h3>通过 API 接入发行能力</h3><p>保留现有产品、账号体系和用户体验，将内容提交、发行、状态与数据能力接入原有产品。</p></article><article class="scenario-card"><span class="scenario-kicker">连接内部业务系统</span><h3>打通现有数据与业务流程</h3><p>通过 API、SFTP、XML、DDEX 等方式，与现有内容系统、业务系统及数据流程集成。</p></article></div></div></section>'''
new_scenarios = '''  <section class="section"><div class="container"><div class="section-head split reveal"><div><span class="eyebrow">SOLUTION SCENARIOS</span><h2>从业务场景出发，选择合适的发行能力</h2></div><p>通过品牌、曲库、API 与系统连接四种典型路径，让不同业务模式快速找到对应的产品组合。</p></div><div class="scenario-card-grid reveal"><article class="scenario-card"><div class="scenario-art"><span class="scenario-icon"><svg viewBox="0 0 24 24"><path d="M4 6h16v12H4zM8 10h8M8 14h5"></path></svg></span><div class="scenario-window"><i></i><i></i><i></i></div></div><span class="scenario-kicker">建设自有品牌发行平台</span><h3>自有品牌发行平台</h3><p>以企业自有品牌开展发行业务，统一提供客户门户、发行运营、数据与收入管理能力。</p></article><article class="scenario-card"><div class="scenario-art"><span class="scenario-icon"><svg viewBox="0 0 24 24"><path d="M4 7l8-3 8 3-8 3-8-3zM4 12l8 3 8-3M4 17l8 3 8-3"></path></svg></span><div class="scenario-stack"><i></i><i></i><i></i></div></div><span class="scenario-kicker">管理规模化曲库</span><h3>统一曲库与发行运营</h3><p>集中管理内容资产、批量发行、平台状态、业务数据和收入，支撑持续增长的发行规模。</p></article><article class="scenario-card"><div class="scenario-art"><span class="scenario-icon"><svg viewBox="0 0 24 24"><path d="M8 4L3 12l5 8M16 4l5 8-5 8M13 3l-2 18"></path></svg></span><div class="scenario-code"><b>POST</b><i>/distribution</i></div></div><span class="scenario-kicker">嵌入现有网站或 App</span><h3>通过 API 接入发行能力</h3><p>保留现有产品、账号体系和用户体验，将内容提交、发行、状态与数据能力接入原有产品。</p></article><article class="scenario-card"><div class="scenario-art"><span class="scenario-icon"><svg viewBox="0 0 24 24"><rect x="3" y="5" width="7" height="6" rx="1.5"></rect><rect x="14" y="13" width="7" height="6" rx="1.5"></rect><path d="M10 8h3a4 4 0 014 4v1M14 16h-3a4 4 0 01-4-4v-1"></path></svg></span><div class="scenario-route"><i></i><i></i><i></i></div></div><span class="scenario-kicker">连接内部业务系统</span><h3>打通现有数据与业务流程</h3><p>通过 API、SFTP、XML、DDEX 等方式，与现有内容系统、业务系统及数据流程集成。</p></article></div></div></section>'''
if old_scenarios not in html:
    raise SystemExit('solution scenarios block not found')
html = html.replace(old_scenarios, new_scenarios, 1)

marker = '/* Enterprise Sonic v2 — light visual storytelling */'
if marker in css:
    css = css.split(marker)[0].rstrip() + '\n'

css += r'''

/* Enterprise Sonic v2 — light visual storytelling */
:root{--sonic-ink:#14213a;--sonic-muted:#6e7b91;--sonic-blue:#4168df;--sonic-soft:#f4f7fd;--sonic-line:#dde5f0}

/* HOME — retain music-tech character without turning the whole site dark */
[data-page="home"] .sonic-hero{min-height:660px;background:radial-gradient(circle at 76% 20%,rgba(71,108,228,.13),transparent 26%),linear-gradient(180deg,#f8faff 0%,#fff 78%);color:var(--sonic-ink)}
[data-page="home"] .sonic-hero-gridlines{opacity:.45;background:linear-gradient(rgba(74,104,177,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(74,104,177,.045) 1px,transparent 1px);background-size:68px 68px}
[data-page="home"] .sonic-hero .eyebrow{color:#6e82ba}
[data-page="home"] .sonic-hero h1{color:#15213a}
[data-page="home"] .sonic-hero h1 em{color:#4168df}
[data-page="home"] .sonic-hero .hero-copy>p{color:#657289}
[data-page="home"] .sonic-hero .btn-secondary{border-color:#d6deeb;background:rgba(255,255,255,.8);color:#273650}
[data-page="home"] .sonic-hero .hero-proof span{border-color:#dce4f1;background:rgba(255,255,255,.76);color:#65738c}
[data-page="home"] .sonic-hero .console{border-color:#d8e1ef;background:#fff;box-shadow:0 34px 88px rgba(41,61,105,.14);transform:perspective(1100px) rotateY(-2deg) rotateX(1deg)}
[data-page="home"] .sonic-hero .console:after{color:#8292ad}
[data-page="home"] .sonic-hero .console-top{border-bottom-color:#e6ebf2;background:#f8faff;color:#293853}
[data-page="home"] .sonic-hero .console-body aside{border-right-color:#e8edf4;background:#f7f9fd}
[data-page="home"] .sonic-hero .console-body aside small,[data-page="home"] .sonic-hero .console-body aside i{color:#7d8798}
[data-page="home"] .sonic-hero .console-body aside i.active{background:#edf2ff;color:#3455bd}
[data-page="home"] .sonic-hero .console-body section{background:#fff}
[data-page="home"] .sonic-hero .console-head h3,[data-page="home"] .sonic-hero .metric-row strong,[data-page="home"] .sonic-hero .release-card b{color:#24324a}
[data-page="home"] .sonic-hero .console-head small,[data-page="home"] .sonic-hero .metric-row span,[data-page="home"] .sonic-hero .release-card span{color:#8390a3}
[data-page="home"] .sonic-hero .metric-row>div,[data-page="home"] .sonic-hero .release-card{border-color:#e5eaf2;background:#fafbfe}
[data-page="home"] .sonic-waveform span{background:linear-gradient(to top,#4168df,#9fb5ff)}
[data-page="home"] .sonic-ticker{border-color:#dfe6f0;background:#fff}
[data-page="home"] .sonic-ticker-track{color:#7c8aa2}
[data-page="home"] .sonic-ticker-track i{background:#d8e1ef}
[data-page="home"] .sonic-ticker-track i:after{background:#5279e8;box-shadow:0 0 10px rgba(82,121,232,.45)}
[data-page="home"] .home-product-pair .visual{background:#f4f7fd;color:#294070}
[data-page="home"] .home-product-pair .visual-platform{background:radial-gradient(circle at 68% 34%,rgba(79,124,255,.18),transparent 30%),linear-gradient(145deg,#eef3ff,#fafcff)}
[data-page="home"] .home-product-pair .visual-api{background:linear-gradient(145deg,#f5f8ff,#eef3fb)}
[data-page="home"] .home-product-pair .visual-api code{color:#3458c4}

/* WHAT IT DOES — product evidence instead of six text boxes */
[data-page="home"] .home-capabilities{padding-top:108px;padding-bottom:112px;background:#fff}
[data-page="home"] .home-capabilities:before{content:""}
[data-page="home"] .home-capabilities .section-head{max-width:none;margin-bottom:34px}
[data-page="home"] .capability-showcase{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
[data-page="home"] .capability-card{min-width:0;padding:18px;border:1px solid #dfe6f0;border-radius:22px;background:#fff;box-shadow:0 12px 34px rgba(32,52,95,.045);transition:transform .2s ease,border-color .2s ease,box-shadow .2s ease}
[data-page="home"] .capability-card:hover{transform:translateY(-3px);border-color:#cbd7ed;box-shadow:0 18px 42px rgba(32,52,95,.075)}
[data-page="home"] .capability-art{position:relative;display:flex;align-items:center;min-height:146px;padding:18px;border:1px solid #e4eaf4;border-radius:16px;overflow:hidden;background:linear-gradient(145deg,#f5f8ff,#fbfcff)}
[data-page="home"] .capability-art:after{content:"";position:absolute;right:-28px;bottom:-44px;width:120px;height:120px;border-radius:50%;background:rgba(75,111,220,.055)}
[data-page="home"] .capability-meta{display:flex;align-items:center;justify-content:space-between;margin-top:18px}
[data-page="home"] .capability-meta>b{color:#a4afc1;font-size:9px;letter-spacing:.14em}
[data-page="home"] .capability-icon{display:grid;place-items:center;width:38px;height:38px;border:1px solid #dce5f5;border-radius:12px;background:#f4f7ff;color:#4168df}
[data-page="home"] .capability-icon svg{width:19px;height:19px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
[data-page="home"] .capability-card h3{margin:14px 0 9px;color:#1d2a43;font-size:20px}
[data-page="home"] .capability-card p{margin:0;color:#738096;font-size:12px;line-height:1.72}
[data-page="home"] .avatar-stack{display:flex;align-items:center}.avatar-stack i{display:grid;place-items:center;width:40px;height:40px;margin-right:-8px;border:3px solid #f7f9ff;border-radius:50%;background:#dce7ff;color:#3159c7;font-size:10px;font-style:normal;font-weight:900}.avatar-stack i:nth-child(2){background:#e8e0ff;color:#7558bf}.avatar-stack i:nth-child(3){background:#dff3ed;color:#3f7b6a}
[data-page="home"] .mini-lines{display:grid;gap:7px;width:92px;margin-left:24px}.mini-lines span{height:7px;border-radius:8px;background:#dbe4f3}.mini-lines span:nth-child(2){width:72%}.mini-lines span:nth-child(3){width:86%}[data-page="home"] .capability-art>em{position:absolute;left:18px;bottom:14px;color:#8190aa;font-size:8px;font-style:normal;font-weight:900;letter-spacing:.12em}
[data-page="home"] .art-catalog{gap:16px}.mini-cover{width:62px;height:62px;border-radius:12px;background:linear-gradient(145deg,#2f4f9f,#8cb4ff);box-shadow:0 10px 22px rgba(54,91,183,.18)}.catalog-lines{display:grid;gap:9px;flex:1}.catalog-lines span{display:flex;justify-content:space-between;gap:10px;padding-bottom:7px;border-bottom:1px solid #e5eaf2}.catalog-lines b,.catalog-lines i{font-size:8px}.catalog-lines b{color:#35435d}.catalog-lines i{color:#9aa5b5;font-style:normal}
[data-page="home"] .art-review{display:block;padding-top:34px}.review-track{display:grid;grid-template-columns:auto 1fr auto 1fr auto;align-items:center;gap:7px}.review-track span{display:grid;place-items:center;min-width:48px;height:30px;border:1px solid #d8e1ef;border-radius:9px;background:#fff;color:#8491a6;font-size:8px;font-weight:800}.review-track span.done{border-color:#c6d6ff;background:#eef3ff;color:#4265ca}.review-track span.active{border-color:#8ca9ff;background:#4168df;color:#fff;box-shadow:0 8px 18px rgba(65,104,223,.2)}.review-track i{height:1px;background:#d7e0ee}.art-review small{display:block;margin-top:21px;color:#8492a8;font-size:8px;letter-spacing:.1em}
[data-page="home"] .art-status{display:grid;align-content:center;gap:8px}.dsp{display:flex;align-items:center;justify-content:space-between;min-width:220px;padding:10px 12px;border:1px solid #e0e6ef;border-radius:10px;background:#fff;color:#526079;font-size:9px}.dsp b{font-size:7px;letter-spacing:.08em}.dsp.ok b{color:#39826d}.dsp.pending b{color:#7a6ab9}
[data-page="home"] .art-data{align-items:flex-end}.bar-chart{display:flex;align-items:flex-end;gap:7px;width:76%;height:82px}.bar-chart i{flex:1;min-height:12px;border-radius:5px 5px 2px 2px;background:linear-gradient(to top,#9cb4f5,#4168df)}.art-data>em{position:absolute;right:18px;top:18px;color:#4266c9;font-size:11px;font-style:normal;font-weight:900}
[data-page="home"] .art-revenue{display:block}.revenue-total span{display:block;color:#8b97aa;font-size:8px;font-weight:900;letter-spacing:.1em}.revenue-total strong{display:block;margin-top:7px;color:#25354f;font-size:22px;letter-spacing:-.04em}.split-bars{display:flex;gap:4px;margin-top:20px}.split-bars i{height:8px;border-radius:99px;background:#4268df}.split-bars i:nth-child(1){width:52%}.split-bars i:nth-child(2){width:28%;background:#89a4f3}.split-bars i:nth-child(3){width:16%;background:#d4def8}

/* Home audience: icon + copy, not just copy */
[data-page="home"] .home-use-cases{gap:14px;border:0}
[data-page="home"] .home-use-cases article{min-height:300px;padding:30px;border:1px solid #dfe6f0;border-radius:20px;background:#fff;box-shadow:0 10px 28px rgba(33,52,94,.035)}
[data-page="home"] .home-use-cases article:last-child{border-right:1px solid #dfe6f0}
[data-page="home"] .case-glyph{display:grid;place-items:center;width:50px;height:50px;margin-bottom:34px;border:1px solid #dce4f2;border-radius:15px;background:#f4f7ff;color:#4168df}
[data-page="home"] .case-glyph svg{width:24px;height:24px;fill:none;stroke:currentColor;stroke-width:1.65;stroke-linecap:round;stroke-linejoin:round}

/* PRODUCT — mostly light; keep data/product evidence as the visual focus */
[data-page="product"] .sonic-product-hero{background:radial-gradient(circle at 82% 24%,rgba(73,110,234,.12),transparent 28%),linear-gradient(180deg,#f8faff,#fff);color:#15213a}
[data-page="product"] .sonic-product-hero:after{background:linear-gradient(90deg,transparent 49.8%,rgba(74,104,177,.045) 50%,transparent 50.2%);background-size:84px 100%}
[data-page="product"] .sonic-product-hero h1{color:#17233a}
[data-page="product"] .sonic-product-hero .product-hero-lead{color:#68758b}
[data-page="product"] .sonic-product-hero .btn-secondary{border-color:#d7dfeb;background:#fff;color:#293750}
[data-page="product"] .sonic-product-hero .product-hero-ui{border-color:#d9e1ed;background:#fff;box-shadow:0 30px 78px rgba(41,61,105,.14)}
[data-page="product"] .sonic-product-hero .phu-top,[data-page="product"] .sonic-product-hero .phu-body aside{background:#f7f9fd;border-color:#e5ebf3}
[data-page="product"] .sonic-product-hero .phu-main{background:#fff}
[data-page="product"] .sonic-product-hero .phu-head strong,[data-page="product"] .sonic-product-hero .phu-list b,[data-page="product"] .sonic-product-hero .phu-metrics b{color:#27354e}
[data-page="product"] .sonic-product-hero .phu-metrics>div,[data-page="product"] .sonic-product-hero .phu-list>div{border-color:#e5eaf2;background:#fafbfe}
[data-page="product"] .product-signal-rail{border-top-color:#d7e0ee}
[data-page="product"] .product-signal-rail:before{background:#5278e7;box-shadow:0 0 10px rgba(82,120,231,.35)}
[data-page="product"] .product-signal-rail>div:before{border-color:#aab7cb;background:#fff}
[data-page="product"] .product-signal-rail>div.active:before{border-color:#5278e7;background:#5278e7}
[data-page="product"] .product-signal-rail span{color:#9aa6b8}.product-signal-rail b{color:#35455f!important}.product-signal-rail small{color:#7e8ba0!important}
[data-page="product"] .product-release{background:linear-gradient(180deg,#f4f7fd,#fff);color:#17233a}
[data-page="product"] .product-release:before{color:rgba(49,73,128,.035)}
[data-page="product"] .product-release .section-head h2{color:#17233a}
[data-page="product"] .product-release .section-head p{color:#6f7c91}
[data-page="product"] .product-release .release-steps{border-top-color:#d9e2ef}
[data-page="product"] .product-release .release-steps>div:before{border-color:#afbbcd;background:#fff}
[data-page="product"] .product-release .release-steps>div.done:before,[data-page="product"] .product-release .release-steps>div.active:before{border-color:#5278e7;background:#5278e7}
[data-page="product"] .product-release .release-steps b{color:#9aa6b8}
[data-page="product"] .product-release .release-steps span{color:#45546d}
[data-page="product"] .product-release .workspace-ui{border-color:#dfe6f0;background:#fff;box-shadow:0 18px 52px rgba(35,54,93,.07)}
[data-page="product"] .product-release .wu-top,[data-page="product"] .product-release .wu-table>div,[data-page="product"] .product-release .admin-status{border-color:#e5eaf2}
[data-page="product"] .product-release .workspace-note{color:#7a879b}

/* SOLUTIONS — light route map and light architecture studio */
[data-page="solutions"] .sonic-solutions-hero{background:radial-gradient(circle at 75% 28%,rgba(75,113,234,.13),transparent 28%),linear-gradient(180deg,#f8faff,#fff);color:#17233a}
[data-page="solutions"] .sonic-solutions-hero:before{background:linear-gradient(rgba(74,104,177,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(74,104,177,.04) 1px,transparent 1px);background-size:64px 64px}
[data-page="solutions"] .sonic-solutions-hero .eyebrow{color:#6e82ba}
[data-page="solutions"] .sonic-solutions-hero h1{color:#17233a}
[data-page="solutions"] .sonic-solutions-hero p{color:#68758b}
[data-page="solutions"] .sonic-solutions-hero .solutions-hero-proof span{border-color:#dce4f1;background:rgba(255,255,255,.82);color:#5d6f8f}
[data-page="solutions"] .solutions-route-hero{border-top-color:#dfe6f0}
[data-page="solutions"] .route-unit{border-color:#dfe6f0;background:#fff;box-shadow:0 8px 24px rgba(34,54,96,.04)}
[data-page="solutions"] .route-unit.core{border-color:#b9c9f5;background:#eef3ff;box-shadow:0 10px 28px rgba(65,104,223,.09)}
[data-page="solutions"] .route-unit small{color:#8997ad}.route-unit b{color:#2f3f59!important}
[data-page="solutions"] .solutions-route-hero>i{background:#ccd8ea}
[data-page="solutions"] .solutions-route-hero>i:after{background:#5278e7;box-shadow:0 0 10px rgba(82,120,231,.4)}
[data-page="solutions"] .scenario-card-grid{gap:16px;border:0}
[data-page="solutions"] .scenario-card{min-height:330px;padding:22px 26px 30px;border:1px solid #dfe6f0;border-radius:20px;background:#fff;box-shadow:0 10px 30px rgba(34,54,96,.035)}
[data-page="solutions"] .scenario-card:hover{transform:translateY(-2px);background:#fff;box-shadow:0 16px 38px rgba(34,54,96,.065)}
[data-page="solutions"] .scenario-card:before{display:none}
[data-page="solutions"] .scenario-art{position:relative;display:flex;align-items:center;justify-content:space-between;min-height:112px;margin-bottom:24px;padding:16px 18px;border:1px solid #e2e8f2;border-radius:15px;overflow:hidden;background:linear-gradient(145deg,#f4f7ff,#fbfcff)}
[data-page="solutions"] .scenario-icon{display:grid;place-items:center;width:42px;height:42px;border-radius:12px;background:#fff;color:#4168df;box-shadow:0 7px 20px rgba(46,74,139,.08)}
[data-page="solutions"] .scenario-icon svg{width:21px;height:21px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
[data-page="solutions"] .scenario-window{display:grid;gap:6px;width:115px;padding:12px;border:1px solid #dfe6f0;border-radius:10px;background:#fff}.scenario-window i{height:7px;border-radius:5px;background:#dfe6f2}.scenario-window i:nth-child(2){width:72%}.scenario-window i:nth-child(3){width:88%}
[data-page="solutions"] .scenario-stack{position:relative;width:100px;height:58px}.scenario-stack i{position:absolute;left:0;right:0;height:34px;border:1px solid #ccd8ec;border-radius:9px;background:#fff}.scenario-stack i:nth-child(1){top:0;left:20px}.scenario-stack i:nth-child(2){top:10px;left:10px;right:10px;background:#f5f8ff}.scenario-stack i:nth-child(3){top:20px;background:#eef3ff}
[data-page="solutions"] .scenario-code{display:flex;align-items:center;gap:8px;padding:10px 12px;border:1px solid #dce4f0;border-radius:10px;background:#fff}.scenario-code b{padding:4px 6px;border-radius:5px;background:#eaf0ff;color:#4163c9;font-size:8px}.scenario-code i{color:#63728a;font-size:9px;font-style:normal}
[data-page="solutions"] .scenario-route{position:relative;width:118px;height:42px}.scenario-route:before{content:"";position:absolute;left:5px;right:5px;top:20px;height:1px;background:#cbd7ea}.scenario-route i{position:absolute;top:15px;width:11px;height:11px;border:3px solid #f5f8ff;border-radius:50%;background:#5278e7}.scenario-route i:nth-child(1){left:2px}.scenario-route i:nth-child(2){left:50%;transform:translateX(-50%)}.scenario-route i:nth-child(3){right:2px}
[data-page="solutions"] .scenario-kicker{margin-bottom:12px}
[data-page="solutions"] .solutions-architecture-section{padding-top:108px;padding-bottom:108px;background:#f5f8fd;color:#17233a}
[data-page="solutions"] .solutions-architecture-section .visual-section-head h2{color:#17233a}
[data-page="solutions"] .solutions-architecture-section .visual-section-head p{color:#6f7c91}
[data-page="solutions"] .architecture-studio{border-color:#dbe4f0;background:#fff;box-shadow:0 24px 64px rgba(34,54,96,.08)}
[data-page="solutions"] .architecture-tabs{border-bottom-color:#e4eaf2;background:#f9fbfe}
[data-page="solutions"] .architecture-tabs button{color:#7a879b}
[data-page="solutions"] .architecture-tabs button.active{background:#edf2ff;color:#3558c1}
[data-page="solutions"] .architecture-canvas{background:linear-gradient(rgba(74,104,177,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(74,104,177,.035) 1px,transparent 1px),#fff;background-size:34px 34px}
[data-page="solutions"] .architecture-panel>i{color:#6e82ad}
[data-page="solutions"] .arch-node{border-color:#dce4f0;background:#fff;box-shadow:0 8px 24px rgba(34,54,96,.045)}
[data-page="solutions"] .arch-node small{color:#8492a8}.arch-node b{color:#2b3a55!important}.arch-node span{color:#7a879b}
[data-page="solutions"] .arch-node.primary{border-color:#b7c8f6;background:#eef3ff}.arch-node.core{border-color:#c7d4ec;background:#f6f8fc}
[data-page="solutions"] .architecture-legend{border-top-color:#e4eaf2;background:#fafbfe;color:#7b879a}

@media(max-width:960px){
  [data-page="home"] .capability-showcase{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media(max-width:680px){
  [data-page="home"] .sonic-hero .console{transform:none}
  [data-page="home"] .capability-showcase{grid-template-columns:1fr}
  [data-page="home"] .capability-art{min-height:132px}
  [data-page="home"] .home-use-cases{gap:12px}
  [data-page="home"] .home-use-cases article{border-right:1px solid #dfe6f0!important;border-bottom:1px solid #dfe6f0}
  [data-page="solutions"] .scenario-card{min-height:0}
  [data-page="solutions"] .solutions-architecture-section{padding-top:76px;padding-bottom:76px}
}
'''

html_path.write_text(html)
css_path.write_text(css)
print('enterprise sonic v2 applied')
