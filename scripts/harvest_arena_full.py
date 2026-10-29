import asyncio
import json
import urllib.request
import websockets
import pathlib

ROOT = pathlib.Path(r"C:\Users\SIGMA\Documents\Trading_2")
OUTPUT_FILE = ROOT / "docs" / "trade_plans" / "ARENA_LATEST_RAW.md"

async def harvest_full_arena():
    tabs = json.loads(urllib.request.urlopen("http://localhost:9222/json").read().decode())
    arena_tab = None
    for t in tabs:
        if "arena.ai" in t.get("url", ""):
            arena_tab = t
            break
    if not arena_tab:
        print("No arena.ai tab found")
        return
        
    ws_url = arena_tab["webSocketDebuggerUrl"]
    async with websockets.connect(ws_url, max_size=40*1024*1024) as ws:
        # Script to find the last assistant message container
        eval_script = """
        (() => {
            // Find all message containers
            // Arena typically uses role or specific message components
            const allElements = Array.from(document.querySelectorAll('*'));
            
            // Look for the user prompt that triggered this:
            // "study all files for 156 assets" or "Cycle_009"
            
            // Let's get the entire conversation scroll container
            const scroller = document.querySelector('[class*="scroll"], main, [role="main"]');
            
            // Or get all assistant message divs
            // In Arena, assistant responses are often in divs containing markdown prose
            const proseList = Array.from(document.querySelectorAll('.prose, [class*="prose"]'));
            
            let fullAssistantText = "";
            if (proseList.length > 0) {
                // If there are multiple prose blocks in the last turn, concatenate them
                // Or find the parent message container of the last prose
                let parent = proseList[proseList.length - 1];
                while (parent && parent.parentElement && !parent.getAttribute('data-message-author-role') && parent.tagName !== 'MAIN' && parent.tagName !== 'BODY') {
                    if (parent.parentElement.querySelectorAll('.prose').length > 1) {
                        parent = parent.parentElement;
                        break;
                    }
                    parent = parent.parentElement;
                }
                fullAssistantText = parent ? parent.innerText : proseList[proseList.length - 1].innerText;
            }
            
            return {
                proseCount: proseList.length,
                fullAssistantTextLen: fullAssistantText.length,
                fullAssistantText: fullAssistantText
            };
        })()
        """
        msg = {
            "id": 1,
            "method": "Runtime.evaluate",
            "params": {
                "expression": eval_script,
                "returnByValue": True
            }
        }
        await ws.send(json.dumps(msg))
        resp = await ws.recv()
        data = json.loads(resp)
        res = data.get("result", {}).get("result", {}).get("value", {})
        print(f"Prose count: {res.get('proseCount')}, Text len: {res.get('fullAssistantTextLen')}")
        text = res.get("fullAssistantText", "")
        if text:
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Full text written to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(harvest_full_arena())
