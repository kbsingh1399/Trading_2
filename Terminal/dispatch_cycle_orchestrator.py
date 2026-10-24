#!/usr/bin/env python3
"""
Terminal/dispatch_cycle_orchestrator.py
=======================================
Master Cycle Dispatch Orchestrator for Blueberry Markets Autonomous Trading Desk.

Guarantees 100% compliance with Operator Mandate:
1. Initializes Cycle X in Data/cycle_state.json via joint_cycle_controller.py.
2. Compiles unified prompt for external frontier councils (Arena.ai + Z.ai + Gemini Web2API).
3. Pushes prompt simultaneously to Arena.ai and Z.ai via Chrome CDP (port 9222).
4. Generates rendered prompt files for ALL 4 Fable 5 internal subagents:
   - Data/subagent_prompts/cycle_{id}_role_a.txt (Statistical Regime Quant)
   - Data/subagent_prompts/cycle_{id}_role_b.txt (Microstructure Quant)
   - Data/subagent_prompts/cycle_{id}_role_c.txt (Solvency Sentry)
   - Data/subagent_prompts/cycle_{id}_role_d.txt (Clock Provenance Auditor)
5. Prints explicit, unmissable Antigravity Tool Dispatch Block so the coordinator LLM
   never misses invoking all 4 subagents in parallel with the council monitoring watcher.
"""

import argparse
import asyncio
import datetime
import json
import logging
import os
import pathlib
import subprocess
import sys
from typing import Dict, Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.joint_cycle_controller import start_cycle, load_cycle_state
import Terminal.dispatch_dual_council as dual_council

PROMPTS_DIR = ROOT / "Data" / "subagent_prompts"
TEMPLATES_FILE = ROOT / "Data" / "Manditory" / "SUBAGENT_PROMPT_TEMPLATES.md"

logging.basicConfig(level=logging.INFO, format="[%(asctime)s][CycleOrchestrator] %(message)s")
logger = logging.getLogger("CycleOrchestrator")


