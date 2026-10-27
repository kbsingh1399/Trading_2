#!/usr/bin/env python3
"""
Terminal/harvest_tri_council.py
================================
Extracts entire Chrome session chat for all 3 council tabs (Argon, Astra, Fable),
and slices the conversation from the current cycle marker onwards.
"""

import argparse
import asyncio
import json
import pathlib
import re
import sys
import urllib.request
import websockets

try:
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)
except Exception:
    pass

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.dispatch_comprehensive_wake_up_prompt import _load_cycle_num

CDP_HTTP_URL = "http://127.0.0.1:9222"


async def harvest_tab_full(ws_url: str, is_gemini: bool = False) -> str:
    """Extracts all text across all turns in the tab session."""
    async with websockets.connect(ws_url, max_size=50 * 1024 * 1024, open_timeout=5) as ws:
        if is_gemini:
            js = """(() => {
                const queries = Array.from(document.querySelectorAll('user-query, .user-query-container'));
                const responses = Array.from(document.querySelectorAll('model-response, message-content, .message-content'));
                // Interleave or concatenate all messages
                const allTurnElements = Array.from(document.querySelectorAll('user-query, model-response, .conversation-turn'));
                if (allTurnElements.length > 0) {
                    return allTurnElements.map(e => (e.innerText || '').trim()).filter(Boolean).join('\\n\\n==================== TURN BOUNDARY ====================\\n\\n');
                }
                const msgs = Array.from(document.querySelectorAll('.message-content, .model-response-text, [data-test-id="response-container"], message-content, user-query'));
                return msgs.map(e => (e.innerText || '').trim()).filter(Boolean).join('\\n\\n==================== TURN BOUNDARY ====================\\n\\n');
            })()"""
        else:
            js = """(() => {
                const allProses = Array.from(document.querySelectorAll('.prose'));
                return allProses.map(pr => (pr.innerText || '').trim()).filter(Boolean).join('\\n\\n==================== MESSAGE BOUNDARY ====================\\n\\n');
            })()"""

        call_id = 101
        await ws.send(json.dumps({"id": call_id, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))

        for _ in range(40):
            try:
                msg = json.loads(await asyncio.wait_for(ws.recv(), timeout=3.0))
                if msg.get("id") == call_id:
                    return msg.get("result", {}).get("result", {}).get("value", "")
            except asyncio.TimeoutError:
                pass
        return ""


def slice_cycle(full_text: str, cycle: int) -> str:
    """Finds the start of current cycle prompt and extracts from there onwards."""
    if not full_text:
        return ""
    pattern = rf"(?:TRADING DESK COUNCIL:\s*)?CYCLE\s+{cycle}\b"
    matches = list(re.finditer(pattern, full_text, flags=re.IGNORECASE))
    if matches:
        start_idx = matches[0].start()
        return full_text[start_idx:].strip()
    return full_text.strip()


async def harvest_all(cycle: int = None):
    if cycle is None:
        cycle = _load_cycle_num()

    print(f"=======================================================")
    print(f"📥 HARVESTING ALL 3 COUNCIL SESSIONS FOR CYCLE {cycle}")
    print(f"=======================================================")

    try:
        pages = json.loads(urllib.request.urlopen(f"{CDP_HTTP_URL}/json", timeout=5).read().decode())
    except Exception as e:
        print(f"Error querying Chrome CDP: {e}", file=sys.stderr)
        return

    pages = [p for p in pages if p.get("type") == "page"]

    # 1. Harvest Gemini Argon
    gemini_tab = next((p for p in pages if "gemini.google.com" in p.get("url", "")), None)
    if gemini_tab:
        print(f"Harvesting Gemini Argon ({gemini_tab.get('id')})...")
        full_argon = await harvest_tab_full(gemini_tab["webSocketDebuggerUrl"], is_gemini=True)
        if full_argon:
            (ROOT / "docs" / "trade_plans" / "SESSION_FULL_ARGON.md").write_text(full_argon, encoding="utf-8")
            print(f"[Argon] Saved full session ({len(full_argon)} chars) -> docs/trade_plans/SESSION_FULL_ARGON.md")
            argon_cycle = slice_cycle(full_argon, cycle)
            (ROOT / "docs" / "trade_plans" / "ARGON_LATEST_RAW.md").write_text(argon_cycle, encoding="utf-8")
            print(f"[Argon] Saved Cycle {cycle} extract ({len(argon_cycle)} chars) -> docs/trade_plans/ARGON_LATEST_RAW.md")

    # 2. Harvest Arena Tabs (Astra & Fable)
    for p in pages:
        url = p.get("url", "")
        if "arena.ai" in url:
            is_fable = ("01a13a13" in url or "af999588" in url or "01a13b4a" in url or "e2edd108" in url or "01a13bea" in url)
            name = "FABLE" if is_fable else "ASTRA"
            print(f"Harvesting Arena {name} ({url})...")
            full_arena = await harvest_tab_full(p["webSocketDebuggerUrl"], is_gemini=False)
            if full_arena:
                (ROOT / "docs" / "trade_plans" / f"SESSION_FULL_{name}.md").write_text(full_arena, encoding="utf-8")
                print(f"[{name}] Saved full session ({len(full_arena)} chars) -> docs/trade_plans/SESSION_FULL_{name}.md")
                arena_cycle = slice_cycle(full_arena, cycle)
                out_name = "ARENA_FABLE_LATEST_RAW.md" if is_fable else "ARENA_LATEST_RAW.md"
                (ROOT / "docs" / "trade_plans" / out_name).write_text(arena_cycle, encoding="utf-8")
                print(f"[{name}] Saved Cycle {cycle} extract ({len(arena_cycle)} chars) -> docs/trade_plans/{out_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cycle", type=int, default=None)
    args = parser.parse_args()
    asyncio.run(harvest_all(args.cycle))
