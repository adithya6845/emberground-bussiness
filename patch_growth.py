import re

with open('api.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert format_with_nvidia to just return empty string on fail
old_nvidia = '''    except:
        pass
        
    return f"Subject: Payment Reminder\\n\\nDear Customer,\\n\\nThis is a polite reminder that your payment is currently overdue. Please process the pending amount at your earliest convenience to avoid any late fees.\\n\\nThank you,\\nCollections Team"'''
new_nvidia = '''    except:
        pass
        
    return ""'''
if old_nvidia in content:
    content = content.replace(old_nvidia, new_nvidia)

# 2. Fix the Collections endpoint to supply the email if NVIDIA fails
old_collections = '''            email_body = format_with_nvidia(system_prompt, user_prompt)
            
            # Send the generated email via DronaHQ Webhook'''
new_collections = '''            email_body = format_with_nvidia(system_prompt, user_prompt)
            if not email_body:
                email_body = f"Subject: Payment Reminder\\n\\nDear {req.customer_name},\\n\\nThis is a polite reminder that your payment of {req.amount} is currently overdue. Please process the pending amount at your earliest convenience to avoid any late fees.\\n\\nThank you,\\nCollections Team"
            
            # Send the generated email via DronaHQ Webhook'''
if old_collections in content:
    content = content.replace(old_collections, new_collections)

# 3. Fix the Growth Advisor fallback to use basic heuristics
old_growth = '''    except Exception as e:
        print("LLM Growth Simulator Error:", str(e))
        return JSONResponse({
            "name": req.query[:25] if len(req.query) <= 25 else req.query[:22] + "...",
            "title": f"Scenario: {req.query}",
            "badge": "AI Simulated",
            "badgeColor": "#8b5cf6",
            "desc": f"Simulated growth trajectory for '{req.query}'. Balances sales volume growth with cost efficiency.",
            "volumeChg": 7.5,
            "priceChg": 3.5,
            "costChg": -2.0,
            "marketingChg": 4.0
        })'''

new_growth = '''    except Exception as e:
        print("LLM Growth Simulator Error:", str(e))
        import re
        q = req.query.lower()
        
        # Simple heuristics
        v_chg = 0.0
        p_chg = 0.0
        c_chg = 0.0
        m_chg = 0.0
        
        # Extract any numbers from query
        nums = re.findall(r'\\d+\\.?\\d*', q)
        val = float(nums[0]) if nums else 5.0
        
        if 'decrease cost' in q or 'reduce cost' in q or 'cost reduction' in q or 'cost decreases' in q or 'cost of tomato' in q:
            c_chg = -val
        elif 'increase price' in q or 'raise price' in q:
            p_chg = val
            v_chg = -(val * 0.2) # Elasticity
        elif 'increase sales' in q or 'increase volume' in q:
            v_chg = val
        elif 'marketing' in q:
            m_chg = val
            v_chg = val * 0.8
        else:
            v_chg = val
            
        return JSONResponse({
            "name": req.query[:25] if len(req.query) <= 25 else req.query[:22] + "...",
            "title": f"Scenario: {req.query}",
            "badge": "Heuristic Engine",
            "badgeColor": "#f59e0b",
            "desc": f"Calculated scenario for '{req.query}'. Showing isolated impact without assuming unrelated growth.",
            "volumeChg": v_chg,
            "priceChg": p_chg,
            "costChg": c_chg,
            "marketingChg": m_chg
        })'''
if old_growth in content:
    content = content.replace(old_growth, new_growth)

with open('api.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Patched api.py")
