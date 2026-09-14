from pathlib import Path

index_path = Path('03-enterprise/prototype-v4/index.html')
readme_path = Path('03-enterprise/README.md')

html = index_path.read_text()
old_batch = '<div class="row"><span>批量发行与批量任务</span><span>标准批量</span><span>高级批量</span><span>高级批量 / API 自动化</span></div>'
new_batch = '<div class="row"><span>批量发行</span><span>—</span><span>✓</span><span>✓</span></div><div class="row"><span>API 自动化发行</span><span>随 API</span><span>随 API</span><span>✓</span></div>'
html = html.replace('<div><span>曲库迁移</span><b>项目制实施</b></div>', '<div><span>曲库迁移</span><b>按项目范围</b></div>')
html = html.replace(old_batch, new_batch)
html = html.replace('<div class="row"><span>历史曲库迁移</span><span>可选服务</span><span>可选服务</span><span>项目制实施</span></div>', '<div class="row"><span>历史曲库迁移</span><span>可选服务</span><span>可选服务</span><span>按项目范围</span></div>')
index_path.write_text(html)

readme = readme_path.read_text()
readme = readme.replace('| 批量发行与批量任务 | 标准批量 | 高级批量 | 高级批量 / API 自动化 |', '| 批量发行 | — | ✓ | ✓ |\n| API 自动化发行 | 随 API | 随 API | ✓ |')
readme = readme.replace('| 历史曲库迁移 | 可选服务 | 可选服务 | 项目制实施 |', '| 历史曲库迁移 | 可选服务 | 可选服务 | 按项目范围 |')
if 'batch_distribution' not in readme:
    readme = readme.replace('webhook_and_api_logs\nmigration_service', 'webhook_and_api_logs\nbatch_distribution\napi_automation\nmigration_service')
    readme = readme.replace('- distribution_api: addon\n- support_level: standard', '- distribution_api: addon\n- batch_distribution: false\n- api_automation: with_api\n- support_level: standard', 1)
    readme = readme.replace('- distribution_api: addon\n- support_level: priority', '- distribution_api: addon\n- batch_distribution: true\n- api_automation: with_api\n- support_level: priority', 1)
    readme = readme.replace('- distribution_api: included\n- support_level: dedicated_manager', '- distribution_api: included\n- batch_distribution: true\n- api_automation: true\n- support_level: dedicated_manager', 1)
readme_path.write_text(readme)

updated = index_path.read_text()
assert old_batch not in updated
assert new_batch in updated
assert '<div><span>曲库迁移</span><b>按项目范围</b></div>' in updated
assert '<div class="row"><span>历史曲库迁移</span><span>可选服务</span><span>可选服务</span><span>按项目范围</span></div>' in updated
assert 'batch_distribution' in readme_path.read_text()
assert 'api_automation' in readme_path.read_text()
print('enterprise plan wording refined')
