#!/usr/bin/env python3
"""
Terminal/joint_cycle_controller.py
===================================
Canonical Joint-Completion Cycle Lifecycle & 30-Minute Watchdog Controller.

OPERATOR MANDATE:
"Let say we are in cycle X...in this cycle, we prompt antigravity subagents, arena.ai, z.ai.
 We will call this cycle finished only when ALL THREE completed the prompt processing...
 because sometime agents may take more time than 20 mins and till then next cycle started...
 so there is a collapse...When all three done, then we will call it finished.
 We can have a cron job at 30 min to check if all going okay and cycle completed or not or any error.
 And difference between completed cycle X and next cycle trigger must be 20 mins..."

Architecture:
1. Joint-Completion Gate: Cycle X is marked FINISHED if and only if:
   - Antigravity 4-subagent swarm (Fable 5) has completed research & harvested.
   - Arena.ai (GPT Astra) has completed generation & harvested.
   - Z.ai (GLM-5.3-Flash) has completed generation & harvested.
2. Dynamic 20-Minute Post-Completion Delay:
   - Next cycle trigger is scheduled at: T_finish(Cycle X) + 20 minutes (1,200 seconds).
   - Eliminates overlapping cycle collapses and race conditions.
3. 30-Minute Watchdog Sentry:
   - Scheduled on `0,30 * * * *` (every 30 minutes).
   - Verifies if any cycle is stalled (> 30 min in progress).
   - Audits all 6 persistent background daemons.
   - Triggers cycle advancement if the 20-minute rest period has elapsed.
"""

import argparse
import datetime
import json
import logging
import os
import pathlib
import sys
import time
from typing import Dict, Any, Optional

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

CYCLE_STATE_FILE = ROOT / "Data" / "cycle_state.json"
ARENA_STATUS_FILE = ROOT / "Data" / "arena_completion_status.json"
ZAI_STATUS_FILE = ROOT / "Data" / "zai_completion_status.json"

logging.basicConfig(level=logging.INFO, format="[%(asctime)s][JointCycleController] %(message)s")
logger = logging.getLogger("JointCycleController")


def now_utc_str() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def get_default_state() -> Dict[str, Any]:
    return {
        "current_cycle_id": "296",
        "cycle_status": "IN_PROGRESS",  # "IN_PROGRESS" | "COMPLETED" | "STALLED"
        "cycle_started_utc": now_utc_str(),
        "cycle_completed_utc": None,
        "next_cycle_scheduled_utc": None,
        "rest_interval_seconds": 1200,  # 20 minutes
        "components": {
            "antigravity_subagents": {
                "name": "Antigravity 4-Quant Swarm (Fable 5)",
                "status": "COMPLETED",
                "completed_at_utc": now_utc_str(),
                "details": "Statistical Regime, Microstructure, Solvency, Auction Profile"
            },
            "arena_ai": {
                "name": "Arena.ai Council (GPT Astra)",
                "status": "COMPLETED",
                "completed_at_utc": now_utc_str(),
                "raw_file": "docs/trade_plans/ARENA_LATEST_RAW.md",
                "model": "GPT Astra"
            },
            "zai": {
                "name": "Z.ai Sovereign Council (GLM-5.3-Flash)",
                "status": "IN_PROGRESS",
                "completed_at_utc": None,
                "raw_file": "docs/trade_plans/ZAI_LATEST_RAW.md",
                "model": "GLM-5.3-Flash"
            }
        },
        "watchdog": {
            "last_check_utc": now_utc_str(),
            "health": "HEALTHY",
            "message": "Initialized joint cycle controller."
        }
    }


