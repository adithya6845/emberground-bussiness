import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_btn_logic = '''          if (res.ok) {
            showToast('success', 'Email Sent', `Collections reminder email sent successfully to ${selectedCollectionsCustomer.name}.`);
            modal.style.display = 'none';'''

new_btn_logic = '''          if (res.ok) {
            if (data.email_body) {
                const subject = encodeURIComponent(`Payment Reminder - ${selectedCollectionsCustomer.name}`);
                const body = encodeURIComponent(data.email_body);
                window.location.href = `mailto:?subject=${subject}&body=${body}`;
            }
            showToast('success', 'Email Sent', `Collections reminder email generated for ${selectedCollectionsCustomer.name}.`);
            modal.style.display = 'none';'''

if old_btn_logic in content:
    content = content.replace(old_btn_logic, new_btn_logic)
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched app.js with mailto logic")
else:
    print("Could not find old_btn_logic")
