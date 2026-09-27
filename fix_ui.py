import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace modal container background
content = content.replace(
    '<div style="background:#1e293b; border:1px solid #334155; border-radius:12px; width:95%; max-width:1200px; max-height:90vh; overflow-y:auto; display:flex; flex-direction:column; padding:24px; color:#f8fafc; font-family:\'Inter\', sans-serif;">',
    '<div style="background:#1f2937; border:1px solid #374151; border-radius:12px; width:95%; max-width:1200px; max-height:90vh; overflow-y:auto; display:flex; flex-direction:column; padding:24px; color:#f9fafb; font-family:\'Inter\', sans-serif;">'
)

# Replace header border
content = content.replace(
    '<div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #334155; padding-bottom:16px; margin-bottom:20px;">',
    '<div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #374151; padding-bottom:16px; margin-bottom:20px;">'
)

# Replace left sidebar background
content = content.replace(
    '<div style="width:300px; background:rgba(255,255,255,0.02); border-radius:8px; border:1px solid #1e293b; display:flex; flex-direction:column; padding:16px;">',
    '<div style="width:300px; background:rgba(255,255,255,0.02); border-radius:8px; border:1px solid #374151; display:flex; flex-direction:column; padding:16px;">'
)

# Replace right panel card backgrounds (DATA INSIGHTS and EXPECTED IMPACT)
# In my previous script, I used `background:#0b1121;` for these cards.
content = content.replace('background:#0b1121;', 'background:#111827;')
# Also remove the border from expected impact cards!
content = content.replace('border:1px solid #1e293b;', '')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print('UI fixed.')
