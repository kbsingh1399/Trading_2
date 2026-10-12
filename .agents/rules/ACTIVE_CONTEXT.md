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
- **PURE TELEMETRY & PLAYBOOK ANALYSIS MANDATE (ZERO DECISION GATES - STRICT OPERATOR DIRECTIVE)**: `Terminal/decision_gates_v3.py` and rigid programmatic gate tokens (`A1-A5`, `B1-B6`, `G-4`, `G-6`, `MAX_TARGET_DIST_ATR = 4.0`, `A2_no_tape_fail_closed`) are permanently retired from trade selection and Arena.ai prompts. Every prompt and trade evaluation must be 100% based on direct, line-by-line analysis of `docs/telemetry/live_snapshot_latest.json` and `docs/specs/TRADE_DECISION_PLAYBOOK.md` — debating the mutual coincidence of psychological round numbers, reconstructed liquidation cascade bands, structural stop clusters, L2 orderbook depth, L3 whale wallet orders (`0x...`), MT5 execution spreads, and VWAP/EMA/Volume Profile shelves.
- **DUAL-VENUE DIVISION OF LABOR (MT5 SPREADS + HYPERDASH/BINANCE MICROSTRUCTURE)**:
  * **Execution & Spreads from MT5 (`quotes`, `execution_specs`)**: Always use live MT5 Bid/Ask quotes for spread filtering (`<= 25 bps` Crypto, `<= 5 bps` TradFi CFDs) and `mt5.order_calc_profit` / `execution_specs` for exact lot sizing.
  * **Orderbook, Whales, Liquidations & Stops from Hyperdash & Binance**: Always use `orderbook_live_depth` (`whale_walls_l3`, `l2_wall_levels`, `top20_bid_depth_usd`, `top20_ask_depth_usd`), `structural_stop_clusters` (`top_*` and `nearest_*`), and `reconstructed_liquidations` (`top_*` and `nearest_*`), mapped onto the MT5 price grid via `venue_basis`.
- **MANDATORY INDEPENDENT LOGICAL VERIFICATION & IMMEDIATE ARENA CORRECTION LOOP (STRICT OPERATOR DIRECTIVE)**:
  * Never blindly accept Arena.ai's output. Immediately after harvesting every Arena.ai response, independently verify every single claim, entry price, SL bunker boundary (`min_price` / `max_price` vs `mid_price`), TP magnet front-run, CVD flow direction, L3 whale wall location, and `mt5.order_calc_profit` risk figure against `docs/telemetry/live_snapshot_latest.json` and live MT5.
  * **Immediate Feedback to Arena on Mistakes**: If Arena.ai makes ANY mistake in its logic or levels (such as measuring an SL buffer from `mid_price` instead of `min_price` so the SL sits inside a liquidation band, or placing a limit entry above an un-swept stop cluster and above the actual whale bid walls), IMMEDIATELY inject a corrective feedback prompt back to Arena.ai right after reading its output so Arena rectifies the error.
- **PERMANENT FEEDBACK DOCUMENTATION MANDATE (ALWAYS-ON REFERENCE)**: Every operator feedback point, microstructure lesson, and verification rule shared in chat MUST be immediately persisted into `.agents/rules/ACTIVE_CONTEXT.md` (auto-loaded on every turn) and `docs/specs/TRADE_DECISION_PLAYBOOK.md`.
- **MANDATORY GITHUB REPOSITORY LINK IN ALL PROMPTS (STRICT OPERATOR DIRECTIVE)**: Every single prompt generated for external models (Arena.ai) or internal subagents MUST prominently include the full GitHub repository URL (`https://github.com/kbsingh1399/Trading_2`), active branch (`main` and `arena/537c1eb8-trading-2`), and direct raw URLs for `docs/telemetry/live_snapshot_latest.json`, `docs/specs/TRADE_DECISION_PLAYBOOK.md`, `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md`, `.agents/rules/ACTIVE_CONTEXT.md`, and `.agents/memory/session_chat_history.md`.
- **BIDIRECTIONAL GIT INTERACTION & TWO-WAY ARENA COLLABORATION MANDATE (STRICT OPERATOR DIRECTIVE)**: Both `main` (`https://github.com/kbsingh1399/Trading_2`) and `arena/537c1eb8-trading-2` (`https://github.com/kbsingh1399/Trading_2/tree/arena%2F537c1eb8-trading-2`) MUST be constantly synchronized and kept up to date on every commit and telemetry push.
- **LEAN PROMPT & LINK-DRIVEN TELEMETRY MANDATE (ZERO RAW DATA BLOAT - STRICT OPERATOR DIRECTIVE)**: Prompts sent to Arena.ai MUST be lean, instruction-dense, and pointer-driven via direct GitHub raw URLs.
- **ZERO SPURIOUS SCRATCH LITTER**: Clean up all intermediate debug scripts immediately after validation.

