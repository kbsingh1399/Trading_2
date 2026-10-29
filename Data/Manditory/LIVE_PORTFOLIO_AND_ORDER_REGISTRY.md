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
- **Floating Equity**: **4,762.83 USD**
- **Free Margin**: **4,762.83 USD**
- **Margin Used**: **0.00 USD**
- **Hard Capital Floor**: **4,775.00 USD** (Statutory Drawdown Defense Floor | Deficit narrowed to: **-12.17 USD**)
- **Operating Buffer**: **4,795.00 USD** (Solvency Kernel Floor | Deficit narrowed to: **-32.17 USD**)
- **Active Running Positions**: **0 ACTIVE (100% Flat Cash)**
- **Active Resting Pending Orders**: **6 LIVE PENDING MAKER LIMIT ORDERS**
- **Total Contingent Downside Risk**: **42.87 USD** (Max per-ticket risk capped at <= 10.00 USD)
- **Execution Posture**: **ARMED_MAKER_LIMITS_ACTIVE**
- **Last Synchronized (UTC)**: `2026-10-29 20:52:00 UTC` (`2026-10-30 02:22:00 IST`)

---

## 🚀 2. LIVE RUNNING POSITIONS (0 ACTIVE — 100% FLAT CASH)

| Ticket | Symbol | Type | Volume | Entry Price | Current Price | Live SL | Live TP | Floating PnL | Dynamic Ratchet State | Interrogation: "Should I let it run or cut it?" |
|---|---|---|---|---|---|---|---|---|---|---|
| - | NONE | - | - | - | - | - | - | 0.00 USD | Flat | **Book is 100% Cash Defense. Zero open risk.** |

---

## 🎯 3. ACTIVE RESTING PENDING MAKER LIMIT ORDERS (6 LIVE BROKER TICKETS EXECUTED)

| Priority | Ticket | Symbol | Order Type | Volume | Limit Entry | Spread-Padded SL | Take Profit | Risk USD | Live Status & Forensic Liquidation Armor |
|---|---|---|---|---|---|---|---|---|---|
| **Resting #1** | `#19489155` | `BTCUSD.pi` | SELL_LIMIT | 0.01 lot | 81,084.00 | **81,680.00** | 80,180.00 | 5.96 USD | **LIVE_RESTING_PENDING** (SL placed +185 pts above 24H Short Max Pain 81,494.86 & +127 pts above 81,553 liq band) |
| **Resting #2** | `#19489157` | `BNBUSD.p` | SELL_LIMIT | 0.05 lot | 753.30 | **761.50** | 743.50 | 0.41 USD | **LIVE_RESTING_PENDING** (SL placed +3.19 pts above 24H Short Max Pain 758.31 & +1.60 pts above 759.90 liq band) |
| **Resting #3** | `#19489158` | `XAUUSD.pi` | SELL_LIMIT | 0.01 lot | 4040.50 | 4049.50 | 4018.00 | 9.00 USD | **LIVE_RESTING_PENDING** (Gold 0.20 bps spread, SL +3.12 pts clear of London High 4046.38 sweep zone) |
| **Resting #4** | `#19489159` | `NAS100.p` | SELL_LIMIT | 0.01 lot | 29,535.00 | 29,620.00 | 29,320.00 | 8.50 USD | **LIVE_RESTING_PENDING** (Nasdaq 0.34 bps spread, SL +13.51 pts beyond London High 29,606.49 sweep peak) |
| **Resting #5** | `#19489160` | `DJ30.p` | SELL_LIMIT | 0.01 lot | 52,638.00 | 52,732.00 | 52,402.00 | 9.40 USD | **LIVE_RESTING_PENDING** (Dow 30 0.23 bps spread, SL +136.66 pts above VAH, low-volume node rejection) |
| **Resting #6** | `#19490051` | `AUDUSD.pi` | BUY_LIMIT | 0.08 lot | 0.70270 | 0.70150 | 0.70570 | 9.60 USD | **LIVE_RESTING_PENDING** (0.14 bps spread, SL -3.0 pips below Asian Low 0.70180 retail sweep pocket) |

---

## 📈 4. RECENT CLOSED TRADES & SESSION EQUITY LOG
- **Ticket #19489156 (`USDJPY.pi` SELL 0.13 lot @ 157.970)**: Filled at VAH sweep (157.970) and **HIT TAKE PROFIT at 157.710 (+26.0 pips)** on `2026-10-29 20:10 UTC` for **+21.43 USD net profit** (+2.50R statistical win)!
- **Ticket #19489161 (`USWTI.p` BUY_LIMIT 0.01 lot @ 101.550)**: Cancelled and purged from MT5 on `2026-10-29 20:13 UTC` per unanimous Tri-Council finding (spread widened to 5.42 bps > 5.0 bps cap; VR(4) = 0.9673 random walk).
- **Ticket #19464650 (`BTCUSD.pi` SELL 0.01 @ 80,340.00, SL 80,563.50)**: Closed for -2.24 USD.
- **Account Solvency Summary**: Realized Balance: **4,762.83 USD** | Floating Equity: **4,762.83 USD** | Operating Buffer Deficit narrowed by +20.52 USD!
