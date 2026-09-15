from pathlib import Path

index_path = Path('03-enterprise/prototype-v4/index.html')
styles_path = Path('03-enterprise/prototype-v4/styles.css')

html = index_path.read_text(encoding='utf-8')
start = html.index('<section class="page" data-page="solutions">')
end = html.index('<section class="page" data-page="pricing">', start)
block = html[start:end]

replacements = {
    '<small>BRANDED PLATFORM</small>': '<small>平台方案</small>',
    '<div class="solution-mode-card api"><span class="mode-no">02</span><small>DISTRIBUTION API</small>': '<div class="solution-mode-card api"><span class="mode-no">02</span><small>接口方案</small>',
    '<div class="solution-flow-label">BUSINESS FLOW</div>': '<div class="solution-flow-label">业务路径</div>',
    '<div class="solution-flow-label">API FLOW</div>': '<div class="solution-flow-label">接口路径</div>',
    '<div class="solution-flow-label">SYSTEM FLOW</div>': '<div class="solution-flow-label">系统路径</div>',
    '<small>CLIENTS</small>': '<small>合作客户</small>',
    '<small>YOUR BRAND</small>': '<small>自有品牌</small>',
    '<small>OPERATIONS</small>': '<small>发行运营</small>',
    '<small>DSP NETWORK</small>': '<small>音乐平台</small>',
    '<small>CATALOG</small>': '<small>曲库</small>',
    '<small>ENTERPRISE</small>': '<small>企业发行</small>',
    '<small>DISTRIBUTION</small>': '<small>发行渠道</small>',
    '<small>FINANCE</small>': '<small>数据结算</small>',
    '<small>PRODUCT</small>': '<small>现有产品</small>',
    '<small>DISTRIBUTION API</small>': '<small>发行 API</small>',
    '<small>INTERNAL SYSTEM</small>': '<small>现有系统</small>',
    '<small>INTEGRATION</small>': '<small>系统集成</small>',
    '<small>CHANNELS</small>': '<small>发行渠道</small>',
}
for old, new in replacements.items():
    if old not in block:
        raise SystemExit(f'missing expected solution markup: {old}')
    block = block.replace(old, new)

html = html[:start] + block + html[end:]
index_path.write_text(html, encoding='utf-8')

