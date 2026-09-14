from pathlib import Path
import re
import sys

repo = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
root = repo / "03-enterprise/prototype-v4"
index = root / "index.html"
styles = root / "styles.css"
base = root / "styles-base.css"
readme = root / "README.md"

s = index.read_text()


def rep(old, new, required=False):
    global s
    if required and old not in s:
        raise SystemExit(f"missing required source: {old[:90]}")
    s = s.replace(old, new)


# Progressive enhancement: content remains visible if JavaScript is unavailable.
rep(
    '<meta name="viewport" content="width=device-width,initial-scale=1">',
    '<meta name="viewport" content="width=device-width,initial-scale=1">\n<script>document.documentElement.classList.add(\'js\')</script>',
    True,
)

# Public product vocabulary.
rep("自有品牌发行系统", "自有品牌发行平台")
rep("年费对应企业系统、版本容量、产品能力及服务等级", "年费对应企业发行平台、版本容量、产品能力及服务等级")

for old, new in {
    "专业的 CP 分账与结算": "合作方分账与结算",
    "计算到每个 CP": "计算到每个合作方",
    "每个 CP 的本期应结算结果": "每个合作方的本期应结算结果",
    "参与分账 CP": "参与分账合作方",
    "CP 分账明细": "合作方分账明细",
    "CP / 分账规则": "合作方 / 分账规则",
    "按照 CP、内容和合作关系配置分账比例": "按照合作方、内容和合作关系配置分账比例",
    "按 CP、内容和合作关系配置分成比例": "按合作方、内容和合作关系配置分成比例",
    "CP 结算单": "合作方结算单",
    "为每个 CP 生成独立结算单": "为每个合作方生成独立结算单",
}.items():
    rep(old, new)

# CTA system.
rep("申请免费试用", "申请企业方案")
rep(">申请企业版</a>", ">申请企业方案</a>")
rep(">申请发行 API</a>", ">申请 API 接入</a>")
rep(">查看 API 文档</a>", ">查看开发者指南</a>")
rep(">API 文档</a>", ">开发者指南</a>")

# Carry intent from Pricing/API into Apply.
s = re.sub(r'href="/enterprise/apply"([^>]*)>申请基础版</a>', r'href="/enterprise/apply?plan=basic"\1>申请基础版</a>', s)
s = re.sub(r'href="/enterprise/apply"([^>]*)>申请专业版</a>', r'href="/enterprise/apply?plan=professional"\1>申请专业版</a>', s)
s = re.sub(r'href="/enterprise/apply"([^>]*)>联系商务</a>', r'href="/enterprise/apply?plan=enterprise"\1>联系商务</a>', s)
s = re.sub(r'href="/enterprise/apply"([^>]*)>申请 API 接入</a>', r'href="/enterprise/apply?solution=api"\1>申请 API 接入</a>', s)

# Product page: move business copy out of CSS pseudo-elements and into HTML.
rep(
    '<h2><span class="title-line">服务更多客户，</span><span class="title-line">管理更大规模曲库</span></h2></div><p>随着业务增长，可统一服务更多客户与厂牌，并通过批量导入、历史曲库迁移和多种对接方式降低重复操作。</p>',
    '<h2>业务规模扩大，<br>运营依然清晰</h2></div><p>随着客户、曲库和发行量增长，通过多客户管理、批量处理和标准化数据接入，减少重复操作，让团队在更大业务规模下保持稳定运营。</p>',
    True,
)

old_scale = '<div class="scale-capabilities"><div><b>Excel 批量处理</b><span>批量整理和导入内容及发行资料。</span></div><div><b>历史曲库导入</b><span>将已有艺人、专辑、歌曲和文件迁移到平台。</span></div><div><b>批量数据与文件处理</b><span>减少大规模内容进入时的重复人工操作。</span></div><div><b>多客户、多账号</b><span>支持更多客户和团队成员共同使用。</span></div><div><b>多种接入方式</b><span>可通过 API、SFTP、XML 或 DDEX 连接现有产品与数据流程。</span></div><a class="text-link" href="/enterprise/api" data-route>了解发行 API →</a></div>'
new_scale = '<div class="scale-capabilities"><div><b>多客户统一运营</b><span>不同合作客户、厂牌和版权方独立管理，团队统一处理。</span></div><div><b>大规模曲库批量处理</b><span>支持历史曲库迁移，以及内容、文件和发行资料批量导入与处理。</span></div><div><b>连接现有业务流程</b><span>通过 API、SFTP、XML 或 DDEX 接入已有产品与数据流程。</span></div><a class="text-link" href="/enterprise/api" data-route>了解发行 API →</a></div>'
rep(old_scale, new_scale, True)

