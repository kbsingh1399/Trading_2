#!/usr/bin/env python3
"""
Terminal/dispatch_cycle_206_redteam.py
======================================
Surgical Red-Team Dispatcher for Arena.ai (Cycle 206).
"""

import asyncio
import sys
import pathlib
import logging

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.arena_bridge import post_prompt_to_arena

logging.basicConfig(level=logging.INFO, format="[%(asctime)s][ArenaCycle206] %(message)s")
logger = logging.getLogger("ArenaCycle206")

PROMPT = """# 🎯 SURGICAL RED-TEAM AUDIT — CYCLE 206 (2026-10-21 16:35 UTC)

> **FORENSIC AUDITOR MANDATE**:
> You are the Forensic Red-Team Auditor for the Blueberry Markets funded account (#5064568).
> Your mandate is strictly quantitative verification: audit candidate levels, stop vulnerability, and wall persistence.

---

### 1. LIVE PORTFOLIO & SOLVENCY STATE
* **Account Balance**: 4,840.39 USD | **Live Equity**: 4,853.19 USD (Session High-Water Mark)
* **Inviolate Hard Floor**: 4,775.00 USD (Live Cushion: +78.19 USD / +1.61%)
* **Operating Defense Buffer**: 4,795.00 USD (Live Cushion: +58.19 USD / +1.20%)
* **Remaining Runway to 5,500.00 USD Goal**: +646.81 USD (~55.5 hours remaining to Oct 23, 23:59 UTC)
* **Active Running Position (1 of 4 slots filled)**:
  - **Ticket #19164106 (`EURUSD.pi`)**: 0.08 lot BUY @ 1.12150. Current Market: 1.12310 (+16.0 pips / +1.60 R0).
  - **Ratchet Locked**: SL moved from 1.12050 to **1.12165** (Phase 0 Risk Cut locked).
  - **Downside Risk**: **0.00 USD** (Guaranteed +1.20 USD net profit even on full retracement).
  - **Next Sentinel**: Phase 1 (+1.65 R0 = 1.12315) locks SL at 1.12230 (+0.80 R0, +$6.40 USD profit). TP @ 1.12420.
* **Available Execution Capacity**: Exactly **3 slots completely open** for orthogonal candidates (Crypto, Metals, Indices).
* **Authorized Cash Risk**: $15.00 to $25.00 USD per trade, with stressed equity strictly >= 4,795.00 USD.

---

### 2. THREE PROSPECTIVE CANDIDATE SHELVES FOR SLOTS 2 & 3
The desk is considering staging passive limit orders on confirmed pullbacks:

1. **Candidate A (Crypto — `BTCUSD.pi`)**:
   - Proposed Posture: BUY_LIMIT on pullback to 84,250.00 USD.
   - Microstructure Backing: Supported by resting L2/L3 bid walls ($849K @ 84,591, $706K @ 84,585, $573K @ 84,584).
   - Proposed SL: 83,850.00 USD (400 pts, $8.00 risk @ 0.02 lot).
   - Proposed TP: 85,200.00 USD (+950 pts, +$19.00 reward, 2.38 R0).

2. **Candidate B (Metals — `XAUUSD.pi` / Gold)**:
   - Proposed Posture: BUY_LIMIT on pullback to 4,128.50 USD.
   - Microstructure Backing: Supported by resting bid walls ($235K @ 4,131.60, $156K @ 4,130.70, $134K @ 4,130.00).
   - Proposed SL: 4,118.50 USD (10.0 pts, $10.00 risk @ 0.01 lot).
   - Proposed TP: 4,151.00 USD (+22.5 pts, +$22.50 reward, 2.25 R0).

3. **Candidate C (Indices — `SP500.p`)**:
   - Proposed Posture: BUY_LIMIT on pullback to 7,743.00 USD.
   - Microstructure Backing: Supported by resting bid walls ($722K @ 7,745.40, $366K @ 7,745.70).
   - Proposed SL: 7,725.00 USD (18.0 pts, $9.00 risk @ 0.01 lot / 0.50 per pt).
   - Proposed TP: 7,785.00 USD (+42.0 pts, +$21.00 reward, 2.33 R0).

---

### 3. THE 4 RED-TEAM VERIFICATION QUESTIONS
Please deliver direct, concise answers without boilerplate disclaimers:

1. **Q1 (Stop Loss Sweep Vulnerability)**:
   - For Candidates A (BTC @ 83,850), B (Gold @ 4,118.50), and C (SP500 @ 7,725.00), does ANY proposed SL sit inside or immediately in front of an un-swept retail stop cluster or liquidation band? What is the exact structural ATR buffer?
2. **Q2 (Take Profit Obstruction Audit)**:
   - Are there massive resting ask/sell walls between the proposed entry and TP for any of these 3 candidates? What is the first major wall in each candidate's path?
3. **Q3 (Whale Wall Persistence)**:
   - Inspect `17_Orderbook` and `10_Whale_Orders`: Are the supporting bid walls for BTC, Gold, or SP500 showing verified persistence (>= 180s) or are they spoofed/fleeting?
4. **Q4 (Tactical Ratification & Sizing)**:
   - Which candidate (if any) should Antigravity stage as a passive limit order right now into Slot 2 or Slot 3? If a candidate needs level adjustments, state the exact compliant Entry, SL, and TP. Or should the desk stand aside on new orders and ride EURUSD?
"""

async def main():
    p_out = ROOT / "docs" / "prompts" / "ARENA_CYCLE_206_REDTEAM_PROMPT.txt"
    p_out.write_text(PROMPT, encoding="utf-8")
    logger.info("Saved Cycle 206 surgical prompt (%d chars) to %s", len(PROMPT), p_out)

    logger.info("Injecting prompt into Arena on Chrome CDP port 9222...")
    success = await post_prompt_to_arena(PROMPT, target="arena-1")
    if success:
        logger.info("SUCCESS: Cycle 206 surgical prompt injected into Arena!")
    else:
        logger.warning("CDP post_prompt_to_arena returned False.")
    return success

if __name__ == "__main__":
    asyncio.run(main())
