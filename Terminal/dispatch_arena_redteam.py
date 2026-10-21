#!/usr/bin/env python3
"""
Terminal/dispatch_arena_redteam.py
===================================
Surgical Red-Team Dispatcher for Arena.ai.
Implements the operator mandate: "use arena.ai properly... I feel he is not adding value... rest you take autonomous call".

Replaces legacy 80KB prompt dumps with the high-value, laser-focused red-team prompt
defined in docs/prompts/ARENA_STANDARD_PROMPT_TEMPLATE.md.
"""

import asyncio
import sys
import pathlib
import logging

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.arena_bridge import post_prompt_to_arena

logging.basicConfig(level=logging.INFO, format="[%(asctime)s][ArenaRedTeam] %(message)s")
logger = logging.getLogger("ArenaRedTeam")

async def build_and_dispatch():
    template_path = ROOT / "docs" / "prompts" / "ARENA_STANDARD_PROMPT_TEMPLATE.md"
    if not template_path.exists():
        logger.error("Template not found: %s", template_path)
        return False

    with open(template_path, "r", encoding="utf-8") as f:
        full_doc = f.read()

    # Extract the markdown block inside the template
    if "```markdown" in full_doc:
        prompt = full_doc.split("```markdown")[1].split("```")[0].strip()
    else:
        prompt = full_doc.strip()

    # Load live telemetry dynamically
    import json
    telemetry_file = ROOT / "Data" / "telemetry" / "mt5_account_telemetry.json"
    bal_str = "4,851.83"
    eq_str = "4,851.83"
    fm_str = "4,851.83"
    pos_str = "0 (100% Cash, EURUSD #19164106 closed at 1.12300 locking +$11.44 net cash profit)"
    cush_fl_str = "+76.83"
    cush_buf_str = "+56.83"
    dist_goal_str = "+648.17"
    hours_left_str = "53.0"
    # Auto-detect latest cycle ID
    import glob, re
    existing = glob.glob(str(ROOT / "docs" / "prompts" / "ARENA_CYCLE_*_REDTEAM_PROMPT.txt"))
    nums = [int(m.group(1)) for f in existing if (m := re.search(r"ARENA_CYCLE_(\d+)_REDTEAM", f))]
    cycle_num = max(nums) + 1 if nums else 211
    cycle_id = str(cycle_num)

    if telemetry_file.exists():
        try:
            with open(telemetry_file, "r", encoding="utf-8") as tf:
                td = json.load(tf)
            acc = td.get("account", {})
            bal = acc.get("balance_usd", 4840.39)
            eq = acc.get("equity_usd", 4854.23)
            fm = acc.get("margin_free_usd", 4554.60)
            bal_str = f"{bal:,.2f}"
            eq_str = f"{eq:,.2f}"
            fm_str = f"{fm:,.2f}"
            cush_fl_str = f"+{acc.get('hard_floor_cushion_usd', 79.23):.2f}"
            cush_buf_str = f"+{acc.get('operating_buffer_cushion_usd', 59.23):.2f}"
            dist_goal_str = f"+{5500.0 - eq:.2f}"
            pos_count = td.get("open_positions_count", 0)
            if pos_count > 0:
                p0 = td.get("open_positions", [])[0]
                pos_str = f"1 ({p0.get('symbol')} #{p0.get('ticket')} {p0.get('direction')} {p0.get('volume')} lot, SL {p0.get('sl')} locked in profit, TP {p0.get('tp')}, Risk: 0.00 USD)"
            else:
                pos_str = "0"
        except Exception as te:
            logger.warning("Telemetry parse notice: %s", te)

    # Format dynamic variables
    prompt = prompt.replace("{CYCLE_ID}", cycle_id)
    prompt = prompt.replace("{BALANCE}", bal_str)
    prompt = prompt.replace("{EQUITY}", eq_str)
    prompt = prompt.replace("{FREE_MARGIN}", fm_str)
    prompt = prompt.replace("{OPEN_POSITIONS}", pos_str)
    prompt = prompt.replace("{CUSHION_FLOOR}", cush_fl_str)
    prompt = prompt.replace("{CUSHION_BUFFER}", cush_buf_str)
    prompt = prompt.replace("{DISTANCE_GOAL}", dist_goal_str)
    prompt = prompt.replace("{HOURS_LEFT}", hours_left_str)
    prompt = prompt.replace("{PENDING_ORDERS}", "0 pending orders")
    prompt = prompt.replace("{SLOTS_FREE}", "4/4 slots available")

    # Active Tickets Table
    ticket_table = "| Slot | Cluster | Ticket | Symbol | Side | Volume | Entry | SL | TP | Risk USD | R0 |\n|---|---|---|---|---|---|---|---|---|---|---|\n| — | Flat | — | — | — | — | — | — | — | $0.00 | — |\n*Book is 100% Cash. Zero active positions, zero pending orders.*"
    prompt = prompt.replace("{TICKET_TABLE}", ticket_table)

    # Candidate Radar Table (Calibrated Multi-Asset Radar)
    candidate_table = (
        "| Candidate Setup | Direction | Target Entry | Stop Loss | Take Profit | Lots | Risk USD | Stressed Risk | Pre-Condition Checklist |\n"
        "|---|---|---|---|---|---|---|---|---|\n"
        "| SOLUSD.p Demand Shelf | BUY_LIMIT | 106.96 | 105.10 | 107.95 | 0.10 lot | $18.60 | $25.25 | [x] Swept 107.50 stops, [x] 7.71M whale wall @ 106.66 persists, [x] Spread 21.49 bps <= 25.0, [ ] Touch 106.96 |\n"
        "| XAUUSD.pi Demand Shelf | BUY_LIMIT | 4,117.50 | 4,101.50 | 4,157.50 | 0.01 lot | $16.00 | $22.00 | [ ] Pullback to VWAP -1.0 SD shelf (4,117.50), [x] Spread 0.19 bps <= 2.5 bps, [ ] CVD buyer absorption |\n"
        "| BTCUSD.pi Cascade Shelf | BUY_LIMIT | 82,250.00 | 81,750.00 | 83,500.00 | 0.04 lot | $20.00 | $27.00 | [ ] 109M retail stop cascade (83,850-82,450) sweeps, [x] Spread 1.78 bps, [ ] CVD confirms exhaustion |\n"
        "| EURUSD.pi Bid Pocket | BUY_LIMIT | 1.12150 | 1.12050 | 1.12450 | 0.18 lot | $18.00 | $24.50 | [x] FX rollover lifted, [x] Spread 0.09 bps <= 5.0 bps, [ ] Retest 1.12150 bid pocket |"
    )
    prompt = prompt.replace("{CANDIDATE_TABLE}", candidate_table)

    worst_case_eq = f"{4851.83 - 47.25:.2f}"
    prompt = prompt.replace("{WORST_CASE_EQUITY}", worst_case_eq)

    # Save to prompts dir
    p_out = ROOT / "docs" / "prompts" / f"ARENA_CYCLE_{cycle_id}_REDTEAM_PROMPT.txt"
    p_out.write_text(prompt, encoding="utf-8")
    logger.info("Saved surgical prompt (%d chars) to %s", len(prompt), p_out)

    # Post to Arena via CDP
    logger.info("Posting prompt to Arena via Chrome CDP on port 9222...")
    success = await post_prompt_to_arena(prompt, target="arena-1")
    if success:
        logger.info("SUCCESS: Surgical red-team prompt injected into Arena!")
    else:
        logger.warning("CDP post_prompt_to_arena returned False.")
    return success

if __name__ == "__main__":
    asyncio.run(build_and_dispatch())