rep(
    '<span class="eyebrow">FROM SETUP TO LAUNCH</span><h2>从配置品牌，到正式开展业务</h2><p>无论是新建发行平台，还是迁移现有业务，都可以按照实际情况逐步上线。</p>',
    '<span class="eyebrow">FROM SETUP TO LAUNCH</span><h2>从配置到正式运营，按步骤完成上线</h2><p>新建发行平台或迁移现有业务，都可按照清晰的上线流程完成品牌配置、业务导入、发行验证和正式运营。</p>',
    True,
)

old_steps = '<div class="launch-steps reveal"><article><b>01</b><h3>配置品牌</h3><p>设置企业品牌、Logo、客户入口和域名。</p></article><article><b>02</b><h3>建立客户和团队</h3><p>创建合作客户、厂牌和内部运营账号。</p></article><article><b>03</b><h3>导入曲库</h3><p>从新发行开始，或逐步迁移已有音乐内容。</p></article><article><b>04</b><h3>跑通发行流程</h3><p>完成内容提交、审核、平台发行和状态验证。</p></article><article><b>05</b><h3>正式运营</h3><p>客户通过发行门户提交内容，团队持续完成审核、发行和后续运营。</p></article></div>'
new_steps = '<div class="launch-steps reveal"><article><b>01</b><h3>配置品牌</h3><p>设置企业品牌、Logo、客户入口和域名。</p></article><article><b>02</b><h3>导入业务</h3><p>建立合作客户与团队，导入已有曲库和发行资料。</p></article><article><b>03</b><h3>完成发行验证</h3><p>验证内容审核、渠道提交、状态回传和上线流程。</p></article><article><b>04</b><h3>正式运营</h3><p>客户开始提交内容，团队进入持续发行运营。</p></article></div>'
rep(old_steps, new_steps, True)

rep(
    '<span class="eyebrow light">BUILT FOR MUSIC BUSINESSES</span><h2>为长期经营发行业务而设计</h2><p>客户从这里提交音乐，团队从这里完成发行。曲库、平台状态、数据和收入都留在同一套业务体系中。</p>',
    '<span class="eyebrow light">GET STARTED</span><h2>搭建自有品牌音乐发行平台</h2><p>覆盖客户入口、曲库管理、发行运营、渠道上线和合作方分账结算，建立可持续运营的企业发行能力。</p>',
    True,
)

# Developers: professional guide language, mobile navigation, and conversion path.
rep(
    '<section class="dev-shell"><aside class="dev-side">',
    '<section class="dev-shell"><button class="dev-mobile-nav" type="button" aria-expanded="false" aria-controls="developer-nav"><span>开发者指南目录</span><b>☰</b></button><aside class="dev-side" id="developer-nav">',
    True,
)
rep('<div class="dev-side-title">API 文档</div>', '<div class="dev-side-title">开发者中心</div>')
rep(
    '<span class="eyebrow">API DOCUMENTATION</span><h1>星球发行 API 文档</h1><p class="lead">用于技术团队评估接口范围、准备接入并了解发行流程、状态回调和运行方式。</p><div class="dev-notice"><b>当前页面为企业版产品 Demo。</b><span>正式接口名称、参数、Base URL 与鉴权细节，以星球发行 API 正式开放文档为准。</span></div>',
    '<span class="eyebrow">DEVELOPER GUIDE</span><h1>发行 API 开发者指南</h1><p class="lead">面向技术团队提供接入准备、资源模型、发行流程、Webhook、运行与排障说明，用于企业接入评估与技术联调。</p><div class="dev-actions"><a class="btn btn-primary" href="/enterprise/apply?solution=api" data-route>申请 API 接入</a><a class="btn btn-secondary" href="/enterprise/api" data-route>返回发行 API</a></div><div class="dev-notice"><b>生产接入信息按项目开通</b><span>接口地址、凭证、权限范围与环境配置将在企业合作与技术联调阶段提供；资源模型与接入流程以当前开发者指南为基础。</span></div>',
    True,
)

