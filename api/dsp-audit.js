module.exports = async function handler(req, res) {
  const presetId = '2097207849833730048';
  const base = 'https://gw.kanjian.com/contract/api/v1';
  try {
    if (req.query && req.query.debug === 'tenant') {
      const src = await (await fetch('https://star.kanjian.com/preset/assets/index-91615d64.js')).text();
      const needles = ['tenant_key','tenantKey','TenantKey','x-tenant','tenant-key'];
      const matches = [];
      for (const needle of needles) {
        let idx = src.indexOf(needle);
        let count = 0;
        while (idx >= 0 && count < 12) {
          matches.push({ needle, context: src.slice(Math.max(0, idx - 280), Math.min(src.length, idx + 420)) });
          idx = src.indexOf(needle, idx + needle.length);
          count++;
        }
      }
      res.status(200).json({ matches });
      return;
    }

    const labelResp = await fetch(`${base}/preset/sharing/${presetId}/preset-label`, {
      headers: { accept: 'application/json' }
    });
    const labelText = await labelResp.text();
    if (!labelResp.ok) {
      res.status(labelResp.status).json({ stage: 'preset-label', body: labelText });
      return;
    }
    let label;
    try { label = JSON.parse(labelText); } catch { label = { raw: labelText }; }
    const labelData = label && label.data !== undefined ? label.data : label;
    const allDsp = !!(labelData && labelData.allDsp);
    const tId = allDsp ? '1' : '2';
    const body = { dspName: '', areaIds: [], presetId, tId };
    const headers = { 'content-type': 'application/json', accept: 'application/json' };
    const dspResp = await fetch(`${base}/preset/sharing/allOrPersonalization/dsps-info`, {
      method: 'POST', headers, body: JSON.stringify(body)
    });
    const dspText = await dspResp.text();
    if (!dspResp.ok) {
      res.status(dspResp.status).json({ stage: 'dsps-info', label, request: body, body: dspText });
      return;
    }
    let dsp;
    try { dsp = JSON.parse(dspText); } catch { dsp = { raw: dspText }; }
    const root = dsp && dsp.data !== undefined ? dsp.data : dsp;
    const includeList = root && Array.isArray(root.includeList) ? root.includeList : [];
    const excludeList = root && Array.isArray(root.excludeList) ? root.excludeList : [];
    const flatten = groups => groups.flatMap(group => (group.dspList || []).map(item => ({
      groupId: group.groupId,
      groupName: group.groupName || group.name || '',
      dspId: item.dspId,
      name: item.name,
      logoPath: item.logoPath,
      url: item.url,
      describe: item.describe,
      note: item.note,
      curationOwner: item.curationOwner
    })));
    res.setHeader('cache-control', 'no-store');
    res.status(200).json({ presetId, allDsp, tId, label: labelData, include: flatten(includeList), exclude: flatten(excludeList) });
  } catch (error) {
    res.status(500).json({ error: String(error && error.stack || error) });
  }
};
