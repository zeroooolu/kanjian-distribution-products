module.exports = async function handler(req, res) {
  const presetId = '2097207849833730048';
  const base = 'https://gw.kanjian.com/contract/api/v1';
  try {
    const commonHeaders = { accept: 'application/json', tenantKey: 'star' };
    const labelResp = await fetch(`${base}/preset/sharing/${presetId}/preset-label`, { headers: commonHeaders });
    const label = await labelResp.json();
    const labelData = label && label.data !== undefined ? label.data : label;
    const allDsp = !!(labelData && labelData.allDsp);
    const body = { dspName: '', areaIds: [], presetId, tId: allDsp ? '1' : '2', language: 'ZH_CN' };
    const dspResp = await fetch(`${base}/preset/sharing/allOrPersonalization/dsps-info`, {
      method: 'POST',
      headers: { ...commonHeaders, 'content-type': 'application/json' },
      body: JSON.stringify(body)
    });
    if (!dspResp.ok) {
      res.status(dspResp.status).send(await dspResp.text());
      return;
    }
    const dsp = await dspResp.json();
    const root = dsp && dsp.data !== undefined ? dsp.data : dsp;
    const groups = [...(root.includeList || []), ...(root.excludeList || [])];
    const items = groups.flatMap(group => (group.dspList || []).map(item => ({ ...item, groupName: group.groupName || group.name || '' })));

    if (req.query && req.query.dspId) {
      const item = items.find(x => String(x.dspId) === String(req.query.dspId));
      if (!item || !item.logoPath) {
        res.status(404).json({ error: 'logo_not_found', dspId: req.query.dspId });
        return;
      }
      const imageResp = await fetch(item.logoPath);
      if (!imageResp.ok) {
        res.status(imageResp.status).json({ error: 'image_fetch_failed', name: item.name });
        return;
      }
      const buf = Buffer.from(await imageResp.arrayBuffer());
      res.setHeader('cache-control', 'no-store');
      res.status(200).json({
        dspId: item.dspId,
        name: item.name,
        groupName: item.groupName,
        mime: imageResp.headers.get('content-type') || 'application/octet-stream',
        base64: buf.toString('base64')
      });
      return;
    }

    const wanted = ['番茄音乐','番茄畅听','咪咕音乐','阿里音乐','Bandcamp','Beatport','Deezer','Meta Fingerprinting（Facebook & Instagram）','Meta Audio Library（Facebook & Instagram）','Qobuz','SoundCloud','Tidal','TIDAL','Yandex Music'];
    const matches = items.filter(item => wanted.includes(item.name)).map(item => ({
      dspId: item.dspId,
      name: item.name,
      groupName: item.groupName,
      logoPath: item.logoPath
    }));
    res.setHeader('cache-control', 'no-store');
    res.status(200).json({ matches });
  } catch (error) {
    res.status(500).json({ error: String(error && error.stack || error) });
  }
};
