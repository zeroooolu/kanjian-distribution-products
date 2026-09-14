from pathlib import Path
import sys

repo = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
root = repo / '03-enterprise/prototype-v4'
index = root / 'index.html'
styles = root / 'styles.css'
base = root / 'styles-base.css'

s = index.read_text()

# Finish developer terminology and API conversion copy.
replacements = {
    '提供 API 文档、接入联调及企业级技术支持': '提供开发者指南、接入联调及企业级技术支持',
    '查看完整 API 文档 →': '查看开发者指南 →',
    '测试环境与 API 文档': '测试环境与开发者指南',
    '查看开发者文档': '查看开发者指南',
    '正式开发者工具将用于查看 API 调用和 Webhook 记录': '开发者工具用于查看 API 调用和 Webhook 记录',
    'API 文档用于开发接入，企业技术支持用于联调和正式运行中的问题处理。': '开发者指南用于接入开发，企业技术支持用于联调和正式运行中的问题处理。',
    'href="/enterprise/apply" data-route>申请 API</a>': 'href="/enterprise/apply?solution=api" data-route>申请 API 接入</a>',
}
for old, new in replacements.items():
    s = s.replace(old, new)

# Mobile plan comparison gets an explicit affordance instead of relying on invisible horizontal overflow.
if '<p class="compare-hint">横向滑动查看完整版本对比</p>' not in s:
    s = s.replace('<div class="compare reveal">', '<p class="compare-hint">横向滑动查看完整版本对比</p><div class="compare reveal">', 1)

# Route-specific metadata for the SPA prototype.
routes_line = "const routes={'/enterprise':'home','/enterprise/':'home','/enterprise/product':'product','/enterprise/product/':'product','/enterprise/solutions':'solutions','/enterprise/solutions/':'solutions','/enterprise/pricing':'pricing','/enterprise/pricing/':'pricing','/enterprise/api':'api','/enterprise/api/':'api','/enterprise/developers':'developers','/enterprise/developers/':'developers','/enterprise/apply':'apply','/enterprise/apply/':'apply'};"
meta_block = routes_line + "\nconst pageMeta={home:['星球发行·企业版｜企业音乐发行平台与发行 API','面向发行商、唱片公司、版权公司和音乐平台，提供自有品牌音乐发行平台与发行 API。'],product:['自有品牌发行平台｜星球发行·企业版','以自有品牌开展音乐发行业务，覆盖客户门户、曲库、发行运营、数据与收入结算。'],solutions:['企业发行解决方案｜星球发行·企业版','面向发行商、唱片公司、版权公司、AI 音乐平台和音乐科技企业的发行解决方案。'],pricing:['企业版价格与版本｜星球发行·企业版','查看基础版、专业版、企业版以及发行 API 的价格、容量和服务范围。'],api:['发行 API｜星球发行·企业版','通过标准 API 将内容管理、发行提交、渠道状态、数据报表与收入结算能力接入现有产品。'],developers:['发行 API 开发者指南｜星球发行·企业版','查看发行 API 的接入准备、资源模型、发行流程、Webhook、错误日志与技术支持说明。'],apply:['申请企业方案｜星球发行·企业版','提交企业发行需求，用于评估自有品牌发行平台、发行 API 或组合方案。']};\nfunction setPageMeta(page){const meta=pageMeta[page]||pageMeta.home;document.title=meta[0];const d=document.querySelector('meta[name=\"description\"]');if(d)d.setAttribute('content',meta[1])}"
if 'const pageMeta=' not in s:
    if routes_line not in s:
        raise SystemExit('routes declaration not found')
    s = s.replace(routes_line, meta_block, 1)

old_render = "function render(path,hash=''){const page=routes[path]||'home';document.querySelectorAll('.page').forEach(el=>el.classList.toggle('active',el.dataset.page===page));setNav(page);closeMenu();applyRouteContext();requestAnimationFrame(()=>{revealVisible();syncSectionNav();if(hash)document.querySelector(hash)?.scrollIntoView();else scrollTo(0,0)})}"
new_render = "function render(path,hash=''){const page=routes[path]||'home';document.querySelectorAll('.page').forEach(el=>el.classList.toggle('active',el.dataset.page===page));setNav(page);setPageMeta(page);closeMenu();applyRouteContext();requestAnimationFrame(()=>{revealVisible();syncSectionNav();if(hash)document.querySelector(hash)?.scrollIntoView();else scrollTo(0,0)})}"
if old_render in s:
    s = s.replace(old_render, new_render, 1)
elif 'setPageMeta(page)' not in s:
    raise SystemExit('render function not found for metadata update')

# Improve readability of functional helper text.
s = s.replace('[data-page="api"] .api-commercial-note{grid-column:1/-1;margin:0;padding-top:16px;border-top:1px solid #edf0f5;color:#929cab;font-size:10px;line-height:1.6}', '[data-page="api"] .api-commercial-note{grid-column:1/-1;margin:0;padding-top:16px;border-top:1px solid #edf0f5;color:#8792a3;font-size:12px;line-height:1.65}')

index.write_text(s)

css = styles.read_text()
finish_css = '''
/* Enterprise consistency finish */
.compare-hint{display:none;margin:0 0 10px;color:#8a95a5;font-size:12px}
[data-page="api"] .api-module-grid article,[data-page="solutions"] .scenario-card,[data-page="solutions"] .fit-card{cursor:default}
[data-page="api"] .api-module-grid article:hover,[data-page="solutions"] .scenario-card:hover,[data-page="solutions"] .fit-card:hover{transform:none}
@media(max-width:820px){.compare-hint{display:block}}
'''
if 'Enterprise consistency finish' not in css:
    css += finish_css
styles.write_text(css)

b = base.read_text()
b = b.replace('.doc-table>div>*{padding:13px 14px;font-size:11px;', '.doc-table>div>*{padding:13px 14px;font-size:12px;')
b = b.replace('.resource-grid span{display:block;font-size:10px;', '.resource-grid span{display:block;font-size:11px;')
base.write_text(b)

final = index.read_text()
for forbidden in ['申请免费试用', '自有品牌发行系统', '>申请 API</a>', '查看完整 API 文档', '查看开发者文档']:
    if forbidden in final:
        raise SystemExit('remaining inconsistency: ' + forbidden)
if 'const pageMeta=' not in final or 'setPageMeta(page)' not in final:
    raise SystemExit('route metadata not installed')
if 'compare-hint' not in final:
    raise SystemExit('mobile compare hint missing')
