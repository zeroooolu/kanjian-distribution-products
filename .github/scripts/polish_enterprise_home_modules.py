from pathlib import Path

p=Path('03-enterprise/prototype-v4/index.html'); s=Path('03-enterprise/prototype-v4/styles.css')
h=p.read_text(); c=s.read_text()

def one(a,b):
    global h
    assert h.count(a)==1,(a[:50],h.count(a))
    h=h.replace(a,b,1)

one('<span>CATALOG</span><i></i><span>REVIEW</span><i></i><span>DISTRIBUTION</span><i></i><span>DSP NETWORK</span><i></i><span>DATA</span><i></i><span>REVENUE</span>','<span>曲库</span><i></i><span>审核</span><i></i><span>发行</span><i></i><span>平台网络</span><i></i><span>数据</span><i></i><span>收入</span>')
one('<div class="avatar-stack"><i>N</i><i>B</i><i>C</i></div><div class="mini-lines"><span></span><span></span><span></span></div><em>128 CLIENTS</em>','<div class="avatar-stack"><i>厂</i><i>牌</i><i>客</i></div><div class="mini-lines"><span></span><span></span><span></span></div><em>128 个合作客户</em>')
one('<div class="capability-art art-catalog"><div class="mini-cover"></div><div class="catalog-lines"><span><b>Midnight Signals</b><i>12 tracks</i></span><span><b>Neon Summer</b><i>Single</i></span><span><b>After Rain</b><i>EP</i></span></div></div>','<div class="capability-art art-catalog"><div class="album-shelf"><span class="album-cover album-a"><b>范特西</b><i>周杰伦</i></span><span class="album-cover album-b"><b>寓言</b><i>王菲</i></span><span class="album-cover album-c"><b>黑色柳丁</b><i>陶喆</i></span></div><em>示例专辑</em></div>')
one('24 ITEMS TO REVIEW','24 个待审核内容')
one('<span class="dsp ok">Spotify <b>LIVE</b></span><span class="dsp pending">Apple <b>PROCESSING</b></span><span class="dsp ok">QQ Music <b>LIVE</b></span>','<span class="dsp ok">QQ 音乐 <b>已上线</b></span><span class="dsp pending">网易云音乐 <b>处理中</b></span><span class="dsp ok">Apple Music <b>已上线</b></span>')
one('<em>+18.4%</em>','<em>本月 +18.4%</em>')
one('<span>AVAILABLE</span><strong>¥428,620</strong>','<span>可结算收入</span><strong>¥428,620</strong>')
one('3 SETTLEMENT GROUPS','3 个结算分组')

mark='/* homepage polish 2026-09-15 */'
if mark not in c:
 c+='''\n\n/* homepage polish 2026-09-15 */
[data-page="home"] .sonic-ticker-track{font-size:11px;letter-spacing:.06em}
[data-page="home"] .home-product-pair{gap:18px;border:0;background:transparent}
[data-page="home"] .home-product-pair article{overflow:hidden;border:1px solid #dfe6f0!important;border-radius:22px!important;background:#fff;box-shadow:0 12px 32px rgba(28,47,89,.045)!important}
[data-page="home"] .home-product-pair article:hover{transform:translateY(-3px)!important;border-color:#cfd9eb!important;background:#fff;box-shadow:0 18px 42px rgba(28,47,89,.075)!important}
[data-page="home"] .album-shelf{z-index:1;display:flex;gap:10px;width:100%}
[data-page="home"] .album-cover{position:relative;display:flex;flex:1;min-width:0;aspect-ratio:1;flex-direction:column;justify-content:flex-end;padding:9px;border-radius:12px;overflow:hidden;box-shadow:0 9px 20px rgba(31,49,88,.13)}
[data-page="home"] .album-cover:before{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 35%,rgba(8,13,25,.62))}
[data-page="home"] .album-cover b,[data-page="home"] .album-cover i{z-index:1;color:#fff;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
[data-page="home"] .album-cover b{font-size:10px}.album-cover i{margin-top:3px;font-size:7px;font-style:normal;opacity:.82}
[data-page="home"] .album-a{background:radial-gradient(circle at 70% 22%,#ffd679,transparent 24%),linear-gradient(145deg,#6b3d28,#1d263f 64%,#0b1325)}
[data-page="home"] .album-b{background:radial-gradient(circle at 30% 28%,#ffe8eb,transparent 25%),linear-gradient(145deg,#d88992,#7b617d 55%,#2f3857)}
[data-page="home"] .album-c{background:radial-gradient(circle at 72% 26%,#ff973e,transparent 23%),linear-gradient(145deg,#191919,#353535 62%,#080808)}
[data-page="home"] .art-catalog>em{z-index:2;padding:4px 7px;border-radius:999px;background:rgba(255,255,255,.86)}
[data-page="home"] .art-review small{font-size:9px;letter-spacing:.02em}.dsp b{letter-spacing:0}.art-data>em{font-size:10px;letter-spacing:0}
[data-page="home"] .case-glyph,[data-page="home"] .home-use-cases span.case-glyph{display:flex!important;align-items:center!important;justify-content:center!important;padding:0!important;text-align:center!important}
[data-page="home"] .case-glyph svg{display:block;margin:auto;flex:none}
@media(max-width:680px){[data-page="home"] .home-product-pair{display:grid;grid-template-columns:1fr;gap:14px;border:0}}
'''

p.write_text(h); s.write_text(c)
assert all(x in h for x in ['平台网络','128 个合作客户','范特西','24 个待审核内容','可结算收入'])
print('ok')