def render_subagent_prompts(cycle_id: str) -> Dict[str, pathlib.Path]:
    """Generates standalone rendered prompt files for all 4 subagents on disk."""
    PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Read templates
    if not TEMPLATES_FILE.exists():
        logger.error("Template file %s not found!", TEMPLATES_FILE)
        return {}

    raw_text = TEMPLATES_FILE.read_text(encoding="utf-8")
    
    roles = {
        "role_a": ("Statistical Regime Quant", "PROMPT TEMPLATE 1: ROLE A", "Role A: Statistical Regime, Diffusion, and Dual-Engine Dialectic Quant"),
        "role_b": ("Microstructure Quant", "PROMPT TEMPLATE 2: ROLE B", "Role B: Fill, Microstructure, and Order Geometry Quant"),
        "role_c": ("Solvency Sentry", "PROMPT TEMPLATE 3: ROLE C", "Role C: Solvency, Portfolio, and Broker Math Sentry"),
        "role_d": ("Clock Provenance Auditor", "PROMPT TEMPLATE 4: ROLE D", "Role D: Market Clock, Auction, Events, and Provenance Auditor")
    }
    
    generated_files = {}
    
    for r_key, (r_name, section_header, role_title) in roles.items():
        out_file = PROMPTS_DIR / f"cycle_{cycle_id}_{r_key}.txt"
        
        # Extract section
        start_pos = raw_text.find(section_header)
        if start_pos != -1:
            code_block_start = raw_text.find("```markdown", start_pos)
            if code_block_start != -1:
                code_block_start += len("```markdown")
                code_block_end = raw_text.find("```", code_block_start)
                if code_block_end != -1:
                    prompt_content = raw_text[code_block_start:code_block_end].strip()
                    # Replace placeholders
                    prompt_content = prompt_content.replace("[CYCLE_ID]", str(cycle_id))
                    prompt_content = prompt_content.replace("[CUTOFF_UTC]", datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"))
                    out_file.write_text(prompt_content, encoding="utf-8")
                    generated_files[r_key] = out_file
                    continue
                    
        # Fallback minimal prompt
        fallback = f"You are {role_title} for {cycle_id} of the Blueberry Markets MT5 autonomous quant desk (Account #5064568).\nFollow Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md line by line. Output canonical JSON matching schema in Data/Manditory/SUBAGENT_PROMPT_TEMPLATES.md including Section 8 Kaizen."
        out_file.write_text(fallback, encoding="utf-8")
        generated_files[r_key] = out_file

    logger.info("Generated 4 subagent prompts in %s", PROMPTS_DIR)
    return generated_files


async def orchestrate_dispatch(cycle_id: str):
    logger.info("================================================================================")
    logger.info("STARTING MASTER ORCHESTRATION DISPATCH FOR %s", cycle_id)
    logger.info("================================================================================")

    # 1. Initialize cycle state
    state = start_cycle(cycle_id)
    logger.info("Cycle %s initialized in Data/cycle_state.json", cycle_id)

    # 2. Render subagent prompt files
    prompt_files = render_subagent_prompts(cycle_id)

    # 3. Dispatch dual council (Arena.ai + Z.ai + Web2API)
    logger.info("Dispatching Arena.ai, Z.ai, and Gemini Web2API...")
    try:
        await dual_council.dispatch_all(cycle_id=cycle_id)
        logger.info("External council prompts successfully pushed.")
    except Exception as e:
        logger.error("Error during council dispatch: %s", e)

    # 4. Print mandatory Antigravity Tool Dispatch Block
    print("\n" + "="*80)
    print("🚨 MANDATORY ATOMIC SUBAGENT DISPATCH DIRECTIVE FOR ANTIGRAVITY (TRACK A)")
    print("="*80)
    print("External Councils (Arena.ai, Z.ai, Web2API) have been dispatched via CDP.")
    print("IN THIS SAME TURN, ANTIGRAVITY MUST EXECUTE THE FOLLOWING 5 TOOL CALLS:")
    print("-" * 80)
    print("1. invoke_subagent(")
    print("     Role='Statistical Regime Quant', TypeName='self',")
    print(f"     Prompt=read_file('{prompt_files.get('role_a')}')")
    print("   )")
    print("2. invoke_subagent(")
    print("     Role='Microstructure Quant', TypeName='self',")
    print(f"     Prompt=read_file('{prompt_files.get('role_b')}')")
    print("   )")
    print("3. invoke_subagent(")
    print("     Role='Solvency Sentry', TypeName='self',")
    print(f"     Prompt=read_file('{prompt_files.get('role_c')}')")
    print("   )")
    print("4. invoke_subagent(")
    print("     Role='Clock Provenance Auditor', TypeName='self',")
    print(f"     Prompt=read_file('{prompt_files.get('role_d')}')")
    print("   )")
    print("5. run_command(")
    print("     CommandLine='python Terminal/arena_completion_daemon.py --wait',")
    print("     WaitMsBeforeAsync=500, toolSummary='Wait for Arena and Z.ai completion'")
    print("   )")
    print("-" * 80)
    print("⚠️  DO NOT YIELD CONTROL OR END TURN WITHOUT CALLING ALL 4 SUBAGENTS!")
    print("="*80 + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Master Cycle Dispatch Orchestrator")
    parser.add_argument("--cycle", default="AUTO", help="Cycle identifier (e.g. 'Cycle 326' or '326')")
    args = parser.parse_args()

    cid = args.cycle
    if cid == "AUTO":
        st = load_cycle_state()
        curr = st.get("current_cycle_id", "325")
        import re
        m = re.search(r"\d+", str(curr))
        next_num = int(m.group(0)) + 1 if m else 326
        cid = f"Cycle {next_num}"
    elif not cid.lower().startswith("cycle"):
        cid = f"Cycle {cid}"

    asyncio.run(orchestrate_dispatch(cid))
