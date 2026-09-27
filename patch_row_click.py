import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Add selected customer variable
content = content.replace(
    "function openCollectionsAgentModal() {\n",
    "function openCollectionsAgentModal() {\n  let selectedCollectionsCustomer = null;\n"
)

# Update row click logic
old_row_logic = '''
          const tr = document.createElement('tr');
          tr.style.cssText = 'border-bottom:1px solid #1e293b; cursor:pointer;';
          tr.innerHTML = `
            <td style="padding:12px 8px; font-weight:500; color:#f8fafc;">${item.CustomerName || 'Unknown'}</td>
            <td style="padding:12px 8px;">${fmtAmount}</td>
            <td style="padding:12px 8px;">${overdue}</td>
            <td style="padding:12px 8px;"><span style="color:${riskColor}; background:${riskBg}; padding:2px 6px; border-radius:4px; font-size:0.7rem;">${risk}</span></td>
            <td style="padding:12px 8px;">${status}</td>
          `;
          tbody.appendChild(tr);'''

new_row_logic = '''
          const tr = document.createElement('tr');
          tr.style.cssText = 'border-bottom:1px solid #1e293b; cursor:pointer;';
          tr.innerHTML = `
            <td style="padding:12px 8px; font-weight:500; color:#f8fafc;">${item.CustomerName || 'Unknown'}</td>
            <td style="padding:12px 8px;">${fmtAmount}</td>
            <td style="padding:12px 8px;">${overdue}</td>
            <td style="padding:12px 8px;"><span style="color:${riskColor}; background:${riskBg}; padding:2px 6px; border-radius:4px; font-size:0.7rem;">${risk}</span></td>
            <td style="padding:12px 8px;">${status}</td>
          `;
          tr.onclick = () => {
            selectedCollectionsCustomer = { name: item.CustomerName || 'Unknown', amount: amount, fmtAmount: fmtAmount, overdue: overdue };
            document.getElementById('colDetailsName').innerText = `Customer Details - ${item.CustomerName || 'Unknown'}`;
            document.getElementById('colDetailsOutstanding').innerHTML = `Outstanding: <strong style="color:#ef4444;">${fmtAmount}</strong> · <strong style="color:#ef4444;">${overdue} days overdue</strong>`;
            const riskSpan = document.getElementById('colDetailsRisk');
            riskSpan.style.display = 'inline-block';
            riskSpan.style.color = riskColor;
            riskSpan.style.background = riskBg;
            riskSpan.innerText = `${risk} Risk`;
            document.getElementById('colDetailsRec').innerText = `Customer has delayed payment by ${overdue} days. Recommend sending a follow-up email with ${fmtAmount} pending.`;
          };
          tbody.appendChild(tr);'''

content = content.replace(old_row_logic, new_row_logic)

# Update button click
old_btn = '''
    const btnApprove = $('btnCollectionsApproveSend');
    if (btnApprove) {
      btnApprove.onclick = async () => {
        btnApprove.innerText = "Sending...";
        btnApprove.style.opacity = '0.7';
        btnApprove.disabled = true;
        try {
          const res = await fetch('/api/collections-action', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ customer_name: 'Rahul Stores', action: 'send_email' })
          });
          const data = await res.json();
          if (res.ok) {
            showToast('success', 'Email Sent', 'Collections reminder email sent successfully to Rahul Stores.');'''

new_btn = '''
    const btnApprove = $('btnCollectionsApproveSend');
    if (btnApprove) {
      btnApprove.onclick = async () => {
        if (!selectedCollectionsCustomer) {
           showToast('error', 'Error', 'Please select a customer first.');
           return;
        }
        btnApprove.innerText = "Sending...";
        btnApprove.style.opacity = '0.7';
        btnApprove.disabled = true;
        try {
          const res = await fetch('/api/collections-action', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ 
              customer_name: selectedCollectionsCustomer.name, 
              amount: selectedCollectionsCustomer.fmtAmount,
              action: 'send_email' 
            })
          });
          const data = await res.json();
          if (res.ok) {
            showToast('success', 'Email Sent', `Collections reminder email sent successfully to ${selectedCollectionsCustomer.name}.`);'''

content = content.replace(old_btn, new_btn)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print('Patched app.js for row clicks')
