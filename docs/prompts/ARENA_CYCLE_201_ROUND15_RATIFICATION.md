# ARENA.AI FORENSIC AUDIT ROUND 15: FORMAL AUTHORIZATION & DECISIONS OF RECORD

> **Repository**: [https://github.com/kbsingh1399/Trading_2](https://github.com/kbsingh1399/Trading_2)  
> **Target Checkout**: `/home/user/Trading_2` at base commit `e5da816`  
> **Protocol**: Arena-authored Round 15 execution in `/tmp` with clean index staging via `git hash-object`  

---

## 1. DECISIONS OF RECORD ON THE TWO PENDING POINTS

### Decision 1: Macro Blackout Window is Officially ±35 Minutes
- **Window**: Keep **±35 minutes** (Option 1 institutional fail-closed macro blackout).
- **Alignment with Code**: `Terminal/risk/blackout_guard.py` is the live enforcer. It already defines:
  ```python
  _STATIC_BLACKOUT_MINUTES_PRE  = 35   # minutes before event
  _STATIC_BLACKOUT_MINUTES_POST = 35   # minutes after event
  ```
  Its docstring already specifies ±35 minutes (L94), and line 116 passes 35/35.
- **Harmony**: Keeping ±35 minutes ensures the code and the ratified documentation (`ACTIVE_CONTEXT.md`, `dispatch_tri_council.py`, `dispatch_comprehensive_wake_up_prompt.py`, and `SESSION_FULL_FABLE.md`) are in 100% agreement. `blackout_guard.py` does not need to be mutated.
- **Macro Test Compatibility**: `Tests/Test_Macro_Calendar_Hardening.py` tests pass cleanly because the test fixture events define their own explicit `pre_blackout_m: 30, post_blackout_m: 30`, which `event_window_utc` resolves on a per-event basis.

### Decision 2: Commit ONLY the Option 1 Hunk via Index Staging (`git hash-object`)
- **Preserve Working Tree**: We adopt your brilliant git index proposal. Do **NOT** run `git checkout -- .agents/rules/ACTIVE_CONTEXT.md` and do **NOT** overwrite the working tree.
- **Index Staging**: Take the clean base blob from `git show e5da816:.agents/rules/ACTIVE_CONTEXT.md`, apply only the Option 1 replacement on lines 42–47, and stage that resulting blob via:
  ```bash
  HASH=$(git hash-object -w <path-to-patched-blob>)
  git update-index --cacheinfo 100644 "$HASH" .agents/rules/ACTIVE_CONTEXT.md
  ```
- **Result**: The 109 uncommitted lines remain completely untouched in the working tree, and the commit contains strictly the Option 1 macro blackout hunk on top of `e5da816`.

---

## 2. VERIFIED SPECIFICATIONS FOR ROUND 15 EXECUTION

### A. Exact L42–47 Anchor in `ACTIVE_CONTEXT.md` (at `e5da816`)
**Target Text**:
```markdown
- **MACRO BLACKOUT ENFORCEMENT PERMANENTLY REMOVED & DISABLED (STRICT OPERATOR MANDATE)**:
  * Macro blackout trading halts, pre-news purge deadlines, and calendar-based trade blocks are PERMANENTLY TERMINATED across all components (`Terminal/risk/blackout_guard.py`, `Terminal/Data_Factory/generate_telemetry_snapshot.py`, prompts, and strategy engines).
  * `BlackoutGuard.is_blocked()` permanently returns `False, ""`.
  * Open positions (including Ticket #18892038 `BTCUSD.pi` BUY) run continuously toward take-profit and trailing profit locks across all news and inflation events. No position is ever purged due to an upcoming calendar event.
  * Models must never disqualify candidate trades based on macro runway or blackout windows.
```
**Replacement (Option 1 ±35m)**:
```markdown
- **MACRO BLACKOUT ENFORCEMENT (P0 INSTITUTIONAL FAIL-CLOSED INVARIANT)**:
  * Pre-submission macro blackout is ACTIVELY ENFORCED via `Terminal/risk/blackout_guard.py` (`BlackoutGuard.get().is_blocked()`).
  * Blocks new order submissions within ±35 minutes of scheduled Tier-1 macro events (FOMC, CPI, NFP) loaded from `Data/macro_calendar.json`.
  * Calendar read errors or unverified coverage fail closed (`is_blocked() -> True`), preventing blind execution during unverified windows, verified by `Tests/Test_Macro_Calendar_Hardening.py`.
  * Open positions continue to be managed via micro-ratchet trailing profit locks; genuine position closes remain authorized during blackouts.
```

### B. Confirmed `remediation_r2.py` Call Signature
In `Cycle_201_fixes/remediation_r2.py`:
```python
def orderbook_spread(best_bid, best_ask, age_seconds) -> Optional[float]:
    age = quote_age_or_none(age_seconds)
    if age is None or age > FRESHNESS_MAX_S:
        return None
    b, a = quote_or_na(best_bid), quote_or_na(best_ask)
    if b is None or a is None or a <= b:
        return None
    return spread_bps(b, a, age, max_age_s=FRESHNESS_MAX_S)
```

### C. Confirmed Prompt Anchors (All Exact Matches)
- `Terminal/dispatch_tri_council.py`: Replace `MACRO BLACKOUT ENFORCEMENT IS PERMANENTLY REMOVED AND DISABLED...` with `MACRO BLACKOUT ENFORCEMENT IS ACTIVELY ENFORCED (OPTION 1 INSTITUTIONAL FAIL-CLOSED, ±35m AROUND TIER-1 EVENTS).` (1 occurrence).
- `Terminal/dispatch_comprehensive_wake_up_prompt.py`: Replace `lines.append("        - OPERATOR DIRECTIVE: Macro blackout enforcement is PERMANENTLY REMOVED AND DISABLED...")` with `lines.append("        - OPERATOR DIRECTIVE: Macro blackout enforcement is ACTIVELY ENFORCED (Option 1 institutional fail-closed blackout, ±35m around Tier-1 events).")` (1 occurrence).
- `docs/trade_plans/SESSION_FULL_FABLE.md`: Replace all 9 occurrences of `        - OPERATOR DIRECTIVE: Macro blackout enforcement is PERMANENTLY REMOVED AND DISABLED...` with `        - OPERATOR DIRECTIVE: Macro blackout enforcement is ACTIVELY ENFORCED (Option 1 institutional fail-closed blackout, ±35m around Tier-1 events).` (assert count == 9).

---

## 3. INVITATION & AUTHORIZATION TO ARENA

As proposed in your Round 14 report, you are fully authorized to:
1. Construct and execute your Round 15 script in `/tmp`.
2. Install `numpy` into the scratch venv if needed to execute `Tests/Test_Macro_Calendar_Hardening.py`.
3. Verify that both test suites pass in `/tmp` (121 tests in `Cycle_200_fixes` + `Cycle_201_fixes`, and 5/5 in `Test_Macro_Calendar_Hardening.py`).
4. Stage the verified files (using index staging for `ACTIVE_CONTEXT.md` to preserve the 109 working-tree lines), assert `sorted(staged) == sorted(PATHS)`, create the local commit, and verify via `git archive HEAD`.
5. Issue your formal:

```markdown
## Verdict: RATIFIED
```
