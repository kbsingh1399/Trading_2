# 🎯 ACTIVE GOAL: PASS BLUEBERRY PHASE 1 (BY END OF OCT 23, 2026)

> **Execution Directive**: `/goal GOAL.md` (Autonomous Long-Running Execution Active)  
> **Target Account**: Blueberry Markets MT5 Account #5064568  
> **Profit Target**: **5,500.00 USD** (+665.17 USD required from current 4,834.83 USD realized equity)  
> **Deadline**: End of Friday, 23rd October 2026 (23:59 UTC)  
> **Inviolable Floor**: **4,775.00 USD** (Never breach under any circumstance)  
> **Operating Buffer**: **4,795.00 USD** (+20.00 USD defense cushion)  
> **Risk Allocation**: 15.00 to 25.00 USD per trade | Frozen R0 Dynamic Profit Ratchet  
> **Authority**: Full autonomous order execution granted by operator  
> **Council Engine**: Antigravity Live Desk & Arena.ai Co-Equal Investment Council  
> **Standard Dual-Council Prompt Template**: `Data/Manditory/Arena_GLM_Standard_Prompt.md` (Mirrored to `docs/prompts/Arena_GLM_Standard_Prompt.md`)  

---

## 🏛️ Mandatory Governance Files in `Data/Manditory/`

All 6 core governance documents reside strictly in [`Data/Manditory/`](file:///c:/Users/SIGMA/Documents/Trading_2/Data/Manditory):
1. **[`ACCOUNT_SWITCH_BOOTSTRAP_PROTOCOL.md`](file:///c:/Users/SIGMA/Documents/Trading_2/Data/Manditory/ACCOUNT_SWITCH_BOOTSTRAP_PROTOCOL.md)**: Universal bootstrap protocol for account switching and daemon initialization.
2. **[`AUTONOMOUS_WAKEUP_CHECKLIST.md`](file:///c:/Users/SIGMA/Documents/Trading_2/Data/Manditory/AUTONOMOUS_WAKEUP_CHECKLIST.md)**: 10-Step Non-bypassable Joint-Completion Wake-Up Sequence.
3. **[`STANDARDIZED_TRADING_DECISION_CHAIN.md`](file:///c:/Users/SIGMA/Documents/Trading_2/Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md)**: Standard Operating Procedure for 5-pillar quantitative confluence.
4. **[`GOAL.md`](file:///c:/Users/SIGMA/Documents/Trading_2/Data/Manditory/GOAL.md)**: Operational `/goal` mission tracker.
5. **[`PASS_BLUEBERRY_PHASE_1_BY_OCT_23_2026.md`](file:///c:/Users/SIGMA/Documents/Trading_2/Data/Manditory/PASS_BLUEBERRY_PHASE_1_BY_OCT_23_2026.md)**: Deep roadmap and risk sizing formulas to pass Phase 1.
6. **[`SUBAGENT_PROMPT_TEMPLATES.md`](file:///c:/Users/SIGMA/Documents/Trading_2/Data/Manditory/SUBAGENT_PROMPT_TEMPLATES.md)**: Canonical Tier 2 Full Unabridged Big Prompts (~350–500 tokens) citing `STANDARDIZED_TRADING_DECISION_CHAIN.md`. **USE THESE TEMPLATES EVERY CYCLE.**

---

## 🔄 Autonomous Execution Lifecycle (Joint 3-Entity Completion & 20-Minute Relative Delay)
The autonomous desk operates under a non-overlapping joint-completion lifecycle managed by `Terminal/joint_cycle_controller.py` and `Data/cycle_state.json`:
1. **Joint 3-Entity Completion Gate**: Cycle X is marked officially **FINISHED** only when **ALL THREE entities complete processing**:
   - Antigravity 4-Quant Subagent Swarm (Fable 5)
   - Arena.ai Frontier Council (GPT Astra)
   - Z.ai Sovereign Council (GLM-5.3-Flash)
2. **Strict 20-Minute Separation**: The trigger for Cycle X+1 is scheduled strictly for `T_completed(Cycle X) + 20 minutes` (1200 seconds). Prevents cycle overlap and context collapse.
3. **30-Minute Watchdog Sentry Cron (`0,30 * * * *`)**: Monitors cycle health, catches stalled cycles (>30 min), verifies all persistent daemons, and triggers cycle advancement safely once the clean 20-minute separation has elapsed.
4. **Execution Steps on Cycle Wakeup**:
   - Verify that all authorized persistent background daemons are running in Antigravity task manager (`manage_task(Action='list')`).
   - Query AST knowledge graph via `/graphify` or `python -m graphify query` to preserve context.
   - Read `Data/Manditory/SUBAGENT_PROMPT_TEMPLATES.md` — inject full Tier 2 Big Prompts citing `STANDARDIZED_TRADING_DECISION_CHAIN.md` for all 4 Fable 5 subagents.
   - Dispatch `Data/Manditory/Arena_GLM_Standard_Prompt.md` simultaneously to Arena.ai (GPT Astra) and Z.ai (GLM-5.3-Flash) via Chrome CDP port 9222.
   - Verify system health and continuous 33-sheet Excel data updation (5m rest interval).
   - Query live MT5 account telemetry and audit floor cushion (+43.51 USD above 4,775 USD floor, +23.51 USD above 4,795 USD buffer).
   - Audit open positions and ratchet stops using Frozen R0 piecewise protocol.
   - Auto-harvest Arena and Z.ai outputs via `arena_completion_daemon.py` and `zai_completion_daemon.py`.
   - Cross-verify all reports across the Co-Equal Council. Macro blackout verdict overrides Orderflow recommendation.
   - Punch qualified limit orders autonomously into MetaTrader 5 without waiting for confirmation.
   - Mark cycle completed via `Terminal/joint_cycle_controller.py`, sync state to GitHub `origin/main`, cleanly prune subagent sockets via `manage_subagents(Action='kill_all')`, and standby.
