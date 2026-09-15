from pathlib import Path

path = Path('03-enterprise/prototype-v4/index.html')
s = path.read_text(encoding='utf-8')

replacements = {
    '<nav class="product-subnav" aria-label="产品页章节"><div class="container"><a href="#product-brand">品牌</a><a href="#product-workspace">客户与团队</a><a href="#product-catalog">曲库</a><a href="#product-release">发行运营</a><a href="#product-distribution">发行网络</a><a href="#product-revenue">分账与结算</a><a href="#product-scale">规模化</a></div></nav>':
    '<nav class="product-subnav" aria-label="产品页章节"><div class="container"><a href="#product-brand">品牌</a><a href="#product-workspace">客户与团队</a><a href="#product-clients">客户管理</a><a href="#product-catalog">曲库管理</a><a href="#product-release">发行运营</a><a href="#product-distribution">发行网络</a><a href="#product-revenue">分账与结算</a><a href="#product-scale">规模化</a></div></nav>',

    '<section class="section product-catalog product-client-management" id="product-catalog">':
    '<section class="section product-catalog product-client-management" id="product-clients">',

    '<div class="client-portfolio-head"><div><span>合作客户</span><strong>128</strong></div><small>团队统一运营 · 客户业务独立</small></div>':
    '<div class="client-portfolio-head"><div><span>合作客户</span><strong>128</strong></div><small>统一运营 · 独立业务空间</small></div>',

    '<div class="client-portfolio-foot"><span>客户账号</span><span>曲库归属</span><span>发行记录</span><span>结算关系</span></div>':
    '<div class="client-portfolio-foot"><span>客户门户</span><span>曲库</span><span>发行</span><span>收入与结算</span></div>',

    '<div class="product-copy reveal"><span class="eyebrow">CLIENT MANAGEMENT</span><h2>先把合作客户与业务归属管理清楚</h2><p>面向多个厂牌、版权方和合作客户时，首先需要建立清晰的客户档案、业务账号与内容归属。不同客户保持独立的曲库、发行记录和结算关系，团队则可以在同一个运营后台集中处理。</p><div class="catalog-tags client-tags"><span>合作客户与厂牌</span><span>客户业务账号</span><span>曲库与内容归属</span><span>发行记录</span><span>收入与结算关系</span><span>团队权限</span></div><p class="product-caption">客户边界清楚，团队才能在客户数量增长后继续保持统一运营。</p></div>':
    '<div class="product-copy reveal"><span class="eyebrow">CLIENT MANAGEMENT</span><h2>一个后台，管理所有合作客户的发行业务</h2><p>为厂牌、版权方、音乐人等合作客户建立独立业务空间，统一管理账号、曲库、发行、数据与结算关系。每个客户保留清晰的数据与权限边界，运营团队则可跨客户集中处理日常业务，支撑从几十到上千客户的规模化发行运营。</p><div class="catalog-tags client-tags"><span>客户与厂牌</span><span>客户门户与账号</span><span>曲库归属</span><span>发行与状态</span><span>数据与收入</span><span>团队角色与权限</span></div><p class="product-caption">从客户入驻到持续发行与结算，完整保留每个客户的业务上下文。</p></div>',

    '<section class="section soft product-visual-section product-catalog-workbench" aria-label="音乐内容管理工作台示意">':
    '<section class="section soft product-visual-section product-catalog-workbench" id="product-catalog" aria-label="企业音乐目录管理工作台示意">',

    '<div class="visual-section-head reveal"><div><span class="eyebrow">CATALOG WORKBENCH</span><h2>音乐内容集中管理，随时进入资产详情</h2></div><p>在一个工作区管理艺人、专辑、歌曲、音频、封面、元数据与发行记录。列表负责快速筛选内容，详情面板保留完整资产上下文。</p></div>':
    '<div class="visual-section-head reveal"><div><span class="eyebrow">CATALOG MANAGEMENT</span><h2>统一管理从艺人到歌曲的完整音乐目录</h2></div><p>以艺人、发行、专辑和歌曲为核心组织音乐内容，将音频、封面、ISRC / UPC、版权信息与发行元数据关联到同一内容记录。支持搜索、筛选、批量处理与历史追踪，让内容从导入、编辑、发行到后续更新始终保持完整和可追溯。</p></div>',

    '<div class="content-capability-strip reveal"><span>艺人</span><span>专辑 / 单曲</span><span>歌曲与版本</span><span>音频与封面</span><span>元数据</span><span>发行记录</span></div>':
    '<div class="content-capability-strip reveal"><span>艺人 / 厂牌</span><span>发行 / 专辑 / 单曲</span><span>歌曲 / 版本</span><span>音频 / 封面</span><span>ISRC / UPC</span><span>发行元数据</span></div>',

    '<div class="cw-row cw-head"><span>音乐内容</span><span>内容类型</span><span>ISRC / UPC</span><span>内容状态</span></div>':
    '<div class="cw-row cw-head"><span>音乐内容</span><span>内容类型</span><span>ISRC / UPC</span><span>资料状态</span></div>',
}

for old, new in replacements.items():
    count = s.count(old)
    if count != 1:
        raise SystemExit(f'expected exactly 1 occurrence, got {count}: {old[:100]}')
    s = s.replace(old, new, 1)

path.write_text(s, encoding='utf-8')
