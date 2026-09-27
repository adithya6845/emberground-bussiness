import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace static timeline HTML with an empty div with id='colDetailsTimeline'
old_timeline = '''              <div style="font-size:0.75rem; color:#cbd5e1; display:flex; flex-direction:column; gap:12px; margin-bottom:20px;">
                <div style="display:flex; gap:12px;">
                  <span style="color:#64748b; width:40px;">5 Sep</span>
                  <div style="flex:1;">
                    <div style="font-weight:600; color:#f8fafc;">Invoice generated</div>
                    <div style="color:#64748b;">₹18,500</div>
                  </div>
                </div>
                <div style="display:flex; gap:12px;">
                  <span style="color:#64748b; width:40px;">8 Sep</span>
                  <div style="flex:1;">
                    <div style="font-weight:600; color:#f8fafc;">Reminder sent (Email)</div>
                  </div>
                </div>
                <div style="display:flex; gap:12px;">
                  <span style="color:#64748b; width:40px;">10 Sep</span>
                  <div style="flex:1;">
                    <div style="font-weight:600; color:#f8fafc;">Customer replied: "Will pay Friday"</div>
                  </div>
                </div>
                <div style="display:flex; gap:12px;">
                  <span style="color:#64748b; width:40px;">13 Sep</span>
                  <div style="flex:1;">
                    <div style="font-weight:600; color:#ef4444;">Escalation recommended</div>
                  </div>
                </div>
              </div>'''

new_timeline = '''              <div id="colDetailsTimeline" style="font-size:0.75rem; color:#cbd5e1; display:flex; flex-direction:column; gap:12px; margin-bottom:20px;">
                <!-- Dynamic timeline will be populated here -->
                <p style="color:#64748b;">Please select a customer to view timeline.</p>
              </div>'''

if old_timeline in content:
    content = content.replace(old_timeline, new_timeline)
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Replaced static timeline with empty div container.')
else:
    print('Static timeline not found.')