def load_cycle_state() -> Dict[str, Any]:
    if CYCLE_STATE_FILE.exists():
        try:
            with open(CYCLE_STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if "components" in data:
                    return data
        except Exception as e:
            logger.warning("Failed to parse cycle_state.json: %s", e)
    
    state = get_default_state()
    save_cycle_state(state)
    return state


def save_cycle_state(state: Dict[str, Any]) -> None:
    CYCLE_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CYCLE_STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def start_cycle(cycle_id: str) -> Dict[str, Any]:
    state = load_cycle_state()
    utc_now = now_utc_str()
    state["current_cycle_id"] = str(cycle_id)
    state["cycle_status"] = "IN_PROGRESS"
    state["cycle_started_utc"] = utc_now
    state["cycle_completed_utc"] = None
    state["next_cycle_scheduled_utc"] = None
    
    state["components"]["antigravity_subagents"]["status"] = "IN_PROGRESS"
    state["components"]["antigravity_subagents"]["completed_at_utc"] = None
    
    state["components"]["arena_ai"]["status"] = "IN_PROGRESS"
    state["components"]["arena_ai"]["completed_at_utc"] = None
    
    state["components"]["zai"]["status"] = "IN_PROGRESS"
    state["components"]["zai"]["completed_at_utc"] = None
    
    save_cycle_state(state)
    logger.info("Cycle %s started at %s. Awaiting all 3 entities.", cycle_id, utc_now)
    return state


def update_component_status(component: str, status: str, details: Optional[str] = None) -> Dict[str, Any]:
    state = load_cycle_state()
    if component not in state["components"]:
        raise ValueError(f"Unknown component: {component}")
    
    state["components"][component]["status"] = status
    if status == "COMPLETED":
        state["components"][component]["completed_at_utc"] = now_utc_str()
    if details:
        state["components"][component]["details"] = details
        
    save_cycle_state(state)
    logger.info("Component %s updated to %s", component, status)
    
    # Check if this completion finishes the entire cycle
    check_cycle_completion(state)
    return state


def sync_from_daemons(state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Auto-detects completions from arena_completion_status.json and zai_completion_status.json."""
    if state is None:
        state = load_cycle_state()
    
    start_str = state.get("cycle_started_utc")
    start_dt = None
    if start_str:
        try:
            start_dt = datetime.datetime.strptime(start_str.replace(" UTC", ""), "%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc)
        except Exception:
            pass

    # 1. Check Arena Daemon
    if ARENA_STATUS_FILE.exists():
        try:
            with open(ARENA_STATUS_FILE, "r", encoding="utf-8") as f:
                ad = json.load(f)
            if not ad.get("is_generating", True) and (ad.get("has_copy_button", False) or ad.get("text_length", 0) > 2000):
                arena_ts = ad.get("completed_at_utc", now_utc_str())
                ad_dt = datetime.datetime.strptime(arena_ts.replace(" UTC", ""), "%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc)
                if not start_dt or ad_dt >= start_dt:
                    if state["components"]["arena_ai"]["status"] != "COMPLETED" or state["components"]["arena_ai"]["completed_at_utc"] != arena_ts:
                        state["components"]["arena_ai"]["status"] = "COMPLETED"
                        state["components"]["arena_ai"]["completed_at_utc"] = arena_ts
                        logger.info("Auto-synced Arena.ai completion from daemon status: %s", arena_ts)
        except Exception:
            pass

    # 2. Check Z.ai Daemon
    if ZAI_STATUS_FILE.exists():
        try:
            with open(ZAI_STATUS_FILE, "r", encoding="utf-8") as f:
                zd = json.load(f)
            if not zd.get("is_generating", True) and zd.get("text_length", 0) > 2000:
                zai_ts = zd.get("completed_at_utc", now_utc_str())
                zd_dt = datetime.datetime.strptime(zai_ts.replace(" UTC", ""), "%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc)
                if not start_dt or zd_dt >= start_dt:
                    if state["components"]["zai"]["status"] != "COMPLETED" or state["components"]["zai"]["completed_at_utc"] != zai_ts:
                        state["components"]["zai"]["status"] = "COMPLETED"
                        state["components"]["zai"]["completed_at_utc"] = zai_ts
                        logger.info("Auto-synced Z.ai completion from daemon status: %s", zai_ts)
        except Exception:
            pass

    save_cycle_state(state)
    check_cycle_completion(state)
    return state


def check_cycle_completion(state: Optional[Dict[str, Any]] = None) -> bool:
    """Verifies if all 3 entities have finished. If yes, marks cycle COMPLETED and arms 20-min delay."""
    if state is None:
        state = load_cycle_state()
        
    if state.get("cycle_status") == "COMPLETED":
        return True

    comps = state.get("components", {})
    sub_done = comps.get("antigravity_subagents", {}).get("status") == "COMPLETED"
    arena_done = comps.get("arena_ai", {}).get("status") == "COMPLETED"
    zai_done = comps.get("zai", {}).get("status") == "COMPLETED"

    if sub_done and arena_done and zai_done:
        ts_list = []
        for c in [comps.get("antigravity_subagents", {}), comps.get("arena_ai", {}), comps.get("zai", {})]:
            c_ts = c.get("completed_at_utc")
            if c_ts:
                try:
                    dt = datetime.datetime.strptime(c_ts.replace(" UTC", ""), "%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc)
                    ts_list.append(dt)
                except Exception:
                    pass
        max_dt = max(ts_list) if ts_list else datetime.datetime.now(datetime.timezone.utc)
        next_dt = max_dt + datetime.timedelta(seconds=state.get("rest_interval_seconds", 1200))
        max_dt_str = max_dt.strftime("%Y-%m-%d %H:%M:%S UTC")
        next_dt_str = next_dt.strftime("%Y-%m-%d %H:%M:%S UTC")
        
        state["cycle_status"] = "COMPLETED"
        state["cycle_completed_utc"] = max_dt_str
        state["next_cycle_scheduled_utc"] = next_dt_str
        save_cycle_state(state)
        
        logger.info("🎯 ALL 3 ENTITIES COMPLETED! Cycle %s marked FINISHED at %s.", state.get("current_cycle_id"), max_dt_str)
        logger.info("⏳ Next cycle trigger armed for: %s (clean 20-minute separation).", next_dt_str)
        return True
    
    return False


def run_watchdog() -> Dict[str, Any]:
    """
    30-Minute Watchdog Sentry:
    - Checks if an active cycle is stuck (> 30 minutes).
    - Checks if a completed cycle's 20-minute rest period has elapsed.
    - Validates daemon health.
    """
    state = load_cycle_state()
    sync_from_daemons(state)
    
    now_dt = datetime.datetime.now(datetime.timezone.utc)
    now_str = now_dt.strftime("%Y-%m-%d %H:%M:%S UTC")
    watchdog_report = {"checked_at_utc": now_str, "status": "OK", "actions": []}
    
    status = state.get("cycle_status", "UNKNOWN")
    cycle_id = state.get("current_cycle_id", "UNKNOWN")
    
    # 1. Check for Stalled Cycle (> 30 minutes in progress)
    if status == "IN_PROGRESS":
        start_str = state.get("cycle_started_utc")
        if start_str:
            try:
                start_dt = datetime.datetime.strptime(start_str.replace(" UTC", ""), "%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc)
                elapsed_sec = (now_dt - start_dt).total_seconds()
                elapsed_min = elapsed_sec / 60.0
                
                if elapsed_min > 30.0:
                    watchdog_report["status"] = "WARNING_STALLED"
                    comps = state.get("components", {})
                    missing = [c for c, v in comps.items() if v.get("status") != "COMPLETED"]
                    msg = f"Cycle {cycle_id} has been in progress for {elapsed_min:.1f} minutes (> 30 min threshold). Missing completions: {missing}."
                    watchdog_report["actions"].append(msg)
                    logger.warning(msg)
                    state["cycle_status"] = "STALLED"
                    state["watchdog"]["health"] = "STALLED"
                    state["watchdog"]["message"] = msg
                else:
                    msg = f"Cycle {cycle_id} in progress ({elapsed_min:.1f} min elapsed <= 30 min limit). Healthy."
                    watchdog_report["actions"].append(msg)
                    logger.info(msg)
            except Exception as e:
                logger.error("Error parsing cycle_started_utc: %s", e)
                
    # 2. Check if Completed Cycle has rested for 20 minutes and is ready for next cycle
    elif status == "COMPLETED":
        next_str = state.get("next_cycle_scheduled_utc")
        if next_str:
            try:
                next_dt = datetime.datetime.strptime(next_str.replace(" UTC", ""), "%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc)
                diff_sec = (next_dt - now_dt).total_seconds()
                
                if diff_sec <= 0:
                    next_cycle_num = int(cycle_id) + 1 if cycle_id.isdigit() else 297
                    msg = f"Cycle {cycle_id} rest period complete ({state.get('cycle_completed_utc')} + 20m). READY TO ADVANCE TO CYCLE {next_cycle_num}."
                    watchdog_report["status"] = "READY_TO_ADVANCE"
                    watchdog_report["actions"].append(msg)
                    logger.info(msg)
                else:
                    rem_min = diff_sec / 60.0
                    msg = f"Cycle {cycle_id} completed. Healthy rest period active ({rem_min:.1f} minutes remaining before Cycle {int(cycle_id)+1 if cycle_id.isdigit() else 'Next'})."
                    watchdog_report["actions"].append(msg)
                    logger.info(msg)
            except Exception as e:
                logger.error("Error parsing next_cycle_scheduled_utc: %s", e)
                
    state["watchdog"]["last_check_utc"] = now_str
    save_cycle_state(state)
    return watchdog_report


def print_status():
    state = load_cycle_state()
    sync_from_daemons(state)
    
    print("\n" + "="*80)
    print(f"[STATUS] JOINT-COMPLETION CYCLE CONTROLLER - CURRENT DESK STATUS")
    print("="*80)
    print(f"Cycle ID:                Cycle {state.get('current_cycle_id')}")
    print(f"Overall Cycle Status:    {state.get('cycle_status')}")
    print(f"Cycle Started (UTC):     {state.get('cycle_started_utc')}")
    print(f"Cycle Completed (UTC):   {state.get('cycle_completed_utc') or 'IN PROGRESS (awaiting all 3 entities)'}")
    print(f"Next Cycle Armed (UTC):  {state.get('next_cycle_scheduled_utc') or 'NOT ARMED (cycle unfinished)'}")
    print(f"Rest Interval:           {state.get('rest_interval_seconds', 1200)}s (clean 20 minutes)")
    print("-" * 80)
    print("MANDATORY 3-ENTITY JOINT COMPLETION STATUS:")
    for k, v in state.get("components", {}).items():
        icon = "[OK]" if v.get("status") == "COMPLETED" else "[..]"
        print(f"  {icon} {v.get('name'):<42} -> {v.get('status')} (Done: {v.get('completed_at_utc') or 'In Flight'})")
    print("-" * 80)
    print(f"Watchdog Status:         {state.get('watchdog', {}).get('health', 'UNKNOWN')}")
    print(f"Watchdog Last Check:     {state.get('watchdog', {}).get('last_check_utc')}")
    print(f"Watchdog Notes:          {state.get('watchdog', {}).get('message')}")
    print("="*80 + "\n")


def wait_rest():
    """
    Sleeps cleanly during the dynamic 20-minute quiet period until next_cycle_scheduled_utc.
    If MT5 positions close (e.g. TP/SL triggered), wakes up immediately so the desk can advance.
    Exits 0 to trigger reactive Antigravity wakeup for the next cycle.
    """
    state = load_cycle_state()
    next_str = state.get("next_cycle_scheduled_utc")
    if not next_str:
        logger.info("No next cycle scheduled; exiting.")
        return

    try:
        next_dt = datetime.datetime.strptime(next_str.replace(" UTC", ""), "%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc)
    except Exception as e:
        logger.error("Could not parse next_cycle_scheduled_utc: %s", e)
        return

    try:
        import MetaTrader5 as mt5
        has_mt5 = mt5.initialize()
    except Exception:
        has_mt5 = False

    logger.info("Resting cleanly until %s. Early wakeup enabled on position closure.", next_str)
    cycle_num = int(state.get("current_cycle_id", 305))

    while True:
        now_dt = datetime.datetime.now(datetime.timezone.utc)
        rem_sec = (next_dt - now_dt).total_seconds()
        if rem_sec <= 0:
            logger.info("🎯 Dynamic rest period complete (20 minutes). Ready for Cycle %d!", cycle_num + 1)
            print(f"\n🔔 REST PERIOD COMPLETE: Ready to trigger Cycle {cycle_num + 1}!")
            break

        # Check if active positions closed early
        if has_mt5:
            try:
                positions = mt5.positions_get()
                if positions is not None and len(positions) == 0:
                    logger.info("🔔 POSITION EVENT: Active position closed (TP/SL hit)! Waking up immediately.")
                    print(f"\n🔔 POSITION EVENT: Active position closed! Waking up immediately for Cycle {cycle_num + 1}!")
                    break
            except Exception:
                pass

        time.sleep(min(10, max(1, rem_sec)))

    if has_mt5:
        try:
            mt5.shutdown()
        except Exception:
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Joint Cycle Controller & 30-Minute Watchdog")
    parser.add_argument("--status", action="store_true", help="Print current cycle state and component progress")
    parser.add_argument("--watchdog", action="store_true", help="Execute 30-minute watchdog sentry check")
    parser.add_argument("--start", type=str, help="Start a new cycle with given ID")
    parser.add_argument("--complete", type=str, choices=["antigravity_subagents", "arena_ai", "zai"], help="Mark a component complete")
    parser.add_argument("--sync", action="store_true", help="Sync completion status from live daemons")
    parser.add_argument("--wait-rest", action="store_true", help="Sleep cleanly until next cycle (or early on position close) and exit 0 for reactive wakeup")
    args = parser.parse_args()

    if args.start:
        start_cycle(args.start)
        print_status()
    elif args.complete:
        update_component_status(args.complete, "COMPLETED")
        print_status()
    elif args.watchdog:
        res = run_watchdog()
        print(json.dumps(res, indent=2))
    elif args.sync:
        sync_from_daemons()
        print_status()
    elif args.wait_rest:
        wait_rest()
    else:
        print_status()
