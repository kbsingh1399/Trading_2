import re

with open('Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Update Equity and Deficit
text = re.sub(r"- \*\*Floating Equity\*\*: \*\*4,773\.31 USD\*\*", "- **Floating Equity**: **4,774.11 USD**", text)
text = re.sub(r"Deficit compressed to: \*\*-1\.69 USD\*\*", "Deficit compressed to: **-0.89 USD**", text)
text = re.sub(r"Deficit compressed to: \*\*-21\.69 USD\*\*", "Deficit compressed to: **-20.89 USD**", text)
text = re.sub(r"- \*\*Free Margin\*\*: \*\*4,585\.92 USD\*\*", "- **Free Margin**: **4,586.72 USD**", text)

# Update AUDUSD row
text = re.sub(r"\| `0\.70401` \| `0\.70282` \| `0\.70570` \| `\+10\.48 USD` \|", "| `0.70411` | `0.70282` | `0.70570` | `+11.28 USD` |", text)

with open('Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md successfully.")
