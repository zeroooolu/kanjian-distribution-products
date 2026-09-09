module.exports = async function handler(req, res) {
  const presetId = '2097207849833730048';
  const base = 'https://gw.kanjian.com/contract/api/v1';
  try {
    const commonHeaders = { accept: 'application/json', tenantKey: 'star' };
    const labelResp = await fetch(`${base}/preset/sharing/${presetId}/preset-label`, { headers: commonHeaders });
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
    const body = { dspName: '', areaIds: [], presetId, tId, language: 'ZH_CN' };
    const dspResp = await fetch(`${base}/preset/sharing/allOrPersonalization/dsps-info`, {
      method: 'POST',
      headers: { ...commonHeaders, 'content-type': 'application/json' },
      body: JSON.stringify(body)
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
