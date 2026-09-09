module.exports = async function handler(req, res) {
  const presetId = '2097207849833730048';
  const base = 'https://gw.kanjian.com/contract/api/v1';
  const exportTargets = {
    '咪咕音乐':'5',
    '阿里音乐':'7',
    'Deezer':'11',
    'Meta（Facebook / Instagram）':'430',
    'Qobuz':'380',
    'SoundCloud':'98',
    'TIDAL':'21',
    'Yandex':'59215'
  };

  try {
    const commonHeaders = { accept: 'application/json', tenantKey: 'star' };
    const labelResp = await fetch(`${base}/preset/sharing/${presetId}/preset-label`, { headers: commonHeaders });
    if (!labelResp.ok) throw new Error(`preset-label ${labelResp.status}`);
    const label = await labelResp.json();
    const labelData = label && label.data !== undefined ? label.data : label;
    const body = { dspName: '', areaIds: [], presetId, tId: labelData && labelData.allDsp ? '1' : '2', language: 'ZH_CN' };

    const dspResp = await fetch(`${base}/preset/sharing/allOrPersonalization/dsps-info`, {
      method: 'POST',
      headers: { ...commonHeaders, 'content-type': 'application/json' },
      body: JSON.stringify(body)
    });
    if (!dspResp.ok) throw new Error(`dsps-info ${dspResp.status}`);
    const dsp = await dspResp.json();
    const root = dsp && dsp.data !== undefined ? dsp.data : dsp;
    const groups = [...(root.includeList || []), ...(root.excludeList || [])];
    const items = groups.flatMap(group => group.dspList || []);

    const logos = {};
    await Promise.all(Object.entries(exportTargets).map(async ([key, dspId]) => {
      const item = items.find(x => String(x.dspId) === dspId);
      if (!item || !item.logoPath) return;
      const imageResp = await fetch(item.logoPath);
      if (!imageResp.ok) return;
      const mime = imageResp.headers.get('content-type') || 'application/octet-stream';
      const buf = Buffer.from(await imageResp.arrayBuffer());
      logos[key] = `data:${mime};base64,${buf.toString('base64')}`;
    }));

    res.setHeader('content-type', 'application/javascript; charset=utf-8');
    res.setHeader('cache-control', 'public, s-maxage=86400, stale-while-revalidate=604800');
    res.status(200).send(`window.STAR_DSP_LOGOS=${JSON.stringify(logos)};\n`);
  } catch (error) {
    res.setHeader('content-type', 'application/javascript; charset=utf-8');
    res.setHeader('cache-control', 'no-store');
    res.status(200).send('window.STAR_DSP_LOGOS=window.STAR_DSP_LOGOS||{};\n');
  }
};
