import re

with open('Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Update Equity and Deficit
text = re.sub(r"- \*\*Floating Equity\*\*: \*\*4,774\.11 USD\*\*", "- **Floating Equity**: **4,773.47 USD**", text)
text = re.sub(r"Deficit compressed to: \*\*-0\.89 USD\*\*", "Deficit compressed to: **-1.53 USD**", text)
text = re.sub(r"Deficit compressed to: \*\*-20\.89 USD\*\*", "Deficit compressed to: **-21.53 USD**", text)
text = re.sub(r"- \*\*Free Margin\*\*: \*\*4,586\.72 USD\*\*", "- **Free Margin**: **4,586.08 USD**", text)
text = re.sub(r"- \*\*Last Synchronized \(UTC\)\*\*: `2026-10-30 04:00:00 UTC`", "- **Last Synchronized (UTC)**: `2026-10-30 04:45:00 UTC`", text)
text = re.sub(r"`2026-10-30 09:30:00 IST`", "`2026-10-30 10:15:00 IST`", text)

# Update AUDUSD row
text = re.sub(r"\| `0\.70411` \| `0\.70282` \| `0\.70570` \| `\+11\.28 USD` \|", "| `0.70403` | `0.70282` | `0.70570` | `+10.64 USD` |", text)

with open('Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md for Cycle_025 successfully.")
