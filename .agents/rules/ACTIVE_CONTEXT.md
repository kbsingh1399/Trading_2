---
trigger: always_on
---

# ⚡ ACTIVE OPERATIONAL CONTEXT & MISSION CONTROL CARD

> **ALWAYS-ON TURN-0 SITUATIONAL AWARENESS**
> Auto-injected on every turn. Eliminates context amnesia, retrieval latency, and model hallucination.

## 1. User Master Mandate (Strict & Non-Negotiable)
- **MANDATORY PREVIOUS CONVERSATION CONTEXT & TRAJECTORY REFERENCE (PERMANENT STEP-LEVEL INVARIANT)**: On EVERY single turn and before taking action on ANY step, the coordinator and all subagents MUST FIRST review the previous conversation history (`.agents/memory/session_chat_history.md`, past turns, transcript). You CANNOT take actions, audit orders, evaluate setups, or propose modifications in a vacuum. You MUST know the complete historical context, evolving operator rules, past rulings, avoided traps, and live position trajectory before evaluating or executing any step. Zero context amnesia.
- **CROSS-ACCOUNT RE-ENGAGEMENT & FULL NARRATIVE AUDIT (HYPERDASH / MULTI-ACCOUNT INVARIANT)**: Whenever the operator switches Gemini accounts and returns to the session chat, the agent MUST explicitly review all past session chat logs (`.agents/memory/session_chat_history.md`, transcript, and `ACTIVE_CONTEXT.md`) to establish total continuity of what we are trying to achieve, internalize all operator feedback, remember past setbacks, and preserve every nuance of the active quantitative mission before taking any action.
- **100% LOCAL QUANTITATIVE DEVELOPMENT & EXECUTION**: All prompt-generation for external agents (Ox Alpha / Arena) is permanently terminated. All engineering, econometric feature integration, model training, backtesting, and 20 OOS window optimization are executed right here locally in this environment.
- **MANDATORY BUY & HOLD BENCHMARKING**: ALWAYS compare strategy performance, equity curves, ROI, and drawdowns directly against the Buy and Hold benchmark (BTC Buy & Hold normalized to identical starting capital).
- **ZERO-HESITATION AUTONOMOUS PUNCH MANDATE (STRICT OPERATOR DIRECTIVE)**: NEVER ask the operator for permission to stage or execute orders. Whenever ANY candidate candle prints an eligible structural setup supported by rigorous quantitative reasoning, mathematical logic, resting L2/L3 whale backing, and capital floor defense under Model 1 (Extreme Mean Reversion) or Model 2 (VWAP Trend Pullbacks), IMMEDIATELY punch the passive limit order live into MetaTrader 5 without hesitation and without asking. Zero hesitation, zero latency, 100% autonomous execution.
- **MANDATORY GITHUB REPOSITORY LINK IN ALL PROMPTS (STRICT OPERATOR DIRECTIVE)**: Every single prompt generated for external models (Microsoft Copilot Studio / Claude Opus 5.5, Arena.ai) or internal subagents MUST ALWAYS prominently include the full GitHub repository URL (`https://github.com/kbsingh1399/Trading_2`), active branch (`main`), commit HEAD, and direct raw URLs for all referenced files (`session_chat_history.md`, `ACTIVE_CONTEXT.md`, `ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md`, `decision_gates_v3.py`, `ROUND2_THINKING_CHAIN_AUDIT.md`). No external or council prompt may ever be generated without full GitHub links so external models can inspect the real codebase via GitHub API/web and maintain total continuity with local repository state.
- **ZERO SPURIOUS SCRATCH LITTER**: Clean up all intermediate debug scripts immediately after validation.

