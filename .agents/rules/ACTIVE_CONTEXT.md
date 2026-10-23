# ACTIVE CONTEXT CARD (LIVE SOVEREIGN QUANT DESK)
**Last Updated**: 2026-10-23 07:42:00 UTC | **Autonomous Cycle**: Cycle 296 Completed / Cycle 297 Trigger Armed (07:42:46 UTC)
**Target Account**: Blueberry Markets MT5 Account #5064568
**Mission**: Pass Phase 1 Challenge (Target: 5,500.00 USD) before Oct 23, 2026 (23:59 UTC) (~16.2 hours runway remaining).

---

## 1. REAL-TIME ACCOUNT TELEMETRY & SOLVENCY SENTRY
- **Balance / Equity**: 4,818.51 USD / 4,818.51 USD
- **Margin / Free Margin**: 0.00 USD / 4,818.51 USD (0.00% utilization)
- **Goal Gap**: +681.49 USD to 5,500.00 USD (+14.14%)
- **Hard Floor (Inviolate)**: 4,775.00 USD | **Floor Cushion**: +43.51 USD
- **Operating Buffer Floor**: 4,795.00 USD | **Buffer Cushion**: +23.51 USD
- **Active Filled Positions**: 0/4 consumed | **Resting Pending Orders**: 2/10 ACTIVE IN MT5
- **Fluid Capacity Available**: 4/4 filled slots free, 8 resting limit slots free
- **Worst-Case Simultaneous Stopout Equity**: 4,780.10 USD (+5.10 USD above 4,775.00 USD hard floor)

---

## 2. ACTIVE RESTING LIMIT ORDERS IN MT5 BROKER BOOK
1. **`Ticket #19244087` — `NZDUSD.pi` (Value Area Reclaim Buy Limit)**:
   - Order Type: `BUY_LIMIT` | Volume: `0.81 lot`
   - Entry: `0.56904` | Stop Loss: `0.56888` (16 pts / 1.6 pips) | Take Profit: `0.56965` (61 pts / 6.1 pips)
   - Risk: 12.96 USD | Reward: 49.41 USD | R:R: 3.81R
   - Stressed Loss: 20.23 USD | Post-Loss Equity: 4,798.28 USD (Buffer Surplus: +3.28 USD)
   - Friction Efficiency: Spread / TP Distance = 3.28% (Well under 10.0% cap)
   - Dynamic Ratchet: Early-BE @ 0.56916 -> move SL to 0.56906 (locks +1.62 USD profit, drops risk to 0 USD)

2. **`Ticket #19244096` — `BTCUSD.pi` (Structural Ask Wall Fade Sell Limit)**:
   - Order Type: `SELL_LIMIT` | Volume: `0.03 lot`
   - Entry: `81,960.00` | Stop Loss: `82,374.19` (414.19 pts) | Take Profit: `80,890.43` (1,069.57 pts)
   - Risk: 12.43 USD | Reward: 32.09 USD | R:R: 2.58R
   - Stressed Loss: 18.18 USD | Post-Loss Equity: 4,800.33 USD (Buffer Surplus: +5.33 USD)
   - Resting behind verified ask wall cluster at 81,950–82,000 USD.
   - Dynamic Ratchet: Early-BE @ 81,649.36 -> move SL to 81,918.58 (locks +1.24 USD profit)

---

## 3. RADAR QUEUE & POST-PMI RE-ARM TRIGGERS (08:35 UTC REOPEN)
1. **`GER40.p / GER30.p`**: European index complex re-audit at 08:35 UTC post-Eurozone Flash PMI (08:00 UTC).
2. **`Native XAGUSD`**: Spot silver re-audit at 54.01 USD shelf, discarding cross-currency clones (XAGSGD/XAGAUD).
3. **`SWISS20.p`**: Re-audit at 14,502 demand shelf post-08:35 UTC.

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
