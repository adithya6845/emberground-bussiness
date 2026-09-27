import re

with open('api.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the rule-based block entirely from api_chat
# We will just replace it with `pass` so we don't have to regex match exactly.

# Find api_chat definition
def_idx = content.find('def api_chat(req: ChatRequest):')
if def_idx != -1:
    # Find the start of rule-based block
    rule_start = content.find('    # 1. Rule-based checks (Fast, deterministic)', def_idx)
    # Find the start of LLM Fallback block
    fallback_start = content.find('    if not bot_response:', rule_start)
    if rule_start != -1 and fallback_start != -1:
        # Erase everything between them
        content = content[:rule_start] + content[fallback_start:]
        print("Removed rule-based checks.")
        
# Fix the fallback to use DronaHQ response if NVIDIA fails
# The old code:
#             dronahq_response = ask_dronahq(full_query)
#             bot_response = format_with_nvidia(system_prompt, f"Raw data from DronaHQ:\n{dronahq_response}\n\nPlease format this to answer the user query: {req.message.strip()}")
#         except Exception as e:
#             print(f"LLM API Error: {e}")
#             # Context-aware intelligent fallback if network times out
#             if "tomato" in msg or "price" in msg:
# ...
#             else:
#                 bot_response = f"🤖 **Gemma AI Strategic Insight:**\n\n• **Revenue:** {kpis.get('totalRevenueFmt', '₹20.19Cr')} · **Health Score:** {kpis.get('healthScore', 82)}/100\n• **Collection Rate:** {kpis.get('collectionRate', 92.1)}% with {kpis.get('overdueAmount', '₹2.54Cr')} overdue.\n• **Actionable Advice:** Optimize procurement pricing with top vendors and maintain strict 15-day collection terms to boost working capital."
#
#     return JSONResponse({"response": bot_response})

fallback_find = '''        try:
            full_query = f"{system_prompt}\\n\\nUser Question: {req.message.strip()}"
            dronahq_response = ask_dronahq(full_query)
            bot_response = format_with_nvidia(system_prompt, f"Raw data from DronaHQ:\\n{dronahq_response}\\n\\nPlease format this to answer the user query: {req.message.strip()}")
        except Exception as e:
            print(f"LLM API Error: {e}")
            # Context-aware intelligent fallback if network times out
            if "tomato" in msg or "price" in msg:
                bot_response = f"📊 **Pricing & Trend Analysis:**\\n\\n• **Price Adjustment (-2%):** Reduces unit price from ₹10.00 to **₹9.80/kg**.\\n• **Demand Elasticity:** Low-to-moderate elasticity in fresh produce. Expected volume increase is **+3.5% to +5.0%**.\\n• **Gross Margin Impact:** Gross margin shifts from ~30.0% to **~28.6%**, but total gross revenue is protected by higher sales volume turnover.\\n• **Recommendation:** Maintain stock velocity and bundle with high-margin items (spices/oil) to maximize basket size."
            else:
                bot_response = f"🤖 **Gemma AI Strategic Insight:**\\n\\n• **Revenue:** {kpis.get('totalRevenueFmt', '₹20.19Cr')} · **Health Score:** {kpis.get('healthScore', 82)}/100\\n• **Collection Rate:** {kpis.get('collectionRate', 92.1)}% with {kpis.get('overdueAmount', '₹2.54Cr')} overdue.\\n• **Actionable Advice:** Optimize procurement pricing with top vendors and maintain strict 15-day collection terms to boost working capital."'''

fallback_replace = '''        try:
            full_query = f"{system_prompt}\\n\\nUser Question: {req.message.strip()}"
            dronahq_response = ask_dronahq(full_query)
            bot_response = format_with_nvidia(system_prompt, f"Raw data from DronaHQ:\\n{dronahq_response}\\n\\nPlease format this to answer the user query: {req.message.strip()}")
            if not bot_response:
                bot_response = dronahq_response
        except Exception as e:
            print(f"LLM API Error: {e}")
            bot_response = "I couldn't process that request right now."'''

if fallback_find in content:
    content = content.replace(fallback_find, fallback_replace)
    print("Replaced fallback block.")
else:
    print("Could not find fallback block.")
    
with open('api.py', 'w', encoding='utf-8') as f:
    f.write(content)

"
