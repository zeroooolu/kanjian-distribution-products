const RAW='/assets/platform-logos/';

const namedLogos={
  'Spotify':RAW+'spotify.jpeg',
  'Apple Music':RAW+'apple-music.jpg',
  'QQ音乐':RAW+'qq-music.png',
  '网易云音乐':RAW+'netease-music.jpg',
  '酷狗音乐':RAW+'kugou-music.png',
  '酷我音乐':RAW+'kuwo-music.png',
  '汽水音乐':RAW+'douyin-qishui.jpg',
  '华为音乐':RAW+'huawei-music.jpg',
  'Amazon Music':RAW+'amazon-music.png',
  'YouTube Music':RAW+'youtube-music.jpg',
  'TikTok':RAW+'tiktok.jpeg',
  'KKBOX':RAW+'kkbox.png'
};

const shortName=n=>({
  Spotify:'SP','Apple Music':'AM','QQ音乐':'QQ','网易云音乐':'网易','酷狗音乐':'酷狗','酷我音乐':'酷我',
  '汽水音乐':'汽水','番茄音乐':'番茄','华为音乐':'华为','咪咕音乐':'咪咕','阿里音乐':'阿里','Amazon Music':'AZ',
  'YouTube Music':'YT',TikTok:'TT','Meta（Facebook / Instagram）':'Meta','SoundCloud':'SC',TIDAL:'TD',Deezer:'DZ',
  Bandcamp:'BC',Beatport:'BP',Qobuz:'QZ',Yandex:'YX',KKBOX:'KK'
}[n]||String(n).slice(0,4));

// 唯一渠道数据源：来自 channel-catalog-ai-policy-v1.0.md。
// 官网 Logo、发行 Builder、渠道数量都从这里生成，禁止再使用旧官网的“25 张图全量轮播”。
const channelData=[
  // 中国大陆 / 华语渠道
  {name:'QQ音乐',region:'cn',logo:'QQ音乐',status:'可发行 · AI 内容需声明；部分 AI 内容收益和推荐受限'},
  {name:'酷狗音乐',region:'cn',logo:'酷狗音乐',status:'可发行 · AI 内容遵循 TME 规则'},
  {name:'酷我音乐',region:'cn',logo:'酷我音乐',status:'可发行 · AI 内容遵循 TME 规则'},
  {name:'网易云音乐',region:'cn',logo:'网易云音乐',status:'可发行 · AI 内容可能被平台标识'},
  {name:'汽水音乐',region:'cn',logo:'汽水音乐',status:'可发行 · 高相似度内容可能被限制'},
  {name:'番茄音乐',region:'cn',logo:'番茄音乐',status:'可发行 · 支持符合要求的 AI 原创音乐'},
  {name:'华为音乐',region:'cn',logo:'华为音乐',status:'可发行 · AI 专属规则持续确认'},
  {name:'咪咕音乐',region:'cn',logo:'咪咕音乐',status:'可发行 · 当前为离线批次交付，处理时效不同',specialDelivery:true},
  {name:'阿里音乐',region:'cn',logo:'阿里音乐',status:'可发行 · AI 专属规则持续确认'},
  {name:'KKBOX',region:'cn',logo:'KKBOX',status:'可发行 · AI 专属规则持续确认'},

  // 海外渠道
  {name:'Amazon Music',region:'global',logo:'Amazon Music',status:'可发行 · 纯 AI 的正式 B2B 规则仍需持续确认',confirmFullAI:true},
  {name:'Apple Music',region:'global',logo:'Apple Music',status:'可发行 · 支持提交 AI 透明度信息'},
  {name:'Bandcamp',region:'global',logo:'Bandcamp',status:'普通音乐可发行 · 全部或实质性 AI 生成内容不可发行',blockedFullAI:true},
  {name:'Beatport',region:'global',logo:'Beatport',status:'AI 辅助可发行 · 完全或主要由 AI 生成的音乐不可发行',blockedFullAI:true},
  {name:'Deezer',region:'global',logo:'Deezer',status:'可发行 · 纯 AI 内容不进入算法推荐或编辑歌单',warning:true},
  {name:'Meta（Facebook / Instagram）',region:'global',logo:'Meta（Facebook / Instagram）',status:'可发行 · 纯 AI 目录的 B2B 准入需按实际规则确认',confirmFullAI:true},
  {name:'Qobuz',region:'global',logo:'Qobuz',status:'普通 / AI 辅助可发行 · 100% AI 内容不可新交付',blockedFullAI:true},
  {name:'SoundCloud',region:'global',logo:'SoundCloud',status:'经 AudioSalad 交付 · 纯 AI 特殊规则需确认',confirmFullAI:true},
  {name:'Spotify',region:'global',logo:'Spotify',status:'可发行 · 部分 AI Persona 的推荐资格可能受限',warning:true},
  {name:'TIDAL',region:'global',logo:'TIDAL',status:'可发行 · 100% AI 录音不参与版税分配',warning:true},
  {name:'TikTok',region:'global',logo:'TikTok',status:'可发行 · 纯 AI 音乐目录的 B2B 规则需持续确认',confirmFullAI:true},
  {name:'Yandex',region:'global',logo:'Yandex',status:'可发行 · AI 标识可能影响推荐权重',warning:true},
  {name:'YouTube Music',region:'global',logo:'YouTube Music',status:'可发行 · 支持 Fully / Partially Gen AI 标记'}
];

