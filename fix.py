import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "detailsContainer.innerHTML = `"
end_marker = "});\n  }"
start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx) + len(end_marker)

new_html = r"""detailsContainer.innerHTML = `
      <div style="display:flex; flex-direction:column; gap:20px;">
        
        <!-- Header -->
        <div>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
            <h3 style="margin:0; font-size:1.4rem; font-weight:700; color:#f8fafc;">${p.name}</h3>
            <span style="background:${p.badgeColor}; color:#fff; font-size:0.8rem; padding:4px 12px; border-radius:6px; font-weight:600;">${p.badge}</span>
          </div>
          <p style="margin:0; color:#94a3b8; font-size:0.9rem; line-height:1.5;">${p.desc}</p>
        </div>

        <!-- DATA INSIGHTS -->
        <div>
          <p style="margin:0 0 10px 0; font-size:0.8rem; color:#64748b; font-weight:700; text-transform:uppercase; letter-spacing:0.5px;">DATA INSIGHTS</p>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
            <div style="background:#0b1121; padding:12px 16px; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
              <span style="color:#94a3b8; font-size:0.85rem;">Current Price</span>
              <span style="color:#f8fafc; font-weight:600;">${insights.currentPrice}</span>
            </div>
            <div style="background:#0b1121; padding:12px 16px; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
              <span style="color:#94a3b8; font-size:0.85rem;">Sales (This Month)</span>
              <span style="color:#f8fafc; font-weight:600;">${insights.sales}</span>
            </div>
            <div style="background:#0b1121; padding:12px 16px; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
              <span style="color:#94a3b8; font-size:0.85rem;">Cost Price</span>
              <span style="color:#f8fafc; font-weight:600;">${insights.costPrice}</span>
            </div>
            <div style="background:#0b1121; padding:12px 16px; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
              <span style="color:#94a3b8; font-size:0.85rem;">Sales Growth</span>
              <span style="color:#10b981; font-weight:600;">${insights.growth}</span>
            </div>
            <div style="background:#0b1121; padding:12px 16px; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
              <span style="color:#94a3b8; font-size:0.85rem;">Current Margin</span>
              <span style="color:#f8fafc; font-weight:600;">${insights.currentMargin}</span>
            </div>
            <div style="background:#0b1121; padding:12px 16px; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
              <span style="color:#94a3b8; font-size:0.85rem;">Price Elasticity</span>
              <span style="color:#f59e0b; font-weight:600;">${insights.elasticity}</span>
            </div>
            <div style="background:#0b1121; padding:12px 16px; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
              <span style="color:#94a3b8; font-size:0.85rem;">Competitor Avg Price</span>
              <span style="color:#f8fafc; font-weight:600;">${insights.compPrice}</span>
            </div>
            <div style="background:#0b1121; padding:12px 16px; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
              <span style="color:#94a3b8; font-size:0.85rem;">Demand Trend</span>
              <span style="color:#10b981; font-weight:600;">${insights.trend}</span>
            </div>
          </div>
        </div>

        <!-- GEMMA ANALYSIS -->
        <div>
          <p style="margin:0 0 10px 0; font-size:0.8rem; color:#64748b; font-weight:700; text-transform:uppercase; letter-spacing:0.5px;">GEMMA ANALYSIS</p>
          <div style="background:rgba(99,102,241,0.1); border-left:4px solid #6366f1; padding:16px; border-radius:0 8px 8px 0; border:1px solid rgba(99,102,241,0.2);">
            <p style="margin:0; font-size:0.9rem; color:#e2e8f0; line-height:1.5;">${p.gemma || 'Based on demand trend, competitor pricing, and low price sensitivity, increasing price by 5-7% can increase monthly profit by ₹18.6L - ₹24.4L, without affecting volume significantly.'}</p>
          </div>
        </div>

        <!-- EXPECTED IMPACT -->
        <div>
          <p style="margin:0 0 10px 0; font-size:0.8rem; color:#64748b; font-weight:700; text-transform:uppercase; letter-spacing:0.5px;">EXPECTED IMPACT</p>
          <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:12px;">
            ${impacts.map(imp => `<div style="background:#0b1121; padding:16px; border-radius:8px; text-align:center; border:1px solid #1e293b;"><div style="color:#64748b; font-size:0.7rem; font-weight:700; text-transform:uppercase; margin-bottom:8px;">${imp.label}</div><div style="color:${imp.color}; font-size:1.1rem; font-weight:700;">${imp.val}</div></div>`).join('')}
          </div>
        </div>
      </div>
    `;
  }"""

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + new_html + content[end_idx:]
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Replaced successfully')
else:
    print('Markers not found')
