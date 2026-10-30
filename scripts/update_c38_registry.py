p = 'Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

target = """- **Account Balance**: **4,755.23 USD**
- **Floating Equity**: **4,755.23 USD**
- **Free Margin**: **4,755.23 USD**
- **Margin Used**: **0.00 USD**
- **Capital Posture**: **ACTIVE_HIGH_CONFLUENCE_OPERATION (Operator Mandate: Hard floor lifted)**
- **Active Running Positions**: **0 ACTIVE** (100% Cash Defense Preserved)
- **Active Resting Pending Orders**: **3 ACTIVE** (Staged per 15-Pillar Mechanical Forensics & Tri-Council Synthesis)
- **Total Contingent Downside Risk**: **18.10 USD** (0.38% of account equity)
- **Execution Capacity**: **3 / 3 Slots Deployed** (Maximum Concurrency Reached - 0 Slots Open)
- **Last Synchronized (UTC)**: 2026-10-30 15:20:30 UTC (2026-10-30 20:50:30 IST) - Cycle_037 Reconciled

---

## 🚀 2. RECENT CLOSED POSITIONS & HISTORICAL AUTOPSY

| Ticket | Symbol | Type | Volume | Entry Price | Exit Price | Exit Reason | Realized PnL | Forensic Autopsy & Risk Control |
|---|---|---|---|---|---|---|---|---|
| **#19532057** | `XMRUSD.p` | BUY | 0.01 lot | `585.50` | `577.50` | `SL Hit [sl 577.50]` | **-8.00 USD** | Filled Deal #17702967 (17:08:37 UTC) @ 585.50; exited Deal #17704303 (17:25:05 UTC) @ 577.50 during market-wide altcoin sweep. Downside strictly contained within $10.00 max limit ($8.00 loss = 0.16% equity). |
| **#19490051** | `AUDUSD.pi` | BUY | 0.08 lot | `0.70270` | `0.70282` | `Ratchet Exit` | **+0.96 USD** | Banked profit via automated trailing ratchet (+1.2 pips). |

*(Currently 0 active running positions. 100% cash flat defense active).*"""

replacement = """- **Account Balance**: **4,755.23 USD**
- **Floating Equity**: **4,774.28 USD** (Unrealized Profit: **+$19.05 USD**)
- **Free Margin**: **1,245.61 USD**
- **Margin Used**: **3,528.67 USD**
- **Capital Posture**: **ACTIVE_HIGH_CONFLUENCE_OPERATION (Live Positions in Green Profit + 3 Limit Orders Resting)**
- **Active Running Positions**: **2 ACTIVE** (Floating Profit: **+$19.05 USD**)
- **Active Resting Pending Orders**: **3 ACTIVE** (Staged per 15-Pillar Mechanical Forensics & Tri-Council Synthesis)
- **Total Contingent Downside Risk**: **18.10 USD** (0.38% of account equity)
- **Execution Capacity**: **Full Deployment** (2 Running Positions + 3 Maker Limit Orders)
- **Last Synchronized (UTC)**: 2026-10-30 15:43:00 UTC (2026-10-30 21:13:00 IST) - Cycle_038 Reconciled

---

## 🚀 2. LIVE ACTIVE RUNNING POSITIONS (2 ACTIVE — FLOATING GREEN +$19.05 USD)

| Ticket | Symbol | Type | Volume | Entry Price | Current Price | SL | TP | Floating PnL | Status & Management |
|---|---|---|---|---|---|---|---|---|---|
| **#19538719** | `BTCUSD.pi` | `SELL` | 0.01 lot | `77,709.50` | `77,404.50` | `78,025.08` | `Open` | **+$3.05 USD** | Active short fading local liquidity sweep; stop safely anchored above 78K high. |
| **#19539053** | `AVEUSD.p` | `SELL` | 0.50 lot | `125.54` | `125.22` | `Open` | `123.15` | **+$16.00 USD** | Active short fading high; target 123.15 aligns above 122.50 resting buy limit. |"""

if target in text:
    new_text = text.replace(target, replacement)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('Updated LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md successfully!')
else:
    print('Target not found in registry!')
