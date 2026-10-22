---
trigger: always_on
---

# ⚡ ACTIVE OPERATIONAL CONTEXT & MISSION CONTROL CARD

> **ALWAYS-ON TURN-0 SITUATIONAL AWARENESS**
> Auto-injected on every turn. Eliminates context amnesia, retrieval latency, and model hallucination.

## 1. User Master Mandate (Strict & Non-Negotiable)
- **ANTIGRAVITY (FLASH) AS ULTIMATE DECIDER & EXECUTIVE LEADER (STRICT OPERATOR DIRECTIVE)**: Antigravity (Flash) is the sole and ultimate quantitative decision-maker on this desk. External models (Opus 5.5 and GPT_ASTRA in Copilot Studio) are strictly auxiliary research consultants and devil's advocates. Antigravity unleashes its full training, institutional econometric reasoning, and deep analytical powers to evaluate setups, override or adopt council inputs based on mathematical proof, and punch live orders autonomously into MetaTrader 5.

- **MANDATORY INVIOLATE SUBAGENT SWARM & ARENA.AI DISPATCH GUARANTEE (PERMANENT OPERATOR DIRECTIVE - NEVER OMITTED)**:
  * On EVERY 20-minute autonomous wake-up cycle and on EVERY decision step, the coordinator is strictly FORBIDDEN from operating as a single isolated agent or bypassing the dual-track council.
  * Antigravity MUST physically invoke the specialized subagent fleet (Orderflow Analyst, Position Manager, Macro Risk Analyst, Chain Verification Auditor) via invoke_subagent.
  * Antigravity MUST prepare and inject the surgical red-team prompt into Arena.ai via Chrome CDP on port 9222.
  * Live MT5 executions and dynamic profit ratchets (Early-BE, Phase 0, Phase 1) MUST be executed immediately to lock gains and protect capital, but MUST SIMULTANEOUSLY dispatch the subagents and Arena prompt. No operational event ever excuses skipping subagent invocation or Arena consultation.

