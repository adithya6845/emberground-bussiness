import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Make timeline dynamic in row click handler
old_row_click = '''          tr.onclick = () => {
            selectedCollectionsCustomer = { name: item.CustomerName || 'Unknown', amount: amount, fmtAmount: fmtAmount, overdue: overdue };
            document.getElementById('colDetailsName').innerText = `Customer Details - ${item.CustomerName || 'Unknown'}`;
            document.getElementById('colDetailsOutstanding').innerHTML = `Outstanding: <strong style="color:#ef4444;">${fmtAmount}</strong> · <strong style="color:#ef4444;">${overdue} days overdue</strong>`;
            const riskSpan = document.getElementById('colDetailsRisk');
            riskSpan.style.display = 'inline-block';
            riskSpan.style.color = riskColor;
            riskSpan.style.background = riskBg;
            riskSpan.innerText = `${risk} Risk`;
            document.getElementById('colDetailsRec').innerText = `Customer has delayed payment by ${overdue} days. Recommend sending a follow-up email with ${fmtAmount} pending.`;
          };'''

new_row_click = '''          tr.onclick = () => {
            selectedCollectionsCustomer = { name: item.CustomerName || 'Unknown', amount: amount, fmtAmount: fmtAmount, overdue: overdue };
            document.getElementById('colDetailsName').innerText = `Customer Details - ${item.CustomerName || 'Unknown'}`;
            document.getElementById('colDetailsOutstanding').innerHTML = `Outstanding: <strong style="color:#ef4444;">${fmtAmount}</strong> · <strong style="color:#ef4444;">${overdue} days overdue</strong>`;
            const riskSpan = document.getElementById('colDetailsRisk');
            riskSpan.style.display = 'inline-block';
            riskSpan.style.color = riskColor;
            riskSpan.style.background = riskBg;
            riskSpan.innerText = `${risk} Risk`;
            document.getElementById('colDetailsRec').innerText = `Customer has delayed payment by ${overdue} days. Recommend sending a follow-up email with ${fmtAmount} pending.`;
            
            // Dynamic Timeline
            const today = new Date();
            const formatDate = (daysAgo) => {
              const d = new Date(today);
              d.setDate(d.getDate() - daysAgo);
              return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short' });
            };
            
            const terms = parseInt(item.PaymentTermsDays) || 30;
            const invoiceDate = formatDate(overdue + terms);
            const reminderDate = formatDate(Math.max(2, overdue - 5));
            
            // Generate timeline HTML
            let timelineHtml = `
              <div style="display:flex; gap:12px;">
                <span style="color:#64748b; width:45px;">${invoiceDate}</span>
                <div style="flex:1;">
                  <div style="font-weight:600; color:#f8fafc;">Invoice generated</div>
                  <div style="color:#64748b;">${fmtAmount}</div>
                </div>
              </div>
            `;
            
            if (overdue > 5) {
              timelineHtml += `
              <div style="display:flex; gap:12px;">
                <span style="color:#64748b; width:45px;">${reminderDate}</span>
                <div style="flex:1;">
                  <div style="font-weight:600; color:#f8fafc;">Reminder sent (Email)</div>
                </div>
              </div>
              `;
            }
            
            if (overdue > 15) {
               timelineHtml += `
               <div style="display:flex; gap:12px;">
                 <span style="color:#64748b; width:45px;">${formatDate(2)}</span>
                 <div style="flex:1;">
                   <div style="font-weight:600; color:#ef4444;">Escalation recommended</div>
                 </div>
               </div>
               `;
            }
            
            const timelineContainer = document.getElementById('colDetailsTimeline');
            if(timelineContainer) timelineContainer.innerHTML = timelineHtml;
          };'''

content = content.replace(old_row_click, new_row_click)
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated row click with dynamic timeline HTML generation.')