# Apply: context inheritance and readable functional type.
rep(
    '</div>\n        <form class="apply-form" id="apply-form">',
    '</div>\n        <div class="apply-context" id="apply-context" hidden></div>\n        <form class="apply-form" id="apply-form">',
    True,
)
rep("Demo 页面暂不提交真实业务数据。", "原型环境：提交不会发送真实业务数据。")
rep("当前为产品 Demo，不会实际发送信息。", "当前为原型环境，不会实际发送信息。")

# Footer trust/terminology.
rep(
    "帮助音乐企业搭建自有品牌发行平台，或通过 API 将发行能力接入现有产品。",
    "面向音乐企业提供自有品牌发行平台与发行 API，覆盖曲库、发行、平台状态、数据和收入结算等核心业务。",
)
rep(
    '<div class="container footer-bottom">© 2026 看见音乐</div>',
    '<div class="container footer-bottom"><span>© 2026 看见音乐</span><span class="footer-legal"><a href="https://www.kanjian.com/privacy" target="_blank" rel="noreferrer">隐私政策</a><a href="https://www.kanjian.com/contact" target="_blank" rel="noreferrer">联系我们</a></span></div>',
    True,
)

rep(
    '[data-page="apply"] .field-label{display:flex;align-items:center;justify-content:space-between;gap:8px;margin:0 0 8px;color:#4f5d73;font-size:11px;font-weight:760}',
    '[data-page="apply"] .field-label{display:flex;align-items:center;justify-content:space-between;gap:8px;margin:0 0 8px;color:#4f5d73;font-size:12px;font-weight:760}',
)
rep(
    '[data-page="apply"] .field-label em{color:#a0a9b7;font-style:normal;font-size:9px;font-weight:600}',
    '[data-page="apply"] .field-label em{color:#98a2b2;font-style:normal;font-size:11px;font-weight:600}',
)
rep(
    '[data-page="apply"] .select-menu button{width:100%;display:flex;align-items:center;min-height:40px;padding:9px 10px;border:0;border-radius:8px;background:transparent;color:#526075;text-align:left;font-size:12px;cursor:pointer}',
    '[data-page="apply"] .select-menu button{width:100%;display:flex;align-items:center;min-height:42px;padding:9px 10px;border:0;border-radius:10px;background:transparent;color:#526075;text-align:left;font-size:13px;cursor:pointer}',
)
rep(
    '[data-page="apply"] .success small{display:block;margin-top:13px;color:#8a9c92;font-size:9px}',
    '[data-page="apply"] .success small{display:block;margin-top:13px;color:#8a9c92;font-size:11px}',
)
rep(
    '[data-page="apply"] .apply-form{padding:0;border:0;border-radius:0;background:transparent;box-shadow:none}',
    '[data-page="apply"] .apply-context{display:inline-flex;align-items:center;margin:-7px 0 22px;padding:7px 10px;border:1px solid #d9e3ff;border-radius:999px;background:#f3f6ff;color:#3157c8;font-size:12px;font-weight:760}\n[data-page="apply"] .apply-context[hidden]{display:none}\n[data-page="apply"] .apply-form{padding:0;border:0;border-radius:0;background:transparent;box-shadow:none}',
    True,
)