## 2. Active Mission & Quantitative Target
- **Universe**: Full broker coverage of **156 Tradeable MT5 Symbols** (Blueberry Markets), with **43 Complete Institutional Universe Assets** (`COMPLETE_UNIVERSE`: 33 Crypto Perpetuals + 10 TradFi CFDs across Indices, Commodities, and Forex in `Terminal/Asset_Universe.py`) supported by 43 historical Parquet datasets (0 nulls) in `Data/Candles/` and real-time dual-venue L2/L3 orderbook depth. The active high-velocity streaming matrix publishes live telemetry across the universe.
- **Active Focus**: Direct Multi-Parameter Coincidence Playbook (`docs/specs/TRADE_DECISION_PLAYBOOK.md`) across all 24 live telemetry assets (`assets_matrix_24` in `docs/telemetry/live_snapshot_latest.json`).
- **Production State**: 
  * **Autonomous 15-Minute Candle AI Trader & MT5 Bridge (`Terminal/OF_Strategy.py` --mode mt5-trader --live --min-risk 10.0 --max-risk 20.0)**:
    - **Institutional Wake-Up & Collaborative Desk Protocol (STRICT OPERATOR SPECIFICATION)**:
      1. *Step 1 (Pure Telemetry Multi-Persona Analysis Prompt to Arena.ai)*:
         - Coordinator prompts Arena.ai in Chrome with the 4-persona council to analyze the latest live telemetry directly from `docs/telemetry/live_snapshot_latest.json` and `docs/specs/TRADE_DECISION_PLAYBOOK.md` (zero `decision_gates_v3.py` references).
         - Must systematically audit: `quotes` (MT5 spread_bps & mid), `execution_specs` (contract_size, min_lot, step_lot), `causal_indicators` (Session VWAP, Z-score, RSI, ATR, EMA 20/50/200), `volume_profile` (POC/VAH/VAL), `orderbook_live_depth` (20-level depth, book_imbalance, `whale_walls_l3`, `l2_wall_levels`, `venue_basis`), `structural_stop_clusters` (`top_*` and `nearest_*`), `reconstructed_liquidations` (`top_*` and `nearest_*`), and `cvd_1m_buckets`.
         - Immediately after Arena outputs, Antigravity independently verifies every figure and level against live MT5 and `live_snapshot_latest.json`. If Arena made any calculation or microstructure error, Antigravity immediately sends the mistake back to Arena.ai for correction.
      2. *Step 2 (Audit Running Trades & Ratchet Management)*:
         - Inspect all active open positions on MetaTrader 5 (`positions_get()`).
         - Trail SL to Phase 0 Break-Even at +0.80R, Phase 1 Profit Lock at +1.50R, Phase 2 Trailing Lock at +2.00R, and align TP with opposing stop/liquidation magnets.
      3. *Step 3 (Audit Resting Limit Orders & Pruning Sentry)*:
         - Audit all pending limit orders on MT5 (`orders_get()`). Verify that supporting L2/L3 whale walls remain intact, SL sits safely outside `min_price`/`max_price` of the liquidation bunker, and TP front-runs the opposing buy-stop/sell-stop magnet by 5–10 bps.
      4. *Position Capacity Policy*:
         - Up to 4 concurrent tickets across orthogonal asset clusters provided total joint worst-case stopout risk unconditionally defends the 4,775.00 USD hard floor and 4,795.00 USD operating buffer (>= 20.00 USD cushion at all times).
    - Connects directly via native IPC to MetaTrader 5 Account 5064568 (Blueberry Markets).
    - **Active Positions & Pending Orders (Live State)**:
      * Current Status: **0 Open Positions | 1 Pending Order | Equity: 4,885.38 USD | Balance: 4,885.38 USD | Free Margin: 4,885.38 USD**.
      * Active Positions (0): Standby / Flat.
      * Active Pending Orders (1): Ticket #18791527 (`BTCUSD.pi` BUY LIMIT 0.02 lots @ 83,150.00 USD | SL: 82,590.00 USD [0.51 ATR below 82,700 cascade min_price] | TP: 84,300.00 USD [front-running 84,350 $7.04M buy-stop cluster by 5.9 bps] | Risk: 11.20 USD / 0.23% | Reward: +23.00 USD | RR: 2.05 | Comment: `OFC_AI_BTC_M2_LIMIT`).
      * G-1 Hard Floor Defense: Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD | Live Floor Cushion: **+110.38 USD** (+90.38 USD above operating buffer).
      * Stressed Post-Loss Simulation:
        - Total Contingent Book Risk across exposed tickets: **11.20 USD**.
        - Stressed Worst-Case Equity: **4,874.18 USD** (Unconditionally defends floor!).
        - Safety Cushion Above 4,775.00 USD Hard Floor: **+99.18 USD** (5.0x mandatory >= 20.00 USD buffer).
        - Safety Cushion Above 4,795.00 USD Operating Buffer: **+79.18 USD**.
      * Closed Trades Today (Realized PnL):
        - Ticket #18785248 (`BTCUSD.pi` closed at **-11.17 USD loss** via Stop Loss at 83,472.55 USD, Deal #16997164, Order #18785248)
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
      * Current collaborative cycle: Opus 5.5 forensic audit ingested and all critical findings mathematically hardened (Commit `0fa4cfd6`). New module `Terminal/dg_hardening.py` shipped with Option A' error-budgeted bands, discrete tick quantization, gap-stressed floor defense, Clopper-Pearson exact bounds, ternary outcome expectancy, causal session dz4, strict A4 reclaim, HAC drift t-stat of returns, and discrete broker constraints. Full test suite passing 936 passed, 0 failed (100% green). Branches `main` and `arena/537c1eb8-trading-2` synchronized. Account in 100% Cash reserves at 4,896.55 USD, cushion +121.55 USD above 4,775.00 USD hard floor. Standing aside awaiting Sunday 22:00 UTC CFD reopen or major crypto breakout. All 5 persistent daemons healthy.
      * **Hyperdash On-Chain Telemetry Upgrade**: Autonomous background telemetry git daemon (`Terminal/Data_Factory/autonomous_telemetry_git_daemon.py`, PID 16548) actively streaming authentic Hyperdash GraphQL & REST data every 60s to `origin/main` and `origin/arena/537c1eb8-trading-2`: 100% verified on-chain Ethereum whale wallet orders (`0x...`, notionals >= 150k USD), real structural stop clusters (`structural_stop_clusters`), real reconstructed liquidation cascade bands (`reconstructed_liquidations`), and 20-level L2 depth across all 22 supported perpetuals (Crypto + Indices + Commodities + Forex), with honest UNAVAILABLE reporting for DJ30 & GER40. `gemini-web2api` active on 8081, Graphify AST watcher active. Ready for Arena.ai multi-persona evaluation.

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
  - Expanded Concurrency: Up to 4 contingent tickets across filled positions and pending orders combined. All pending fills reserve book risk; profit-side broker stops retain execution-cost reserves and still consume capacity. Native admission requires stressed post-stop equity >= 4,795.00 USD, using the 4,775.00 USD floor plus the 20.00 USD buffer. This is a modeled stress constraint, not immunity to unbounded gaps.
