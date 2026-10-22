# 🚀 CROSS-ACCOUNT BOOTSTRAP & RE-ENGAGEMENT MASTER SOP
## Universal Turn-0 Reconnection Protocol for Blueberry Markets Autonomous Desk

> **Document Status**: CANONICAL PRODUCTION RE-ENGAGEMENT PROTOCOL  
> **Location**: `Data/Manditory/ACCOUNT_SWITCH_BOOTSTRAP_PROTOCOL.md`  
> **Purpose**: When the operator switches Gemini/Antigravity accounts, launches a new session, or re-engages after an interruption, the incoming agent MUST execute this exact sequence to achieve 100% operational continuity, restore all background daemons, verify account solvency, and resume autonomous 20-minute multi-agent execution with zero context amnesia.

---

## ⚡ OPERATOR QUICK-START TRIGGER (COPY & PASTE TO ANY NEW AGENT)

```markdown
Read and execute Data/Manditory/ACCOUNT_SWITCH_BOOTSTRAP_PROTOCOL.md immediately.
Verify MT5 connectivity, audit account solvency, verify all 5 persistent daemons, and launch the mandatory 4-subagent fleet and Arena.ai council for the current 20-minute cycle.
```

---

## 🏛️ PART 1: THE 6-STEP BOOTSTRAP ACTIVATION CHAIN

Whenever an agent receives the trigger or re-engages on a fresh session, execute these 6 steps sequentially without asking:

```mermaid
flowchart TD
    Step1["Step 1: Ingest Core Governance & Memory<br/>(AGENTS.md, ACTIVE_CONTEXT.md, session_chat_history.md)"]
    Step2["Step 2: Live MT5 Telemetry & Solvency Audit<br/>(Query Account, Cushions, Positions, Pending Orders)"]
    Step3["Step 3: Hexad-Daemon Sentry Audit<br/>(Verify 5 Daemons + 20-Min Cron Active)"]
    Step4["Step 4: Master 32-Sheet Excel Integrity<br/>(Verify DataBase_Trading.xlsx & Zero Errors)"]
    Step5["Step 5: Mandatory 4-Subagent Swarm & Arena Dispatch<br/>(Orderflow, Position, Macro, Excel Auditor + Arena CDP)"]
    Step6["Step 6: Harvest, Co-Equal Debate, Clean Socket Pruning<br/>(kill_all Subagents, Update Desk Ledger, Standby)"]

    Step1 --> Step2 --> Step3 --> Step4 --> Step5 --> Step6
```

### STEP 1: INGEST CORE GOVERNANCE & MEMORY (ZERO AMNESIA)
1. Physical Reading Gate: Physically load and read the following core files using `read_file`:
   - `Data/Manditory/GOAL.md` (Active mission anchor, target 5,500.00 USD, runway to Oct 23, 2026)
   - `.agents/rules/ACTIVE_CONTEXT.md` (Real-time live account state, open positions, floor cushions)
   - `.agents/memory/session_chat_history.md` (Tail 100 lines — recent turns, avoided traps, lost trade autopsies)
   - `Data/Manditory/AUTONOMOUS_WAKEUP_CHECKLIST.md` (10-Step autonomous sequence)
   - `docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md` (Canonical 10-Step Quant SOP)
   - `Data/Manditory/TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md` (Lethal trading traps)
2. Compliance Header: Emit the mandatory acknowledgment line at the top of your response:
   ```
   ✅ AGENTS.md fully loaded — All 12 Core Domains & Execution Protocols Activated.
   > 📚 Active Skills Loaded & Applied: @[quant-analyst], @[clean-code], @[systematic-debugging]
   ```

### STEP 2: LIVE MT5 TELEMETRY & SOLVENCY SENTRY
1. Initialize MetaTrader 5 and export fresh telemetry to `Data/telemetry/mt5_account_telemetry.json`:
   ```bash
   python -c "
   import json, pathlib, datetime, MetaTrader5 as mt5
   ROOT = pathlib.Path('.')
   if mt5.initialize():
       acc = mt5.account_info()
       positions = mt5.positions_get()
       orders = mt5.orders_get()
       pos_list = [{'ticket': p.ticket, 'symbol': p.symbol, 'direction': 'BUY' if p.type == 0 else 'SELL', 'volume': p.volume, 'price_open': p.price_open, 'sl': p.sl, 'tp': p.tp, 'profit_usd': p.profit} for p in (positions or [])]
       order_list = [{'ticket': o.ticket, 'symbol': o.symbol, 'direction': 'BUY_LIMIT' if o.type == 2 else 'SELL_LIMIT' if o.type == 3 else str(o.type), 'volume': o.volume_current, 'price_open': o.price_open, 'sl': o.sl, 'tp': o.tp} for o in (orders or [])]
       telemetry = {
           'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'account': {
               'balance_usd': acc.balance, 'equity_usd': acc.equity, 'margin_usd': acc.margin,
               'margin_free_usd': acc.margin_free, 'margin_level': acc.margin_level,
               'hard_floor_cushion_usd': round(acc.equity - 4775.0, 2),
               'operating_buffer_cushion_usd': round(acc.equity - 4795.0, 2)
           },
           'open_positions_count': len(pos_list), 'open_positions': pos_list,
           'pending_orders_count': len(order_list), 'pending_orders': order_list
       }
       out_path = ROOT / 'Data' / 'telemetry' / 'mt5_account_telemetry.json'
       out_path.parent.mkdir(parents=True, exist_ok=True)
       with open(out_path, 'w', encoding='utf-8') as f: json.dump(telemetry, f, indent=2)
       print('MT5 Connected: Equity =', acc.equity, 'Floor Cushion =', telemetry['account']['hard_floor_cushion_usd'])
       mt5.shutdown()
   "
   ```
