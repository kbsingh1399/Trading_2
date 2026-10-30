path = 'Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Section 0 to reference the 4 mandatory governance documents and 7-day memory
sec0_target = """### 0.4 Canonical Spread & Blackout Gates"""

sec0_addition = """### 0.4.1 Mandatory Canonical Governance Document Read Gate (Line-by-Line Study on Every Cycle)
On EVERY single turn, cycle wakeup, candidate scan, and subagent dispatch, the coordinator and all agents MUST systematically read and ingest the last 7 days of session history (`.agents/memory/session_chat_history.md`, past turns, transcript), the persistent memory index (`.agents/memory/MEMORY.md`), and operator directives (`.agents/memory/operator-directives.md`) via the persistent `memory-system`.

Furthermore, before evaluating ANY candidate asset or proposing/executing ANY trade, the desk MUST physically execute the **4-Document Governance Read Gate**:
1. `Read: Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md` (Section 1.7 SOP, Section 1.5 Dynamic Capacity Policy, Section 2 In-Memory Pre-Load Architecture, Section 10 Active Order Management).
2. `Read: Data/Manditory/TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md` (Verify zero ghost whale walls [Pitfall 1], zero staging above un-swept stop cascades [Pitfall 2], zero unabsorbed CVD waterfalls [Pitfall 3], zero sub-ATR stops inside liquidity sweep zones [Pitfall 4], zero random-walk fades [Pitfall 5], zero high spread friction > 5.0 bps TradFi / > 25.0 bps Crypto [Pitfall 6], zero rollover spread traps [Pitfall 7], and zero correlated cluster double-bets [Pitfall 8]).
3. `Read: Data/Manditory/32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md` (35-feed row-by-row interrogation across all 4 strategic groups).
4. `Read & Track: Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md` (Authoritative 7-step On-Wakeup execution checklist and active cycle scorecard).

### 0.4 Canonical Spread & Blackout Gates"""

if sec0_target in content:
    content = content.replace(sec0_target, sec0_addition, 1)
    print("Added Section 0.4.1 to STANDARDIZED_TRADING_DECISION_CHAIN.md")
else:
    print("sec0_target not found")

# 2. Update Step 10 to add 10.1, 10.2, 10.3, 10.4
step10_target = """4. **Joint-Completion Lifecycle & Sentry**: Orders and ratchets are managed via `Terminal/joint_cycle_controller.py` and `Data/cycle_state.json`. A cycle is complete only when all 3 entities finish. Next cycle triggers strictly 20 minutes after completion (`T_finish + 20 min`), supervised by the 30-minute watchdog sentry (`0,30 * * * *`).

---

## SECTION 2.5:"""

step10_replacement = """4. **Joint-Completion Lifecycle & Sentry**: Orders and ratchets are managed via `Terminal/joint_cycle_controller.py` and `Data/cycle_state.json`. A cycle is complete only when all 3 entities finish. Next cycle triggers strictly 20 minutes after completion (`T_finish + 20 min`), supervised by the 30-minute watchdog sentry (`0,30 * * * *`).

---

### 10.1 Active Order Lifecycle & Position Health Interrogation Protocol
On EVERY cycle wakeup and in every response, the desk MUST systematically interrogate each live filled position and resting limit order with the core existential question:
> **"Should I let it run or cut it? Is it still a valid trade?"**

#### 10.2 Resting Maker Limit Orders Invalidation & Immediate Purge Rules
If ANY of the following 5 invalidation triggers occurs, the resting limit order MUST be cancelled immediately via `mt5.order_send(TRADE_ACTION_REMOVE)`:
1. **Defending Whale Wall Dissolution**: If the defending institutional resting wall (> 100K USD nominal, > 180s persistence) vanishes, gets pulled, cancels, or decays below $100K before price reaches the entry $\to$ **PURGE / CANCEL IMMEDIATELY** (Pitfall 1 defense).
2. **Adverse Liquidity Sweep Premature Penetration**: If price aggressively sweeps through the target entry level without filling our limit, or sweeps the level and initiates second-leg momentum $\to$ **PURGE / CANCEL IMMEDIATELY** (Pitfall 2 defense).
3. **CVD Orderflow Waterfall Against Setup**: If multi-timeframe CVD delta shifts aggressively in the direction opposing the limit order thesis (e.g., severe aggressive market sell delta cascading directly into a BUY_LIMIT) $\to$ **PURGE / CANCEL IMMEDIATELY** (Pitfall 3 defense).
4. **Rollover Spread Blackout Quarantine**: If the clock enters the 21:15–22:30 UTC interbank rollover window for Forex pairs and CFDs, cancel all resting limit orders $\to$ **PURGE / CANCEL IMMEDIATELY** (Pitfall 7 defense).
5. **Time-Decay Expiration**: If a resting limit order remains unfilled for > 24 bars (6 hours) without being tapped $\to$ **PURGE / CANCEL IMMEDIATELY** to free up contingent risk capacity.

#### 10.3 Live Filled Positions Real-Time Diagnostics, Early Cut & Dynamic Trailing
When a trade is filled and active on the broker book, enforce the following active management rules:
1. **Adverse Orderflow Breakdown (Cut Loss Early)**: If an active position moves adversely, CVD delta exhibits aggressive counter-absorption against our position, or auction value area (VAH/VAL) is violated $\to$ **CUT IMMEDIATELY AT MARKET** by taking a small, controlled loss (e.g. -0.20R to -0.40R) rather than passively waiting for the full bunker stop loss to be struck.
2. **Dynamic Profit Ratchet & Trailing Stop**:
   - **+0.75R to +0.80R Gain**: Move Stop Loss to Entry $\pm 0.10\text{R}$ / $0.15\text{R}$ (Early Breakeven Lock).
   - **+1.25R Gain**: Move Stop Loss to Entry $\pm 0.15\text{R}$ (Phase 0 Lock).
   - **+1.50R to +1.65R Gain**: Move Stop Loss to Entry $\pm 0.80\text{R}$ (Phase 1 Profit Lock).
   - **$\ge +2.00$R Gain**: Activate continuous 0.50 ATR trailing stop behind 15m micro-shelves (Phase 2).
3. **Dynamic Take Profit Extension Rule**: If strong institutional orderflow momentum, massive defending whale walls, and multi-horizon CVD delta confirm continuous expansion beyond $+2.5\text{R}$, dynamically extend the Take Profit target toward the next high-timeframe auction boundary or major liquidation cluster while locking in banked profits via trailing stop!

#### 10.4 Canonical Pre-Trade & Running Governance Links
Before executing any trade or order modification, the desk must verify compliance with:
- `Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md` (authoritative running checklist)
- `Data/Manditory/TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md` (10 lethal pitfalls)
- `Data/Manditory/32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md` (35-feed interrogation)
- `Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md` (canonical 10-step SOP)

---

## SECTION 2.5:"""

if step10_target in content:
    content = content.replace(step10_target, step10_replacement, 1)
    print("Added Section 10.1-10.4 to STANDARDIZED_TRADING_DECISION_CHAIN.md")
else:
    print("step10_target not found")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated STANDARDIZED_TRADING_DECISION_CHAIN.md successfully!")
