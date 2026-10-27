# ACTIVE CONTEXT CARD (LIVE SOVEREIGN QUANT DESK)
**Last Updated**: 2026-10-27 19:50:00 IST (2026-10-27 14:20:00 UTC) | **Session**: Post-Trade Autopsy Complete | In-House Antigravity Fleet Active
**Target Account**: Blueberry Markets MT5 Account #5064568 (SVG-Live, raw spread)
**Mission**: Pass Phase 1 Challenge (Target: 5,500.00 USD).

---

## 1. REAL-TIME ACCOUNT TELEMETRY & SOLVENCY SENTRY
- **Balance / Equity**: **4,826.99 USD** / **4,826.99 USD** (Floating PnL: **0.00 USD**)
- **Margin Used / Free Margin**: **0.00 USD** / **4,826.99 USD**
- **Margin Utilization**: **0.00%** (Strictly <= 50.00% statutory ceiling: PASS)
- **Margin Level**: **N/A (No Open Debt)** (Inviolable invariant >= 200.0%: PASS)
- **Active Running Positions**: **1 Position (Model 2 Trend Following Short)**:
  - Ticket: `#19376886` | Symbol: `GBPUSD.pi` | Side: `SELL` | Volume: `0.12 lots`
  - Open Price: `1.33242` | Current Quote: `1.33195` | Floating PnL: **+5.64 USD (+0.62R)**
  - Attached Protective Bracket: SL = `1.33318` | TP = `1.33051` (2.51 R:R)
  - Dynamic Ratchet: Armed. Stage 1 ratchet (+0.15R lock) triggers at price <= 1.33181 (+0.80R).
  - *Previous Trade Autopsy*: Ticket #19367388 (`XAUUSD.pi` Short 0.01 lot @ 4024.95 USD) stopped out at **4034.97 USD** at 14:04:31 UTC. Loss: **-10.02 USD** nominal (-10.09 USD total). Stop loss executed at broker level with 0 slippage.
- **Active Pending Limit Orders**: **1 Order (Model 1 Mean Reversion)**:
  - Ticket `#19376039`: `USDJPY.pi` SELL_LIMIT `0.08 lots` @ `157.850` (SL: `158.024`, TP: `157.450`, Risk: `8.81 USD`).
- **Inviolable Triple Floor Governance**:
  - Hard Floor: **4,775.00 USD** (Cushion: **+51.99 USD** -> 100% Intact)
  - Operating Defense Buffer: **4,795.00 USD** (Cushion: **+31.99 USD** -> 100% Intact)
  - Global Contingency Reserve: **2.00 USD** (deducted ex-ante)
  - Net Realized Headroom: **+29.99 USD**
- **Capital Regime**: **TIER 1 STANDARD** (10.00-12.00 USD nominal risk per ticket).
- **Dynamic Capacity**: **4 concurrent filled slots allowed** (3 slots free, 1 filled: #19376886); **N resting limit orders allowed** (1 active: #19376039).

---

## 2. 100% PURE PARQUET DATA LAKE (36 FEEDS) & ATOMIC OVERWRITE INVARIANT
- **Total Parquet Feeds**: 42 production feeds in `Data/feeds/*.parquet` (all verified present, 0 nulls).
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