2. Verify Inviolable Solvency Cushions:
   - Hard Floor (4,775.00 USD): Equity - 4,775.00 USD must be strictly positive (Never breach under any condition).
   - Operating Buffer (4,795.00 USD): Equity - 4,795.00 USD (+20.00 USD defense cushion).
   - Worst-Case Stressed Post-Loss Equity: `Equity - sum(Risk_i * 1.25 + 2.00) >= 4,795.00 USD`.

### STEP 3: TRI-DAEMON SENTRY AUDIT & AUTO-RESTART (NO TELEMETRY DAEMON)
Verify with `manage_task(Action='list')` that EXACTLY the 3 authorized persistent background processes are active. Any extra daemons (such as legacy telemetry git daemon) are strictly unauthorized and must be killed immediately. If any of the 3 required daemons is missing, immediately relaunch it:

1. **Daemon 1 (Continuous 32-Sheet Excel Pipeline Daemon)**:
   - Command: `python Data/Excel_Modules/Run_Parallel_Pipeline.py --continuous --gap 300 --workers 1`
   - Setting: `IsDaemon=true`, `WaitMsBeforeAsync=500`
   - Purpose: Cycles full pipeline continuously with an exact 5-minute (300s) cooldown gap between cycles. Maintains fresh orderbook, CVD, liq maps, and technical data in `Data/DataBase_Trading.xlsx` with zero race conditions (workers=1 atomic safety).

2. **Daemon 2 (20-Minute Cron Sentry)**:
   - Tool: `schedule`
   - Setting: `CronExpression="0,20,40 * * * *"`, `IsDaemon=true`
   - Purpose: Autonomous wake-up at 20th, 40th, and 60th/00th minute.

3. **Daemon 3 (Arena Completion Daemon)**:
   - Command: `python Terminal/arena_completion_daemon.py --daemon`
   - Setting: `IsDaemon=true`, `WaitMsBeforeAsync=500`
   - Purpose: Monitors Chrome CDP (port 9222) and auto-harvests Arena responses to `docs/trade_plans/ARENA_LATEST_RAW.md`.

> ⚠️ **TELEMETRY GIT DAEMON RETIRED / DISABLED**:
> The legacy `autonomous_telemetry_git_daemon.py` is permanently DEPRECATED and MUST NOT BE RUN. It spams git commits every 60s and consumes unnecessary CPU. Git synchronization is executed manually upon milestones or cycle completions only. Zero telemetry daemons allowed.

### STEP 4: MASTER 32-SHEET EXCEL INTEGRITY GATE
Verify that `Data/DataBase_Trading.xlsx` is fresh, uncorrupted, and has zero formula errors:
- Path: `Data/DataBase_Trading.xlsx` (Size ~12.9 to 13.1 MB).
- Check that all 32 sheets load cleanly via `openpyxl`.
- Attest that formula errors (`#REF!`, `#DIV/0!`, `#N/A`, `#VALUE!`) count = 0 across all 1.6M+ cells.

### STEP 5: MANDATORY 4-SUBAGENT FLEET & ARENA.AI DISPATCH (COMPREHENSIVE BIG PROMPTS)
On EVERY autonomous wake-up, the agent is STRICTLY FORBIDDEN from generating narrative prose or doing manual checks before dispatching the subagents. The agent MUST FIRST call `invoke_subagent` for all 4 subagents in parallel (using `Model='flash'`). Per operator directive ("ensure we prompt big prompts"), always inject the full, comprehensive **Tier 2 Big Prompts** from `Data/Manditory/SUBAGENT_PROMPT_TEMPLATES.md` to ensure deep, exhaustive forensic rigor across all 32 sheets:

