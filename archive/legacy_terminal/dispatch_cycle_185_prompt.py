#!/usr/bin/env python3
"""
Terminal/dispatch_cycle_185_prompt.py
======================================
Dispatches docs/prompts/ARENA_CYCLE_185_DIALECTIC_RATIFICATION.md
directly into the active Arena.ai tab via CDP on port 9222.
"""
import asyncio
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.arena_bridge import (
    get_arena_tab_ws_url,
    post_prompt_to_arena_single,
    dismiss_arena_popup,
)

PROMPT_FILE = ROOT / "docs" / "prompts" / "ARENA_CYCLE_185_DIALECTIC_RATIFICATION.md"


async def main():
    if not PROMPT_FILE.exists():
        print(f"Error: {PROMPT_FILE} does not exist", file=sys.stderr)
        return 1

    prompt_text = PROMPT_FILE.read_text(encoding="utf-8")
    print(f"Loaded prompt from {PROMPT_FILE.name} ({len(prompt_text)} chars)")

    ws_url = await get_arena_tab_ws_url("primary")
    if not ws_url:
        print("Error: No active Arena tab found on CDP port 9222", file=sys.stderr)
        return 1

    print(f"Found Arena tab: {ws_url}")
    await dismiss_arena_popup("all")
    await asyncio.sleep(0.5)

    ok = await post_prompt_to_arena_single(ws_url, prompt_text, tab_label="Arena Primary")
    if ok:
        print("✅ Cycle 185 Prompt successfully dispatched to Arena.ai!")
        return 0
    else:
        print("❌ Failed to dispatch prompt to Arena.ai", file=sys.stderr)
        return 1


if __name__ == "__main__":
    rc = asyncio.run(main())
    sys.exit(rc)
