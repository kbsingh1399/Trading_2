import re

with open('Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Update Equity and Deficit
text = re.sub(r"- \*\*Floating Equity\*\*: \*\*4,773\.47 USD\*\*", "- **Floating Equity**: **4,767.47 USD**", text)
text = re.sub(r"Deficit compressed to: \*\*-1\.53 USD\*\*", "Deficit compressed to: **-7.53 USD**", text)
text = re.sub(r"Deficit compressed to: \*\*-21\.53 USD\*\*", "Deficit compressed to: **-27.53 USD**", text)
text = re.sub(r"- \*\*Free Margin\*\*: \*\*4,586\.08 USD\*\*", "- **Free Margin**: **4,580.08 USD**", text)
text = re.sub(r"- \*\*Last Synchronized \(UTC\)\*\*: `2026-10-30 04:45:00 UTC`", "- **Last Synchronized (UTC)**: `2026-10-30 05:25:00 UTC`", text)
text = re.sub(r"`2026-10-30 10:15:00 IST`", "`2026-10-30 10:55:00 IST`", text)

# Update AUDUSD row
text = re.sub(r"\| `0\.70403` \| `0\.70282` \| `0\.70570` \| `\+10\.64 USD` \|", "| `0.70328` | `0.70282` | `0.70570` | `+4.64 USD` |", text)

with open('Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md for Cycle_026 successfully.")
