# ACTIVE CONTEXT CARD (LIVE SOVEREIGN QUANT DESK)
**Last Updated**: 2026-10-23 05:00:00 UTC | **Autonomous Cycle**: Cycle 295 (Cycle 295 Parallel Dual-Council Deliberation / European Pre-Market Standby)
**Target Account**: Blueberry Markets MT5 Account #5064568
**Mission**: Pass Phase 1 Challenge (Target: 5,500.00 USD) before Oct 23, 2026 (23:59 UTC) (~19.00 hours runway remaining).

---

## 1. REAL-TIME ACCOUNT TELEMETRY & SOLVENCY SENTRY
- **Balance / Equity**: 4,818.51 USD / 4,818.51 USD (100% Flat Cash Defense)
- **Margin / Free Margin**: 0.00 USD / 4,818.51 USD (0.00% utilization)
- **Goal Gap**: +681.49 USD to 5,500.00 USD (+14.14%)
- **Hard Floor (Inviolate)**: 4,775.00 USD | **Floor Cushion**: +43.51 USD
- **Operating Buffer Floor**: 4,795.00 USD | **Buffer Cushion**: +23.51 USD
- **Active Filled Positions**: 0/4 consumed | **Resting Pending Orders**: 0/10 (100% Clean Book)
- **Fluid Capacity Available**: 4/4 filled slots free, 10 resting limit slots free
- **Single-Slot Risk Law**: Active. Dynamic risk capacity: max 16.81 USD nominal risk under current buffer cushion.

---

## 2. CANONICAL 156-ASSET SCREENER UPGRADE & HARMONIZATION
- **Upgraded Screener (`Terminal/institutional_95_screener.py`)**:
  * Ingests canonical 156-asset universe from `Data/Assets/mt5_full_symbol_universe.json`.
  * Dynamic spread friction baselines: Crypto <= 35 bps, Exotics <= 25 bps, Commodities/Indices <= 10 bps, Forex <= 6 bps.
  * Relative Spread Cannibalization Gate: Spread / TP Distance <= 15.0%.
  * Live broker lot snapping via `mt5.order_calc_profit()` guaranteeing buffer surplus >= 0.
  * Completed benchmark in 0.646s across 106 eligible symbols, identifying 30 qualified setups.
- **Harmonized 4-Quant Subagent Swarm (`Data/Manditory/SUBAGENT_PROMPT_TEMPLATES.md`)**:
  1. Statistical Regime & Diffusion Quant (Lo-MacKinlay VR, Kaufman ER, NW t-stat, First-Exit TTL)
  2. Microstructure & Liquidation Quant (LIR, L2/L3 whale persistence >= 180s, stop sweeps, CVD)
  3. Convex Portfolio & Solvency Sentry (EV, broker order_calc_profit sizing, stressed buffer sentry)
  4. Auction Profile & Friction Arbitrageur (Sheet 33 VAH/VAL/POC, relative friction gate <= 10%)

---

## 3. LIVE MULTI-ASSET RADAR QUEUE (PRE-LONDON EXPANSION)
1. **`GER40.p` — European Cash Session Auction Short (Arena #1 Ranked Index Setup)**:
   - Sizing: `SELL_LIMIT 0.03 to 0.06 lot @ 25,321.66 to 25,381.39` | SL: 25,345.69 to 25,420.23 | TP: 25,261.57 to 25,286.79 | 2.44R to 3.00R
   - Risk: Nominal -$13.05 to -$16.16 USD | Stressed Loss: -$18.65 to -$22.20 USD | Stressed Equity: 4,796.31 to 4,799.86 USD (Positive buffer surplus).
   - Timing Trigger: European Pre-market stage at 06:45 UTC (15m before Frankfurt cash open). Strict PMI exit clock at 07:14:59 UTC ahead of Eurozone PMIs (07:15–08:00 UTC).
2. **`SP500.p` — US Index Trend Pullback Short**:
   - Sizing: `SELL_LIMIT 0.22 lot @ 7,658.80` | SL: 7,666.17 (7.37 pts) | TP: 7,640.37 (18.43 pts) | 2.50R
   - Risk: -$16.22 USD | Nominal Reward: +$40.55 USD | Stressed Equity: 4,796.24 USD (+1.24 USD surplus).
3. **`NAS100.p` — US Tech Trend Pullback Short**:
   - Sizing: `SELL_LIMIT 0.03 lot @ 28,963.11` | SL: 29,016.02 (52.91 pts) | TP: 28,830.84 (132.27 pts) | 2.50R
   - Risk: -$15.87 USD | Nominal Reward: +$39.68 USD | Stressed Equity: 4,796.67 USD (+1.67 USD surplus).
4. **`BTCUSD.pi` — Repaired Asian High Resistance Short**:
   - Geometry: `SELL_LIMIT 0.03 lot @ 81,960.00` | SL: 82,374.19 (414.19 pts) | TP: 80,890.43 (1,069.57 pts) | 2.58R
   - Risk: -$12.43 USD | Nominal Reward: +$32.09 USD | Stressed Equity: 4,800.97 USD (+5.97 USD buffer surplus).
   - Resting behind verified $20.15M ask wall at 81,950–82,000.
5. **`XAGUSD.pi` — Silver Trend Pullback Short**:
   - Sizing: `SELL_LIMIT 0.01 lot @ 54.01` | SL: 54.223 | TP: 53.476 | 2.50R
   - Risk: -$10.68 USD | Nominal Reward: +$26.69 USD | Buffer Surplus: +$8.16 USD.

---

## 4. PARALLEL DUAL-COUNCIL TRACKING
- **Arena.ai**: Prompt injected (Cycle 295, 5,884 chars), currently generating via Chrome CDP.
- **Z.ai (GLM-5.3-Flash)**: Monitored via Task 110203.
- **Gemini Web2API**: Background council task running on port 8081.
