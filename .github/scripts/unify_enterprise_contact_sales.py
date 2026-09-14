from pathlib import Path

index_path = Path('03-enterprise/prototype-v4/index.html')
style_path = Path('03-enterprise/prototype-v4/styles.css')
html = index_path.read_text(encoding='utf-8')

cta = '''  <section class="enterprise-contact-cta"><div class="container"><div class="enterprise-contact-panel reveal"><div><span class="eyebrow light">CONTACT SALES</span><h2>获取适配业务需求的企业发行方案</h2><p>提交基本业务信息，结合曲库规模、客户协作方式与系统集成需求，评估适合的产品版本、发行 API 或组合方案。</p></div><div class="enterprise-contact-actions"><a class="btn btn-white btn-lg" href="/enterprise/apply" data-route>申请企业方案</a></div></div></div></section>'''

replacements = {
'''  <section class="home-final-cta"><div class="container"><div class="home-final-panel reveal"><div><span class="eyebrow">CONTACT SALES</span><h2>匹配适合业务规模的企业发行方案</h2><p>提交曲库规模、合作客户数量和现有系统信息，用于评估合适的产品版本与接入方式。</p></div><div class="home-final-actions"><a class="btn btn-primary btn-lg" href="/enterprise/apply" data-route>申请企业方案</a><a class="btn btn-secondary" href="/enterprise/pricing" data-route>查看版本与价格</a></div></div></div></section>''': cta,
'''  <section class="product-final"><div class="container"><div class="product-final-panel reveal"><div><span class="eyebrow light">GET STARTED</span><h2>搭建自有品牌音乐发行平台</h2><p>覆盖客户入口、曲库管理、发行运营、渠道上线和合作方分账结算，建立可持续运营的企业发行能力。</p></div><div class="product-final-actions"><a class="btn btn-white btn-lg" href="/enterprise/apply" data-route>申请企业方案</a><a class="btn btn-ghost" href="/enterprise/pricing" data-route>查看版本与价格</a></div></div></div></section>''': cta,
'''  <section class="cta solutions-cta"><div class="container cta-grid reveal"><div><h2>构建适配业务需求的发行基础设施</h2><p>提交曲库规模、客户结构和现有系统信息，用于评估合适的产品组合与实施方案。</p></div><a class="btn btn-white btn-lg" href="/enterprise/apply" data-route>申请企业方案</a></div></section>''': cta,
'''  <section class="cta"><div class="container cta-grid reveal"><div><h2>选择与业务规模匹配的企业发行方案</h2><p>根据曲库规模、合作客户数量及系统集成需求确定版本；复杂项目可由商务与技术团队共同评估实施范围。</p></div><a class="btn btn-white btn-lg" href="/enterprise/apply" data-route>申请企业方案</a></div></section>''': cta,
'''  <section class="cta api-final-cta"><div class="container cta-grid reveal"><div><span class="eyebrow light">GET STARTED</span><h2>将音乐发行能力接入现有产品</h2><p>提交业务场景、预计发行规模与现有系统信息，用于确认接口范围、接入方式、测试环境与联调计划。</p></div><div class="api-cta-actions"><a class="btn btn-white btn-lg" href="/enterprise/apply?solution=api" data-route>申请 API 接入</a><a class="btn btn-ghost btn-lg" href="/enterprise/developers" data-route>查看开发者指南</a></div></div></section>''': cta,
}

for old, new in replacements.items():
    count = html.count(old)
    if count != 1:
        raise SystemExit(f'Expected exactly one CTA block, found {count}: {old[:80]}')
    html = html.replace(old, new, 1)

marker = '\n</section>\n<section class="page apply-page" data-page="apply">'
if html.count(marker) != 1:
    raise SystemExit(f'Expected developer/apply marker exactly once, found {html.count(marker)}')
html = html.replace(marker, '\n' + cta + '\n</section>\n<section class="page apply-page" data-page="apply">', 1)

index_path.write_text(html, encoding='utf-8')

css = style_path.read_text(encoding='utf-8')
css_block = '''\n\n/* Enterprise shared Contact Sales CTA */\n.enterprise-contact-cta{padding:76px 0 88px;background:#fff}\n.enterprise-contact-panel{position:relative;overflow:hidden;display:flex;align-items:center;justify-content:space-between;gap:48px;padding:48px 52px;border-radius:28px;background:radial-gradient(circle at 86% 18%,rgba(92,123,255,.24),transparent 34%),linear-gradient(135deg,#0a1221 0%,#0e1b34 55%,#102650 100%);box-shadow:0 24px 70px rgba(20,39,82,.14)}\n.enterprise-contact-panel:after{content:\"\";position:absolute;right:-90px;bottom:-150px;width:330px;height:330px;border:1px solid rgba(255,255,255,.1);border-radius:50%;box-shadow:0 0 0 54px rgba(255,255,255,.025),0 0 0 108px rgba(255,255,255,.018);pointer-events:none}\n.enterprise-contact-panel>div{position:relative;z-index:1}\n.enterprise-contact-panel h2{max-width:720px;margin:9px 0 12px;color:#fff;font-size:34px;line-height:1.18;letter-spacing:-.035em;text-wrap:balance}\n.enterprise-contact-panel p{max-width:760px;margin:0;color:#aebbd0;font-size:14px;line-height:1.8;text-wrap:pretty}\n.enterprise-contact-actions{flex:none}\n.enterprise-contact-actions .btn{min-width:148px}\n@media(max-width:820px){.enterprise-contact-cta{padding:64px 0 72px}.enterprise-contact-panel{align-items:flex-start;flex-direction:column;padding:40px 34px}.enterprise-contact-panel h2{font-size:30px}.enterprise-contact-actions{width:100%}.enterprise-contact-actions .btn{width:100%}}\n@media(max-width:560px){.enterprise-contact-cta{padding:52px 0 62px}.enterprise-contact-panel{gap:30px;padding:32px 22px;border-radius:22px}.enterprise-contact-panel h2{font-size:27px}.enterprise-contact-panel p{font-size:13px}}\n'''
if '/* Enterprise shared Contact Sales CTA */' not in css:
    css += css_block
style_path.write_text(css, encoding='utf-8')

# Guardrails: six public enterprise pages before Apply share the same CTA copy.
html = index_path.read_text(encoding='utf-8')
assert html.count('CONTACT SALES') >= 7  # six shared CTAs + Apply intro
assert html.count('获取适配业务需求的企业发行方案') >= 6
assert html.count('提交基本业务信息，结合曲库规模、客户协作方式与系统集成需求，评估适合的产品版本、发行 API 或组合方案。') == 6
print('Unified enterprise Contact Sales CTA across Home, Product, Solutions, Pricing, API and Developers.')
