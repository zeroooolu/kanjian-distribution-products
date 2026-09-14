from pathlib import Path

path = Path('03-enterprise/prototype-v4/styles.css')
css = path.read_text()
marker = '/* Pricing plan comparison: isolated responsive component */'
if marker in css:
    css = css.split(marker)[0].rstrip() + '\n\n'

block = r'''/* Pricing plan comparison: isolated responsive component */
[data-page="pricing"] .plan-matrix-section{overflow:clip}
[data-page="pricing"] .plan-matrix-section .section-head{max-width:860px;margin-bottom:30px}
[data-page="pricing"] .compare-hint{display:none;margin:0 0 12px;color:#8792a3;font-size:11px}
[data-page="pricing"] .mobile-plan-compare{display:none}
[data-page="pricing"] .plan-compare{overflow:hidden;border:1px solid #dce3ed;border-radius:20px;background:#fff;box-shadow:0 16px 44px rgba(27,43,82,.055)}
[data-page="pricing"] .plan-compare .row{display:grid;grid-template-columns:minmax(240px,1.35fr) repeat(3,minmax(170px,1fr));min-height:58px;border-bottom:1px solid #e9edf3;background:#fff}
[data-page="pricing"] .plan-compare .row:last-child{border-bottom:0}
[data-page="pricing"] .plan-compare .row>*{min-width:0;display:flex;align-items:center;padding:15px 18px;border-right:1px solid #e9edf3;color:#556176;font-size:12px;line-height:1.55;overflow-wrap:anywhere}
[data-page="pricing"] .plan-compare .row>*:last-child{border-right:0}
[data-page="pricing"] .plan-compare .row>*:first-child{color:#26334a;font-weight:700}
[data-page="pricing"] .plan-compare .row>span:not(:first-child),[data-page="pricing"] .plan-compare .row>b:not(:first-child){justify-content:center;text-align:center}
[data-page="pricing"] .plan-compare .row>span:nth-child(3){background:#f7f9ff;color:#274cc5;font-weight:750}
[data-page="pricing"] .plan-compare .row.head{min-height:66px;background:#111827;color:#fff}
[data-page="pricing"] .plan-compare .row.head>*{border-color:rgba(255,255,255,.1);color:#d9e0ec;font-size:12px;font-weight:800}
[data-page="pricing"] .plan-compare .row.head>*:first-child{color:#fff}
[data-page="pricing"] .plan-compare .row.head>*:nth-child(3){background:#315ff4;color:#fff}
[data-page="pricing"] .plan-compare .group{padding:11px 18px;border-bottom:1px solid #e3e8ef;background:#f1f4f8;color:#68758b;font-size:10px;font-weight:900;letter-spacing:.08em;text-transform:uppercase}

@media(max-width:1040px) and (min-width:681px){
  [data-page="pricing"] .compare-hint{display:block}
  [data-page="pricing"] .plan-compare{overflow-x:auto;overscroll-behavior-inline:contain;scrollbar-width:thin}
  [data-page="pricing"] .plan-compare .row,[data-page="pricing"] .plan-compare .group{min-width:900px}
}

@media(max-width:680px){
  [data-page="pricing"] .compare-hint,[data-page="pricing"] .plan-compare{display:none!important}
  [data-page="pricing"] .mobile-plan-compare{display:block;border:1px solid #dce3ed;border-radius:18px;background:#fff;box-shadow:0 12px 34px rgba(27,43,82,.05);overflow:hidden}
  [data-page="pricing"] .mobile-plan-tabs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0;padding:6px;border-bottom:1px solid #e8edf4;background:#f7f9fc}
  [data-page="pricing"] .mobile-plan-tabs button{min-width:0;padding:10px 6px;border:0;border-radius:10px;background:transparent;color:#788496;font-size:12px;font-weight:760;cursor:pointer;transition:background .18s ease,color .18s ease,box-shadow .18s ease}
  [data-page="pricing"] .mobile-plan-tabs button.active{background:#fff;color:#315ff4;box-shadow:0 2px 10px rgba(31,49,91,.08)}
  [data-page="pricing"] .mobile-plan-panel{display:none;padding:5px 18px 8px}
  [data-page="pricing"] .mobile-plan-panel.active{display:block}
  [data-page="pricing"] .mobile-plan-panel>div{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:18px;align-items:center;min-height:49px;padding:10px 0;border-bottom:1px solid #edf0f4}
  [data-page="pricing"] .mobile-plan-panel>div:last-child{border-bottom:0}
  [data-page="pricing"] .mobile-plan-panel span{min-width:0;color:#687487;font-size:12px;line-height:1.45}
  [data-page="pricing"] .mobile-plan-panel b{max-width:165px;color:#243149;font-size:12px;line-height:1.45;text-align:right;overflow-wrap:anywhere}
  [data-page="pricing"] .mobile-plan-panel.active b{font-weight:800}
}

@media(max-width:420px){
  [data-page="pricing"] .mobile-plan-tabs button{font-size:11px}
  [data-page="pricing"] .mobile-plan-panel{padding-left:15px;padding-right:15px}
  [data-page="pricing"] .mobile-plan-panel>div{gap:12px}
  [data-page="pricing"] .mobile-plan-panel b{max-width:145px}
}
'''

path.write_text(css + block + '\n')
print('pricing compare styles fixed')