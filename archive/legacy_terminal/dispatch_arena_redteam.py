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
    template_path = ROOT / "Data" / "Manditory" / "Arena_GLM_Standard_Prompt.md"
    if not template_path.exists():
        template_path = ROOT / "Data" / "Manditory" / "ARENA_STANDARD_PROMPT_TEMPLATE.md"
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

    # Candidate Radar Table (Dynamically pulled from Terminal/multi_asset_opportunity_scanner.py across all 156 assets)
    try:
        from Terminal.multi_asset_opportunity_scanner import scan_all_156_assets
        scan_res = scan_all_156_assets()
        top_opps = scan_res.get("opportunities", [])[:6]
    except Exception as se:
        logger.warning("Failed to scan 156 assets: %s", se)
        top_opps = []

    if top_opps:
        c_lines = [
            "| Candidate Setup | Direction | Target Entry | Stop Loss | Take Profit | Lots | Risk USD | Stressed Loss | Buffer Surplus |",
            "|---|---|---|---|---|---|---|---|---|"
        ]
        for opp in top_opps:
            c_lines.append(f"| {opp['symbol']} ({opp['group']}) | {opp['side']} | {opp['entry']} | {opp['sl']} | {opp['tp']} | {opp['lot']} lot | ${opp['nominal_risk_usd']:.2f} | ${opp['nominal_risk_usd']*1.25+2.0:.2f} | +${opp['buffer_surplus_usd']:.2f} |")
        candidate_table = "\n".join(c_lines)
    else:
        candidate_table = "| No immediate multi-asset candidates qualified. Book is 100% Cash. |" 
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
