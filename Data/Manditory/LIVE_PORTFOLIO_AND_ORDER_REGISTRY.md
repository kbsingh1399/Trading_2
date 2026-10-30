# 📊 LIVE PORTFOLIO & ORDER REGISTRY
**Authoritative Real-Time Position, Order & Solvency Registry**
*Maintained Continuously by Antigravity Autonomous Position Supervisor*

> **GOVERNANCE PURPOSE**:
> This registry serves as the single source of truth for all live running positions, resting pending maker limit orders, locked-in profit ratchets, and banked session profits.
> It is automatically updated by the dynamic position supervisor daemon and pushed to GitHub main every 60 seconds (`https://github.com/kbsingh1399/Trading_2.git`).
> 
> **RAW GITHUB FETCH URL FOR ARENA.AI & Z.AI**:
> `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md`

---

## 🏛️ 1. ACCOUNT SOLVENCY & CAPITAL METRICS
- **Broker & Account**: Blueberry Markets MT5 Account #5064568 (`BlueberryMarketsSVG-Live`, Raw Spread)
- **Account Balance**: **4,762.83 USD**
- **Floating Equity**: **4,768.35 USD**
- **Free Margin**: **4,580.96 USD**
- **Margin Used**: **187.39 USD**
- **Hard Capital Floor**: **4,775.00 USD** (Statutory Drawdown Defense Floor | Deficit compressed to: **-6.65 USD**)
- **Operating Buffer**: **4,795.00 USD** (Solvency Kernel Floor | Deficit compressed to: **-26.65 USD**)
- **Active Running Positions**: **1 ACTIVE (AUDUSD.pi Long)**
- **Active Resting Pending Orders**: **5 LIVE PENDING MAKER LIMIT ORDERS**
- **Total Contingent Downside Risk**: **42.87 USD** (Max per-ticket risk capped at <= 10.00 USD)
- **Execution Posture**: **ARMED_MAKER_LIMITS_ACTIVE**
- **Last Synchronized (UTC)**: `2026-10-30 02:30:00 UTC` (`2026-10-30 08:00:00 IST`)

---

## 🚀 2. LIVE RUNNING POSITIONS (1 ACTIVE — TIER 0 DEFENSIVE)

| Ticket | Symbol | Type | Volume | Entry Price | Current Price | Live SL | Live TP | Floating PnL | Dynamic Ratchet State | Interrogation: "Should I let it run or cut it?" |
|---|---|---|---|---|---|---|---|---|---|---|
| **#19490051** | `AUDUSD.pi` | BUY | 0.08 lot | `0.70270` | `0.70339` | `0.70150` | `0.70570` | `+5.52 USD` | Floating in Profit (+0.58R) | **LET RUN. Sits at Asian Range Low / VAL support. Price holding firmly (+15.8 pips off low of 0.70181); 5m CVD buying (+83% delta) defending. Advancing toward +0.80R BE lock at 0.70366.** |

---

## 🎯 3. ACTIVE RESTING PENDING MAKER LIMIT ORDERS (5 LIVE BROKER TICKETS EXECUTED)

| Priority | Ticket | Symbol | Order Type | Volume | Limit Entry | Spread-Padded SL | Take Profit | Risk USD | Live Status & Forensic Liquidation Armor |
|---|---|---|---|---|---|---|---|---|---|
| **Resting #1** | `#19489155` | `BTCUSD.pi` | SELL_LIMIT | 0.01 lot | 81,084.00 | **81,680.00** | 80,180.00 | 5.96 USD | **LIVE_RESTING_PENDING** (SL placed +185 pts above 24H Short Max Pain 81,494.86 & +127 pts above 81,553 48H peak. Leans against PD_VAH 81,003.11) |
| **Resting #2** | `#19489157` | `BNBUSD.p` | SELL_LIMIT | 0.05 lot | 753.30 | **761.50** | 743.50 | 0.41 USD | **LIVE_RESTING_PENDING** (SL placed +3.01 pts above 24H Short Max Pain 758.49. Aligned with Weekly VAH 751.13 and PD_VAH 754.57) |
| **Resting #3** | `#19489158` | `XAUUSD.pi` | SELL_LIMIT | 0.01 lot | 4,040.50 | **4,049.50** | 4,018.00 | 9.00 USD | **LIVE_RESTING_PENDING** (SL leans against 4,050.00 institutional ask wall. Fades PD_VAH 4,039.67 sweep exhaustion. Purged to raw +2.5R target) |
| **Resting #4** | `#19489159` | `NAS100.p` | SELL_LIMIT | 0.01 lot | 29,535.00 | **29,620.00** | 29,320.00 | 8.50 USD | **LIVE_RESTING_PENDING** (SL padded by 85 index points. Leans against Low Volume Node above PD_VAH 29,520.00. Risk strictly <= 10.00 USD) |
| **Resting #5** | `#19489160` | `DJ30.p` | SELL_LIMIT | 0.01 lot | 52,638.00 | **52,732.00** | 52,402.00 | 9.40 USD | **LIVE_RESTING_PENDING** (SL padded by 94 index points. Leans against exhaustion node above PD_VAH 52,579.18. Risk strictly <= 10.00 USD) |

---

## 🛡️ 4. ANTI-RETRACEMENT PROFIT RATCHET PROTOCOL
- **Tier 1 (BE Lock)**: At `+0.80R` gain ($0.70366$ on AUDUSD.pi), move Stop Loss to Entry `+0.15R` ($0.70288$).
- **Tier 2 (Profit Lock)**: At `+1.50R` gain ($0.70450$ on AUDUSD.pi), move Stop Loss to Entry `+0.80R` ($0.70366$).
- **Tier 3 (Terminal Exit)**: At `+2.50R` target ($0.70570$ on AUDUSD.pi), close position for full statistical profit extraction.
- **Time Decay Rule**: If trade produces `< +0.20R` within 24 bars (6 hours), close at market.
