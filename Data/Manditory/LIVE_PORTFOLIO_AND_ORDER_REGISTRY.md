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
- **Account Balance**: **4,763.23 USD**
- **Floating Equity**: **4,763.23 USD**
- **Free Margin**: **4,763.23 USD**
- **Margin Used**: **0.00 USD**
- **Hard Capital Floor**: **4,775.00 USD** (Statutory Drawdown Defense Floor | Deficit: **-11.77 USD**)
- **Operating Buffer**: **4,795.00 USD** (Solvency Kernel Floor | Deficit: **-31.77 USD**)
- **Active Running Positions**: **0 ACTIVE** (100% Cash Defense)
- **Active Resting Pending Orders**: **0 ACTIVE** (All resting limit orders cancelled on MT5 per Tri-Council consensus)
- **Total Contingent Downside Risk**: **0.00 USD**
- **Execution Posture**: **FLAT_100_PERCENT_CASH_DEFENSE (TIER_0_DEFENSIVE)**
- **Last Synchronized (UTC)**: 2026-10-30 09:21:00 UTC (2026-10-30 14:51:00 IST)

---

## 🚀 2. LIVE RUNNING POSITIONS (0 ACTIVE — BANKED IN GREEN)

| Ticket | Symbol | Type | Volume | Entry Price | Exit Price | Exit SL | Realized PnL | Dynamic Ratchet Exit Outcome |
|---|---|---|---|---|---|---|---|---|
| **#19490051** | `AUDUSD.pi` | BUY | 0.08 lot | `0.70270` | `0.70282` | `0.70282` | **+0.96 USD (+0.40 USD net)** | **CLOSED IN PROFIT VIA RATCHET (+1.2 pips). Banked into balance (4,763.23 USD).** |

*(Currently 0 active running positions. 100% capital preserved in cash under TIER_0_DEFENSIVE posture).*

---

## 🎯 3. ACTIVE RESTING PENDING MAKER LIMIT ORDERS (0 ACTIVE — 100% FLAT)

*(Zero pending orders resting on MT5. Total contingent risk = 0.00 USD).*

---

### 🚫 CANCELLED / REMOVED ORDERS IN CYCLE_029 & CYCLE_030 (Tri-Council Solvency Enforcement):
| Ticket | Symbol | Original Order | Limit Entry | Original SL | Original TP | R:R Ratio | Cancellation Rationale & Broker Confirmation |
|---|---|---|---|---|---|---|---|
| `#19489158` | `XAUUSD.pi` | SELL_LIMIT | 4,040.50 | 4,049.50 | 4,018.00 | **2.500R** | **CANCELLED ON MT5 (`retcode=10009`, Request executed)**. Cycle_030 Tri-Council unanimous consensus: eliminate contingent downside risk ($9.00) under TIER_0_DEFENSIVE floor deficit (-11.77 USD) ahead of weekend rollover. |
| `#19489159` | `NAS100.p` | SELL_LIMIT | 29,535.00 | 29,620.00 | 29,320.00 | **2.529R** | **CANCELLED ON MT5 (`retcode=10009`, Request executed)**. Cycle_030 Tri-Council unanimous consensus: entry stale vs fresh VAH (Δ673.91), eliminate contingent downside risk ($8.50) ahead of weekend rollover. |
| `#19489160` | `DJ30.p` | SELL_LIMIT | 52,638.00 | 52,732.00 | 52,402.00 | **2.511R** | **CANCELLED ON MT5 (`retcode=10009`, Request executed)**. Cycle_030 Tri-Council unanimous consensus: entry stale vs fresh VAH (Δ270.77), eliminate contingent downside risk ($9.40) ahead of weekend rollover. |
| `#19489155` | `BTCUSD.pi` | SELL_LIMIT | 81,084.00 | 81,680.00 | 80,180.00 | **1.517R** | **CANCELLED ON MT5 (`retcode=10009`)**. Violated statutory 2.5R minimum mandate. Reduced risk by 5.96 USD. |
| `#19489157` | `BNBUSD.p` | SELL_LIMIT | 753.30 | 761.50 | 743.50 | **1.195R** | **CANCELLED ON MT5 (`retcode=10009`)**. Violated statutory 2.5R minimum mandate. Reduced risk by 0.41 USD. |

---

## 🛡️ 4. ANTI-RETRACEMENT PROFIT RATCHET PROTOCOL
- **Tier 1 (BE Lock - EXECUTED)**: Reached `+0.80R` gain ($0.70370$ on AUDUSD.pi). Stop Loss moved to `0.70282` (+1.2 pips in profit).
- **Tier 2 (Profit Lock)**: At `+1.50R` gain ($0.70450$ on AUDUSD.pi), move Stop Loss to Entry `+0.80R` ($0.70366$).
- **Tier 3 (Terminal Exit)**: At `+2.50R` target ($0.70570$ on AUDUSD.pi), close position for full statistical profit extraction.
- **Time Decay Rule**: If trade produces `< +0.20R` within 24 bars (6 hours), close at market.
