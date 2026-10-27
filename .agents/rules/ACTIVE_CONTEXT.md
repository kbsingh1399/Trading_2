# ACTIVE CONTEXT CARD (LIVE SOVEREIGN QUANT DESK)
**Last Updated**: 2026-10-28 01:00:00 IST (2026-10-27 19:30:00 UTC) | **Session**: Multi-Asset Portfolio Supervision & Autonomous Cron Iteration 2 | In-House Antigravity Fleet Active
**Target Account**: Blueberry Markets MT5 Account #5064568 (SVG-Live, raw spread)
**Mission**: Pass Phase 1 Challenge (Target: 5,500.00 USD).

---

## 1. REAL-TIME ACCOUNT TELEMETRY & SOLVENCY SENTRY
- **Balance / Equity**: **4,833.47 USD** / **4,830.84 USD** (Floating PnL: **-2.63 USD**)
- **Margin Used / Free Margin**: **1,072.27 USD** / **3,758.57 USD**
- **Margin Utilization**: **22.18%** (Strictly <= 50.00% statutory ceiling: PASS)
- **Margin Level**: **450.5%** (Inviolable invariant >= 200.0%: PASS)
- **Active Running Positions**: **2 Positions (Model 1 Mean Reversion & Model 2 Pullback)**:
  - Ticket `#19376039`: `USDJPY.pi` SELL `0.08 lots` @ `157.850` | Current: `157.905` | PnL: **-2.79 USD** | SL: `158.024` | TP: `157.450` (Nominal Risk: `8.81 USD`)
  - Ticket `#19379711`: `BTCUSD.pi` SELL `0.02 lots` @ `80560.00` | Current: `80552.00` | PnL: **+0.16 USD (IN PROFIT)** | SL: `80860.00` | TP: `79910.00` (Nominal Risk: `6.00 USD`)
- **Active Pending Limit Orders**: **3 Resting Maker Limit Orders (Strict 4-Filled Auto-Pull Invariant)**:
  - Ticket `#19384166`: `UKBRENT.p` SELL_LIMIT `0.12 lots` @ `115.400` (SL: `115.980`, TP: `113.943`, Risk: `6.96 USD`, Commodities/Energy - Cluster 4, 0.946 pts away).
  - Ticket `#19384254`: `AUDNZD.pi` SELL_LIMIT `0.07 lots` @ `1.23675` (SL: `1.23825`, TP: `1.23300`, Risk: `6.30 USD`, Australasian Non-USD Cross, 7.7 pips away).
  - Ticket `#19384256`: `XAUUSD.pi` BUY_LIMIT `0.01 lots` @ `4,020.25` (SL: `4,013.00`, TP: `4,051.75`, Risk: `7.25 USD`, Precious Metals - Cluster 3, 40.75 pts away).
- **Inviolable Triple Floor & Capacity Governance**:
  - Hard Floor: **4,775.00 USD** (Statutory DD Stop)
  - Operating Defense Buffer: **4,795.00 USD** (Internal Risk Defense)
  - Floor Cushion: **+35.84 USD** to 4,795.00 USD buffer | **+55.84 USD** to 4,775.00 USD hard floor.
  - Autonomous Cron Task: Running on `0,20,40 * * * *` (20th, 40th, and 60th minutes of every hour) for continuous asset screening, candidate discovery, and stale limit purges.
  - Active Supervisor Daemon: Strictly enforces `MAX_FILLED_POSITIONS = 4`. The instant filled positions reach 4, all remaining resting limit orders are automatically pulled.
  - Multi-Asset Orthogonality: Each active ticket sits in a distinct, uncorrelated macro cluster (Crypto, USD FX, Energy, Australasian Cross, Metals), eliminating cluster concentration risk.
- **Capital Regime**: **TIER 1 STANDARD** (8.00-10.00 USD nominal risk per ticket).
- **Dynamic Capacity**: **4 concurrent filled slots allowed** (2 slots filled: #19376039 USDJPY, #19379711 BTCUSD; 2 slots free); **Pre-fill stressed solvency gate strictly active**.

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
