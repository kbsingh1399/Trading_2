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
    Step4["Step 4: Master 33-Sheet Excel Integrity<br/>(Verify DataBase_Trading.xlsx & Zero Errors)"]
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


### STEP 2.1: POSITION CAPACITY, LIMIT ORDER ACCOUNTING & AUTONOMOUS AUTHORITY (OPERATOR MANDATE)
1. **Max 4 Running Filled Positions**: The desk is authorized to maintain up to 4 concurrent running (filled) positions across orthogonal asset clusters.
2. **Limit Order Slot Rule**: A slot is considered filled ONLY when an order is filled into an active position. Resting/pending limit orders do NOT consume capacity slots! Limit orders may be pre-staged at structural whale shelves without blocking capacity.
3. **Full Autonomous Trading Rights**: Antigravity has full autonomous rights to punch, delete, cancel, or modify orders and trailing stops in MetaTrader 5 without seeking manual operator approval.
4. **Dynamic Buffer Defense**: Single filled trades risk 15.00–20.00 USD nominal. Once a filled position reaches Early-BE (+0.75R to +0.80R), its stop is ratcheted to Entry + 0.10R0, dropping risk to 0.00 USD and instantly freeing risk capacity for subsequent fills while preserving the 4,795.00 USD operating buffer.

### STEP 3: QUAD-DAEMON SENTRY AUDIT & AUTO-RESTART
Verify with `manage_task(Action='list')` that EXACTLY the 4 authorized persistent background processes are active. Any extra or zombie processes are killed immediately. If any of the 4 required daemons is missing, immediately relaunch it:

1. **Daemon 1 (Continuous 33-Sheet Excel Pipeline Daemon)**:
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
   - Purpose: Monitors Chrome CDP (port 9222) continuously. The instant Arena.ai completes its response, it auto-harvests the full output into `docs/trade_plans/ARENA_LATEST_RAW.md` and wakes up Antigravity for joint evaluation.

4. **Daemon 4 (Autonomous 5-Minute Git Sync Daemon)**:
   - Command: `python Terminal/Data_Factory/autonomous_git_sync_daemon.py`
   - Setting: `IsDaemon=true`, `WaitMsBeforeAsync=500`
   - Purpose: Runs continuously every 5 minutes (300s). Stages all modified and new workspace files (`git add -A`), validates `Data/DataBase_Trading.xlsx` zip CRC integrity before committing, commits with timestamped provenance, and pushes cleanly to `origin/main`. Guarantees zero local/remote desynchronization with zero manual intervention.

---

### STEP 4: MASTER 32-SHEET EXCEL INTEGRITY GATE
Verify that `Data/DataBase_Trading.xlsx` is fresh, uncorrupted, and has zero formula errors:
- Path: `Data/DataBase_Trading.xlsx` (Size ~12.9 to 13.7 MB).
- Check that all 33 sheets (including Sheet 33 '20_Auction_Market_Structure') load cleanly via `openpyxl`.
- Attest that formula errors (`#REF!`, `#DIV/0!`, `#N/A`, `#VALUE!`, `#NAME?`, `#NUM!`, `#NULL!`) count = 0 across all cells.

---

### STEP 5: SIMULTANEOUS DUAL-TRACK DISPATCH (4-SUBAGENT FLEET & ARENA.AI IN PARALLEL)
On EVERY autonomous wake-up, the agent executes the **Simultaneous Dual-Track Dispatch Protocol**:
1. **Track A (Internal Subagent Fleet Invocation in Parallel)**:
   - Immediately invoke all 4 specialized subagents simultaneously using `invoke_subagent` (`Model='flash'`):
     * **Subagent 1: Orderflow Analyst** (Tier 2 Big Prompt: Sheets 00–28, spread gates, 5-pillar confluence, L2/L3 orderbook depth, resting whale bunkers).
     * **Subagent 2: Position Manager** (Tier 2 Big Prompt: MT5 telemetry, ratchet progression, stressed capacity audit strictly enforcing 1-position slot under +$39.83 buffer).
     * **Subagent 3: Macro Risk Analyst** (Tier 2 Big Prompt: Sheet 28 `19_Calendar`, `macro_calendar.json`, ETF flows, CEX netflows, 21:15–22:30 UTC rollover embargo).
     * **Subagent 4: Excel Data Quality Auditor** (Tier 2 Big Prompt: 33-sheet coverage, CRC checks, zero formula errors, pipeline daemon health).
2. **Track B (Parallel Arena.ai Red-Team Prompt Dispatch)**:
   - PARALLEL TO SUBAGENT INVOCATION, immediately dispatch the surgical red-team prompt to Arena.ai via Chrome CDP on port 9222:
     `python Terminal/dispatch_arena_redteam.py`
   - Arena.ai begins generation on Chrome CDP simultaneously while subagents conduct their independent empirical analyses.

---

### STEP 6: REACTIVE HARVEST, ARENA OUTPUT EVALUATION, CO-EQUAL DEBATE & PRUNING
1. **Reactive Auto-Wakeup**: Standby for incoming messages. When the subagents finish or when `arena_completion_daemon.py` detects completion, Antigravity wakes up reactively with zero token polling.
2. **Mandatory Arena.ai Evaluation**: Immediately read `docs/trade_plans/ARENA_LATEST_RAW.md` harvested by the daemon. Thoroughly evaluate Arena.ai's ruling, entry/SL/TP critiques, 17-gate audit, and mathematical proofs.
3. **Co-Equal Council Synthesis & Dialectic Debate**:
   - Synthesize Arena.ai's critique with the independent findings of all 4 subagents.
   - If mathematical confluence, resting whale defense, and Anti-Knife contracts are validated: punch live limit order into MT5.
   - If market momentum flushes toward un-swept stops or safe stops exceed the risk budget: issue unanimous **STAND ASIDE IN 100% CASH** and update the Candidate Radar Checklist.
4. **Clean Socket Pruning Mandate**: Immediately execute `manage_subagents(Action='kill_all')` to terminate all SSE connections and prevent Windows socket exhaustion.
5. **Desk Ledger Update**: Update `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md`, `ACTIVE_CONTEXT.md`, and append turn to `.agents/memory/session_chat_history.md`.
6. **5-Minute Git Sync**: Daemon 4 automatically pushes all committed state to `origin/main` within its 300s window.
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
