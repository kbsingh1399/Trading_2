"""
Terminal/dispatch_cycle_202_prompt.py
Dispatches docs/prompts/ARENA_CYCLE_202_CANDIDATE_SEARCH.md to active Arena.ai tab via CDP port 9222.
"""
import asyncio
import json
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.arena_bridge import post_prompt_to_arena_single

PROMPT_FILE = ROOT / "docs" / "prompts" / "ARENA_CYCLE_202_CANDIDATE_SEARCH.md"


async def main():
    if not PROMPT_FILE.exists():
        print(f"[-] Prompt file not found: {PROMPT_FILE}")
        return False

    prompt_body = PROMPT_FILE.read_text(encoding="utf-8").strip()
    print(f"[*] Prepared prompt ({len(prompt_body)} characters)...")

    try:
        tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read().decode())
    except Exception as e:
        print(f"[-] Could not connect to Edge CDP: {e}")
        return False

    arena_tab = None
    for t in tabs:
        u = t.get("url", "")
        if "arena.ai" in u:
            arena_tab = t
            break

    if not arena_tab:
        print("[-] Arena.ai tab not found on port 9222!")
        return False

    ws_url = arena_tab.get("webSocketDebuggerUrl")
    print(f"[+] Found Arena tab: {arena_tab.get('title')} (ID: {arena_tab.get('id')})")
    print(f"[+] URL: {arena_tab.get('url')}")

    success = await post_prompt_to_arena_single(ws_url, prompt_body, tab_label="Arena-Cycle202")
    print(f"[+] Dispatch result: {success}")
    return success


if __name__ == "__main__":
    asyncio.run(main())