# Router + section navigation + Apply context inheritance.
old_router = "function render(path,hash=''){const page=routes[path]||'home';document.querySelectorAll('.page').forEach(el=>el.classList.toggle('active',el.dataset.page===page));setNav(page);closeMenu();requestAnimationFrame(()=>{revealVisible();if(hash)document.querySelector(hash)?.scrollIntoView();else scrollTo(0,0)})}"
new_router = '''function applyRouteContext(){const page=document.querySelector('[data-page="apply"]');if(!page)return;const params=new URLSearchParams(location.search),plan=params.get('plan'),solution=params.get('solution'),badge=page.querySelector('#apply-context');let value='',label='';if(solution==='api'){value='api';label='已选择：发行 API'}else if(plan){value='platform';label='已选择：'+({basic:'基础版',professional:'专业版',enterprise:'企业版'}[plan]||'自有品牌发行平台')}if(value){const radio=page.querySelector('input[name="solution"][value="'+value+'"]');if(radio)radio.checked=true}if(badge){badge.textContent=label;badge.hidden=!label}}
function syncSectionNav(){document.querySelectorAll('.product-subnav,.api-subnav').forEach(nav=>{const links=[...nav.querySelectorAll('a[href^="#"]')],targets=links.map(a=>document.querySelector(a.getAttribute('href'))).filter(Boolean);if(!targets.length)return;const update=()=>{const y=scrollY+150;let current=targets[0];targets.forEach(t=>{if(t.offsetTop<=y)current=t});links.forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#'+current.id))};update();if(!nav.dataset.spy){nav.dataset.spy='1';addEventListener('scroll',update,{passive:true})}})}
function render(path,hash=''){const page=routes[path]||'home';document.querySelectorAll('.page').forEach(el=>el.classList.toggle('active',el.dataset.page===page));setNav(page);closeMenu();applyRouteContext();requestAnimationFrame(()=>{revealVisible();syncSectionNav();if(hash)document.querySelector(hash)?.scrollIntoView();else scrollTo(0,0)})}'''
rep(old_router, new_router, True)
rep("history.pushState({},'',u.pathname+u.hash);render(u.pathname,u.hash);", "history.pushState({},'',u.pathname+u.search+u.hash);render(u.pathname,u.hash);", True)

rep(
    "const toggle=document.querySelector('.nav-toggle'),nav=document.querySelector('.nav-links');if(toggle&&nav)toggle.onclick=()=>{const open=nav.classList.toggle('open');toggle.textContent=open?'×':'☰';toggle.setAttribute('aria-expanded',open)};",
    "const toggle=document.querySelector('.nav-toggle'),nav=document.querySelector('.nav-links');if(toggle&&nav)toggle.onclick=()=>{const open=nav.classList.toggle('open');toggle.textContent=open?'×':'☰';toggle.setAttribute('aria-expanded',open)};const devToggle=document.querySelector('.dev-mobile-nav'),devNav=document.querySelector('.dev-side');if(devToggle&&devNav)devToggle.onclick=()=>{const open=devNav.classList.toggle('open');devToggle.setAttribute('aria-expanded',String(open));devToggle.querySelector('b').textContent=open?'×':'☰'};",
    True,
)

index.write_text(s)

