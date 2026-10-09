"""Script to dispatch the exhaustive Round 4 Thinking Chain & Codebase Audit prompt
to Claude Opus 5.5 in Microsoft Copilot Studio via Chrome DevTools Protocol.
"""
import asyncio
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.copilot_studio_bridge import (
    get_copilot_studio_ws_url,
    post_prompt_to_copilot_studio,
    check_copilot_studio_response,
)


def build_round4_prompt() -> str:
    lines = []
    lines.append("=" * 80)
    lines.append("EXHAUSTIVE ROUND 4 CODEBASE & THINKING CHAIN AUDIT | CHIEF QUANTITATIVE REVIEW")
    lines.append("ENGINE: CLAUDE OPUS 5.5 (MICROSOFT COPILOT STUDIO - SECOND BRAIN)")
    lines.append("CANONICAL GITHUB REPOSITORY: https://github.com/kbsingh1399/Trading_2 (Branch: main)")
    lines.append("COMMIT HEAD: ee3ade9ae4c018e23d466b5bb2dacf212565e736")
    lines.append("=" * 80)
    lines.append("")
    lines.append("[SECTION 0: MANDATORY PRE-FLIGHT CONTEXT REVIEW & CONTINUITY ORIENTATION]")
    lines.append("You are Claude Opus 5.5, operating as our Elite Chief Quantitative Strategist and institutional Second Brain.")
    lines.append("Before analyzing code or providing rulings, you MUST review our authentic repository state and trajectory directly via GitHub API:")
    lines.append("1. Canonical Repository Root: https://github.com/kbsingh1399/Trading_2")
    lines.append("2. Session Historical Memory: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md")
    lines.append("   - Review the complete session narrative to understand our trajectory, operator directives, historical setbacks, and avoided traps. Never evaluate in a vacuum!")
    lines.append("3. Active Operational Context: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md")
    lines.append("   - Review live account state (Equity: 4,896.55 USD | Balance: 4,896.55 USD | Hard Floor: 4,775.00 USD | Buffer: 4,795.00 USD | Cushion: +121.55 USD).")
    lines.append("4. Master Agent Enforcement Rules: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/AGENTS.md")
    lines.append("5. Thinking Chain Protocol V2.0 Hardened: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md")
    lines.append("6. Decision Gates V3 Implementation: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/decision_gates_v3.py")
    lines.append("7. MT5 Execution Bridge: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/MT5_Execution_Bridge.py")
    lines.append("8. Decision Gates V3 Pytest Suite: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Tests/Test_Decision_Gates_v3.py")
    lines.append("9. Forensic 360 Verifier: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/chain_verification_360.py")
    lines.append("10. Live Telemetry Snapshot: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/live_telemetry_snapshot.json")
    lines.append("11. Round 3 Audit Archive: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/reviews/ROUND3_OPUS55_AUDIT_REPORT.md")
    lines.append("")
    lines.append("[SECTION 1: STATUS OF ROUND 3 DEFECT REMEDIATIONS (COMMITTED IN ee3ade9a)]")
    lines.append("We have actively ingested and resolved all findings from your Round 3 Audit:")
    lines.append("1. Dynamic Broker DST Calibration (MT5_Execution_Bridge.py): Replaced hardcoded 10,800s offset with dynamic _utc_offset_seconds('BTCUSD.pi') snapped to 30-min intervals. Survives Blueberry Markets GMT+3 to GMT+2 shift on Nov 1.")
    lines.append("2. Model 1 Tape Requirement Fail-Closed (decision_gates_v3.py): Removed allow_price_only_variant from model1_checklist. Mean reversion strictly requires tape/CVD absorption or fails closed.")
    lines.append("3. Mandatory First Obstacle & Win-Rate Lower Bound (decision_gates_v3.py): B6 first_obstacle and _net_ev p_win_lower_bound are now mandatory; missing values fail closed.")
    lines.append("4. Raw Spread Zero-Median Invalidation (decision_gates_v3.py): Patched spread cancellation to spread_bps > max(1.0, 2.5 * spread_median_bps), preventing instant cancellation on raw 0.0-median pairs.")
    lines.append("5. Diffusion TTL Staging Anchor (decision_gates_v3.py): diffusion_ttl_minutes now computes once at order staging time with a 15-minute minimum safeguard. Price nearing limit cannot shrink TTL to 0.")
    lines.append("6. Model 1 Sweep Z Check (decision_gates_v3.py): Uses z_sweep = ctx.get('sweep_z', z) so rebounded entry does not trigger a Catch-22 rejection.")
    lines.append("7. In-Range Stand-Aside Conflict Repealed (AGENTS.md & ACTIVE_CONTEXT.md): Repealed legacy in-range entitlement; established that if classify_regime() returns UNDEFINED, the desk MUST stand aside unconditionally across both engines.")
    lines.append("8. Test Suite & Verifier Verified: Tests/Test_Decision_Gates_v3.py created and passing (8/8). Full suite: 413 passed, 1 skipped, 0 failed. chain_verification_360.py: PASS (+121.55 USD cushion above 4,775.00 USD floor).")
    lines.append("")
    lines.append("[SECTION 2: MANDATORY EXHAUSTIVE REVIEW & THINKING CHAIN CRITIQUE]")
    lines.append("Please conduct an exhaustive, rigorous quantitative review addressing:")
    lines.append("1. Verification of Commit ee3ade9a: Audit the 8 patches above directly from the GitHub links. Confirm whether all P0/P1 code defects are resolved.")
    lines.append("2. Thinking Chain & Pre-Trade Decision Points:")
    lines.append("   - What exact points and checks must the desk verify before making a trading decision for Trend Following (Model 2)?")
    lines.append("   - What exact points and checks must the desk verify before making a trading decision for Extreme Mean Reversion (Model 1)?")
    lines.append("   - Provide a concise, bulleted pre-flight checklist that our execution loop and subagents can run deterministically on every 15-minute candle.")
    lines.append("3. Live Wiring Roadmap for decision_gates_v3.py into Terminal/Omni_Trader.py:")
    lines.append("   - Detail the exact step-by-step procedure to wire classify_regime, model1_checklist, model2_checklist, pre_send_gate, and resting_order_invalidation into AI15mMT5Trader.")
    lines.append("   - Outline the transition from Shadow Mode (logging verdicts alongside existing trades) to Enforcement Mode (hard admission gatekeeper).")
    lines.append("4. Full Text of /app/created/ROUND3_REPO_AND_THINKING_CHAIN_AUDIT.md:")
    lines.append("   - In your previous response, you noted files were created in /app/created/ROUND3_REPO_AND_THINKING_CHAIN_AUDIT.md. Please print the complete, unabridged text of that report directly in your reply.")
    lines.append("")
    lines.append("Be as thorough, mathematically rigorous, and exhaustive as you want. Deliver your complete quantitative ruling.")
    return "\n".join(lines)


async def main():
    prompt = build_round4_prompt()
    print(f"Built Round 4 prompt ({len(prompt)} chars).")
    ws_url = get_copilot_studio_ws_url()
    if not ws_url:
        print("ERROR: Copilot Studio tab not found on port 9222", file=sys.stderr)
        return False
    print(f"Posting prompt to Copilot Studio...")
    success = await post_prompt_to_copilot_studio(prompt, ws_url)
    print(f"Post result: {success}")
    return success


if __name__ == "__main__":
    asyncio.run(main())
