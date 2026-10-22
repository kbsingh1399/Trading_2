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
    bal_str = "4,834.83"
    eq_str = "4,834.83"
    fm_str = "4,834.83"
    pos_str = "0 (100% Flat Cash, 0 positions, 0 pending orders)"
    cush_fl_str = "+59.83"
    cush_buf_str = "+39.83"
    dist_goal_str = "+665.17"
    hours_left_str = "38.0"
    # Auto-detect latest cycle ID
    import glob, re
    existing = glob.glob(str(ROOT / "docs" / "prompts" / "ARENA_CYCLE_*_REDTEAM_PROMPT.txt"))
    nums = [int(m.group(1)) for f in existing if (m := re.search(r"ARENA_CYCLE_(\d+)_REDTEAM", f))]
    cycle_num = max(nums) + 1 if nums else 247
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

    pending_orders = td.get("pending_orders", [])
    pending_count = len(pending_orders)
    prompt = prompt.replace("{PENDING_ORDERS}", f"{pending_count} pending limit orders")

    # Active Tickets & Pending Orders Table
    table_rows = ["| Slot | Cluster | Ticket | Symbol | Side | Volume | Entry | SL | TP | Risk USD | R0 |",
                  "|---|---|---|---|---|---|---|---|---|---|---|"]
    if pos_count > 0:
        for idx, p0 in enumerate(td.get("open_positions", [])):
            table_rows.append(f"| Filled {idx+1} | Open | #{p0.get('ticket')} | {p0.get('symbol')} | {p0.get('direction')} | {p0.get('volume')} lot | {p0.get('price_open')} | {p0.get('sl')} | {p0.get('tp')} | Sized | — |")
    if pending_count > 0:
        for idx, po in enumerate(pending_orders):
            side = po.get("direction", "LIMIT")
            sym = po.get("symbol", "")
            cluster = "Forex" if "EUR" in sym or "GBP" in sym or "USD" in sym else "Index" if "100" in sym or "500" in sym or "30" in sym else "Crypto"
            risk_usd = "$18.00" if "EUR" in sym else "$18.72" if "UK100" in sym else "$18.40"
            dist = "10.0 pips" if "EUR" in sym else "20.0 pts" if "UK100" in sym else "460 pts"
            table_rows.append(f"| Pending {idx+1} | {cluster} | #{po.get('ticket')} | {sym} | {side} | {po.get('volume')} lot | {po.get('price_open')} | {po.get('sl')} | {po.get('tp')} | {risk_usd} | {dist} |")
    if pos_count == 0 and pending_count == 0:
        table_rows.append("| — | Flat | — | — | — | — | — | — | — | $0.00 | — |")
        table_rows.append("*Book is 100% Cash. Zero active positions, zero pending orders.*")
    else:
        status_note = f"*Book State: {pos_count} filled positions, {pending_count} pending limit orders resting on broker book.*"
        table_rows.append(status_note)

    ticket_table = "\n".join(table_rows)
    prompt = prompt.replace("{TICKET_TABLE}", ticket_table)

    # Candidate Radar Table (Calibrated Multi-Asset Radar incorporating Operator Risk & Arena Feedback)
    candidate_table = (
        "| Candidate Setup | Direction | Target Entry | Stop Loss | Take Profit | Lots | Risk USD | Stressed Risk | Pre-Condition Checklist |\n"
        "|---|---|---|---|---|---|---|---|---|\n"
        "| DJ30.p Daily VAL Shelf | BUY_LIMIT | 52,455.00 | 52,360.00 | 52,650.00 | 0.02 lot | $19.00 | $24.00 | [ ] Pullback into Daily VAL 52,451.94, [ ] M15 volume exhaustion, [ ] TP front-runs VAH 52,673, [x] Spread 0.22 bps |\n"
        "| NAS100.p Volume Rebound | BUY_LIMIT | 29,245.00 | 29,150.00 | 29,480.00 | 0.02 lot | $19.00 | $24.00 | [ ] Pullback into Daily VAL 29,236.95, [ ] Resting bid support, [ ] TP front-runs VAH 29,505, [x] Spread 0.36 bps |\n"
        "| UK100.p Structural Short | SELL_LIMIT | 10,724.00 | 10,752.00 | 10,682.00 | 0.07 lot | $19.60 | $25.00 | [ ] Pullback to Daily VAH 10,716-10,724, [ ] SL safely beyond Weekly POC (10,742.87), [ ] TP front-runs VAL 10,679, [x] Spread 1.59 bps |\n"
        "| GER40.p Auction Balance | BUY_LIMIT | 25,320.00 | 25,230.00 | 25,480.00 | 0.02 lot | $18.00 | $23.00 | [ ] Retest of Daily VAL 25,308.18, [ ] Delta turn, [ ] TP front-runs VAH 25,491, [x] Spread 0.31 bps |\n"
        "| EURUSD.pi Value Retest | BUY_LIMIT | 1.11920 | 1.11820 | 1.12300 | 0.18 lot | $18.00 | $23.00 | [ ] Post-macro sweep into 1.11900 support, [ ] Tape reversal, [ ] TP front-runs Daily POC 1.12334, [x] Spread 0.09 bps |\n"
        "| XAUUSD.pi Demand Shelf | BUY_LIMIT | 4,058.50 | 4,050.50 | 4,072.00 | 0.02 lot | $16.00 | $22.00 | [ ] 4,058-4,060 bunker defense, [ ] Tick CVD deceleration, [ ] TP front-runs VAL, [x] Spread 0.20 bps |\n"
        "| BTCUSD.pi Whale Bunker | BUY_LIMIT | 81,640.00 | 81,180.00 | 82,440.00 | 0.04 lot | $18.40 | $25.00 | [ ] Sweep into 81,525-81,650 VAL shelf, [ ] CVD absorption flip, [ ] 7.53M wall holds, [x] Spread 1.83 bps |"
    )
    prompt = prompt.replace("{CANDIDATE_TABLE}", candidate_table)

    worst_case_eq = f"{eq - 27.00:.2f}"
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
    import argparse
    parser = argparse.ArgumentParser(description="Arena.ai Surgical Red-Team Dispatcher")
    parser.add_argument("--status", action="store_true", help="Check status without dispatching")
    args = parser.parse_args()

    if args.status:
        import json
        st_file = ROOT / "Data" / "arena_completion_status.json"
        if st_file.exists():
            print(st_file.read_text(encoding="utf-8"))
        else:
            print("No status file found.")
    else:
        asyncio.run(build_and_dispatch())