## 2. Active Mission & Quantitative Target
- **Universe**: Certified Genuine 11 Binance USDT-M Perpetuals (BTC, ETH, XRP, BNB, DOGE, ADA, TRX, LINK, DOT, LTC, BCH) with 100% verified tick footprint ladders. The 7 synthetic assets are quarantined.
- **Active Focus**: Triple Trend-Following Orderflow Suite (Sleeve S1: Dual-Model Liquidation Pullback, Sleeve T1: Quiet-Flow Donchian Breakout) evaluated across all 20 Out-Of-Sample (OOS) Quarterly Windows (2021–2026).
- **Certified Pass Criteria**: Net ROI >= +10.00% (+500.00 USD net on 5,000.00 USD capital), Max Drawdown <= 5.00%, Win Rate >= 40.0%, Min Completed Trades >= 15 per quarter.
- **Production State**: 
  * Master Forex & CFD Pipeline audited through OX ALPHA 54 -> 55 -> 56 -> 57 (Commit: `9559471`). Scorecard upgraded to **8 / 8 / 6 / 8** (Architecture 8/10, Causal Soundness 8/10, Microstructure Realism 6/10, Production Readiness 8/10) with 64/64 cumulative verification checks passing (100%).
  * Paper and dry-run forward validation officially certified at score 8. Final funded-live promotion narrowed solely to R4 (deterministic walk-forward generator) and R6 (rolling purge/cutoff retraining). Prompt cycle complete (`Ox_Alpha_57` is the final prompt).
  * Master Forex & CFD Orchestration Suite (`Engine/forex_engine.py`, `Engine/live/run_forex_dry_run.py`, `Engine/live/order_manager.py`) fully hardened with P0 leverage caps (10:1/5:1/3:1), margin level/utilization circuit breakers, 4H causal shift(1) parity, state persistence, decoupled structural Take-Profit, correlation cluster governors, and spread/ATR hysteresis quarantine (Commit: `c6ef13c`).
  * Master Forex & CFD Orchestration Engine (`Engine/forex_engine.py`, `Engine/FVG_ML_ForexCFD_Strategy.py`, `Engine/ORB_CRT_ForexCFD_Strategy.py`) officially achieved **10/10 Institutional Production Certification** from Ox Alpha / Arena (Commit: `3ecc253` / `81a3a79`).
  * 0.00e+00 Polars-Pandas feature parity certified, 15m+4H+D1 causal data synchronization, 5-stage automated startup pre-flight lifecycle, 7-stage microstructure ratchets, 20/20 profitable OOS regimes (19,480 trades, +330,766.70 USD profit, 59.3% WR), and fully cleared for live broker deployment.
  * Master S3 ORB/CRT Multiverse Engine (`Engine/run_20_oos_multiverse.py` & `Engine/strategy/s3_orb_ml.py`) officially achieved **10/10 Production Certification** from Ox Alpha / Arena (Commit: `706039d` / `c0a5237`). 
  * Verified 100% causal execution: entry at next bar open (`opens[j+1]`), daily session VWAP resets, clamped CRT features, FVG sanity filters, causal Judas sweeps, and 8 bps friction penalty.
  * 18 Outright Passes across the 20 OOS regimes (2021-2026), 0 losing regimes across 5 full years (outliers W05 Terra-Luna and W08 FTX Collapse preserved in positive profit at +15.26 USD and +42.05 USD with max DD contained below 4.69%), and +11,290.24 USD Total Net Profit (+225.80% Net ROI on 5,000.00 USD capital) across 2,187 completed trades.
  * Master dual-model baseline `Engine/run_20_oos_dual_model.py` achieves 13 Outright Passes and +6,454.66 USD net PnL (+129.09% Net ROI).
  * **Autonomous 15-Minute Candle AI Trader & MT5 Bridge (`Terminal/OF_Strategy.py` --mode mt5-trader --live --min-risk 10.0 --max-risk 20.0)**:
    - **Unified 13th-Minute Wake-Up System**:
      1. *Tier 1 (Execution Daemon - `task-24931`)*: Continuous background telemetry git daemon auto-syncing authentic state to GitHub every 60 seconds with honest R-denominators and spec blocks.
      2. *Tier 2 (AI Assistant Cron - Two-Phase Collaborative Execution Loop - OPERATOR MANDATE)*: Unified collaborative loop. At the trigger minute, the coordinator posts the fresh prompt to debug Chrome (Copilot Studio / Arena.ai). **MANDATORY 4-MINUTE INFERENCE TIMER AT ALL TIMES**: Immediately upon prompt injection, the coordinator MUST set a full 4-minute timer (240s) from injection time. All subagents MUST be killed / remain offline during these 4 minutes. Only after the 4 minutes have elapsed does the coordinator harvest the completed response (`copilot_studio_bridge.py --check` / `arena_bridge.py check`) and THEN dispatch the 4-subagent swarm (`Orderflow Analyst`, `Position Manager`, `Macro Risk Analyst`, `Chain Verification Auditor`) to conduct independent empirical research and evaluate their findings against the model's ruling.
      3. *Tier 3 (Mandatory Subagent Pre-Flight Study & Independent Research Mandate - OPERATOR INVARIANT)*: Every invoked subagent MUST FIRST study:
         * `@[.agents/AGENTS.md]` (Execution rules, risk invariants, anti-lookahead)
         * `@[.agents/memory/session_chat_history.md]` (Historical trajectory, avoided traps, past decisions)
         * `@[.agents/rules/ACTIVE_CONTEXT.md]` (Real-time account state, live orders, floor defense)
         * Query the AST knowledge graph via `python -m graphify query "<concept>"` or `/graphify` before proposing or analyzing any trade.
         * **MANDATORY INDEPENDENT RESEARCH (OPERATOR MANDATE)**: Subagents are strictly FORBIDDEN from passively echoing Arena.ai's output. Alongside reviewing Arena's ruling, each subagent MUST execute its OWN independent empirical research:
           - *Orderflow Analyst*: Pull live MT5 tick Bid/Ask quotes, calculate real spreads in bps, query Binance Futures L2 orderbook depth directly, calculate 1m/5m/15m taker CVD delta, locate actual liquidation bands and stop sweep clusters, and test whether Arena's candidates satisfy the 5-pillar confluence stack.
           - *Position Manager*: Directly query MT5 account state (`mt5.account_info()`, `positions_get()`, `orders_get()`), calculate live floor cushion against the 4,775.00 USD hard floor and 4,795.00 USD operating buffer, run stressed post-loss simulations independently, check symbol-specific tick sizes and margin requirements, and audit whether proposed orders respect the dynamic capacity policy.
           - *Macro Risk Analyst*: Directly inspect `Data/macro_calendar.json` for Tier-1 event proximity, audit the session progression (e.g. 21:30–22:30 UTC interbank FX rollover spread expansion), evaluate cross-asset correlation clusters, and determine whether macro conditions warrant entering or standing aside.
      4. *Tier 4 (Continuous Blackboard Review & Trade Punch Mandate - USER DIRECTIVE)*: On EVERY wake-up cycle, coordinator and subagents MUST read and review `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md`, engage in dialectic debate contrasting their independent research against Arena.ai's output, render explicit verdicts, make suggestions, counter proposals, and punch high-confluence orders into MT5 without asking.
      5. *Tier 5 (4th Swarm Member: Continuous Forensic System & Chain Verification Auditor - OPERATOR DIRECTIVE)*:
         * A dedicated 4th subagent (`Chain Verification Auditor`) continuously audits the entire execution chain, guarantees that ALL past issues and invariants raised in chat history remain active and unregressed, actively hunts for runtime/code/data anomalies across `Terminal/`, `Engine/`, and `Tests/`, and immediately fixes any discovered anomaly.
    - Connects directly via native IPC to MetaTrader 5 Account 5064568 (Blueberry Markets).
    - GitHub Commits `0b0aa14`, `13e2e2a`, `11a220e`, `9c1cb2d`, `bddcfd4`, `a03a3ed`: Merged Arena.ai quantitative governance, continuous orderflow scoring, decayed L3 evidence, Kaufman/Garman-Klass regime vetoes, BTC beta factor risk models, and verified 97/97 pytest suite passing.
    - Full Arena Audit Report: Archived in `docs/audits/institutional-quant-audit-2026-10-04.md` and `docs/audits/ARENA_ANTIGRAVITY_HANDSHAKE_COUNCIL_67.md`.
    - **Dynamic Conviction Risk Budget**: Flexible **10.00 to 20.00 USD** (0.20% to 0.40% on 5,000.00 USD capital) dynamically scaled by orderflow confluence, resting L3 whale presence, and macro alignment.
    - **Active Positions & Pending Orders (Live State)**:
      * Current Status: **0 Open Positions | 1 Active Pending Limit Order (1 Total Ticket) | Equity: 4,896.55 USD | Balance: 4,896.55 USD | Free Margin: 4,896.55 USD | Margin Used: 0.00 USD**.
      * Active Positions (0) — **ALL 4 POSITION CAPACITY SLOTS LIBERATED & VACANT**:
        - Zero active positions deployed. 4 slots available for high-confluence deployments.
      * Active Pending Orders (1) — **BTC MODEL 2 VWAP PULLBACK LIMIT STAGED**:
        - Ticket #18762114: `BTCUSD.pi` BUY LIMIT 0.02 lots @ 82,580.00 USD | SL: 82,080.00 USD | TP: 83,850.00 USD | Risk: 10.00 USD (0.02 lots x 500 pts).
      * Capacity Sentry: **0 / 4 filled positions deployed | 1 pending limit resting | 3 slots vacant on desk**.
      * G-1 Hard Floor Defense: Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD | Live Floor Cushion: **+121.55 USD** (+101.55 USD above operating buffer).
      * Stressed Post-Loss Simulation & Absolute Immunity:
        - Total Contingent Book Risk across all exposed tickets: **10.30 USD** (10.00 USD SL + 0.30 USD friction).
        - Stressed Worst-Case Equity: `4,896.55 - 10.30 =` **4,886.25 USD** (Unconditionally defends floor!).
        - Safety Cushion Above 4,775.00 USD Hard Floor: **+111.25 USD** (5.5x mandatory >= 20.00 USD buffer).
        - Safety Cushion Above 4,795.00 USD Operating Buffer: **+91.25 USD**.
      * Closed Trades Today (Realized PnL):
        - Ticket #18740569 (`SP500.p` closed at **-13.00 USD loss** via Stop Loss at 7,778.50 USD, Deal #16962450, Order #18749312)
        - Ticket #18734182 (`ETHUSD.pi` closed at **-11.90 USD loss** via Stop Loss at 2,477.50 USD, Deal #16961654, Order #18748507)
        - Ticket #18734361 (`XAUUSD.pi` closed at **-13.70 USD loss** via Stop Loss at 4,175.80 USD, Deal #16957838, Order #18744533)
        - Ticket #18734917 (`BTCUSD.pi` closed at **+24.00 USD cash profit** via Full Take Profit at 83,250.00 USD, Deal #16954370, Order #18740985)
        - Ticket #18736423 (`USWTI.p` closed at **+0.70 USD cash profit** via Phase 0 BE Stop Loss at 91.555 USD, Order #18738998, Deal #16952451)
        - Ticket #18723453 (`SP500.p` closed at **+34.00 USD cash profit** via Full Take Profit at 7,798.50 USD, Order #18734579)
        - Ticket #18723454 (`GBPUSD.pi` closed at **+0.72 USD cash profit** via Phase 0 BE Stop Loss at 1.32391 USD, Order #18732065)
        - Ticket #18723450 (`USWTI.p` closed at **+30.00 USD cash profit** via Take Profit at 92.000 USD, Deal #16944675)
        - Ticket #18706769 (`ETHUSD.pi` closed at +16.32 USD profit via Phase 2 Trailing Ratchet SL at 2,455.10 USD)
        - Ticket #18710722 (`SOLUSD.p` closed -9.20 USD loss via emergency shelf cut at 108.87 USD)
        - Ticket #18703132 (`NAS100.p` closed at +25.00 USD profit via Take Profit at 30,739.10 USD)
        - Ticket #18686607 (`ETHUSD.pi` closed at +2.37 USD profit via market close at 2,533.70 USD)
        - Ticket #18625151 (`USWTI.p` closed at +9.88 USD profit via SL profit lock at 91.720 USD)
        - Ticket #18640304 (`SP500.p` closed at +3.87 USD profit via Phase 0 BE lock at 7,772.98 USD)
        - Ticket #18644889 (`USDJPY.pi` closed at +1.82 USD profit via Phase 0 BE lock at 158.046 USD)
        - Ticket #18630694 (`BTCUSD.pi` closed -6.80 USD loss via SL at 82,700.00 USD)
        - Ticket #18644262 (`USWTI.p` closed -10.03 USD loss via SL at 90.113 USD)
        - Net Realized Session PnL: **+84.05 USD** across 17 completed trades (initial capital 5,000.00 USD; 97.93% preserved; 11 wins / 6 losses = 64.7% win rate).
      * 360-Degree Forensic Verification Certification: [`Terminal/chain_verification_360.py`](file:///c:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py) reports `CERTIFIED_100_PERCENT_PRISTINE`. All 24 Parquet archives verified with 0 nulls and 100% strictly monotonic timestamps; causal anti-lookahead verified; broker feed ping 3.65 ms; Binance L2 depth monotonic; full pytest suite passing (405 passed, 0 failed). All P0 admission defects, P1 timestamp rejuvenation, P1 CVD future trade leak, and P1 certification fail-closed checks resolved and regression-tested.
      * Current collaborative cycle: Cycle 20:45 UTC (Section 90) completed. Unanimous stand-aside ratified between Opus 5.5 and subagent swarm. All 6 daemons healthy.
      * **Hyperdash On-Chain Telemetry Upgrade**: Autonomous background telemetry git daemon (`Terminal/Data_Factory/autonomous_telemetry_git_daemon.py`, PID 16548) actively streaming authentic Hyperdash GraphQL & REST data every 60s to `origin/main`: 100% verified on-chain Ethereum whale wallet orders (`0x...`, notionals >= 150k USD), real structural stop clusters (`structural_stop_clusters`), real reconstructed liquidation cascade bands (`reconstructed_liquidations`), and 20-level L2 depth across all 22 supported perpetuals (Crypto + Indices + Commodities + Forex), with honest UNAVAILABLE reporting for DJ30 & GER40. `gemini-web2api` active on 8081, Graphify AST watcher active. Ready for Arena.ai multi-persona evaluation.

## 3. Settled Mathematical & Strategy Invariants
- **Institutional VWAP & Orderflow Confluence Framework (Strict Mandate)**:
  - **Core Mindset**: Maximize capital efficiency and deploy free margin (>4,000 USD available) by staging passive limit orders into high-confluence structural liquidity zones across orthogonal asset clusters.
  - **Model 1: Extreme Standard Deviation Flushes (|Z| >= 2.0 SD)**:
    * Long Entry: Price stretched to <= -2.0 SD (or extreme -3SD to -10SD flushes) from Session VWAP with confirmed CVD selling exhaustion, discount stop cluster sweep, and resting L2/L3 bid whale support.
    * Short Entry: Price stretched to >= +2.0 SD above Session VWAP with confirmed CVD buying exhaustion, buy-stop liquidity sweep, and resting ask whale resistance.
    * Execution: Passive Limit Order resting directly at the liquidity band.
  - **Model 2: Trend-Continuation Pullback to VWAP (Joining Momentum Toward Liquidity Magnets)**:
    * Bullish Regime: Price > Session VWAP and positive 200 EMA slope. Enter Long on pullbacks to Session VWAP / Value Area Low / Support Shelf. Targets set at overhead liquidity magnets: short squeeze bands, resting buy-stop clusters, and ask whale walls.
    * Bearish Regime: Price < Session VWAP and negative 200 EMA slope. Enter Short on pullbacks up into Session VWAP / Value Area High / Resistance Shelf. Targets set at downside liquidation cascade pools and sell-stop clusters.
  - **Mandatory Dual-Engine Governance (|Z| >= 2.0 SD Mean Reversion vs |Z| < 2.0 SD Trend Following)**:
    * **Regime-Gated Execution & Stand-Aside Mandate**: When `classify_regime()` returns `UNDEFINED`, the desk MUST stand aside unconditionally across both engines. Never force trades in choppy, non-trending noise.
    * In-range location (|Z| < 2.0 SD, e.g. 0.2 to 1.7 SD) is admissible for **Model 2 Trend Following** ONLY when a verified `TREND_UP` or `TREND_DOWN` regime is confirmed by HTF structure: pullbacks to confirmed support/resistance shelves (EMA, VAL/VAH, session VWAP) in the direction of the dominant trend, backed by resting L2/L3 whale depth.
    * **Extreme Mean Reversion (Model 1)** is admissible ONLY in confirmed `MEAN_REVERT` regimes at extreme locations (|Z| >= 2.0 SD to 3.5 SD) with verified tape exhaustion.
    * **Mandatory Dialectic Debate**: Every review cycle evaluates both engines under empirical regime classification. If neither engine confirms a statistically valid structural setup or regime is `UNDEFINED`, standing aside is the mandatory, disciplined action.
  - **Mandatory 5-Pillar Confluence Stack**: Every order must be backed by (1) VWAP Z-score / SD bands, (2) CVD orderflow absorption, (3) Reconstructed liquidation bands, (4) Structural stop clusters, and (5) Live L2/L3 whale depth. Trades must follow this exact framework or provide very strong mathematical justification otherwise.
- **Dynamic Capacity & Risk Budget (Floor Defense)**:
  - Base Capital: 5,000.00 USD | Hard Equity Floor: 4,775.00 USD.
  - Risk Budget per Trade: 10.00 to 14.50 USD (0.20% to 0.29%).
  - Expanded Concurrency: Concurrency expanded from 2 up to 4 concurrent positions across orthogonal asset clusters (Forex, Energy, Indices, Crypto), provided total joint worst-case stopout risk strictly preserves >= 20.00 USD cushion above the 4,775.00 USD floor at all times.
- **Active Order Queue Sentry & Continuous Punch/Prune Protocol (Strict Mandate)**:
  - **Dynamic Pruning / Deletion**: Continuously audit all resting limit orders. If an order's structural thesis degrades (supporting whale wall pulled/thinned by >50%, price drifted beyond 2.0x ATR, or adverse regime break), **immediately delete/cancel the pending order** to unencumber capital and margin.
  - **Dynamic Punching on Confluence**: When an un-allocated asset prints extreme confluence under Model 1 (Extreme 2SD Mean Reversion) or Model 2 (VWAP Trend Pullbacks) with verified resting L2/L3 whale walls and sufficient floor cushion clearance, **immediately stage the limit order**.
  - **Running Position Sentry**: Continuously monitor floating entries (e.g. USWTI #18625151) for piecewise ratchets (Phase 0 BE lock @ +0.80R, Phase 1 Profit Lock @ +1.50R, target @ +2.50R, 24-bar time decay, and emergency shelf cuts).
  - **Dynamic Risk Budget Recirculation**: Moving an active trade's stop to Phase 0 BE drops its allocated risk to 0.00R, immediately liberating risk budget to punch the next highest-confluence standby limit into vacant capacity (up to 4 concurrent positions).
- **Microstructure Piecewise Ratchet**:
  - Phase 0 (BE Lock): At +0.70R to +0.80R gain, move stop to Entry +0.35R (clearing 41 bps friction with guaranteed profit).
  - Phase 1 (Profit Lock): At +1.50R gain, move stop to Entry +0.80R.
  - Target: +1.85R to +2.50R exit (structural liquidity target).
  - Time Decay: Exit at market if trade fails to gain +0.20R within 24 bars (6 hours).

## 4. Local Execution Protocol
- **End-to-End Local Development**: All strategy logic, ML training, walk-forward simulations, and risk governance are implemented, tested, and optimized directly within the local python environment.
- **Strict Anti-Lookahead Enforcement**: Entries booked at next bar open `opens[j+1]`, causal HTF `shift(1)` backward-as-of joins, and zero test-set tuning.
- **Zero Dollar Signs**: Strict prohibition on dollar symbols; always write USD.

## 5. Quantitative Knowledge Grounding & Minimal Token Reference Mandate
- **Always Reference Quant-Developers-Resources**: For all quantitative modeling, risk management, econometrics, and execution math, actively ground solutions in the canonical libraries inside `Quant-Developers-Resources-main/` (Risk Management, Econometrics, Financial Theory, Technical Indicators, Microstructure, and C++).
- **Minimal Token Querying via Graphify**: NEVER dump entire files into context. Always query specific subgraphs via `python -m graphify query "<concept>" --budget 300` or `graphify explain "<concept>"` to retrieve scoped AST nodes, classes, and call-flows with minimal token footprint.

## 6. Institutional Orderflow & Microstructure Live Execution Checklist (Always Enforced)
- **Canonical Checklist**: Strictly follow `[docs/specs/institutional_orderflow_live_checklist.md](file:///c:/Users/SIGMA/Documents/Trading_2/docs/specs/institutional_orderflow_live_checklist.md)` on every 14th-minute wake-up cycle.
- **Pre-Order Gating**: Must verify all 7 sub-gates (Price Action geometry, CVD divergence, 20-level L2 depth, L3 whales >= 150k USD with >= 180s persistence, liquidation FFR, macro blackouts, covariance room vs 4,775.00 USD floor).
- **Smart SL & TP Adjustments**: Deterministic ratchets (Phase 0 BE @ +0.80R, Phase 1 Profit Lock @ +1.50R, Phase 2 Trailing Lock @ +2.00R). TP extensions into orderbook liquidity vacuums require simultaneous Phase 2 SL profit lock.

