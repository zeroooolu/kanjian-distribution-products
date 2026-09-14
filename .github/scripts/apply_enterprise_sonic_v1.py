from pathlib import Path
import re

INDEX = Path('03-enterprise/prototype-v4/index.html')
STYLES = Path('03-enterprise/prototype-v4/styles.css')

html = INDEX.read_text(encoding='utf-8')
css = STYLES.read_text(encoding='utf-8')

MARKER = '/* Enterprise Sonic Infrastructure v1 */'
if MARKER in css:
    print('Sonic visual system already applied; nothing to do.')
    raise SystemExit(0)

# Page-level hooks.
html = html.replace('<section class="page active" data-page="home">', '<section class="page active sonic-page sonic-home" data-page="home">', 1)
html = html.replace('<section class="page product-page" data-page="product">', '<section class="page product-page sonic-page sonic-product" data-page="product">', 1)
html = html.replace('<section class="page" data-page="solutions">', '<section class="page sonic-page sonic-solutions" data-page="solutions">', 1)

# Home hero: dark sonic infrastructure canvas + waveform evidence.
html = html.replace('<section class="hero"><div class="container hero-grid">', '<section class="hero sonic-hero"><div class="sonic-hero-gridlines" aria-hidden="true"></div><div class="container hero-grid">', 1)
waveform = '''<div class="sonic-waveform home-waveform" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>'''
html, n = re.subn(r'(<div class="hero-proof">.*?</div>)', r'\1' + waveform, html, count=1, flags=re.S)
assert n == 1, 'home hero proof not found'

ticker = '''\n  <section class="sonic-ticker" aria-label="音乐发行信号流"><div class="container sonic-ticker-track"><span>CATALOG</span><i></i><span>REVIEW</span><i></i><span>DISTRIBUTION</span><i></i><span>DSP NETWORK</span><i></i><span>DATA</span><i></i><span>REVENUE</span></div></section>\n'''
needle = '  </div></section>\n\n  <section class="section home-choice-section">'
assert needle in html, 'home hero ending not found'
html = html.replace(needle, '  </div></section>' + ticker + '\n  <section class="section home-choice-section">', 1)

# Product hero: add signal rail after CTA to make the business flow feel like a DAW timeline.
html = html.replace('<section class="product-hero"><div class="container product-hero-grid">', '<section class="product-hero sonic-product-hero"><div class="sonic-product-grid" aria-hidden="true"></div><div class="container product-hero-grid">', 1)
product_signal = '''<div class="product-signal-rail" aria-label="发行流程"><div class="active"><span>01</span><b>CATALOG</b><small>内容进入曲库</small></div><div><span>02</span><b>REVIEW</b><small>资料与内容审核</small></div><div><span>03</span><b>DELIVERY</b><small>渠道交付</small></div><div><span>04</span><b>LIVE</b><small>上线与持续运营</small></div></div>'''
html, n = re.subn(r'(<p class="product-hero-lead">.*?</p><div class="hero-actions">.*?</div>)', r'\1' + product_signal, html, count=1, flags=re.S)
assert n == 1, 'product hero actions not found'

# Solutions hero: turn the opening into a routing / patch-bay metaphor.
html = html.replace('<section class="subhero solutions-hero">', '<section class="subhero solutions-hero sonic-solutions-hero">', 1)
route = '''<div class="solutions-route-hero" aria-label="企业发行连接路径"><div class="route-unit source"><small>BUSINESS</small><b>品牌 · 曲库 · 产品 · 系统</b></div><i aria-hidden="true"></i><div class="route-unit core"><small>STAR DISTRIBUTION</small><b>企业发行基础设施</b></div><i aria-hidden="true"></i><div class="route-unit output"><small>NETWORK</small><b>国内外音乐平台</b></div></div>'''
html, n = re.subn(r'(<div class="solutions-hero-proof">.*?</div>)', r'\1' + route, html, count=1, flags=re.S)
assert n == 1, 'solutions hero proof not found'

