"""
Terminal/dispatch_master_prompt.py
Dispatches UNIVERSAL_AUTONOMOUS_TRADING_PROMPT.md directly to Arena.ai tab via CDP.
"""
import asyncio
import json
import pathlib
import sys
import urllib.request
import websockets

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.arena_bridge import post_prompt_to_arena_single

PROMPT_FILE = ROOT / "docs" / "prompts" / "UNIVERSAL_AUTONOMOUS_TRADING_PROMPT.md"

def get_prompt_body() -> str:
    raw = PROMPT_FILE.read_text(encoding="utf-8")
    if "```markdown" in raw:
        return raw.split("```markdown")[1].split("```")[0].strip()
    return raw.strip()

async def main():
    prompt_body = get_prompt_body()
    print(f"[*] Prepared prompt ({len(prompt_body)} characters)...")
    
    tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read().decode())
    arena_tab = None
    for t in tabs:
        if "arena.ai" in t.get("url", ""):
            arena_tab = t
            break
            
    if not arena_tab:
        print("[-] Arena.ai tab not found on port 9222!")
        return False
        
    ws_url = arena_tab["webSocketDebuggerUrl"]
    print(f"[+] Found Arena tab: {arena_tab.get('title')}")
    print(f"[+] URL: {arena_tab.get('url')}")
    
    success = await post_prompt_to_arena_single(ws_url, prompt_body, tab_label="Arena-Master")
    print(f"[+] Dispatch result: {success}")
    return success

if __name__ == "__main__":
    asyncio.run(main())
