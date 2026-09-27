import re

with open('api.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_endpoint = '''
class CollectionsActionRequest(BaseModel):
    customer_name: str
    action: str

@app.post("/api/collections-action")
def api_collections_action(req: CollectionsActionRequest):
    if req.action == "send_email":
        # Simulate sending the email via DronaHQ Webhook
        prompt = f"Send a collections reminder email to {req.customer_name} for their pending payment."
        try:
            # We call the webhook
            ask_dronahq(prompt)
            return JSONResponse({"status": "success", "message": "Email sent successfully."})
        except Exception as e:
            return JSONResponse({"status": "error", "message": str(e)}, status_code=500)
    
    return JSONResponse({"status": "error", "message": "Unknown action"}, status_code=400)
'''

insert_target = 'def api_chat(req: ChatRequest):'
insert_idx = content.find(insert_target)

if insert_idx != -1:
    content = content[:insert_idx] + new_endpoint + '\n\n' + content[insert_idx:]
    with open('api.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Added /api/collections-action endpoint to api.py')
else:
    print('Failed to find insertion point in api.py')