SONIC_CSS = r'''

/* Enterprise Sonic Infrastructure v1 */
:root{--sonic-ink:#07111f;--sonic-ink-2:#0c1829;--sonic-line:rgba(130,158,214,.18);--sonic-blue:#4f7cff;--sonic-blue-soft:#8eacff;--sonic-paper:#f4f7fb}
.sonic-page{--sonic-grid:rgba(110,142,202,.08)}

/* Shared sonic motion */
@keyframes sonic-bar{0%,100%{transform:scaleY(.62);opacity:.45}50%{transform:scaleY(1);opacity:1}}
@keyframes sonic-dot{0%{transform:translateX(-12px);opacity:0}18%{opacity:1}82%{opacity:1}100%{transform:translateX(calc(100% + 12px));opacity:0}}
@keyframes sonic-breathe{0%,100%{box-shadow:0 0 0 0 rgba(79,124,255,.08)}50%{box-shadow:0 0 0 9px rgba(79,124,255,0)}}
@media(prefers-reduced-motion:reduce){.sonic-page *{animation:none!important;transition:none!important}}

/* HOME — music infrastructure, not music decoration */
[data-page="home"] .sonic-hero{position:relative;overflow:hidden;min-height:760px;padding-top:78px;padding-bottom:78px;background:radial-gradient(circle at 80% 22%,rgba(65,101,225,.23),transparent 31%),radial-gradient(circle at 28% 80%,rgba(44,94,214,.12),transparent 28%),linear-gradient(135deg,#07111f 0%,#0a1424 52%,#0d1b30 100%);color:#fff}
[data-page="home"] .sonic-hero:before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,transparent 49.8%,rgba(143,170,226,.05) 50%,transparent 50.2%),linear-gradient(0deg,transparent 49.8%,rgba(143,170,226,.04) 50%,transparent 50.2%);background-size:72px 72px;mask-image:linear-gradient(to bottom,rgba(0,0,0,.9),transparent 92%);pointer-events:none}
[data-page="home"] .sonic-hero:after{content:"";position:absolute;right:-180px;top:120px;width:620px;height:620px;border:1px solid rgba(130,158,214,.08);border-radius:50%;box-shadow:0 0 0 80px rgba(130,158,214,.025),0 0 0 160px rgba(130,158,214,.014);pointer-events:none}
[data-page="home"] .sonic-hero-gridlines{position:absolute;left:0;right:0;top:54%;height:1px;background:linear-gradient(90deg,transparent 0,rgba(113,147,221,.26) 13%,rgba(113,147,221,.26) 87%,transparent 100%);opacity:.65}
[data-page="home"] .sonic-hero .hero-grid{position:relative;z-index:2;min-height:600px;align-items:center;gap:72px}
[data-page="home"] .sonic-hero .hero-copy{max-width:650px}
[data-page="home"] .sonic-hero .eyebrow{color:#93a9d6}
[data-page="home"] .sonic-hero h1{max-width:690px;margin-top:14px;color:#fff;font-size:clamp(56px,6.4vw,88px);line-height:.98;letter-spacing:-.055em}
[data-page="home"] .sonic-hero h1 em{color:#83a4ff;font-style:normal;font-weight:inherit}
[data-page="home"] .sonic-hero .hero-copy>p{max-width:620px;color:#aebbd0;font-size:16px;line-height:1.86}
[data-page="home"] .sonic-hero .btn-secondary{border-color:rgba(255,255,255,.18);background:rgba(255,255,255,.045);color:#fff;backdrop-filter:blur(10px)}
[data-page="home"] .sonic-hero .btn-secondary:hover{background:rgba(255,255,255,.09)}
[data-page="home"] .sonic-hero .hero-proof span{border-color:rgba(150,177,232,.16);background:rgba(255,255,255,.045);color:#aebbd0}
[data-page="home"] .sonic-hero .console{position:relative;border:1px solid rgba(145,170,221,.20);background:rgba(13,25,43,.87);box-shadow:0 34px 90px rgba(0,0,0,.34),0 0 0 1px rgba(255,255,255,.02) inset;transform:perspective(1200px) rotateY(-2deg) rotateX(1deg);backdrop-filter:blur(18px)}
[data-page="home"] .sonic-hero .console:after{content:"LIVE SIGNAL";position:absolute;right:18px;bottom:-26px;color:#64789f;font-size:8px;font-weight:900;letter-spacing:.22em}
[data-page="home"] .sonic-hero .console-top{border-bottom-color:rgba(255,255,255,.07);background:#0d192b;color:#dbe4f5}
[data-page="home"] .sonic-hero .console-body aside{border-right-color:rgba(255,255,255,.07);background:#0b1727}
[data-page="home"] .sonic-hero .console-body aside small,[data-page="home"] .sonic-hero .console-body aside i{color:#7d8da8}
[data-page="home"] .sonic-hero .console-body aside i.active{background:#172745;color:#dbe7ff}
[data-page="home"] .sonic-hero .console-body section{background:#101c2e}
[data-page="home"] .sonic-hero .console-head h3,[data-page="home"] .sonic-hero .metric-row strong,[data-page="home"] .sonic-hero .release-card b{color:#eef4ff}
[data-page="home"] .sonic-hero .console-head small,[data-page="home"] .sonic-hero .metric-row span,[data-page="home"] .sonic-hero .release-card span{color:#8495b0}
[data-page="home"] .sonic-hero .metric-row>div,[data-page="home"] .sonic-hero .release-card{border-color:rgba(255,255,255,.07);background:#0c1828}
[data-page="home"] .sonic-waveform{display:flex;align-items:center;gap:4px;width:260px;height:48px;margin-top:30px;padding:10px 0;opacity:.92}
[data-page="home"] .sonic-waveform span{width:3px;height:70%;border-radius:99px;background:linear-gradient(to top,#416ee8,#9eb5ff);transform-origin:center;animation:sonic-bar 3.8s ease-in-out infinite}
[data-page="home"] .sonic-waveform span:nth-child(2n){height:38%;animation-delay:-.8s}[data-page="home"] .sonic-waveform span:nth-child(3n){height:92%;animation-delay:-1.7s}[data-page="home"] .sonic-waveform span:nth-child(4n){height:54%;animation-delay:-2.4s}[data-page="home"] .sonic-waveform span:nth-child(5n){height:26%;animation-delay:-3.1s}
[data-page="home"] .sonic-ticker{border-top:1px solid #142136;border-bottom:1px solid #142136;background:#091321}
[data-page="home"] .sonic-ticker-track{display:flex;align-items:center;justify-content:space-between;min-height:64px;gap:20px;color:#8b9bb7;font-size:9px;font-weight:900;letter-spacing:.18em}
[data-page="home"] .sonic-ticker-track i{position:relative;flex:1;height:1px;max-width:110px;background:#24334b}
[data-page="home"] .sonic-ticker-track i:after{content:"";position:absolute;top:-2px;left:0;width:5px;height:5px;border-radius:50%;background:#6f95ff;box-shadow:0 0 12px #6f95ff;animation:sonic-dot 6s linear infinite}
[data-page="home"] .home-choice-section{padding-top:104px;padding-bottom:104px;background:#f7f9fc}
[data-page="home"] .home-choice-section .section-head h2{font-size:clamp(40px,4.6vw,64px);letter-spacing:-.04em}
[data-page="home"] .home-product-pair{gap:1px;border-top:1px solid #dce3ed;border-bottom:1px solid #dce3ed;background:#dce3ed}
[data-page="home"] .home-product-pair article{border:0!important;border-radius:0!important;background:#f7f9fc;box-shadow:none!important}
[data-page="home"] .home-product-pair article:hover{transform:none!important;background:#fff}
[data-page="home"] .home-product-pair .visual{min-height:220px;border-radius:0;background-color:#0c1728}
[data-page="home"] .home-product-pair .visual-platform{background:radial-gradient(circle at 65% 35%,rgba(79,124,255,.25),transparent 28%),linear-gradient(135deg,#0b1525,#111f35)}
[data-page="home"] .home-product-pair .visual-api{background:linear-gradient(145deg,#07101d,#101e32)}
[data-page="home"] .home-capabilities{position:relative;overflow:hidden;padding-top:110px;padding-bottom:110px;background:#fff}
[data-page="home"] .home-capabilities:before{content:"06";position:absolute;right:4vw;top:42px;color:#f1f4f9;font-size:180px;font-weight:900;line-height:1;letter-spacing:-.08em;pointer-events:none}
[data-page="home"] .home-capabilities .section-head{position:relative;z-index:1}
[data-page="home"] .home-capabilities .feature-grid{position:relative;z-index:1;gap:0;border-top:1px solid #dfe5ee;border-left:1px solid #dfe5ee}
[data-page="home"] .home-capabilities .feature-grid article{min-height:220px;border:0;border-right:1px solid #dfe5ee;border-bottom:1px solid #dfe5ee;border-radius:0;background:#fff;box-shadow:none}
[data-page="home"] .home-capabilities .feature-grid article b{font-size:10px;letter-spacing:.14em}
[data-page="home"] .home-capabilities .feature-grid article h3{margin-top:54px;font-size:21px}
[data-page="home"] .home-audience-section{padding-top:112px;padding-bottom:112px;background:#f4f7fb}
[data-page="home"] .home-use-cases{gap:0;border-top:1px solid #d8e0eb}
[data-page="home"] .home-use-cases article{position:relative;min-height:300px;padding:30px 28px 34px;border:0;border-right:1px solid #d8e0eb;border-radius:0;background:transparent;box-shadow:none}
[data-page="home"] .home-use-cases article:last-child{border-right:0}
[data-page="home"] .home-use-cases article:after{content:"↗";position:absolute;right:24px;bottom:26px;color:#a9b4c7;font-size:16px}
[data-page="home"] .home-distribution{position:relative;overflow:hidden;background:radial-gradient(circle at 75% 30%,rgba(70,110,235,.18),transparent 24%),linear-gradient(145deg,#07111f,#0c1829)}
[data-page="home"] .home-distribution:after{content:"";position:absolute;right:-120px;top:-90px;width:520px;height:520px;border:1px solid rgba(135,164,225,.08);border-radius:50%;box-shadow:0 0 0 75px rgba(135,164,225,.025),0 0 0 150px rgba(135,164,225,.014)}
[data-page="home"] .home-distribution .container,[data-page="home"] .home-distribution .logo-marquee{position:relative;z-index:1}

/* PRODUCT — timeline, track and operational rhythm */
[data-page="product"] .sonic-product-hero{position:relative;overflow:hidden;padding-top:96px;padding-bottom:92px;background:radial-gradient(circle at 82% 24%,rgba(73,110,234,.20),transparent 30%),linear-gradient(135deg,#07111f,#0d1a2d);color:#fff}
[data-page="product"] .sonic-product-hero:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,transparent 49.8%,rgba(137,164,219,.04) 50%,transparent 50.2%);background-size:84px 100%;pointer-events:none}
[data-page="product"] .sonic-product-grid{position:absolute;left:0;right:0;bottom:88px;height:1px;background:linear-gradient(90deg,transparent,rgba(112,149,229,.26),transparent)}
[data-page="product"] .sonic-product-hero .product-hero-grid{position:relative;z-index:2;align-items:center;gap:68px}
[data-page="product"] .sonic-product-hero h1{color:#fff;font-size:clamp(52px,5.7vw,80px);line-height:1.02;letter-spacing:-.052em}
[data-page="product"] .sonic-product-hero .product-hero-lead{color:#adbad0;font-size:16px;line-height:1.85}
[data-page="product"] .sonic-product-hero .btn-secondary{border-color:rgba(255,255,255,.17);background:rgba(255,255,255,.045);color:#fff}
[data-page="product"] .sonic-product-hero .product-hero-ui{border-color:rgba(153,178,230,.18);background:#101c2e;box-shadow:0 32px 88px rgba(0,0,0,.32);transform:translateY(12px) rotate(1deg)}
[data-page="product"] .sonic-product-hero .phu-top,[data-page="product"] .sonic-product-hero .phu-body aside{background:#0b1727;border-color:rgba(255,255,255,.07)}
[data-page="product"] .sonic-product-hero .phu-main{background:#101c2d}
[data-page="product"] .sonic-product-hero .phu-head strong,[data-page="product"] .sonic-product-hero .phu-list b,[data-page="product"] .sonic-product-hero .phu-metrics b{color:#eef4ff}
[data-page="product"] .sonic-product-hero .phu-metrics>div,[data-page="product"] .sonic-product-hero .phu-list>div{border-color:rgba(255,255,255,.07);background:#0c1828}
[data-page="product"] .product-signal-rail{position:relative;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:0;max-width:610px;margin-top:34px;border-top:1px solid #2b3b55}
[data-page="product"] .product-signal-rail:before{content:"";position:absolute;left:0;top:-1px;width:25%;height:1px;background:#6f95ff;box-shadow:0 0 12px rgba(111,149,255,.7)}
[data-page="product"] .product-signal-rail>div{position:relative;padding:18px 15px 0 0}
[data-page="product"] .product-signal-rail>div:before{content:"";position:absolute;top:-4px;left:0;width:7px;height:7px;border:2px solid #52627d;border-radius:50%;background:#0a1525}
[data-page="product"] .product-signal-rail>div.active:before{border-color:#7b9cff;background:#7b9cff;animation:sonic-breathe 3.6s ease-in-out infinite}
[data-page="product"] .product-signal-rail span{display:block;margin-bottom:8px;color:#637594;font-size:8px;font-weight:900;letter-spacing:.12em}
[data-page="product"] .product-signal-rail b{display:block;color:#dce6f7;font-size:10px;letter-spacing:.09em}
[data-page="product"] .product-signal-rail small{display:block;margin-top:5px;color:#6f809d;font-size:9px;line-height:1.45}
[data-page="product"] .product-subnav{border-bottom:1px solid #e0e6ee;background:rgba(255,255,255,.94);backdrop-filter:blur(18px)}
[data-page="product"] .product-catalog{position:relative;overflow:hidden}
[data-page="product"] .product-catalog:before{content:"CATALOG";position:absolute;left:-12px;top:28px;color:#f1f4f9;font-size:118px;font-weight:900;line-height:1;letter-spacing:-.06em;pointer-events:none}
[data-page="product"] .product-catalog>.container{position:relative;z-index:1}
[data-page="product"] .product-catalog-workbench{background:#f5f8fc}
[data-page="product"] .product-release{position:relative;overflow:hidden;background:radial-gradient(circle at 78% 18%,rgba(78,113,229,.16),transparent 25%),linear-gradient(145deg,#07111f,#0d192a);color:#fff}
[data-page="product"] .product-release:before{content:"TIMELINE";position:absolute;right:3vw;top:38px;color:rgba(255,255,255,.025);font-size:120px;font-weight:900;letter-spacing:-.06em}
[data-page="product"] .product-release .section-head h2,[data-page="product"] .product-release .section-head p{color:#fff}
[data-page="product"] .product-release .section-head p{color:#9cacC3}
[data-page="product"] .product-release .release-steps{position:relative;gap:0;border-top:1px solid #2b3a52}
[data-page="product"] .product-release .release-steps>div{min-height:112px;padding:23px 12px 12px 0;border:0;background:transparent}
[data-page="product"] .product-release .release-steps>div:before{content:"";position:absolute;top:-5px;width:9px;height:9px;border:2px solid #52647f;border-radius:50%;background:#0b1626}
[data-page="product"] .product-release .release-steps>div.done:before{border-color:#6f95ff;background:#6f95ff}
[data-page="product"] .product-release .release-steps>div.active:before{border-color:#8eaaff;background:#8eaaff;box-shadow:0 0 16px rgba(111,149,255,.8);animation:sonic-breathe 3s ease-in-out infinite}
[data-page="product"] .product-release .release-steps b{color:#627797;font-size:9px;letter-spacing:.1em}
[data-page="product"] .product-release .release-steps span{display:block;margin-top:34px;color:#cfd9ea;font-size:11px}
[data-page="product"] .product-release .workspace-ui{border-color:rgba(255,255,255,.08);background:#0c1828}
[data-page="product"] .product-release .wu-top,[data-page="product"] .product-release .wu-table>div,[data-page="product"] .product-release .admin-status{border-color:rgba(255,255,255,.07)}
[data-page="product"] .product-release .workspace-note{color:#778aa8}
[data-page="product"] .product-distribution{padding-top:112px;padding-bottom:112px;background:#f7f9fc}
[data-page="product"] .product-distribution .distribution-proof strong{font-size:50px;letter-spacing:-.05em}

/* SOLUTIONS — patch bay / signal routing */
[data-page="solutions"] .sonic-solutions-hero{position:relative;overflow:hidden;padding-top:104px;padding-bottom:92px;background:radial-gradient(circle at 75% 30%,rgba(75,113,234,.23),transparent 29%),linear-gradient(140deg,#07111f,#0e1c31);color:#fff}
[data-page="solutions"] .sonic-solutions-hero:before{content:"";position:absolute;inset:0;background:linear-gradient(rgba(130,158,214,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(130,158,214,.045) 1px,transparent 1px);background-size:64px 64px;mask-image:linear-gradient(to bottom,rgba(0,0,0,.95),transparent)}
[data-page="solutions"] .sonic-solutions-hero .container{position:relative;z-index:1}
[data-page="solutions"] .sonic-solutions-hero .eyebrow{color:#8fa6d3}
[data-page="solutions"] .sonic-solutions-hero h1{max-width:900px;color:#fff;font-size:clamp(50px,5.8vw,78px);line-height:1.04;letter-spacing:-.05em}
[data-page="solutions"] .sonic-solutions-hero p{color:#aab8ce}
[data-page="solutions"] .sonic-solutions-hero .solutions-hero-proof span{border-color:rgba(149,176,230,.16);background:rgba(255,255,255,.045);color:#b4c0d4}
[data-page="solutions"] .solutions-route-hero{display:grid;grid-template-columns:minmax(0,1fr) 90px minmax(0,1.1fr) 90px minmax(0,1fr);align-items:center;gap:0;margin-top:48px;padding-top:28px;border-top:1px solid rgba(141,168,223,.16)}
[data-page="solutions"] .route-unit{padding:16px 18px;border:1px solid rgba(140,167,223,.14);background:rgba(255,255,255,.035);backdrop-filter:blur(10px)}
[data-page="solutions"] .route-unit.core{border-color:rgba(111,149,255,.42);background:rgba(56,91,190,.16);box-shadow:0 0 36px rgba(70,108,225,.10)}
[data-page="solutions"] .route-unit small{display:block;margin-bottom:7px;color:#667b9f;font-size:8px;font-weight:900;letter-spacing:.14em}
[data-page="solutions"] .route-unit b{display:block;color:#dbe6f8;font-size:12px;line-height:1.55}
[data-page="solutions"] .solutions-route-hero>i{position:relative;height:1px;background:#33445f}
[data-page="solutions"] .solutions-route-hero>i:after{content:"";position:absolute;top:-2px;left:0;width:5px;height:5px;border-radius:50%;background:#7d9dff;box-shadow:0 0 12px #7d9dff;animation:sonic-dot 5.5s linear infinite}
[data-page="solutions"] .scenario-card-grid{gap:0;border-top:1px solid #dce3ed;border-left:1px solid #dce3ed}
[data-page="solutions"] .scenario-card{min-height:270px;padding:34px 34px 38px;border:0;border-right:1px solid #dce3ed;border-bottom:1px solid #dce3ed;border-radius:0;background:#fff;box-shadow:none}
[data-page="solutions"] .scenario-card:hover{transform:none;background:#f8faff;box-shadow:none}
[data-page="solutions"] .scenario-card:before{position:absolute;left:30px;bottom:22px;color:#eef2f7;font-size:76px;font-weight:900;line-height:1;letter-spacing:-.06em;z-index:0}
[data-page="solutions"] .scenario-card:nth-child(1):before{content:"01"}[data-page="solutions"] .scenario-card:nth-child(2):before{content:"02"}[data-page="solutions"] .scenario-card:nth-child(3):before{content:"03"}[data-page="solutions"] .scenario-card:nth-child(4):before{content:"04"}
[data-page="solutions"] .scenario-card>*{position:relative;z-index:1}
[data-page="solutions"] .solutions-architecture-section{padding-top:112px;padding-bottom:112px;background:radial-gradient(circle at 70% 15%,rgba(72,108,223,.14),transparent 24%),linear-gradient(145deg,#07111f,#0c1829);color:#fff}
[data-page="solutions"] .solutions-architecture-section .visual-section-head h2{color:#fff}
[data-page="solutions"] .solutions-architecture-section .visual-section-head p{color:#91a1b9}
[data-page="solutions"] .architecture-studio{border-color:rgba(145,170,220,.15);background:#0b1727;box-shadow:0 26px 70px rgba(0,0,0,.25)}
[data-page="solutions"] .architecture-tabs{border-bottom-color:rgba(255,255,255,.07);background:#091421}
[data-page="solutions"] .architecture-tabs button{color:#71819b}
[data-page="solutions"] .architecture-tabs button.active{background:#14233b;color:#dce7fa}
[data-page="solutions"] .architecture-canvas{position:relative;background:linear-gradient(rgba(130,158,214,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(130,158,214,.035) 1px,transparent 1px),#0d1929;background-size:34px 34px}
[data-page="solutions"] .architecture-panel>i{color:#637da7}
[data-page="solutions"] .arch-node{border-color:rgba(145,170,220,.14);background:#0a1524;box-shadow:none}
[data-page="solutions"] .arch-node small{color:#607593}
[data-page="solutions"] .arch-node b{color:#d7e2f3}
[data-page="solutions"] .arch-node span{color:#71839f}
[data-page="solutions"] .arch-node.primary{border-color:rgba(111,149,255,.45);background:#112445}
[data-page="solutions"] .arch-node.core{border-color:rgba(124,151,220,.28);background:#101f35}
[data-page="solutions"] .architecture-legend{border-top-color:rgba(255,255,255,.07);background:#091421;color:#72839e}

/* Responsive sonic system */
@media(max-width:1100px){
  [data-page="home"] .sonic-hero .hero-grid,[data-page="product"] .sonic-product-hero .product-hero-grid{gap:38px}
  [data-page="solutions"] .solutions-route-hero{grid-template-columns:1fr 46px 1.1fr 46px 1fr}
}
@media(max-width:900px){
  [data-page="home"] .sonic-hero{min-height:0;padding-top:74px}
  [data-page="home"] .sonic-hero .console{transform:none}
  [data-page="home"] .sonic-ticker-track{overflow:hidden;justify-content:flex-start}
  [data-page="home"] .sonic-ticker-track span{white-space:nowrap}
  [data-page="home"] .home-use-cases article{min-height:250px}
  [data-page="product"] .sonic-product-hero .product-hero-ui{transform:none}
  [data-page="solutions"] .solutions-route-hero{grid-template-columns:1fr;gap:10px}
  [data-page="solutions"] .solutions-route-hero>i{width:1px;height:28px;margin-left:22px}
  [data-page="solutions"] .solutions-route-hero>i:after{animation:none;top:12px;left:-2px}
}
@media(max-width:680px){
  [data-page="home"] .sonic-hero{padding-top:60px;padding-bottom:58px}
  [data-page="home"] .sonic-hero h1{font-size:48px;line-height:1.02}
  [data-page="home"] .sonic-waveform{width:210px}
  [data-page="home"] .sonic-ticker-track{min-height:52px;gap:12px}
  [data-page="home"] .sonic-ticker-track i{min-width:30px}
  [data-page="home"] .home-choice-section,[data-page="home"] .home-capabilities,[data-page="home"] .home-audience-section{padding-top:72px;padding-bottom:72px}
  [data-page="home"] .home-capabilities:before{font-size:110px;right:10px}
  [data-page="home"] .home-product-pair{display:block;border-left:1px solid #dce3ed;border-right:1px solid #dce3ed}
  [data-page="home"] .home-product-pair article+article{border-top:1px solid #dce3ed!important}
  [data-page="home"] .home-use-cases article{min-height:0;border-right:0;border-bottom:1px solid #d8e0eb}
  [data-page="product"] .sonic-product-hero{padding-top:66px;padding-bottom:62px}
  [data-page="product"] .sonic-product-hero h1{font-size:46px}
  [data-page="product"] .product-signal-rail{grid-template-columns:repeat(2,1fr);gap:18px 0;border-top:0}
  [data-page="product"] .product-signal-rail:before{display:none}
  [data-page="product"] .product-signal-rail>div{border-top:1px solid #2b3b55}
  [data-page="product"] .product-catalog:before{font-size:72px;top:18px}
  [data-page="product"] .product-release:before{font-size:70px}
  [data-page="product"] .product-release .release-steps{border-top:0;border-left:1px solid #2b3a52}
  [data-page="product"] .product-release .release-steps>div{min-height:0;padding:10px 0 20px 22px}
  [data-page="product"] .product-release .release-steps>div:before{top:14px;left:-5px}
  [data-page="product"] .product-release .release-steps span{margin-top:6px}
  [data-page="solutions"] .sonic-solutions-hero{padding-top:68px;padding-bottom:62px}
  [data-page="solutions"] .sonic-solutions-hero h1{font-size:44px}
  [data-page="solutions"] .solutions-route-hero{margin-top:34px}
  [data-page="solutions"] .scenario-card-grid{grid-template-columns:1fr}
  [data-page="solutions"] .scenario-card{min-height:230px}
  [data-page="solutions"] .solutions-architecture-section{padding-top:76px;padding-bottom:76px}
}
'''

css += SONIC_CSS

# Sanity checks: only these three public pages should opt in.
assert html.count('sonic-home') == 1
assert html.count('sonic-product') >= 1
assert html.count('sonic-solutions') >= 1
assert 'Enterprise Sonic Infrastructure v1' in css

INDEX.write_text(html, encoding='utf-8')
STYLES.write_text(css, encoding='utf-8')
print('Applied Sonic Infrastructure v1 to Home, Product and Solutions.')
