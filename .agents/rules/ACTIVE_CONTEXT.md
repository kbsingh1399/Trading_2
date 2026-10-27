# ACTIVE CONTEXT CARD (LIVE SOVEREIGN QUANT DESK)
**Last Updated**: 2026-10-27 22:20:00 IST (2026-10-27 16:50:00 UTC) | **Session**: Multi-Asset Portfolio Supervision & Screener | In-House Antigravity Fleet Active
**Target Account**: Blueberry Markets MT5 Account #5064568 (SVG-Live, raw spread)
**Mission**: Pass Phase 1 Challenge (Target: 5,500.00 USD).

---

## 1. REAL-TIME ACCOUNT TELEMETRY & SOLVENCY SENTRY
- **Balance / Equity**: **4,833.47 USD** / **4,832.37 USD** (Floating PnL: **-1.10 USD**)
- **Margin Used / Free Margin**: **1,073.56 USD** / **3,759.91 USD**
- **Margin Utilization**: **22.20%** (Strictly <= 50.00% statutory ceiling: PASS)
- **Margin Level**: **450.1%** (Inviolable invariant >= 200.0%: PASS)
- **Active Running Positions**: **2 Positions (Model 1 Mean Reversion & Model 2 Pullback)**:
  - Ticket `#19376039`: `USDJPY.pi` SELL `0.08 lots` @ `157.850` | Current: `157.896` | PnL: **-2.33 USD** | SL: `158.024` | TP: `157.450` (Risk: `8.81 USD`)
  - Ticket `#19379711`: `BTCUSD.pi` SELL `0.02 lots` @ `80560.00` | Current: `80498.50` | PnL: **+1.23 USD (IN PROFIT)** | SL: `80860.00` | TP: `79910.00` (Risk: `6.00 USD`)
- **Active Pending Limit Orders**: **2 Resting Maker Limit Orders**:
  - Ticket `#19378313`: `UKBRENT.p` SELL_LIMIT `0.20 lots` @ `115.175` (SL: `115.668`, TP: `113.943`, Risk: `9.86 USD`, Commodities/Energy).
  - Ticket `#19381300`: `XAUUSD.pi` BUY_LIMIT `0.01 lots` @ `4033.00` (SL: `4025.50`, TP: `4051.75`, Risk: `7.50 USD`, Precious Metals Raw).
- **Inviolable Triple Floor Governance**:
  - Hard Floor: **4,775.00 USD** (Cushion: **+58.47 USD** -> 100% Intact)
  - Operating Defense Buffer: **4,795.00 USD** (Cushion: **+38.47 USD** -> 100% Intact)
  - Total Joint Stressed Risk (all 4 orders): **32.17 USD**
  - Stressed Worst-Case Equity: **4,801.30 USD** (+26.30 USD above Hard Floor, +6.30 USD above Operating Buffer)
- **Capital Regime**: **TIER 1 STANDARD** (10.00-12.00 USD nominal risk per ticket).
- **Dynamic Capacity**: **4 concurrent filled slots allowed** (3 slots free, 1 filled: #19376039); **N resting limit orders allowed** (3 active: #19378313, #19379711, #19381300).

---

## 2. 100% PURE PARQUET DATA LAKE (36 FEEDS) & ATOMIC OVERWRITE INVARIANT
- **Total Parquet Feeds**: 42 production feeds in `Data/feeds/*.parquet` (all verified present, 0 nulls, stamped fresh < 5.0m).
- **Zero-Deletion Protocol**: Feeds are NEVER deleted or unlinked from disk. All updates use atomic `os.replace` from temporary files.
- **Truncation Guarantee**: In-place overwriting resets file size to 0 bytes upon open; writing 90 rows completely replaces 100 rows with zero remnant records.
- **In-House Antigravity 4-Agent Quant Fleet**:
  1. **Agent 1: Statistical Diffusion & Regime Gatekeeper**: Lo-MacKinlay `VR(4)` (N >= 120 bars, `|z*| >= 1.96` required to reject random walk), `ER(48)` with regime hysteresis, Newey-West HAC drift `|t_drift| < 1.5`, OU mean drift.
  2. **Agent 2: Microstructure, CVD & Adverse Selection Sentry**: Anti-winner's-curse passivity filter, anti-short-squeeze delta inversion gate (negative CVD on rising prices is a short squeeze, not exhaustion), L2/L3 orderbook asymmetry (> +0.25 / < -0.25), persistent whale armor (>= 100K USD, tau >= 180s).
  3. **Agent 3: Liquidation Geometry, Stop Hunt & Auction Profile Quant**: Stops placed safely outside the 1.0–1.5 ATR liquidity sweep zone, cumulative liquidation ladders, max pain magnets, Daily/Weekly Volume Profile VPOC/VAH/VAL.
  4. **Agent 4: Solvency, Execution & Dynamic Ratchet Supervisor**: MT5 account telemetry verification (#5064568), 4,775.00 USD hard floor defense, single-trade risk capped at 10.00 USD, dynamic ratchet actuation (+0.80R to BE +/- 0.15R, +1.50R to +/- 0.80R lock, 6h time decay exit).

---

## 3. CANONICAL GOVERNANCE SPECIFICATIONS (DATA/MANDITORY/)
All canonical governance specifications are verified, active, and synchronized in `Data/Manditory/`:
1. `Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md` (Canonical In-House Antigravity Quantitative Decision Architecture)
2. `Data/Manditory/TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md` (Forensic Pitfall Directory including Gold Stop-Out Inquest)
3. `Data/Manditory/32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md` (Risk Checklist)
4. `Data/Manditory/SUBAGENT_PROMPT_TEMPLATES.md` (4-Quant Subagent Roles: Role A, B, C, D)