function imageMarkup(name){
  const url=namedLogos[name];
  return url?`<img src="${url}" alt="${name}" loading="lazy">`:`<span class="logo-wordmark">${name}</span>`;
}

function addImgFallback(scope=document){
  scope.querySelectorAll('img').forEach(img=>{
    if(img.dataset.fallbackBound)return;
    img.dataset.fallbackBound='1';
    img.addEventListener('error',()=>{
      const p=img.parentElement;
      if(!p)return;
      p.classList.add('logo-failed');
      p.dataset.fallback=img.alt||'DSP';
      img.remove();
    });
  });
}

function buildMarquee(){
  document.querySelectorAll('[data-dsp-marquee]').forEach(el=>{
    if(el.children.length)return;
    const items=[...channelData,...channelData];
    el.innerHTML=items.map(c=>`<div class="logo-box" data-fallback="${c.name}" title="${c.name}">${imageMarkup(c.logo||c.name)}</div>`).join('');
  });
  addImgFallback();
}

function hydrateNamedLogos(){
  document.querySelectorAll('[data-logo]').forEach(el=>{
    const name=el.dataset.logo;
    el.dataset.fallback=name;
    el.innerHTML=imageMarkup(name);
  });
  addImgFallback();
}

function initBilling(){
  const buttons=[...document.querySelectorAll('[data-billing]')];
  if(!buttons.length)return;
  const prices={monthly:{china:'29.9',global:'59.9',chinaUnit:'/月',globalUnit:'/月'},annual:{china:'299',global:'599',chinaUnit:'/年',globalUnit:'/年'}};
  buttons.forEach(btn=>btn.addEventListener('click',()=>{
    buttons.forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    const p=prices[btn.dataset.billing];
    document.querySelector('[data-price-china]').textContent='¥'+p.china;
    document.querySelector('[data-unit-china]').textContent=p.chinaUnit;
    document.querySelector('[data-price-global]').textContent='¥'+p.global;
    document.querySelector('[data-unit-global]').textContent=p.globalUnit;
    document.querySelectorAll('[data-billing-note]').forEach(n=>n.textContent=btn.dataset.billing==='monthly'?'按月支付，适合更灵活地管理发行预算':'一次支付全年，价格更优惠');
  }));
}

function initEstimator(){
  const tracks=document.querySelector('[data-track-count]'),channels=document.querySelector('[data-channel-count]');
  if(!tracks||!channels)return;
  let t=5,c=6;
  const refresh=()=>{
    tracks.textContent=t;
    channels.textContent=c;
    const e=document.querySelector('[data-estimate]');
    if(e)e.textContent='¥'+t*c;
  };
  document.querySelectorAll('[data-step]').forEach(b=>b.addEventListener('click',()=>{
    const x=b.dataset.step;
    if(x==='track-up')t=Math.min(200,t+1);
    if(x==='track-down')t=Math.max(1,t-1);
    if(x==='channel-up')c=Math.min(channelData.length,c+1);
    if(x==='channel-down')c=Math.max(1,c-1);
    refresh();
  }));
  refresh();
}

