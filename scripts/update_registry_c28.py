with open('Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Update Section 1
old_s1 = """## 🏛️ 1. ACCOUNT SOLVENCY & CAPITAL METRICS
- **Broker & Account**: Blueberry Markets MT5 Account #5064568 (`BlueberryMarketsSVG-Live`, Raw Spread)
- **Account Balance**: **4,762.83 USD**
- **Floating Equity**: **4,767.47 USD**
- **Free Margin**: **4,580.08 USD**
- **Margin Used**: **187.39 USD**
- **Hard Capital Floor**: **4,775.00 USD** (Statutory Drawdown Defense Floor | Deficit compressed to: **-7.53 USD**)
- **Operating Buffer**: **4,795.00 USD** (Solvency Kernel Floor | Deficit: **-27.53 USD**)
- **Capital Allocation Posture**: **TIER_0_DEFENSIVE** (`new_risk_admissible = false`)
- **Active Tickets Total**: 1 Running Runner + 5 Resting Maker Limits = 6 MT5 Tickets"""

new_s1 = """## 🏛️ 1. ACCOUNT SOLVENCY & CAPITAL METRICS
- **Broker & Account**: Blueberry Markets MT5 Account #5064568 (`BlueberryMarketsSVG-Live`, Raw Spread)
- **Account Balance**: **4,763.23 USD**
- **Floating Equity**: **4,763.23 USD**
- **Free Margin**: **4,763.23 USD**
- **Margin Used**: **0.00 USD**
- **Hard Capital Floor**: **4,775.00 USD** (Statutory Drawdown Defense Floor | Deficit: **-11.77 USD**)
- **Operating Buffer**: **4,795.00 USD** (Solvency Kernel Floor | Deficit: **-31.77 USD**)
- **Capital Allocation Posture**: **TIER_0_DEFENSIVE** (`new_risk_admissible = false`)
- **Active Tickets Total**: 0 Running Positions + 5 Resting Maker Limits = 5 MT5 Tickets"""

if old_s1 in text:
    text = text.replace(old_s1, new_s1)

# Update Section 2
old_s2 = """## 🚀 2. LIVE RUNNING POSITIONS (1 ACTIVE — RISK-FREE RATCHET LOCKED)

| Ticket | Symbol | Type | Volume | Entry Price | Current Price | Live SL | Live TP | Floating PnL | Dynamic Ratchet State | Interrogation: "Should I let it run or cut it?" |
|---|---|---|---|---|---|---|---|---|---|---|
| **#19490051** | `AUDUSD.pi` | BUY | 0.08 lot | `0.70270` | `0.70328` | `0.70282` | `0.70570` | `+4.64 USD` | **BE+ Locked (+1.09R Gain)** | **LET RUN. Early-BE ratchet successfully executed on MT5! SL moved to 0.70282 (+1.2 pips above entry). Trade is 100% risk-free ex-ante. Floating profit expanding (+1.09R) toward +1.50R target (0.70450). TP: 0.70570 (+2.5R).** |"""

new_s2 = """## 🚀 2. LIVE RUNNING POSITIONS (0 ACTIVE — BANKED IN GREEN VIA RATCHET)

| Ticket | Symbol | Type | Volume | Entry Price | Exit Price | Exit SL | Realized PnL | Dynamic Ratchet Exit Outcome |
|---|---|---|---|---|---|---|---|---|
| **#19490051** | `AUDUSD.pi` | BUY | 0.08 lot | `0.70270` | `0.70282` | `0.70282` | **+0.96 USD (+0.40 USD net)** | **CLOSED IN PROFIT VIA RATCHET (+1.2 pips). Stop loss locked in green protected gains. Realized capital banked into balance (4,763.23 USD).** |

*(Currently 0 active running positions. 100% capital preserved in cash under TIER_0_DEFENSIVE posture).*"""

if old_s2 in text:
    text = text.replace(old_s2, new_s2)

with open('Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md cleanly!')