# Remove CSS-authored business copy from Product.
css = styles.read_text()
for pat in [
    r'^\[data-page="product"\] \.product-scale \.section-head h2 \.title-line\{[^\n]*\}\n?',
    r'^\[data-page="product"\] \.product-scale \.section-head h2:before\{[^\n]*\}\n?',
    r'^\[data-page="product"\] \.product-scale \.section-head>p\{font-size:0;line-height:0\}\n?',
    r'^\[data-page="product"\] \.product-scale \.section-head>p:before\{[^\n]*\}\n?',
    r'^\[data-page="product"\] \.product-scale \.scale-capabilities>div:nth-child\(2\),[^\n]*\n?',
    r'^\[data-page="product"\] \.product-scale \.scale-capabilities>div:nth-child\(4\)\{order:1\}\n?',
    r'^\[data-page="product"\] \.product-scale \.scale-capabilities>div:nth-child\(1\)\{order:2\}\n?',
    r'^\[data-page="product"\] \.product-scale \.scale-capabilities>div:nth-child\(5\)\{order:3\}\n?',
    r'^\[data-page="product"\] \.product-scale \.scale-capabilities>div b\{display:block;margin-bottom:10px;font-size:0\}\n?',
    r'^\[data-page="product"\] \.product-scale \.scale-capabilities>div span\{display:block;font-size:0;line-height:0\}\n?',
    r'^\[data-page="product"\] \.product-scale \.scale-capabilities>div:nth-child\([^\n]*:before\{content:[^\n]*\n?',
    r'^\[data-page="product"\] \.product-launch \.section-head h2\{font-size:0;line-height:0\}\n?',
    r'^\[data-page="product"\] \.product-launch \.section-head h2:before\{[^\n]*\}\n?',
    r'^\[data-page="product"\] \.product-launch \.section-head>p\{font-size:0;line-height:0\}\n?',
    r'^\[data-page="product"\] \.product-launch \.section-head>p:before\{[^\n]*\}\n?',
    r'^\[data-page="product"\] \.product-launch \.launch-steps article:nth-child\(5\)\{display:none\}\n?',
    r'^\[data-page="product"\] \.product-launch \.launch-steps article:nth-child\([^\n]*font-size:0[^\n]*\n?',
    r'^\[data-page="product"\] \.product-launch \.launch-steps article:nth-child\([^\n]*:before\{content:[^\n]*\n?',
    r'^\[data-page="product"\] \.product-final-panel \.eyebrow\{font-size:0\}\n?',
    r'^\[data-page="product"\] \.product-final-panel \.eyebrow:before\{[^\n]*\}\n?',
    r'^\[data-page="product"\] \.product-final-panel h2\{font-size:0;line-height:0\}\n?',
    r'^\[data-page="product"\] \.product-final-panel h2:before\{[^\n]*\}\n?',
    r'^\[data-page="product"\] \.product-final-panel p\{font-size:0;line-height:0\}\n?',
    r'^\[data-page="product"\] \.product-final-panel p:before\{[^\n]*\}\n?',
]:
    css = re.sub(pat, "", css, flags=re.M)

if '[data-page="product"] .product-scale .scale-capabilities>div b{display:block;margin-bottom:10px;font-size:13px}' not in css:
    css += '\n[data-page="product"] .product-scale .scale-capabilities>div b{display:block;margin-bottom:10px;font-size:13px}\n'
if '[data-page="product"] .product-scale .scale-capabilities>div span{display:block;color:#748095;font-size:11px;line-height:1.65}' not in css:
    css += '[data-page="product"] .product-scale .scale-capabilities>div span{display:block;color:#748095;font-size:11px;line-height:1.65}\n'
css = css.replace(
    '[data-page="product"] .product-scale .scale-capabilities .text-link{grid-column:1/-1;order:4;',
    '[data-page="product"] .product-scale .scale-capabilities .text-link{grid-column:1/-1;',
)

system_css = '''
/* Enterprise system cleanup: shared interaction and navigation rules */
[data-page="product"] .product-subnav{top:72px}
[data-page="product"] .section[id]{scroll-margin-top:128px}
[data-page="product"] .product-subnav a,[data-page="api"] .api-subnav a{border-bottom:2px solid transparent}
[data-page="product"] .product-subnav a.active,[data-page="api"] .api-subnav a.active{color:#2149d8;border-bottom-color:#315ff4}
.dev-mobile-nav{display:none}
.dev-actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:24px}
.footer-bottom{display:flex;align-items:center;justify-content:space-between;gap:20px}
.footer-legal{display:flex;gap:18px}.footer-legal a{color:#8d98a8}.footer-legal a:hover{color:#fff}
@media(max-width:820px){[data-page="product"] .product-subnav{top:64px}[data-page="product"] .section[id]{scroll-margin-top:116px}.dev-mobile-nav{display:flex;position:sticky;top:64px;z-index:30;width:100%;align-items:center;justify-content:space-between;padding:13px 20px;border:0;border-bottom:1px solid #e5e9f0;background:rgba(255,255,255,.97);color:#26334b;font-size:12px;font-weight:800;backdrop-filter:blur(14px)}.dev-mobile-nav b{font-size:16px}.dev-side{display:none!important}.dev-side.open{display:flex!important;position:sticky;top:108px;z-index:29;height:auto;max-height:calc(100vh - 108px);background:#fff}.footer-bottom{align-items:flex-start;flex-direction:column}}
@media(max-width:560px){[data-page="product"] .product-subnav{top:64px}.footer-legal{flex-wrap:wrap}}
'''
if "Enterprise system cleanup: shared interaction" not in css:
    css += system_css
styles.write_text(css)

