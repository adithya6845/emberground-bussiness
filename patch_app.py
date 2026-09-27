import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the second search box (collectionsSearchInput)
content = re.sub(
    r'<div style="display:flex; gap:8px; margin-bottom:12px;">\s*<input id="collectionsSearchInput"[^>]*>\s*</div>',
    '',
    content
)

# 2. Empty the table body
content = re.sub(
    r'<tbody id="collectionsTableBody" style="color:#cbd5e1;">.*?</tbody>',
    '<tbody id="collectionsTableBody" style="color:#cbd5e1;"></tbody>',
    content,
    flags=re.DOTALL
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print('Patched app.js to remove extra search box and empty table')