function initReleaseBuilder(){
  const root=document.querySelector('[data-release-builder]');
  if(!root)return;
  let aiMode='assisted',region='all',term=1;
  let selected=new Set(channelData.slice(0,10).map(c=>c.name));
  const list=document.querySelector('[data-channels]');

  const stateFor=(c)=>{
    if(aiMode==='full'&&c.blockedFullAI)return {disabled:true,text:'当前这类作品不能发行到该平台'};
    if(aiMode==='full'&&c.confirmFullAI)return {disabled:true,text:'100% AI 内容当前需要渠道确认，暂不计入本次可发行平台'};
    return {disabled:false,text:c.status};
  };

  const render=()=>{
    const filtered=channelData.filter(c=>region==='all'||c.region===region);
    list.innerHTML=filtered.map(c=>{
      const state=stateFor(c);
      if(state.disabled)selected.delete(c.name);
      const sel=selected.has(c.name)&&!state.disabled;
      return `<div class="channel ${sel?'selected':''} ${state.disabled?'disabled':''}" data-channel="${c.name}">
        <div class="channel-logo" data-logo="${c.logo||c.name}" data-fallback="${shortName(c.name)}"></div>
        <div><strong>${c.name}</strong><small>${state.text}</small></div>
        <div class="check">✓</div>
      </div>`;
    }).join('');

    hydrateNamedLogos();
    document.querySelectorAll('[data-channel]').forEach(el=>el.addEventListener('click',()=>{
      if(el.classList.contains('disabled'))return;
      const n=el.dataset.channel;
      selected.has(n)?selected.delete(n):selected.add(n);
      render();
    }));

    document.querySelector('[data-selected-count]').textContent=selected.size;
    document.querySelector('[data-summary-channels]').textContent=selected.size+' 个';
    document.querySelector('[data-summary-term]').textContent=term+' 年';
    document.querySelector('[data-summary-total]').innerHTML='¥'+selected.size*term+'<span> / 本次</span>';

    const available=channelData.filter(c=>!stateFor(c).disabled).length;
    const rec=document.querySelector('[data-sub-recommend]');
    if(rec)rec.innerHTML=selected.size>=10
      ?`<div class="top"><strong>经常发行？订阅可能更划算</strong><span class="tag">可选</span></div><p>全球发行订阅最多覆盖 50 首当前在架歌曲；按这首歌目前的作品属性，可从 ${available} 个已接入平台中选择。</p>`
      :`<div class="top"><strong>这次按量发行更合适</strong><span class="tag">按实际使用付费</span></div><p>你只选择了 ${selected.size} 个平台，只需要为实际使用的平台付费。</p>`;
  };

  document.querySelectorAll('[data-ai-mode]').forEach(el=>el.addEventListener('click',()=>{
    document.querySelectorAll('[data-ai-mode]').forEach(x=>x.classList.remove('active'));
    el.classList.add('active');
    aiMode=el.dataset.aiMode;
    render();
  }));
  document.querySelectorAll('[data-region]').forEach(el=>el.addEventListener('click',()=>{
    document.querySelectorAll('[data-region]').forEach(x=>x.classList.remove('active'));
    el.classList.add('active');
    region=el.dataset.region;
    render();
  }));
  document.querySelectorAll('[data-term]').forEach(el=>el.addEventListener('click',()=>{
    document.querySelectorAll('[data-term]').forEach(x=>x.classList.remove('active'));
    el.classList.add('active');
    term=Number(el.dataset.term);
    render();
  }));
  render();
}

document.addEventListener('DOMContentLoaded',()=>{
  buildMarquee();
  hydrateNamedLogos();
  initBilling();
  initEstimator();
  initReleaseBuilder();
});