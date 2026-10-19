# ARENA.AI FORENSIC AUDIT ROUND 16: DEFINITIVE RATIFICATION APPROVAL & CODE EMBED

> **Repository**: [https://github.com/kbsingh1399/Trading_2](https://github.com/kbsingh1399/Trading_2)  
> **Target Checkout**: `/home/user/Trading_2` at base commit `e5da816`  
> **Commit Protocol**: Staging 16 paths via index staging (`git hash-object`) with zero working-tree destruction  

---

## 1. FORMAL OPERATOR DECISIONS ON THE TWO ROUND 15 QUESTIONS

### Decision 1: Blackout Window is Confirmed at ±30 Minutes
- **Decision**: Keep **±30 minutes** (Option 1 institutional fail-closed macro blackout).
- **Rationale**: All 19 events in `Data/macro_calendar.json` carry `pre_blackout_m: 30, post_blackout_m: 30`, and `calendar_observation` calls `event_window_utc(event, 30, 30)`.
- **Text Alignment**: All documentation and prompt text must state **±30 minutes** (replacing legacy `PERMANENTLY REMOVED` with Option 1 ±30m).

### Decision 2: Implement Option 1 in `calendar_observation` (Terminal/Data_Factory/generate_telemetry_snapshot.py)
- **Decision**: **YES, proceed with the Option 1 implementation in `calendar_observation`**.
- **Implementation**: At lines 1039–1047 of `generate_telemetry_snapshot.py` (at `e5da816`), replace the hardcoded `blackout_active: False` with active evaluation:
  ```python
  if windows:
      ws, we, release, purge, event = windows[0]
      is_active = bool(ws <= now < we)
      runway = max(0.0, round((ws - now) / 3600.0, 2)) if now < ws else (0.0 if is_active else None)
      result.update(
          event=event["name"],
          event_release_utc=text_stamp(release),
          event_source=event["source"],
          hard_blackout_window_utc=[text_stamp(ws), text_stamp(we)],
          purge_deadline_utc=text_stamp(purge) if purge else None,
          runway_hours_to_blackout=runway,
          blackout_active=is_active,
          blackout_enforcement="FAIL_CLOSED_OPTION_1" if is_active else "ARMED"
      )
  return result
  ```
  And on error (lines 1045–1047):
  ```python
  except (OSError, ValueError, KeyError, TypeError, OverflowError) as exc:
      return {"calendar_status": "FAIL_CLOSED_ERROR", "blackout_active": True, "blackout_enforcement": "FAIL_CLOSED_OPTION_1",
              "event": None, "event_release_utc": None, "hard_blackout_window_utc": None,
              "runway_hours_to_blackout": None, "error": str(exc)}
  ```
- **Result**: `test_telemetry_calendar_uses_the_same_half_hour_window` passes 100%, achieving the required **5 of 5 passing tests** in `Tests/Test_Macro_Calendar_Hardening.py`.

---

## 2. EXACT ANCHORS FOR ROUND 16 EXECUTION

### Anchor A: `Terminal/Data_Factory/generate_telemetry_snapshot.py` (Lines 1039–1048 at `e5da816`)
**Target Text**:
```python
        if windows:
            ws, we, release, purge, event = windows[0]
            result.update(event=event["name"], event_release_utc=text_stamp(release), event_source=event["source"],
                          hard_blackout_window_utc=[text_stamp(ws), text_stamp(we)], purge_deadline_utc=None,
                          runway_hours_to_blackout=None, blackout_active=False, blackout_enforcement="DISABLED_BY_OPERATOR")
        return result
    except (OSError, ValueError, KeyError, TypeError, OverflowError) as exc:
        return {"calendar_status": "COVERAGE_AVAILABLE", "blackout_active": False, "blackout_enforcement": "DISABLED_BY_OPERATOR",
                "event": None, "event_release_utc": None, "hard_blackout_window_utc": None,
                "runway_hours_to_blackout": None, "error": str(exc)}
```
**Replacement**:
```python
        if windows:
            ws, we, release, purge, event = windows[0]
            is_active = bool(ws <= now < we)
            runway = max(0.0, round((ws - now) / 3600.0, 2)) if now < ws else (0.0 if is_active else None)
            result.update(event=event["name"], event_release_utc=text_stamp(release), event_source=event["source"],
                          hard_blackout_window_utc=[text_stamp(ws), text_stamp(we)],
                          purge_deadline_utc=text_stamp(purge) if purge else None,
                          runway_hours_to_blackout=runway, blackout_active=is_active,
                          blackout_enforcement="FAIL_CLOSED_OPTION_1" if is_active else "ARMED")
        return result
    except (OSError, ValueError, KeyError, TypeError, OverflowError) as exc:
        return {"calendar_status": "FAIL_CLOSED_ERROR", "blackout_active": True, "blackout_enforcement": "FAIL_CLOSED_OPTION_1",
                "event": None, "event_release_utc": None, "hard_blackout_window_utc": None,
                "runway_hours_to_blackout": None, "error": str(exc)}
```

### Anchor B: `ACTIVE_CONTEXT.md` (via index staging blob)
**Target Text at `e5da816`**:
```markdown
- **MACRO BLACKOUT ENFORCEMENT PERMANENTLY REMOVED & DISABLED (STRICT OPERATOR MANDATE)**:
  * Macro blackout trading halts, pre-news purge deadlines, and calendar-based trade blocks are PERMANENTLY TERMINATED across all components (`Terminal/risk/blackout_guard.py`, `Terminal/Data_Factory/generate_telemetry_snapshot.py`, prompts, and strategy engines).
  * `BlackoutGuard.is_blocked()` permanently returns `False, ""`.
  * Open positions (including Ticket #18892038 `BTCUSD.pi` BUY) run continuously toward take-profit and trailing profit locks across all news and inflation events. No position is ever purged due to an upcoming calendar event.
  * Models must never disqualify candidate trades based on macro runway or blackout windows.
```
**Replacement (Option 1 ±30m)**:
```markdown
- **MACRO BLACKOUT ENFORCEMENT (P0 INSTITUTIONAL FAIL-CLOSED INVARIANT)**:
  * Pre-submission macro blackout is ACTIVELY ENFORCED via `Terminal/risk/blackout_guard.py` (`BlackoutGuard.get().is_blocked()`).
  * Blocks new order submissions within ±30 minutes of scheduled Tier-1 macro events (FOMC, CPI, NFP) loaded from `Data/macro_calendar.json`.
  * Calendar read errors or unverified coverage fail closed (`is_blocked() -> True`), preventing blind execution during unverified windows, verified by `Tests/Test_Macro_Calendar_Hardening.py`.
  * Open positions continue to be managed via micro-ratchet trailing profit locks; genuine position closes remain authorized during blackouts.
```

### Anchor C: Prompt Scripts & Fable
- `Terminal/dispatch_tri_council.py`: Replace `MACRO BLACKOUT ENFORCEMENT IS PERMANENTLY REMOVED AND DISABLED...` with `MACRO BLACKOUT ENFORCEMENT IS ACTIVELY ENFORCED (OPTION 1 INSTITUTIONAL FAIL-CLOSED, ±30m AROUND TIER-1 EVENTS).` (1 occurrence).
- `Terminal/dispatch_comprehensive_wake_up_prompt.py`: Replace `lines.append("        - OPERATOR DIRECTIVE: Macro blackout enforcement is PERMANENTLY REMOVED AND DISABLED...")` with `lines.append("        - OPERATOR DIRECTIVE: Macro blackout enforcement is ACTIVELY ENFORCED (Option 1 institutional fail-closed blackout, ±30m around Tier-1 events).")` (1 occurrence).
- `docs/trade_plans/SESSION_FULL_FABLE.md`: Replace all 9 occurrences of `        - OPERATOR DIRECTIVE: Macro blackout enforcement is PERMANENTLY REMOVED AND DISABLED...` with `        - OPERATOR DIRECTIVE: Macro blackout enforcement is ACTIVELY ENFORCED (Option 1 institutional fail-closed blackout, ±30m around Tier-1 events).` (assert count == 9).

### Anchor D: `remediation_r2.py`
Use the verified call signature:
```python
return spread_bps(b, a, age, max_age_s=FRESHNESS_MAX_S)
```

---

## 3. FULL AUTHORIZATION TO EXECUTE & RATIFY

You are fully authorized to execute your proposed Round 16 workflow:
1. Build the commit in `/tmp` with the Option 1 telemetry implementation in `calendar_observation`.
2. Run both test suites in `/tmp` (asserting **121 passed** in `Cycle_200_fixes` + `Cycle_201_fixes`, and **5 passed** in `Tests/Test_Macro_Calendar_Hardening.py`).
3. Stage all 16 paths using the index staging approach for `ACTIVE_CONTEXT.md` (leaving the 109 uncommitted working tree lines intact).
4. Assert `sorted(staged) == sorted(PATHS)`.
5. Create the local commit and verify directly from `git archive HEAD`.
6. Issue your formal:

```markdown
## Verdict: RATIFIED
```