# Base design tokens + safe reveal behavior.
b = base.read_text()
b = b.replace(
    "--green:#20a36a;--max:1220px;--radius:18px;",
    "--green:#20a36a;--max:1220px;--radius:18px;--radius-control:10px;--radius-card:16px;--radius-panel:22px;--text-secondary:#687487;--text-tertiary:#8d98a8;--shadow-card:0 12px 32px rgba(26,42,82,.05);--shadow-panel:0 24px 64px rgba(26,42,82,.10);",
)
b = b.replace(
    ".reveal{opacity:0;transform:translateY(16px);transition:.55s ease}.reveal.in{opacity:1;transform:none}",
    ".reveal{opacity:1;transform:none}.js .reveal{opacity:0;transform:translateY(16px);transition:.55s ease}.js .reveal.in{opacity:1;transform:none}",
)
b = b.replace(
    ".btn{display:inline-flex;align-items:center;justify-content:center;border-radius:10px;",
    ".btn{display:inline-flex;align-items:center;justify-content:center;border-radius:var(--radius-control);",
)
b = b.replace("border-radius:16px;padding:26px;background:#fff", "border-radius:var(--radius-card);padding:26px;background:#fff")
b = b.replace("border-radius:16px;padding:24px", "border-radius:var(--radius-card);padding:24px")
b = b.replace("border-radius:18px;padding:28px;background:#fff", "border-radius:var(--radius-card);padding:28px;background:#fff")
b = b.replace(".compare{border:1px solid var(--line);border-radius:18px;", ".compare{border:1px solid var(--line);border-radius:var(--radius-card);")
b = b.replace(".api-price-card{margin-top:18px;border:1px solid #dce3ed;border-radius:18px;", ".api-price-card{margin-top:18px;border:1px solid #dce3ed;border-radius:var(--radius-card);")
b = b.replace(".dev-notice{border:1px solid #dce4f7;background:#f5f8ff;border-radius:14px;", ".dev-notice{border:1px solid #dce4f7;background:#f5f8ff;border-radius:var(--radius-card);")
b = b.replace(
    "@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.reveal{opacity:1;transform:none;transition:none}",
    "@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.js .reveal{opacity:1;transform:none;transition:none}",
)
base.write_text(b)

# README as source of truth.
r = readme.read_text()
r = r.replace("用自己的品牌快速搭建音乐发行系统", "以自有品牌快速搭建音乐发行平台")
r = r.replace("1. 自有品牌发行系统", "1. 自有品牌发行平台")
r = r.replace("- White Label → 自有品牌", "- White Label → 自有品牌发行平台")
if "## CTA 规则" not in r:
    r += '''
## CTA 规则

- 全站通用主 CTA：`申请企业方案`
- API 场景主 CTA：`申请 API 接入`
- Pricing 版本卡：`申请基础版` / `申请专业版` / `联系商务`
- Apply 表单提交：`提交企业咨询`
- 不使用“免费试用”，除非产品实际提供无需商务审核即可进入的试用环境。

## 术语补充

- 官网产品名统一使用“自有品牌发行平台”，不与“自有品牌发行系统”混用。
- 对外商业页面优先使用“合作方 / 合作客户”，`CP` 仅允许出现在内部产品或技术语境。
- “音乐平台”用于市场与能力描述；“渠道”用于发行操作和 `¥1 / 首 / 渠道` 的计费口径。
- Developer 页面统一称“开发者指南 / 开发者中心”，不在非正式 API Reference 页面使用“正式 API 文档”的表达。
'''
readme.write_text(r)

# Guardrails.
final = index.read_text()
forbidden = ["申请免费试用", "自有品牌发行系统", "专业的 CP 分账与结算", "当前页面为企业版产品 Demo。"]
leftovers = [x for x in forbidden if x in final]
if leftovers:
    raise SystemExit("forbidden enterprise copy remains: " + ", ".join(leftovers))
if "u.pathname+u.search+u.hash" not in final:
    raise SystemExit("router query preservation missing")
if 'id="apply-context"' not in final:
    raise SystemExit("apply context badge missing")
if "开发者指南目录" not in final:
    raise SystemExit("mobile developer nav missing")
