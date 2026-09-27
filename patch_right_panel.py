import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Right Panel HTML with IDs
old_right_panel = '''          <!-- Right: Customer Details -->
          <div style="flex:1; background:#0f172a; border-radius:8px; border:1px solid #334155; padding:16px; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
                <div>
                  <h4 style="margin:0 0 4px 0; font-size:1.05rem; font-weight:600; color:#f8fafc;">Customer Details - Rahul Stores</h4>
                  <span style="font-size:0.75rem; color:#94a3b8;">Outstanding: <strong style="color:#ef4444;">₹18,500</strong> · <strong style="color:#ef4444;">12 days overdue</strong></span>
                </div>
                <span style="background:rgba(239,68,68,0.1); color:#ef4444; font-size:0.7rem; padding:4px 8px; border-radius:4px; font-weight:600;">High Risk</span>
              </div>'''

new_right_panel = '''          <!-- Right: Customer Details -->
          <div style="flex:1; background:#0f172a; border-radius:8px; border:1px solid #334155; padding:16px; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
                <div>
                  <h4 id="colDetailsName" style="margin:0 0 4px 0; font-size:1.05rem; font-weight:600; color:#f8fafc;">Customer Details - (Select Customer)</h4>
                  <span id="colDetailsOutstanding" style="font-size:0.75rem; color:#94a3b8;">Outstanding: <strong>--</strong> · <strong>-- days overdue</strong></span>
                </div>
                <span id="colDetailsRisk" style="background:rgba(239,68,68,0.1); color:#ef4444; font-size:0.7rem; padding:4px 8px; border-radius:4px; font-weight:600; display:none;">High Risk</span>
              </div>'''

content = content.replace(old_right_panel, new_right_panel)

# 2. Update AI Recommendation text with ID
old_rec = '''<p style="margin:0 0 12px 0; font-size:0.75rem; color:#cbd5e1; line-height:1.5;">Customer has 2 previous delayed payments. Recommend sending a stronger follow-up with late fee notice.</p>'''
new_rec = '''<p id="colDetailsRec" style="margin:0 0 12px 0; font-size:0.75rem; color:#cbd5e1; line-height:1.5;">Please select a customer to view AI recommendations.</p>'''

content = content.replace(old_rec, new_rec)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print('Patched HTML in app.js')