- **Active Order Queue Sentry & Continuous Punch/Prune Protocol (Strict Mandate)**:
  - **Dynamic Pruning / Deletion**: Continuously audit all resting limit orders. If an order's structural thesis degrades (supporting whale wall pulled/thinned by >50%, price drifted beyond 2.0x ATR, or adverse regime break), **immediately delete/cancel the pending order** to unencumber capital and margin.
  - **Dynamic Punching on Confluence**: When an un-allocated asset prints extreme confluence under Model 1 (Extreme 2SD Mean Reversion) or Model 2 (VWAP Trend Pullbacks) with verified resting L2/L3 whale walls and sufficient floor cushion clearance, **immediately stage the limit order**.
  - **Running Position Sentry**: Continuously monitor floating entries (e.g. USWTI #18625151) for piecewise ratchets (Phase 0 BE lock @ +0.80R, Phase 1 Profit Lock @ +1.50R, target @ +2.50R, 24-bar time decay, and emergency shelf cuts).
  - **Dynamic Risk Budget Recirculation**: A confirmed profit-side broker stop can release nominal stop-loss exposure, but native admission retains at least 2.00 USD execution-cost reserve per ticket. Filled and pending tickets continue consuming the four-ticket capacity; a BE label alone releases neither capacity nor broker-verified risk.
- **Microstructure Piecewise Ratchet**:
  - Phase 0 (BE Lock): At +0.70R to +0.80R gain, move stop to Entry +0.35R subject to broker distances and cost-aware qualification. Stop profit is modeled; gaps, commissions and slippage prevent a guaranteed realized profit claim.
  - Phase 1 (Profit Lock): At +1.50R gain, move stop to Entry +0.80R.
  - Target: +1.85R to +2.50R exit (structural liquidity target).
  - Time Decay: Exit at market if trade fails to gain +0.20R within 24 bars (6 hours).

## 4. Local Execution Protocol
- **End-to-End Local Development**: All strategy logic, ML training, walk-forward simulations, and risk governance are implemented, tested, and optimized directly within the local python environment.
 - **Strict Anti-Lookahead Enforcement**: Historical signal tests may book entry only on a subsequently observed bar or tick, such as `opens[j+1]`; never use the signal candle close as its fill. Live execution consumes completed HTF bars and stages passive limits against fresh quotes, then reconciles actual broker fills. Causal HTF `shift(1)` backward-as-of joins and zero test-set tuning remain mandatory.
- **Zero Dollar Signs**: Strict prohibition on dollar symbols; always write USD.

## 5. Quantitative Knowledge Grounding & Minimal Token Reference Mandate
- **Always Reference Quant-Developers-Resources**: For all quantitative modeling, risk management, econometrics, and execution math, actively ground solutions in the canonical libraries inside `Quant-Developers-Resources-main/` (Risk Management, Econometrics, Financial Theory, Technical Indicators, Microstructure, and C++).
- **Minimal Token Querying via Graphify**: NEVER dump entire files into context. Always query specific subgraphs via `python -m graphify query "<concept>" --budget 300` or `graphify explain "<concept>"` to retrieve scoped AST nodes, classes, and call-flows with minimal token footprint.

## 6. Institutional Orderflow & Microstructure Live Execution Checklist (Always Enforced)
- **Canonical Checklist**: Strictly follow `[docs/specs/institutional_orderflow_live_checklist.md](file:///c:/Users/SIGMA/Documents/Trading_2/docs/specs/institutional_orderflow_live_checklist.md)` on every 14th-minute wake-up cycle.
- **Pre-Order Gating**: Must verify all 7 sub-gates (Price Action geometry, CVD divergence, 20-level L2 depth, L3 whales >= 150k USD with >= 180s persistence, liquidation FFR, macro blackouts, covariance room vs 4,775.00 USD floor).
- **Smart SL & TP Adjustments**: Deterministic ratchets (Phase 0 BE @ +0.80R, Phase 1 Profit Lock @ +1.50R, Phase 2 Trailing Lock @ +2.00R). TP extensions into orderbook liquidity vacuums require simultaneous Phase 2 SL profit lock.