1. **Subagent 1: Orderflow Analyst** (`invoke_subagent(TypeName='research', Role='Orderflow Analyst', Model='flash', ...)`):
   - Injects Tier 2 Subagent 1 prompt: Full line-by-line study of `Data/DataBase_Trading.xlsx` (Sheets 00–28).
   - Evaluates spread gates, 5-pillar confluence, L2/L3 orderbook depth, resting whale bunkers (BTC 80,300 USD, Gold 4,060 USD), and CVD divergences.
   - Formulates the Potential Candidate Radar Checklist `[ ]` with checkable pre-condition triggers.

2. **Subagent 2: Position Manager** (`invoke_subagent(TypeName='research', Role='Position Manager', Model='flash', ...)`):
   - Injects Tier 2 Subagent 2 prompt: Audits MT5 telemetry, verifies open position ratchets (Early-BE at +0.75R to +0.80R, Phase 0 at +1.25R, Phase 1 at +1.65R).
   - Computes stressed capital capacity under the expanded $15.00–$20.00 nominal risk envelope (strictly 1 live position slot under current +$39.83 buffer cushion).

3. **Subagent 3: Macro Risk Analyst** (`invoke_subagent(TypeName='research', Role='Macro Risk Analyst', Model='flash', ...)`):
   - Injects Tier 2 Subagent 3 prompt: Audits Sheet 28 (`19_Calendar`) and `Data/macro_calendar.json` for high-impact Tier-1 events in next 4h.
   - Audits institutional ETF spot inflows/redemptions and CEX netflows.
   - Enforces the 21:15–22:30 UTC interbank FX rollover blackout.

4. **Subagent 4: Excel Data Quality Auditor** (`invoke_subagent(TypeName='research', Role='Excel Data Quality Auditor', Model='flash', ...)`):
   - Injects Tier 2 Subagent 4 prompt: Audits all 32 sheets for freshness, row counts, and zero formula errors.
   - Audits continuous pipeline daemon (`task-104314`) and 5-minute rest interval cycling.

5. **Arena.ai Co-Equal Quantitative Council**:
   - Injects full, comprehensive Big Prompts (such as `ARENA_CYCLE_245_RECALIBRATED_SETUPS.txt`) containing full market microstructure footprint, 17-gate criteria, and detailed mathematical questions.

5. **Arena.ai Surgical Red-Team Dispatch**:
   - Run `python Terminal/dispatch_arena_redteam.py` to inject the standardized surgical red-team prompt into Arena.ai via Chrome CDP on port 9222.
   - Launch reactive watcher `python Terminal/arena_completion_daemon.py --wait` (`WaitMsBeforeAsync=500`).

### STEP 6: HARVEST, CO-EQUAL DEBATE & SOCKET PRUNING
1. Wait reactively for subagent messages and Arena completion (Zero token polling; never use timers <= 60s).
2. Harvest Arena response from `docs/trade_plans/ARENA_LATEST_RAW.md`.
3. Conduct Co-Equal Council debate:
   - Compare subagent empirical findings against Arena red-team critique.
   - If 5-pillar confluence passes with verified resting whale walls, punch limit order live into MT5.
   - If 5-pillar confluence fails or active seller momentum flushes toward un-swept stops, issue unanimous **STAND ASIDE UNCONDITIONALLY** while updating candidate radar pre-conditions.
4. **Clean Socket Pruning Mandate**: Immediately execute `manage_subagents(Action='kill_all')` to terminate SSE connections and eliminate Windows socket leaks.
5. Update `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md`, `ACTIVE_CONTEXT.md`, and append turn to `.agents/memory/session_chat_history.md`.
6. Synchronize dual-repo parity via `python .agents/scripts/verify_and_sync_agents.py`.

---

## 🔒 PERPETUAL GOAL INVARIANTS (NEVER COMPROMISED)
1. **Perpetual Goal Contract**: Under NO circumstances may `<!-- GOAL_COMPLETE -->` or `<!-- GOAL_CANCELLED -->` be emitted until live equity >= 5,500.00 USD is proven on MetaTrader 5.
2. **Inviolable Hard Floor**: 4,775.00 USD must NEVER be breached under any condition (0 exceptions).
3. **Operating Buffer Defense**: 4,795.00 USD (+20.00 USD cushion) strictly preserved under worst-case 1.25x slippage stress.
4. **Strict Passive Limit Execution**: Passive limit orders only, safely anchored behind resting institutional whale walls (>= $100K to $1M+, persisting >= 180s). Zero market orders crossing the spread.
5. **Zero Token Polling**: Polling timers <= 60s are permanently banned. Rely strictly on native event-driven reactive wakeups and the 20-minute cron sentry (`0,20,40 * * * *`).
6. **Plain-Text Formatting**: Zero raw LaTeX delimiters (`$` or `$$`) in chat responses; write plain-text variables and USD amounts.