css = styles_path.read_text(encoding='utf-8')
marker = '/* Enterprise Solutions v2 polish: unified width, typography and Chinese micro-labels */'
if marker not in css:
    css += r'''

/* Enterprise Solutions v2 polish: unified width, typography and Chinese micro-labels */
[data-page="solutions"] .solutions-hero-v2>.container,
[data-page="solutions"] .solutions-subnav>.container,
[data-page="solutions"] .solutions-selector-section>.container,
[data-page="solutions"] .solutions-fit-section>.container,
[data-page="solutions"] .solutions-implementation>.container,
[data-page="solutions"] .enterprise-contact-cta>.container{max-width:1180px}

[data-page="solutions"] .solutions-hero-v2{padding:90px 0 84px}
[data-page="solutions"] .solutions-hero-layout{grid-template-columns:minmax(0,.94fr) minmax(460px,1.06fr);gap:56px}
[data-page="solutions"] .solutions-hero-copy h1{max-width:760px;margin:10px 0 22px;font-size:56px;line-height:1.07;letter-spacing:-.048em;text-wrap:balance}
[data-page="solutions"] .solutions-hero-copy p{max-width:610px;font-size:16px;line-height:1.76}
[data-page="solutions"] .solutions-mode-map{gap:10px;padding:14px;border-radius:22px;box-shadow:0 18px 48px rgba(27,45,87,.07)}
[data-page="solutions"] .solution-mode-card{min-height:176px;padding:23px 22px;border-radius:16px}
[data-page="solutions"] .solution-mode-card small{font-size:9px;letter-spacing:.04em}
[data-page="solutions"] .solution-mode-core{min-height:44px;border-radius:12px}

[data-page="solutions"] .solutions-subnav .container{gap:34px}
[data-page="solutions"] .solutions-selector-section,
[data-page="solutions"] .solutions-fit-section,
[data-page="solutions"] .solutions-implementation{padding-top:96px;padding-bottom:100px}
[data-page="solutions"] .section-head{max-width:none}
[data-page="solutions"] .section-head h2{max-width:760px;margin-top:8px;font-size:40px;line-height:1.16;letter-spacing:-.04em;text-wrap:balance}
[data-page="solutions"] .section-head>p{max-width:520px;color:#6f7b8e;font-size:14px;line-height:1.76}
[data-page="solutions"] .solutions-selector-section .section-head{max-width:860px;margin-bottom:32px}
[data-page="solutions"] .solutions-fit-section .section-head,
[data-page="solutions"] .solutions-implementation .section-head{display:grid;grid-template-columns:minmax(0,1fr) minmax(320px,410px);gap:64px;align-items:end;margin-bottom:34px}
[data-page="solutions"] .solutions-fit-section .section-head>p,
[data-page="solutions"] .solutions-implementation .section-head>p{margin:0}

[data-page="solutions"] .solution-role-tabs{overflow:hidden;border:1px solid var(--sol-line);border-radius:16px;background:#fff}
[data-page="solutions"] .solution-role-tabs button{min-height:68px;padding:0 20px}
[data-page="solutions"] .solution-role-tabs button.active{background:#f3f6ff;box-shadow:inset 0 -2px 0 var(--sol-blue)}
[data-page="solutions"] .solution-role-stage{margin-top:22px;padding:34px 36px;border:1px solid var(--sol-line);border-radius:24px;background:#fff;box-shadow:0 18px 48px rgba(28,45,84,.045)}
[data-page="solutions"] .solution-role-panel{grid-template-columns:minmax(310px,.76fr) minmax(0,1.24fr);gap:54px;align-items:center}
[data-page="solutions"] .solution-role-copy{padding:8px 0}
[data-page="solutions"] .solution-role-kicker{margin-bottom:12px;letter-spacing:0}
[data-page="solutions"] .solution-role-copy h3{max-width:520px;margin-bottom:14px;font-size:32px;line-height:1.2;text-wrap:balance}
[data-page="solutions"] .solution-role-copy>p{max-width:510px;font-size:13px;line-height:1.72}
[data-page="solutions"] .solution-recommend{margin-top:24px;padding-top:18px}
[data-page="solutions"] .solution-recommend small{letter-spacing:0}
[data-page="solutions"] .solution-architecture{min-height:356px;padding:24px;border-radius:20px;box-shadow:none}
[data-page="solutions"] .solution-flow-label{margin-bottom:34px;color:#8693a6;font-size:9px;letter-spacing:.05em}
[data-page="solutions"] .solution-flow{min-height:214px;gap:9px}
[data-page="solutions"] .flow-node{min-height:124px;padding:17px 15px;border-radius:13px}
[data-page="solutions"] .flow-node small{font-size:9px;letter-spacing:.02em}
[data-page="solutions"] .flow-node b{font-size:11px;line-height:1.45}
[data-page="solutions"] .flow-node span{font-size:8px;line-height:1.5}

[data-page="solutions"] .solutions-fit-section{background:#f7f9fd}
[data-page="solutions"] .solution-fit-matrix{overflow:hidden;border:1px solid #dce3ed;border-radius:18px;background:#fff}
[data-page="solutions"] .fit-matrix-head,[data-page="solutions"] .fit-matrix-row{grid-template-columns:.48fr 1.5fr .72fr;gap:30px;padding:0 26px}
[data-page="solutions"] .fit-matrix-head{min-height:48px}
[data-page="solutions"] .fit-matrix-row{min-height:78px}
[data-page="solutions"] .fit-matrix-action{margin-top:18px;padding:0 2px}

[data-page="solutions"] .solutions-implementation{background:#fff}
[data-page="solutions"] .solutions-timeline{margin-top:4px}
[data-page="solutions"] .solutions-timeline article{padding:30px 24px 0 0}
[data-page="solutions"] .solutions-timeline h3{font-size:15px;line-height:1.4}
[data-page="solutions"] .solutions-timeline p{max-width:190px;font-size:10px;line-height:1.68}

@media(min-width:1051px){
  [data-page="solutions"] .section-head h2{white-space:nowrap}
  [data-page="solutions"] .solution-role-copy h3{white-space:nowrap}
}
@media(max-width:1050px){
  [data-page="solutions"] .solutions-hero-layout{grid-template-columns:1fr;gap:38px}
  [data-page="solutions"] .solutions-mode-map{max-width:820px}
  [data-page="solutions"] .solutions-fit-section .section-head,
  [data-page="solutions"] .solutions-implementation .section-head{grid-template-columns:1fr;gap:14px;align-items:start}
  [data-page="solutions"] .section-head h2{white-space:normal}
  [data-page="solutions"] .solution-role-stage{padding:30px}
  [data-page="solutions"] .solution-role-panel{grid-template-columns:1fr;gap:26px}
  [data-page="solutions"] .solution-role-copy{max-width:760px}
}
@media(max-width:820px){
  [data-page="solutions"] .solutions-hero-v2{padding:68px 0 64px}
  [data-page="solutions"] .solutions-hero-copy h1{font-size:47px}
  [data-page="solutions"] .solutions-selector-section,
  [data-page="solutions"] .solutions-fit-section,
  [data-page="solutions"] .solutions-implementation{padding-top:82px;padding-bottom:86px}
  [data-page="solutions"] .section-head h2{font-size:35px}
  [data-page="solutions"] .solution-role-tabs{grid-template-columns:repeat(2,1fr)}
  [data-page="solutions"] .solution-role-tabs button:nth-child(2){border-right:0}
  [data-page="solutions"] .solution-role-tabs button:nth-child(-n+2){border-bottom:1px solid var(--sol-line)}
  [data-page="solutions"] .solution-role-stage{padding:26px;border-radius:20px}
  [data-page="solutions"] .solution-architecture{min-height:0}
}
@media(max-width:620px){
  [data-page="solutions"] .solutions-hero-v2{padding-top:54px}
  [data-page="solutions"] .solutions-hero-copy h1{font-size:39px;line-height:1.1}
  [data-page="solutions"] .solutions-hero-copy p{font-size:14px}
  [data-page="solutions"] .solutions-mode-map{padding:10px;border-radius:18px}
  [data-page="solutions"] .solution-mode-card{padding:20px}
  [data-page="solutions"] .solutions-selector-section,
  [data-page="solutions"] .solutions-fit-section,
  [data-page="solutions"] .solutions-implementation{padding-top:70px;padding-bottom:74px}
  [data-page="solutions"] .section-head h2{font-size:30px;line-height:1.2}
  [data-page="solutions"] .solution-role-tabs{grid-template-columns:1fr}
  [data-page="solutions"] .solution-role-tabs button{border-right:0;border-bottom:1px solid var(--sol-line)!important}
  [data-page="solutions"] .solution-role-tabs button:last-child{border-bottom:0!important}
  [data-page="solutions"] .solution-role-stage{padding:20px;border-radius:18px;box-shadow:none}
  [data-page="solutions"] .solution-role-copy h3{font-size:27px;white-space:normal}
  [data-page="solutions"] .solution-architecture{padding:17px;border-radius:16px}
  [data-page="solutions"] .fit-matrix-row{padding:18px 17px}
}
'''
    styles_path.write_text(css, encoding='utf-8')
