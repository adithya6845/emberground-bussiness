import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the main modal background slate-900 (very dark)
content = content.replace(
    '<div style="background:#1f2937; border:1px solid #374151; border-radius:12px; width:95%; max-width:1200px; max-height:90vh; overflow-y:auto; display:flex; flex-direction:column; padding:24px; color:#f9fafb; font-family:\'Inter\', sans-serif;">',
    '<div style="background:#0f172a; border:1px solid #1e293b; border-radius:12px; width:95%; max-width:1200px; max-height:90vh; overflow-y:auto; display:flex; flex-direction:column; padding:24px; color:#f8fafc; font-family:\'Inter\', sans-serif;">'
)

# Fix the header border
content = content.replace(
    '<div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #374151; padding-bottom:16px; margin-bottom:20px;">',
    '<div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #1e293b; padding-bottom:16px; margin-bottom:20px;">'
)

# Left sidebar background
content = content.replace(
    '<div style="width:300px; background:rgba(255,255,255,0.02); border-radius:8px; border:1px solid #374151; display:flex; flex-direction:column; padding:16px;">',
    '<div style="width:300px; background:rgba(255,255,255,0.02); border-radius:8px; border:1px solid #1e293b; display:flex; flex-direction:column; padding:16px;">'
)

# Inner cards should be slightly lighter, matching the left sidebar.
content = content.replace('background:#111827;', 'background:rgba(255,255,255,0.03);')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print('Colors inverted to match Image 2')
