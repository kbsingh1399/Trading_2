# ACTIVE CONTEXT CARD (LIVE SOVEREIGN QUANT DESK)
**Last Updated**: 2026-10-27 16:00:30 IST (2026-10-27 10:30:30 UTC) | **Session**: Cycle 371 Active | Sentry Iteration 26 | 36 Parquet Pure Lake
**Target Account**: Blueberry Markets MT5 Account #5064568 (SVG-Live, raw spread)
**Mission**: Pass Phase 1 Challenge (Target: 5,500.00 USD).

---

## 1. REAL-TIME ACCOUNT TELEMETRY & SOLVENCY SENTRY
- **Balance / Equity**: **4,837.08 USD** / **4,837.08 USD** (Floating PnL: **0.00 USD**)
- **Margin Used / Free Margin**: **0.00 USD** / **4,837.08 USD**
- **Margin Utilization**: **0.00%** (Strictly <= 50.00% statutory ceiling: PASS)
- **Margin Level**: **0.00%** (Flat, zero margin risk: PASS)
- **Active Running Positions**: **0 positions** (BNBUSD.p Ticket #19329907 closed at SL 732.65 USD with controlled 10.80 USD loss).
- **Active Pending Limit Orders (2 Orders)**:
  1. **Ticket #19330613**: `ETHUSD.pi` SELL_LIMIT 0.50 lot @ **2,320.50** (SL: 2,343.50, TP: 2,274.50)
     - Risk: 11.50 USD nominal / 14.38 USD stressed | Margin Req: ~580.00 USD
     - Microstructure: High-confluence VAL rejection setup backed by resting whale ask block.
     - Status: **RESTING**.
  2. **Ticket #19343853**: `SOLUSD.p` SELL_LIMIT 0.20 lot @ **100.38** (SL: 100.94, TP: 99.20)
     - Risk: 0.11 USD nominal / 0.14 USD stressed | Margin Req: ~20.00 USD
     - Microstructure: Local shelf retest with negative taker divergence.
     - Status: **RESTING**.
- **Inviolable Triple Floor Governance**:
  - Hard Floor: **4,775.00 USD** (Cushion: **+62.08 USD**)
  - Operating Defense Buffer: **4,795.00 USD** (Cushion: **+42.08 USD**)
  - Global Contingency Reserve: **2.00 USD** (deducted ex-ante)
  - Net Realized Headroom: **+40.08 USD**
  - Joint Stressed Risk of 2 Resting Limits: **14.52 USD** (Worst-case post-loss equity: **4,822.56 USD** -> Preserves 4,795.00 USD operating floor by +27.56 USD).
- **Capital Regime**: **TIER 1 STANDARD** (10.00-12.00 USD nominal risk per ticket).
- **Dynamic Capacity**: **4 slots available** for new entries.

---

## 2. 100% PURE PARQUET DATA LAKE (36 FEEDS) & INSTANT GIT PUSH
- **Total Parquet Feeds**: 36 canonical production feeds in `Data/feeds/*.parquet`. Zero Excel dependencies.
- **Automatic Metadata Stamping**: `Terminal/Data_Factory/stamp_all_parquet_feeds.py` stamps all 42 Parquet feeds with current cycle UTC/IST metadata prior to commit.
- **Synchronized Git Sync**: Every data collection cycle immediately commits and pushes all Parquet feeds, metadata, cycle envelopes, and trade plans to GitHub `origin main`. All feeds update simultaneously ("now") on GitHub.
- **Quad-Council Architecture**:
  1. **Arena.ai Sovereign Council**: GPT-5.4 Astra / Frontier Model (via Chrome CDP Port 9222)
  2. **Z.ai Sovereign Council**: GLM-5.3-Flash / Claude 3.7 Sonnet (via Chrome CDP Port 9222)
  3. **Gemini-4 Argon High Council**: Institutional Deep Reasoning (via Web2API port 8081 `gemini-4-argon-high`)
  4. **Antigravity 4-Quant Subagents**: Roles A, B, C, D (Executed In-Context per Operator Token Preservation Pivot)

---

## 3. CANONICAL GOVERNANCE SPECIFICATIONS (DATA/MANDITORY/)
All canonical governance specifications are verified, active, and synchronized in `Data/Manditory/` and `docs/specs/`:
1. `Data/Manditory/AUTONOMOUS_WAKEUP_CHECKLIST.md` (Mandatory Master Autonomous Wake-Up Sequence)
2. `Data/Manditory/ACCOUNT_SWITCH_BOOTSTRAP_PROTOCOL.md` (Universal Turn-0 Reconnection Protocol)
3. `Data/Manditory/SUBAGENT_PROMPT_TEMPLATES.md` (4-Quant Subagent Roles: Role A, B, C, D)
4. `Data/Manditory/ARENA_AI_STANDARD_PROMPT_TEMPLATE.md` (Exhaustive prompt architecture for Arena.ai across all 36 feeds)
5. `Data/Manditory/Z_AI_STANDARD_PROMPT_TEMPLATE.md` (Exhaustive adversarial prompt architecture for Z.ai across all 36 feeds)
6. `Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md` (10-Step Standardized Trading Decision Chain SOP)
7. `Data/Manditory/TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md` (10 lethal execution traps & prevention)
8. `Data/Manditory/CONTINUOUS_KAIZEN_SELF_IMPROVEMENT_PROTOCOL.md` (PDCA-Omega self-improvement protocol)
9. `Data/Manditory/32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md` (Socratic audit questions per data domain)

---

## 4. OPERATOR DIRECTIVE & AUTONOMOUS WAKEUP INSTRUCTION
- **Wakeup Protocol**: On every wakeup (from dynamic post-cycle timers or the standing 0th/30th minute cron), the agent MUST immediately read and follow `Data/Manditory/AUTONOMOUS_WAKEUP_CHECKLIST.md`.
- **Token Preservation Pivot**: Process `SUBAGENT_PROMPT_TEMPLATES.md` directly in-context across all 4 quantitative roles (Role A, Role B, Role C, Role D) rather than launching multiple external subagent processes, eliminating 429 quota exhaustion while guaranteeing 100% mathematical fidelity.
- **Continuous Timer Chaining**: The desk NEVER stops running autonomously. There must ALWAYS be an active timer scheduled for the next cycle upon completing current cycle synthesis.

---

## 5. ACTIVE HEPTAD DAEMONS & PERSISTENT TASKS
1. **Task 1**: `autonomous_telemetry_git_daemon.py --interval 60` (`isDaemon=true`, pushes to GitHub every 60s)
2. **Task 2**: `gemini_web2api.py` on port 8081 (`isDaemon=true`, Endogen architecture)
3. **Task 3**: `run_graphify_watcher.py` (`isDaemon=true`, AST graph updater)
4. **Task 4**: `run_pipeline_continuous_daemon.py --gap 120` (`isDaemon=true`, collects 36 feeds & stamps metadata)
5. **Task 5**: `dual_completion_daemon.py --daemon` (`isDaemon=true`, monitors CDP 9222, auto-harvests & refreshes tabs)
6. **Task 6**: `dynamic_position_supervisor.py` (`isDaemon=true`, dynamic 4-fill capacity limit & auto-pull)
7. **Task 7**: Standing Watchdog Sentry Cron (`schedule` cron `0,30 * * * *`, `isDaemon=true`, wakes desk at :00 and :30)

---

## 6. MULTI-ASSET CANDIDATE RADAR (METALS, INDICES, FOREX, CRYPTO)
The desk actively screens across all 4 core asset classes on Blueberry Markets MT5 (#5064568):
1. **Precious Metals**:
   - `XAUUSD.pi` (Gold): Live Price 4,009.84 USD | Spread 0.08 USD (0.20 bps) | 15m ATR 7.11 USD | 15m RSI 56.1.
     * Bullish EMA20 Pullback Setup: Entry BUY_LIMIT @ 4,002.00 USD, SL @ 3,991.33 USD (10.67 USD distance = 1.5 ATR), TP @ 4,018.00 USD (+16.00 USD gain = 1.5R). Size: 0.01 lot. Planned Risk: 10.67 USD.
   - `XAGUSD.pi` (Silver): Price 53.37 USD | Spread 6.75 bps | 15m RSI 68.0.
2. **Major Equity Indices**:
   - `NAS100.p` (Nasdaq 100): Live Price 29,363.65 USD | Spread 1.06 USD (0.36 bps) | 15m ATR 60.20 pts | 15m RSI 73.1 (Overbought Exhaustion).
     * Mean Reversion Fade Setup: Entry SELL_LIMIT @ 29,440.00 USD, SL @ 29,530.30 USD (90.30 pts = 1.5 ATR), TP @ 29,260.00 USD (EMA20 shelf, +180 pts = 2.0R). Size: 0.01 lot. Planned Risk: 9.03 USD.
   - `GER40.p` (DAX 40): Price 25,491.35 EUR | Spread 0.80 EUR (0.31 bps) | 15m RSI 72.9 (Overbought).
     * Mean Reversion Fade Setup: Entry SELL_LIMIT @ 25,535.00 EUR, SL @ 25,607.28 EUR (72.28 pts = 1.5 ATR), TP @ 25,395.00 EUR (+140 pts = 1.94R). Size: 0.01 lot. Planned Risk: 8.06 USD.
   - `SP500.p` (S&P 500): Price 7,692.47 USD | Spread 0.30 USD (0.39 bps) | 15m RSI 66.9.
3. **Foreign Exchange (FX Majors)**:
   - `EURUSD.pi`: Live Price 1.11470 | Spread 0.00001 (0.09 bps) | 15m ATR 0.0007 | 15m RSI 30.2 (Deeply Oversold).
     * Mean Reversion Bounce Setup: Entry BUY_LIMIT @ 1.11360, SL @ 1.11260 (10 pips = 1.4 ATR), TP @ 1.11560 (20 pips = 2.0R). Size: 0.11 lot. Planned Risk: 11.00 USD.
   - `AUDUSD.pi`: Live Price 0.70330 | Spread 0.00001 (0.14 bps) | 15m ATR 0.0005 | 15m RSI 75.2 (Extreme Overbought).
     * Mean Reversion Fade Setup: Entry SELL_LIMIT @ 0.70355, SL @ 0.70425 (7 pips = 1.4 ATR), TP @ 0.70215 (14 pips = 2.0R). Size: 0.15 lot. Planned Risk: 10.50 USD.
4. **Crypto CFDs & Perpetuals**:
   - `BTCUSD.pi`: Price 79,879 USD | Spread 1.88 bps | 15m RSI 60.2 | 15m ATR 213.18 USD.
   - `ETHUSD.pi`: Active resting SELL_LIMIT Ticket #19330613 @ 2,320.50 USD (SL 2,343.50, TP 2,274.50, Risk 11.50 USD).
   - `SOLUSD.p`: Active resting SELL_LIMIT Ticket #19343853 @ 100.38 USD (SL 100.94, TP 99.20, Risk 0.11 USD).
