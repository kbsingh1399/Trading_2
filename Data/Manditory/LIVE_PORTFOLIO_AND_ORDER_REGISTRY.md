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
- **Active Resting Pending Orders**: **3 ACTIVE** (High-confluence maker limit orders placed per Tri-Council)
- **Total Contingent Downside Risk**: **25.62 USD**
- **Execution Posture**: **ARMED_MAKER_LIMITS (N=3 <= 3, Total Risk = 25.62 USD)**
- **Last Synchronized (UTC)**: 2026-10-30 10:50:00 UTC (2026-10-30 16:20:00 IST)

---

## 🚀 2. LIVE RUNNING POSITIONS (0 ACTIVE — BANKED IN GREEN)

| Ticket | Symbol | Type | Volume | Entry Price | Exit Price | Exit SL | Realized PnL | Dynamic Ratchet Exit Outcome |
|---|---|---|---|---|---|---|---|---|
| **#19490051** | `AUDUSD.pi` | BUY | 0.08 lot | `0.70270` | `0.70282` | `0.70282` | **+0.96 USD (+0.40 USD net)** | **CLOSED IN PROFIT VIA RATCHET (+1.2 pips). Banked into balance (4,763.23 USD).** |

*(Currently 0 active running positions. Capital deployed strictly in resting maker limit orders).*

---

## 🎯 3. ACTIVE RESTING PENDING MAKER LIMIT ORDERS (3 ACTIVE — ARMED ON BROKER)

| Ticket | Symbol | Order Type | Volume | Limit Entry | Spread-Padded SL | Take Profit | R:R Ratio | Nominal Risk USD | Confluence Rationale & Status |
|---|---|---|---|---|---|---|---|---|---|
| **#19520222** | `BTCUSD.pi` | SELL_LIMIT | 0.02 lot | `78,962.00` | `79,318.00` | `78,072.00` | **2.500R** | 7.12 USD | **ACTIVE_ON_BROKER** (`retcode=10009`). Daily VAH sweep fade + $16.3M Ask wall at 81.5k. |
| **#19520223** | `XAUUSD.pi` | SELL_LIMIT | 0.01 lot | `4,007.50` | `4,017.00` | `3,983.70` | **2.505R** | 9.50 USD | **ACTIVE_ON_BROKER** (`retcode=10009`). Gold Daily VAH sweep fade + 0.20 bps spread. |
| **#19520224** | `AUDUSD.pi` | BUY_LIMIT | 0.15 lot | `0.70240` | `0.70180` | `0.70390` | **2.500R** | 9.00 USD | **ACTIVE_ON_BROKER** (`retcode=10009`). Daily VAL sweep fade + 0.14 bps spread. |

*Total contingent downside risk across all 3 resting orders: **25.62 USD** (Capacity $N=3 \le 3$, each trade $\le 10.00$ USD risk).*

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