- **MANDATORY PREVIOUS CONVERSATION CONTEXT & TRAJECTORY REFERENCE (PERMANENT STEP-LEVEL INVARIANT)**: On EVERY single turn and before taking action on ANY step, the coordinator and all subagents MUST FIRST review the previous conversation history (`.agents/memory/session_chat_history.md`, past turns, transcript). You CANNOT take actions, audit orders, evaluate setups, or propose modifications in a vacuum. You MUST know the complete historical context, evolving operator rules, past rulings, avoided traps, and live position trajectory before evaluating or executing any step. Zero context amnesia.
- **CROSS-ACCOUNT RE-ENGAGEMENT & FULL NARRATIVE AUDIT (HYPERDASH / MULTI-ACCOUNT INVARIANT)**: Whenever the operator switches Gemini accounts and returns to the session chat, the agent MUST explicitly review all past session chat logs (`.agents/memory/session_chat_history.md`, transcript, and `ACTIVE_CONTEXT.md`) to establish total continuity of what we are trying to achieve, internalize all operator feedback, remember past setbacks, and preserve every nuance of the active quantitative mission before taking any action.
- **100% LOCAL QUANTITATIVE DEVELOPMENT & EXECUTION**: All prompt-generation for external agents (Ox Alpha / Arena) is permanently terminated. All engineering, econometric feature integration, model training, backtesting, and 20 OOS window optimization are executed right here locally in this environment.
- **MANDATORY BUY & HOLD BENCHMARKING**: ALWAYS compare strategy performance, equity curves, ROI, and drawdowns directly against the Buy and Hold benchmark (BTC Buy & Hold normalized to identical starting capital).
- **MANDATORY ARENA SKILL (https://github.com/Jakeschincariol/arena-skill) IN ALL UPCOMING PROMPTS & AUDITS (STRICT OPERATOR DIRECTIVE)**: Every upcoming prompt generated for external models (Arena Astra, Claude Fable, Gemini Argon, Copilot Studio) and internal subagents MUST prominently mandate that `https://github.com/Jakeschincariol/arena-skill` is a strict, non-negotiable prerequisite to use always. Models must verify/read the skill (`.agent/skills/arena/SKILL.md` or `git clone https://github.com/Jakeschincariol/arena-skill.git ~/.claude/skills/arena`) and execute the tournament bracket evaluation (`bracket.py`, `rubric.md`) across competing personas to score trade hypotheses before issuing any trading verdict or code commit.
- **ZERO-HESITATION AUTONOMOUS PUNCH MANDATE (STRICT OPERATOR DIRECTIVE)**: NEVER ask the operator for permission to stage or execute orders. Whenever ANY candidate candle prints an eligible structural setup supported by rigorous quantitative reasoning, mathematical logic, resting L2/L3 whale backing, and capital floor defense under Model 1 (Extreme Mean Reversion) or Model 2 (VWAP Trend Pullbacks), IMMEDIATELY punch the passive limit order live into MetaTrader 5 without hesitation and without asking. Zero hesitation, zero latency, 100% autonomous execution.
- **PURE TELEMETRY & PLAYBOOK ANALYSIS MANDATE (ZERO DECISION GATES - STRICT OPERATOR DIRECTIVE)**: `Terminal/decision_gates_v3.py` and rigid programmatic gate tokens (`A1-A5`, `B1-B6`, `G-4`, `G-6`, `MAX_TARGET_DIST_ATR = 4.0`, `A2_no_tape_fail_closed`) are permanently retired from trade selection and Arena.ai prompts. Every prompt and trade evaluation must be 100% based on direct, line-by-line analysis of `docs/telemetry/live_snapshot_latest.json` and `docs/Mandatory_Rules/TRADE_DECISION_PLAYBOOK.md` — debating the mutual coincidence of psychological round numbers, reconstructed liquidation cascade bands, structural stop clusters, L2 orderbook depth, L3 whale wallet orders (`0x...`), MT5 execution spreads, and VWAP/EMA/Volume Profile shelves.
- **DUAL-VENUE DIVISION OF LABOR (MT5 SPREADS + HYPERDASH/BINANCE MICROSTRUCTURE)**:
  * **Execution & Spreads from MT5 (`quotes`, `execution_specs`)**: Always use live MT5 Bid/Ask quotes for spread filtering (`<= 25 bps` Crypto, `<= 5 bps` TradFi CFDs) and `mt5.order_calc_profit` / `execution_specs` for exact lot sizing.
  * **Orderbook, Whales, Liquidations & Stops from Hyperdash & Binance**: Always use `orderbook_live_depth` (`whale_walls_l3`, `l2_wall_levels`, `top20_bid_depth_usd`, `top20_ask_depth_usd`), `structural_stop_clusters` (`top_*` and `nearest_*`), and `reconstructed_liquidations` (`top_*` and `nearest_*`), mapped onto the MT5 price grid via `venue_basis`.
- **MANDATORY INDEPENDENT LOGICAL VERIFICATION & IMMEDIATE ARENA CORRECTION LOOP (STRICT OPERATOR DIRECTIVE)**:
  * Never blindly accept Arena.ai's output. Immediately after harvesting every Arena.ai response, independently verify every single claim, entry price, SL bunker boundary (`min_price` / `max_price` vs `mid_price`), TP magnet front-run, CVD flow direction, L3 whale wall location, and `mt5.order_calc_profit` risk figure against `docs/telemetry/live_snapshot_latest.json` and live MT5.
  * **Immediate Feedback to Arena on Mistakes**: If Arena.ai makes ANY mistake in its logic or levels (such as measuring an SL buffer from `mid_price` instead of `min_price` so the SL sits inside a liquidation band, or placing a limit entry above an un-swept stop cluster and above the actual whale bid walls), IMMEDIATELY inject a corrective feedback prompt back to Arena.ai right after reading its output so Arena rectifies the error.
- **PERMANENT FEEDBACK DOCUMENTATION MANDATE (ALWAYS-ON REFERENCE)**: Every operator feedback point, microstructure lesson, and verification rule shared in chat MUST be immediately persisted into `.agents/rules/ACTIVE_CONTEXT.md` (auto-loaded on every turn) and `docs/Mandatory_Rules/TRADE_DECISION_PLAYBOOK.md`.
- **MANDATORY GITHUB REPOSITORY LINK IN ALL PROMPTS (STRICT OPERATOR DIRECTIVE)**: Every single prompt generated for external models (Arena.ai) or internal subagents MUST prominently include the full GitHub repository URL (`https://github.com/kbsingh1399/Trading_2`), active branch (`main` and `arena/537c1eb8-trading-2`), and direct raw URLs for `docs/telemetry/live_snapshot_latest.json`, `docs/Mandatory_Rules/TRADE_DECISION_PLAYBOOK.md`, `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md`, `.agents/rules/ACTIVE_CONTEXT.md`, and `.agents/memory/session_chat_history.md`.
- **MANDATORY MAIN-BRANCH-ONLY ROUTING MANDATE (STRICT OPERATOR DIRECTIVE)**: From Cycle 102 onwards, ALL prompt generators (`dispatch_comprehensive_wake_up_prompt.py`, `dispatch_tri_council.py`, etc.), external council instructions, and raw repository URLs MUST strictly and exclusively route all models (Arena Astra, Claude Fable, Gemini Argon, Copilot Studio) to fetch data, telemetry, and files from the canonical `main` branch of GitHub (`https://github.com/kbsingh1399/Trading_2/tree/main`, `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/...`). Secondary/split branch URLs (`arena/...`) are permanently prohibited in prompts.
- **BIDIRECTIONAL GIT INTERACTION & TWO-WAY ARENA COLLABORATION MANDATE (STRICT OPERATOR DIRECTIVE)**: Both `main` (`https://github.com/kbsingh1399/Trading_2`) and `arena/537c1eb8-trading-2` (`https://github.com/kbsingh1399/Trading_2/tree/arena%2F537c1eb8-trading-2`) MUST be constantly synchronized and kept up to date on every commit and telemetry push.
- **FULL-PARAMETER TELEMETRY SYNTHESIS MANDATE (ZERO ARTIFICIAL CONSTRAINTS - STRICT OPERATOR DIRECTIVE)**: Prompts sent to Arena.ai or council models must NEVER artificially limit the model to narrow, dogmatic checklists. Empower the model to evaluate both Mean Reversion and Trend Following opportunities by cross-verifying ALL 12 parameters in `docs/telemetry/live_snapshot_latest.json` (MT5 Bid/Ask spreads, causal regimes, VWAP SD bands, volume profile POC/VAH/VAL, 1m/15m/30m CVD taker flow & absorption, 20-level L2 depth, L3 on-chain Ethereum whale orders `0x...`, reconstructed liquidation cascade bands, structural stop clusters, macro calendar, funding velocity, and execution specs).
- **MANDATORY LOSING TRADE AUTOPSY & 5 ANTI-TRAP INVARIANTS IN ALL FUTURE PROMPTS (STRICT OPERATOR DIRECTIVE)**: Every future prompt generated for Arena.ai, Z.ai, or subagents MUST explicitly detail the autopsy of recent stopped-out trades (`SOLUSD.p #18806752`, `BTCUSD.pi #18798018`, `BTCUSD.pi #18786372`, `SP500.p #18749312`, `ETHUSD.pi #18748507`, `XAUUSD.pi #18744533`) and enforce the 5 Anti-Trap Invariants: (1) SL placed safely outside `[min_price, max_price]` with >= 0.35–0.50 ATR buffer; (2) Confirmed CVD delta deceleration/absorption before long entry (never catch falling knives); (3) Never place entry limits directly above un-swept opposing stop clusters; (4) Supporting whale walls must show verified persistence >= 180s; (5) Multi-timeframe trend alignment must be respected.
- **TREND-FIRST HTF HIERARCHY & MULTI-DIMENSIONAL CONFLUENCE (STRICT OPERATOR DIRECTIVE)**:
  * **Ban on VWAP-Band Tunnel Vision**: Never stick dogmatically to VWAP standard deviation bands alone or fall into the retail trap of dip-buying falling knives in strong downtrends.
  * **1D / -1D Daily VWAP Band Coincidence with Whale Walls**: For Model 2 Trend Pullbacks, look for the mutual coincidence of the 1-Day VWAP band (+1.0 SD / -1.0 SD) AND persistent resting L2/L3 whale walls (>= 180s). This convergence marks high-conviction structural inflection shelves.
  * **Liquidation Cascade Bands as Target Magnets & Momentum Riders**: Reconstructed liquidation bands and dense stop clusters act as high-probability price magnets that pull price toward them. We ride the cascade momentum into the magnet for take-profit targets.
  * **Absorption vs Trend Blow-Through Forensics**: When price reaches a liquidation magnet, never assume an automatic mean-reversion fade. Sometime the market consumes all resting orders and continues running violently. Differentiate absorption from continuation by inspecting: (1) multi-horizon taker CVD acceleration, (2) L2 orderbook replenishment velocity, (3) Arkham on-chain exchange net inflows/outflows, and (4) macro narrative sentiment.
  * **HTF Trend Hierarchy (1H/4H EMAs + Footprint + CVD + Whales)**: Always evaluate the Higher Timeframe Trend Hierarchy (1H/4H EMA alignments, 15m structural slopes) supported by the complete multi-dimensional data stack:
    1. *Regime Alignment*: If Price < EMA20 < EMA50 < EMA200 on 1H/4H (Bearish regime), Model 1 dip-buying Longs are strictly FORBIDDEN. All priority shifts to staging Model 2 Trend Pullback SHORTS at overhead resistance shelves.
    2. *CVD Flow as Trend Momentum*: Massive negative taker CVD (-1M to -3M USD) confirms aggressive seller domination. Never buy against it; use it as confirmation to short intraday rallies.
    3. *Model 2 Pullback Short Protocol*: In a bear trend, never chase breakdowns at the lows. Wait for relief rallies into the EMA20/EMA50/VAH shelves backed by resting L2/L3 Ask Whale Walls (e.g. 7.79M USD Ask @ 82,670 on BTC) to defend stops.
    4. *Expanded Risk Envelope (10.00 to 25.00 USD - Operator Directive)*: The operator has explicitly granted full rights to expand the stop loss dollar budget up to 20.00 to 25.00 USD (0.40% to 0.51% equity) to ensure stops are safely placed behind genuine resting institutional whale walls (Invariant A) without choking. Never discard a valid setup or squeeze stops into sweep zones just to meet an artificial sub-15 USD cap. Sizing must prioritize whale bunker safety while guaranteeing Stressed Equity >= 4,795.00 USD.
    5. *Broker Ticker Mapping*: Remember that Avalanche is mapped to `AVXUSD.p` on Blueberry Markets (Contract Size 100, min lot 0.01, digits 2).
- **EXPANDED STOP LOSS DOLLAR BUDGET & SAFE WHALE BUNKER SIZING (STRICT OPERATOR DIRECTIVE)**:
  * Full rights granted by the operator to increase stop loss dollar risk up to **$20.00 – $25.00 USD** whenever needed to capture high-conviction structural trades and prevent stop hunts.
  * Invariant A takes absolute precedence: stops MUST sit behind verified resting whale walls (`persist >= 180s`) with 0.35–0.50 ATR structural buffer. Never choke stops.
  * Stressed simulation requirement: `Stressed Equity = Current Equity - (Risk * 1.25 + 2.00) >= 4,795.00 USD`. With $4,857.32 USD equity, a $25.00 USD risk trade is safely supported (+29.07 USD above operating buffer, +49.07 USD above hard floor).
- **MACRO BLACKOUT ENFORCEMENT (P0 INSTITUTIONAL FAIL-CLOSED INVARIANT)**:
  * Pre-submission macro blackout is ACTIVELY ENFORCED via `Terminal/risk/blackout_guard.py` (`BlackoutGuard.get().is_blocked()`).
  * Blocks new order submissions within ±30 minutes of scheduled Tier-1 macro events (FOMC, CPI, NFP) loaded from `Data/macro_calendar.json` (aligned with institutional 15m candle boundaries, two bars pre-event and two bars post-event).
  * Calendar read errors or unverified coverage fail closed (`is_blocked() -> True`), preventing blind execution during unverified windows, verified by `Tests/Test_Macro_Calendar_Hardening.py`.
  * Open positions continue to be managed via micro-ratchet trailing profit locks; genuine position closes remain authorized during blackouts.
- **EDGE BROWSER PRESERVATION INVARIANT (STRICT OPERATOR DIRECTIVE)**:
  * NEVER terminate, kill, or flush Microsoft Edge (`msedge.exe`) during RAM or system optimization routines.
  * In all memory cleanup scripts (`scripts/deep_optimize_ram.ps1`, `scripts/free_ram.ps1`, and future utilities), Microsoft Edge is strictly exempted from application termination and native working set trimming. Edge instances and user tabs must remain untouched at all times.
- **MANDATORY FUTURE-AGI PLATFORM INTEGRATION & OBSERVABILITY (STRICT OPERATOR DIRECTIVE)**:
  * Always install and use [future-agi/future-agi](https://github.com/future-agi/future-agi) across all workflows and agent runs.
  * Cloned repository: `C:\Users\SIGMA\Documents\Trading\future-agi`.
  * Python core package installed: `futureagi` (Open-source platform for evaluating, observing, tracing, simulations, gateway, and guardrails for AI agents).
  * Always incorporate Future AGI evaluations, tracing, and feedback loops into agent telemetry, model evaluations, and prompt quality scoring.
- **MANDATORY STANDARDIZED TRADING DECISION CHAIN (SOP) & WAKE-UP SKILL SUITE (STRICT OPERATOR DIRECTIVE)**:
  * **Always Enforce Canonical SOP**: On EVERY wake-up turn and on EVERY order decision step, Antigravity and all auxiliary models MUST strictly adhere to and execute through `docs/Mandatory_Rules/STANDARDIZED_TRADING_DECISION_CHAIN.md` (Raw URL: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/Mandatory_Rules/STANDARDIZED_TRADING_DECISION_CHAIN.md`).
  * **Mandatory 10-Step Sequential Traversal**:
    1. *Step 1: Data Contract, Ingestion & Sanity Gate* (`/data-engineer`, `/dataform-bigquery`) — verify clock freshness (< 180s), monotonic OHLCV, 0 nulls, `venue_basis`, and strict spread friction (<= 25 bps Crypto, <= 5 bps TradFi).
    2. *Step 2: Tri-Layer Memory & Trajectory Audit* (`/remember`, `/anti-sycophancy`) — review `session_chat_history.md` and `ACTIVE_CONTEXT.md`; enforce 5 anti-trap invariants; eliminate context amnesia.
    3. *Step 3: AST Knowledge Graph Traversal* (`/graphify`) — inspect repository schema (`graphify-out/graph.json`, 7.4k+ nodes) before modifying code, verifying symbols, contract specifications, and risk formulas.
    4. *Step 4: HTF Auction & Regime Profiling* (`/data-analyst`) — calculate VWAP SD bands, volume profile POC/VAH/VAL, and classify market regime (`TREND_UP`, `TREND_DOWN`, `MEAN_REVERT`, `RANGE_BOUND`, `UNDEFINED`). Stand aside if `UNDEFINED`.
    5. *Step 5: Dual-Engine Strategy Dialectic* (`/brainstorm`, `/data-engineering-data-driven-feature`) — Model 1 Extreme Mean Reversion (|Z| >= 2.0 to 3.5 SD in `MEAN_REVERT` with tape exhaustion) vs Model 2 Trend Pullback (|Z| 0.2 to 1.8 SD pullback to EMA20/EMA50/VWAP/VAL shelf in dominant trend).
    6. *Step 6: Microstructure Coincidence Stack & On-Chain Intel* — cross-verify resting L2/L3 whale walls (persistence >= 180s), multi-horizon taker CVD delta deceleration/absorption, and Arkham on-chain intelligence.
    7. *Step 7: Liquidation & Stop Magnet Dynamics* — ensure SL sits safely outside `[min_price, max_price]` with >= 0.35–0.50 ATR structural buffer; TP front-runs opposing liquidation/stop magnet by 5–10 bps.
    8. *Step 8: Mathematical Risk Budget & Capital Floor Gate* (`/quant-analyst`) — enforce 4,775.00 USD hard floor and 4,795.00 USD operating buffer; verify stressed worst-case equity >= 4,795.00 USD; expanded risk budget 15.00 to 25.00 USD per operator rights; max 2-3 concurrent positions.
    9. *Step 9: Pre-Execution Ex-Ante Audit* (`/verify`, `test-guard`) — verify exact cash risk via `mt5.order_calc_profit`; check passive limit order posture; confirm no spread crossing.
    10. *Step 10: Autonomous Punch & Dynamic Ratchet Lifecycle* (`/quant-analyst`) — punch passive limit order into MT5 immediately without asking; enforce frozen initial R0 ratchet progression (Phase 0 BE cut at +1.25R0, Phase 1 Profit Lock at +1.65R0, Phase 2 Running Trail at >= +2.00R0).
  * **Mandatory All-Attached-Skills Activation on Wake-Up**: Always activate the multi-domain skill ensemble on wake-up for superior decision-making. No decision is ever made in an ad-hoc or single-agent vacuum.
  * **Mandatory Arena.ai Prompt SOP Inclusion**: Every prompt dispatched to Arena.ai, Z.ai, or Copilot Studio MUST explicitly include:
    1. Direct raw URL to `STANDARDIZED_TRADING_DECISION_CHAIN.md`
    2. The 10-Step Decision Chain directive block obligating models to execute each step with skill tags
    3. Mandatory Ingestion Citation requiring models to confirm compliance with the 10-Step Decision Chain.
- **THE 10-STEP AUTONOMOUS JOINT-COMPLETION WAKE-UP CHECKLIST (MANDATORY INVARIANT - docs/Mandatory_Rules/AUTONOMOUS_WAKEUP_CHECKLIST.md)**:
  * *Strict Operational Invariant*: A cycle is NEVER completed upon prompt dispatch. A cycle is ONLY complete once BOTH Antigravity and Arena.ai have completed analysis, outputs are harvested and cross-verified, and all necessary live MT5 actions (order punch, ratchet adjustment, order cancellation) are executed.
  1. *Step 1 — System Health, Telemetry Updation & RAM Optimization*: Inspect `docs/telemetry/live_snapshot_latest.json` to verify telemetry age <= 120s and `autonomous_telemetry_git_daemon.py` is actively committing and pushing every 60s; if stale, run `generate_telemetry_snapshot.py` and relaunch daemon; run `powershell -ExecutionPolicy Bypass -File .agents/scripts/free_ram.ps1` to clear RAM, prune zombie processes, and optimize CPU latency; verify 6 persistent daemons.
  2. *Step 2 — MT5 Account & Capital Floor Defense Audit*: Query `mt5.account_info()` to verify Balance, Equity, and Free Margin. Confirm live equity cushion against the 4,775.00 USD hard floor and 4,795.00 USD operating buffer. Audit open positions (`positions_get()`) and pending orders (`orders_get()`).
  3. *Step 3 — Active Position & Trailing Ratchet Audit*: Enforce Frozen Initial R0 Ratchet progression (Phase 0 BE at +1.25R0, Phase 1 Lock at +1.65R0, Phase 2 Trail at >= +2.00R0).
  4. *Step 4 — Institutional 93-Asset Market Scan*: Run `institutional_95_screener.py` to identify candidates with strict spread friction (<= 5 bps TradFi, <= 25 bps Crypto).
  5. *Step 5 — Dual-Track Analysis Initiation*: Launch Track A (Internal Subagent Research & SOP Traversal via Orderflow, Position, Macro Analysts) and Track B (Prompt Construction & Arena.ai Dispatch via `dispatch_comprehensive_wake_up_prompt.py --arena-only`).
  6. *Step 6 — Arena.ai Completion Wait & Harvesting Gate*: Launch `python Terminal/arena_completion_daemon.py --wait`; wait until Arena.ai finishes generation; harvest `docs/trade_plans/ARENA_LATEST_RAW.md`. Confirm BOTH Antigravity and Arena.ai have completed analysis.
  7. *Step 7 — Joint Output Forensic Cross-Verification & Dialectic Synthesis*: Perform side-by-side comparison of Antigravity internal subagent findings vs Arena.ai recommendations. Audit entry shelves, SL bunker boundaries (`[min_price, max_price]`), TP liquidity magnets, spread costs, and exact cash risk via `mt5.order_calc_profit`.
  8. *Step 8 — Error Correction & Part-B Re-Prompt Gate*: If Arena made any logical, mathematical, or boundary mistake, immediately inject corrective prompt and wait via daemon before taking MT5 actions.
  9. *Step 9 — Autonomous Live Execution on MT5*: If a setup is ratified by verified math and 5-pillar confluence, IMMEDIATELY punch the passive limit order into MetaTrader 5 without asking; apply trailing ratchets or amend/delete pending orders.
  10. *Step 10 — Dual-Repo Git Sync, Record Append & Sentry Arming*: Synchronize git commits across `main` and `arena` branches via `autonomous_telemetry_git_daemon.py`; update `ACTIVE_CONTEXT.md`; append turn record to `session_chat_history.md`; re-arm the 20-minute cycle sentry timer via `schedule` with mandatory prompt template: `Prompt: "MANDATORY WAKE-UP AUDIT: Follow @[c:\Users\SIGMA\Documents\Trading_2\docs\specs\AUTONOMOUS_WAKEUP_CHECKLIST.md] & @[c:\Users\SIGMA\.gemini\antigravity\brain\b00c810a-61bb-46bf-a147-4c8859c64058\LOSING_TRADES_DEEP_FORENSIC_AUTOPSY.md] - execute all 10 steps sequentially: Step 1 System Health, Telemetry Updation Check & RAM, Step 2 MT5 Account, Floor Defense & Forensic Autopsy Audit, Step 3 Position & Ratchet Audit, Step 4 93-Asset Scan, Step 5 Dual-Track Analysis (Internal Subagents + Arena Dispatch), Step 6 Arena Completion Wait & Harvest, Step 7 Joint Cross-Verification, Step 8 Error Correction, Step 9 Autonomous MT5 Live Punch/Ratchet, Step 10 Telemetry Git Sync & Sentry Arming."`. ONLY NOW is the cycle officially complete.
- **ARENA ACTIVE BRANCHES & DUAL-BRANCH TELEMETRY SYNC (STRICT OPERATOR DIRECTIVE)**:
  * Current active Arena.ai branch is `arena/74cd2d1a-trading-2` (alongside prior `arena/7a89a384-trading-2`, Astra `arena/d6de1eb4-trading-2`, Fable `arena/af999588-trading-2`, and `arena/5c05910e-trading-2`). All branches are created on origin and continuously updated by `autonomous_telemetry_git_daemon.py` every 60s alongside `main`.
- **ARENA AUTO-RECOVERY DAEMON (ZERO-TOKEN RECOVERY MANDATE)**:
  * `Terminal/arena_auto_recovery_daemon.py` runs persistently in the background. If it detects the red error banner "The AI service encountered an error. Please try again." on any Arena tab when generation has halted, it automatically injects "continue and fix The AI service encountered an error. Please try again." and hits Enter without human intervention and without token cost.
- **TRI-COUNCIL CROSS-POLLINATION / ADVERSARIAL DIALECTIC ARCHITECTURE (STRICT OPERATOR DIRECTIVE)**:
  * Prompts across the 3 frontier models (GPT_Astra, Claude Fable, Gemini Argon) must be dynamically cross-pollinated:
    - To GPT_Astra: Cross-inject Fable's & Argon's findings and critiques (e.g. Fable's L2 vs L3 persistence proof, TRX spread cost).
    - To Fable: Cross-inject GPT_Astra's & Argon's findings and critiques (e.g. Astra's proof that BTC SL @ 82,213 is inside the basis-mapped liquidation band 82,151–82,251).
    - To Gemini Argon: Cross-inject GPT_Astra's and Fable's findings and critiques for comprehensive deep reasoning review.
- **MINUTE-BY-MINUTE TELEMETRY HISTORICAL LOGGING & IMMUTABLE PROVENANCE (STRICT OPERATOR DIRECTIVE)**:
  * Telemetry is captured and stored continuously:
    - `Data/Hyperdash_Flows/hyperdash_flows_history.json` & `.parquet` (7.05 MB) records full timestamped orderflow and wallet event history.
    - `docs/telemetry/live_snapshot_latest.json` (4.46 MB) is committed to Git every 60s with exact UTC timestamps (`telemetry: observed snapshot [as_of YYYY-MM-DD HH:MM:SS UTC]`), preserving an immutable minute-by-minute historical record accessible across all branches.
- **AUTONOMOUS 59TH-MINUTE SENTRY SCHEDULE (STRICT OPERATOR DIRECTIVE)**:
  * The autonomous desk loop wakes up directly at the **59th minute of every hour** (`59 * * * *`, e.g. 11:59 UTC, 12:59 UTC) to harvest rulings, audit MT5, execute ratified trades, and re-prompt for the next cycle. Intermediate wake-ups between cycles are suppressed to let models complete full generation uninterrupted.
- **ZERO SPURIOUS SCRATCH LITTER**: Clean up all intermediate debug scripts immediately after validation.

## 2. Active Mission & Quantitative Target
- **Universe**: Full broker coverage of **156 Tradeable MT5 Symbols** (Blueberry Markets), with **43 Complete Institutional Universe Assets** (`COMPLETE_UNIVERSE`: 33 Crypto Perpetuals + 10 TradFi CFDs across Indices, Commodities, and Forex in `Terminal/Asset_Universe.py`) supported by 43 historical Parquet datasets (0 nulls) in `Data/Candles/` and real-time dual-venue L2/L3 orderbook depth. The active high-velocity streaming matrix publishes live telemetry across the universe.
- **Active Focus**: Direct Multi-Parameter Coincidence Playbook (`docs/Mandatory_Rules/TRADE_DECISION_PLAYBOOK.md`) across all 24 live telemetry assets (`assets_matrix_24` in `docs/telemetry/live_snapshot_latest.json`) fully upgraded with Multi-Horizon CVD (Session/Weekly/24h), MT5 Lee-Ready synthetic TradFi orderflow & OFI, HTF Auction Profiles (Prior Day/Week POC/VAH/VAL, Weekly VWAP), and Footprint POC Trapped Trader detection. Zero data voids across both Crypto and TradFi.
- **Production State**: 
  * **Autonomous 15-Minute Candle AI Trader & MT5 Bridge (`Terminal/OF_Strategy.py` --mode mt5-trader --live --min-risk 10.0 --max-risk 20.0)**:
    - **Institutional Wake-Up & Collaborative Desk Protocol (STRICT OPERATOR SPECIFICATION)**:
      * **TRI-COUNCIL DECISION ARCHITECTURE (ARENA.AI + Z.AI CHAT + ANTIGRAVITY — STRICT OPERATOR SPECIFICATION)**:
        - **Arena.ai (Two-Way Git & DOM)**: Receives the 3-Mandate prompt via Chrome CDP (`127.0.0.1:9222`), reads GitHub raw URLs, pushes its council report and ledger update to `origin/arena/5c05910e-trading-2`, and is harvested into `docs/trade_plans/ARENA_LATEST_RAW.md`.
        - **Z.ai Chat (One-Way Read-Only Sandbox & DOM Harvest)**: Receives the exact same 3-Mandate prompt simultaneously via Chrome CDP (`textarea#chat-input` / `button#send-message-button` on `chat.z.ai`). Because Z.ai Chat is one-way (can read our prompt and fetch public GitHub raw URLs in its sandbox, but cannot push back to Git), Antigravity harvests Z.ai's completed `.markdown-prose` response directly from the Z.ai Chrome tab DOM into `docs/trade_plans/ZAI_LATEST_RAW.md`.
        - **Antigravity (Final Synthesis & MT5 Execution Muscle)**: Independently audits `docs/telemetry/live_snapshot_latest.json` and live MT5 quotes/risk, compares **Arena.ai + Z.ai Chat + Antigravity** side-by-side across all 3 mandates, re-prompts on any mathematical or boundary flaw, and executes verified rulings on MetaTrader 5.
      * **PHASE 1 — Simultaneous Prompting to Arena.ai & Z.ai Chat (3 Mandatory Points to be Considered in Every Prompt via `Terminal/dispatch_comprehensive_wake_up_prompt.py`)**:
        1. **Mandate 1 (Look for New Trading Opportunities)**: Screen all 24 assets in `docs/telemetry/live_snapshot_latest.json` line-by-line under `docs/Mandatory_Rules/TRADE_DECISION_PLAYBOOK.md` (zero `decision_gates_v3.py` references) to identify high-confluence Model 1 (`|Z| >= 2.0 SD` Mean Reversion) or Model 2 (Trend Pullback to VWAP/VAL/VAH/EMA) passive limit order candidates backed by persistent (`>= 180s`) L3 whale walls, positive L2/CVD absorption, SL outside `min_price`/`max_price` of the bunker, and TP front-running the opposing magnet by 5–10 bps.
        2. **Mandate 2 (Look for Active / Running Trades — Logical TP or SL Modification Based on Latest Data)**: Inspect all active open positions on MetaTrader 5 (`positions_get()`). Evaluate logically based on the latest data snapshot whether TP or SL modification is required: (a) Upgraded Dynamic Ratchets (Phase 0 Risk Cut to -0.25R0 at +1.25R0, Phase 1 Profit Lock at +1.65R0, Phase 2 Continuous Running Trail at >= +2.00R0), or (b) Live Microstructure Shifts (tightening SL behind a newly formed liquidation/stop bunker, adjusting TP to front-run a shifted buy-stop/sell-stop magnet, or emergency exit if the structural shelf broke).
        3. **Mandate 3 (Look for Unfilled Limit Orders — Viability to Wait & Fill vs. Slight Modification vs. Complete Deletion)**: Inspect all pending limit orders on MT5 (`orders_get()`). Check each unfilled limit order logically against the latest data snapshot to determine whether:
           - **(A) Viable & Wait to be Filled As-Is**: Distance `<= 2.0 ATR`, supporting L3 whale walls (`>= 180s`) intact, 5m/15m/30m CVD & L2 depth absorbing, SL outside `min_price`/`max_price`, TP front-running magnet by 5–10 bps.
           - **(B) Slight Modification Required**: Core thesis intact, but shifted whale walls, stop clusters (`nearest_*`), or liquidation band edges require modifying Entry, SL, or TP.
           - **(C) Delete / Cancel Immediately**: Thesis degraded (supporting whale walls pulled/thinned `> 50%`, price drifted `> 2.0 ATR` away, or adverse regime break).
      * **PHASE 2 — Always-On Tri-Council Completion & Instant Wakeup Daemon (`Terminal/arena_completion_daemon.py`)**:
        - Persistent Daemon (`python Terminal/arena_completion_daemon.py --daemon`, `IsDaemon=true`) continuously watches Chrome CDP for both Arena.ai (`ARENA_LATEST_RAW.md`) and Z.ai Chat (`ZAI_LATEST_RAW.md`).
        - Instant Reactive Wakeup (`python Terminal/arena_completion_daemon.py --wait`, `IsDaemon=false`): Launched immediately after every prompt injection into Arena.ai and Z.ai Chat; exits `0` and saves both `docs/trade_plans/ARENA_LATEST_RAW.md` and `docs/trade_plans/ZAI_LATEST_RAW.md` the exact second both councils finish.
      * **PHASE 3 — Antigravity Wake-Up to Check Arena.ai & Z.ai Chat Output (2 Mandatory Steps)**:
        1. **Tri-Council Logical & Quantitative Reasoning Verification**: Compare **Arena.ai + Z.ai Chat + Antigravity's independent telemetry audit** across all 3 mandates (New Opportunities, Active Running Trades, Unfilled Limit Orders) against live MT5 and `docs/telemetry/live_snapshot_latest.json` (`min_price`/`max_price` boundaries, `>= 180s` whale persistence, 15m/30m CVD windows, and `mt5.order_calc_profit` cash risk).
        2. **Same-Cycle Part-B Re-Prompt on Any Flaw (`Cycle NB`)**: If ANY logic does not match live telemetry or if there is ANY flaw in council reasoning or levels, immediately re-prompt as **Part 2 of the exact same cycle (`Cycle NB`)** (`python Terminal/dispatch_comprehensive_wake_up_prompt.py --reprompt-file ...`) and wait via `arena_completion_daemon.py --wait` before executing on MT5.
      * **Position Capacity & Slot Accounting Policy (STRICT OPERATOR DIRECTIVE - OCT 22 2026)**:
        - **Max 4 Running Filled Positions**: Up to 4 maximum running (filled) positions allowed concurrently across orthogonal asset clusters.
        - **Limit Order Slot Rule**: A slot is considered filled ONLY when an order is filled into an active position. Pending/resting limit orders do NOT consume capacity slots!
        - **Full Autonomous Trading Authority**: Antigravity has full autonomous rights to punch, delete, cancel, or modify orders and trailing stops in MetaTrader 5 without seeking manual operator approval.
        - **Solvency Defense & Dynamic Capacity**: Total joint worst-case stopout risk across active running positions unconditionally defends the 4,775.00 USD hard floor and 4,795.00 USD operating buffer. When positions reach Early-BE (+0.75R to +0.80R), stop is ratcheted to Entry + 0.10R0, dropping cash risk to 0.00 USD and instantly freeing risk capacity for subsequent fills.
    - Connects directly via native IPC to MetaTrader 5 Account 5064568 (Blueberry Markets).
    - **Active Positions & Pending Orders (Live State: 0 Active Positions | 1 Resting Limit Order | 4 Available Running Slots)**:
       * Current Status: **0 Active Positions | 1 Resting Limit Order | Balance: 4,818.51 USD | Equity: 4,818.51 USD | Margin: 0.00 USD | Free Margin: 4,818.51 USD**.
       * Hard Floor Defense: Hard Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD | Live Cushion: **+43.51 USD above hard floor (+23.51 USD above operating buffer)**.
       * Live Resting Pending Orders on MetaTrader 5:
         1. **Order #19224157: USDJPY.pi SELL_LIMIT** | Vol: 0.18 | Entry: 157.053 | SL: 157.206 | TP: 156.670 | Max Loss: -.52 | Max Profit: +.00 | R:R: 2.51 | Stressed Equity: 4,794.61 USD (+19.61 floor surplus) | Passive: True
       * Realized Trades This Session:
         - Ticket #19225284 (XAUUSD.pi BUY 0.06 @ 4034.40): Stopped out at 4031.75 during Asian pre-market sweep. Realized Loss: **-.90 USD** (exact 1.00R, 0 slippage). Capital floor defended (+43.51 USD cushion).
       * Candidate Pipeline (45 Total Across 4 Clusters):
         - EURGBP.pi SELL_LIMIT @ 0.83817 (Dist: 0.11% / 9 pips, Risk .51, Profit +.98, R:R 3.13)
         - UK100.p BUY_LIMIT @ 10707.47 (Dist: 0.20% / 21 pts, Risk .97, Profit +.84, R:R 3.00)
         - AUDUSD.pi BUY_LIMIT @ 0.70024 (Dist: 0.18% / 12 pips, Risk .95, Profit +.52, R:R 2.93)
         - BTCUSD.pi SELL_LIMIT @ 81840.00 (Dist: 0.71% / 580 pts, Risk .90, Profit +.69, R:R 3.00)
       * Sentry & Daemon State:
         - All 6 persistent background daemons actively running in Antigravity task manager (manage_task):
           1. Run_Parallel_Pipeline.py --continuous --gap 300 --workers 1 (Task #109472)
           2. schedule Cron (0,20,40 * * * *, 20-min wake-up sentry, Task #109478)
           3. arena_completion_daemon.py --daemon (Task #109474)
           4. autonomous_git_sync_daemon.py (Task #109476)
           5. run_graphify_watcher.py (Task #109451)
           6. gemini_web2api.py on port 8081 (Task #109455)
      * Closed Trades Today (Realized PnL):
        - Ticket #19146275 (NAS100.p closed at **+15.50 USD cash profit** via Full Take Profit at 29,715.00 USD, Deal #17347431, +155.0 pts / +1.03R banked after Early-BE lock at 29,575.00 USD)
        - Ticket #18977509 (`XAUUSD.pi` closed at **-9.07 USD loss** via Stop Loss at 4,148.00 USD during Cycle 138 institutional stop sweep into [4140, 4150] cluster; zero slippage, strictly capped at 1.00R0 nominal risk)
        - Ticket #18969343 (`SP500.p` closed at **+8.80 USD cash profit** via Trailing Stop Loss profit lock at 7,729.70 USD, Deal #17175660, opened at 7,738.50 USD)
        - Ticket #18836609 (`SP500.p` closed at **+0.90 USD cash profit** via Trailing Stop Loss profit lock at 7,807.75 USD, Deal #17073763, opened at 7,810.00 USD)
        - Ticket #18826511 (`ETHUSD.pi` closed at **+1.92 USD cash profit** via Stop Loss profit lock at 2,513.02 USD, Deal #17050770, net +0.51 USD after C49 partial resize)
        - Ticket #18825384 (`SOLUSD.p` closed at **-11.05 USD loss** via Stop Loss at 108.55 USD after `108.34 / 108.75` Ask Whale walls relocated above 108.55 to 108.68 / 109.22)
        - Ticket #18813767 (`BTCUSD.pi` closed at **+16.10 USD cash profit** via Full Take Profit at 81,845.00 USD, Deal #17024690, +1.71R banked after Phase 0 BE Lock at 82,579.50 USD)
        - Ticket #18813768 (`SOLUSD.p` closed at **+9.52 USD cash profit** via Autonomous Ratchet Daemon Phase 1 Profit Lock Stop Loss at 107.32 USD, Deal #17024104, +0.80R banked)
        - Ticket #18813343 (`BTCUSD.pi` closed at **-11.58 USD loss** via Stop Loss at 82,158.00 USD, Deal #17022979, during market cascade)
        - Ticket #18795304 (`SOLUSD.p` closed at **-10.88 USD loss** via Stop Loss at 108.79 USD during deepening crypto flush)
        - Ticket #18791527 (`BTCUSD.pi` closed at **-11.20 USD loss** via Stop Loss at 82,590.00 USD during capitulation flush to 82,627 USD)
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
        - Net Realized Session PnL: **+110.57 USD** across 20 completed trades (initial capital 5,000.00 USD; 98.44% preserved; 14 wins / 6 losses = 70.0% win rate).
      * 360-Degree Forensic Verification Certification: [`Terminal/chain_verification_360.py`](file:///c:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py) reports `CERTIFIED_100_PERCENT_PRISTINE`. All 24 Parquet archives verified with 0 nulls and 100% strictly monotonic timestamps; causal anti-lookahead verified; broker feed ping 3.65 ms; Binance L2 depth monotonic; full pytest suite passing (405 passed, 0 failed).
      * Current collaborative cycle: Cycle 66 tailored prompts successfully injected across all 4 tabs (Arena Tab 1 GPT Astra, Arena Tab 2 Claude Fable Orchestrator, Copilot Studio Tab 1 Claude Opus 5.5, Copilot Studio Tab 2 GPT Astra) with the complete Retracement Stop Loss Defense Invariant (Gates R-1 to R-4) active.
      * **Triple-Branch Real-Time Telemetry Git Sync**: Autonomous background telemetry git daemon (`Terminal/Data_Factory/autonomous_telemetry_git_daemon.py`, PID 19644) actively streaming and publishing authentic observed telemetry snapshots every 60s to all 3 canonical remote branches simultaneously: `main`, `arena/5c05910e-trading-2`, and `arena/e3d7cc98-trading-2`. 30-minute autonomous cron (`task-56500`, schedule `28,58 * * * *`) governs periodic wake-ups. Standalone arena completion daemon killed. Account in 1 open position (Ticket #18847111 ETHUSD.pi SHORT 0.50 lots @ 2,508.50 USD), cushion +96.23 USD above hard floor. Operating within 100% mathematical integrity.

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
- **Microstructure Piecewise Ratchet (Anti-Choke & Anti-Retracement Invariant)**:
  - Phase 0 (BE Lock): At +1.25R0 gain, move SL to Entry + 0.20R0 (clears spread/friction and avoids choking early 0.8R expansion and retests).
  - Phase 1 (Profit Lock): At +1.65R0 gain, move SL to Entry + 1.00R0 (locks in +1.00R guaranteed profit).
  - Phase 2 (Running Trail): At +2.00R0 gain, move SL to Entry + 1.50R0 (locks in +1.50R profit, preventing +2.0R to +2.5R trades from round-tripping).
  - Target Extension Safeguard: At +2.30R0 gain (near +2.50R target), move SL to Entry + 1.85R0 (safeguards profit if target is front-run).
  - Time Decay: Exit at market if trade fails to gain +0.20R within 24 bars (6 hours).

## 4. Local Execution Protocol
- **End-to-End Local Development**: All strategy logic, ML training, walk-forward simulations, and risk governance are implemented, tested, and optimized directly within the local python environment.
 - **Strict Anti-Lookahead Enforcement**: Historical signal tests may book entry only on a subsequently observed bar or tick, such as `opens[j+1]`; never use the signal candle close as its fill. Live execution consumes completed HTF bars and stages passive limits against fresh quotes, then reconciles actual broker fills. Causal HTF `shift(1)` backward-as-of joins and zero test-set tuning remain mandatory.
- **Zero Dollar Signs**: Strict prohibition on dollar symbols; always write USD.

## 5. Quantitative Knowledge Grounding & Minimal Token Reference Mandate
- **Always Reference Quant-Developers-Resources**: For all quantitative modeling, risk management, econometrics, and execution math, actively ground solutions in the canonical libraries inside `Quant-Developers-Resources-main/` (Risk Management, Econometrics, Financial Theory, Technical Indicators, Microstructure, and C++).
- **Minimal Token Querying via Graphify**: NEVER dump entire files into context. Always query specific subgraphs via `python -m graphify query "<concept>" --budget 300` or `graphify explain "<concept>"` to retrieve scoped AST nodes, classes, and call-flows with minimal token footprint.

## 6. Institutional Orderflow & Microstructure Live Execution Checklist (Always Enforced)
- **Canonical Checklist**: Strictly follow `[docs/Mandatory_Rules/institutional_orderflow_live_checklist.md](file:///c:/Users/SIGMA/Documents/Trading_2/docs/Mandatory_Rules/institutional_orderflow_live_checklist.md)` on every 14th-minute wake-up cycle.
- **Pre-Order Gating**: Must verify all 7 sub-gates (Price Action geometry, CVD divergence, 20-level L2 depth, L3 whales >= 150k USD with >= 180s persistence, liquidation FFR, macro blackouts, covariance room vs 4,775.00 USD floor).
- **Smart SL & TP Adjustments**: Deterministic ratchets (Phase 0 BE @ +0.80R, Phase 1 Profit Lock @ +1.50R, Phase 2 Trailing Lock @ +2.00R). TP extensions into orderbook liquidity vacuums require simultaneous Phase 2 SL profit lock.

## 7. Live Account State & Active Orderflow Invariants (Cycle 249 Verified)
- **MT5 Account State (Blueberry Markets Account #5064568)**:
  * Balance: **4,834.83 USD**
  * Live Equity: **4,834.83 USD** (100% Flat in Cash, Margin: 0.00 USD)
  * Free Margin: **4,834.83 USD**
  * Hard Floor (4,775.00 USD) Cushion: **+59.83 USD (+1.25%)**
  * Operating Buffer (4,795.00 USD) Cushion: **+39.83 USD (+0.83%)**
  * Remaining Distance to 5,500.00 USD Goal: **+665.17 USD** (~37.2 hours remaining to Oct 23, 23:59 UTC)

- **Active Market Positions (0 of 4 slots filled, 4 slots available)**:
  * 100% Flat in Cash. Zero active market positions.
  * Solvency Cushion: Stressed Equity post-loss under Scenario B (1 position @ 20.00 USD nominal risk) = **4,807.83 USD** (**+12.83 USD above 4,795.00 USD Operating Buffer**, **+32.83 USD above 4,775.00 USD Hard Floor**).
  * Capacity Policy: Max 4 running filled positions authorized. Limit orders do NOT consume slots. Full autonomous trading rights active.

- **Active Pending Limit Orders (0 resting | Limit orders do NOT consume slots)**:
  * None resting. Gated strictly on 5-pillar confluence and Anti-Knife Contract.

- **Potential Candidate Radar (Cycle 249 Calibrated — Sheet 33 Auction Structure Integrated)**:
  1. **BTCUSD.pi (Institutional Demand Sweep & Whale Bunker Retest)**: Entry 81,640.0 | SL 81,240.0 (400 pts) | TP 82,640.0 (1,000 pts / +2.5R0) | Lot 0.03 (12.00 USD risk | Stressed: 17.00 USD) | Pre-conditions: flush of 22.77M USD sell-stop cascade at [81,650–81,850 USD] + 15m CVD absorption flip + 81,637–81,670 USD wall (7.53M USD) persistence.
  2. **XAUUSD.pi (Deep Fortress Whale Bunker Rebound)**: Entry 4,081.00 | SL 4,074.50 (6.50 pts) | TP 4,097.25 (16.25 pts / +2.5R0) | Lot 0.02 (13.00 USD risk | Stressed: 18.25 USD) | Pre-conditions: test into 4,080.00–4,081.00 USD bunker (0.941M USD / 475 oz, persist >12h) + tick CVD flip to buyer absorption.
  3. **SOLUSD.p (Deep Structural Demand Shelf)**: Entry 103.80 | SL 102.30 (1.50 pts) | TP 107.55 (3.75 pts / +2.5R0) | Lot 0.10 (15.00 USD risk | Stressed: 20.75 USD) | Pre-conditions: flush of retail stops below 104.00 USD + 15m CVD delta deceleration (>30%) + 103.75 USD wall (0.83M USD) persistence.
