"""
Terminal/harvest_quad_council.py
Harvests outputs from all 4 frontier agents:
  1. Arena Tab 1 (GPT Astra)
  2. Arena Tab 2 (Claude Fable Orchestrator)
  3. Copilot Studio Tab 1 (Claude Opus 5.5)
  4. Copilot Studio Tab 2 (GPT Astra)
Saves raw markdown artifacts and returns a structured synthesis.
"""
from __future__ import annotations
import asyncio
import json
import pathlib
import sys
import time
import urllib.request
import websockets

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

CDP_HTTP_URL = "http://127.0.0.1:9222"
TRADE_PLANS_DIR = ROOT / "docs" / "trade_plans"
TRADE_PLANS_DIR.mkdir(parents=True, exist_ok=True)

async def check_arena_tab(name: str, ws_url: str) -> dict:
    js_code = """
    (() => {
      const stopBtn = document.querySelector('button[aria-label="Stop generating"], button:has(svg.lucide-square)');
      const isGenerating = Boolean(stopBtn);
      const proseElements = Array.from(document.querySelectorAll('.prose')).filter(el => !el.classList.contains('tiptap'));
      const lastText = proseElements.length > 0 ? proseElements[proseElements.length - 1].innerText : '';
      const hasCopy = Boolean(document.querySelector('button[aria-label="Copy"]'));
      return {
        isGenerating,
        textLen: lastText.length,
        hasCopy,
        lastText
      };
    })()
    """
    try:
        async with websockets.connect(ws_url, max_size=50_000_000) as ws:
            await ws.send(json.dumps({"id": 1, "method": "Page.bringToFront"}))
            try:
                await asyncio.wait_for(ws.recv(), timeout=2.0)
            except Exception:
                pass
            msg_id = int(time.time() * 1000) % 1000000
            await ws.send(json.dumps({
                "id": msg_id,
                "method": "Runtime.evaluate",
                "params": {"expression": js_code, "returnByValue": True}
            }))
            val = {}
            for _ in range(10):
                try:
                    resp_str = await asyncio.wait_for(ws.recv(), timeout=3.0)
                    resp = json.loads(resp_str)
                    if resp.get("id") == msg_id:
                        val = resp.get("result", {}).get("result", {}).get("value", {})
                        break
                except Exception:
                    break
            
            is_gen = val.get("isGenerating", False)
            text = val.get("lastText", "")
            out_file = "ARENA_LATEST_RAW.md" if "primary" in name else "ARENA_FABLE_LATEST_RAW.md"
            out_path = TRADE_PLANS_DIR / out_file
            if text and len(text) > 100:
                out_path.write_text(text, encoding="utf-8")
            
            return {
                "name": name,
                "is_generating": is_gen,
                "text_len": len(text),
                "file": str(out_path),
                "preview": text[:300] if text else "",
                "done": (not is_gen) and len(text) > 200
            }
    except Exception as e:
        return {"name": name, "error": str(e), "done": False}

async def check_copilot_tab(tab_info: dict) -> dict:
    ws_url = tab_info.get("ws_url")
    name = tab_info.get("name", "Copilot")
    agent_id = tab_info.get("agent_id", "")
    js_code = """
    (() => {
        const stopBtn = Boolean(document.querySelector('button[aria-label="Stop"], button[title="Stop"]'));
        const typing = Boolean(document.querySelector('[class*="typing"], [class*="thinking"], [class*="streaming"], .webchat__typing-indicator'));
        const isGenerating = stopBtn || typing;
        const allElements = Array.from(document.querySelectorAll('div, span, p'));
        const matches = [];
        for (const el of allElements) {
            const txt = (el.innerText || '').trim();
            if ((txt.includes("The snapshot confirms") || txt.includes("audit the attached snapshot") || txt.includes("Mandate 1") || txt.includes("MANDATE 1") || txt.includes("MANDATE 2") || txt.includes("TRADING DESK COUNCIL") || txt.includes("ETHUSD.pi") || txt.includes("STAND ASIDE")) && txt.length > 200 && !txt.startsWith("TRADING DESK COUNCIL: CYCLE 60") && !txt.startsWith("TRADING DESK COUNCIL: CYCLE 61")) {
                matches.push(txt);
            }
        }
        const longest = matches.length > 0 ? matches.reduce((a, b) => a.length > b.length ? a : b) : "";
        return {
            isGenerating,
            textLen: longest.length,
            latestText: longest
        };
    })()
    """
    try:
        async with websockets.connect(ws_url, max_size=50_000_000) as ws:
            msg_id = int(time.time() * 1000) % 1000000
            await ws.send(json.dumps({
                "id": msg_id,
                "method": "Runtime.evaluate",
                "params": {"expression": js_code, "returnByValue": True, "awaitPromise": True}
            }))
            val = {}
            for _ in range(6):
                try:
                    resp_str = await asyncio.wait_for(ws.recv(), timeout=3.0)
                    resp = json.loads(resp_str)
                    if resp.get("id") == msg_id:
                        val = resp.get("result", {}).get("result", {}).get("value", {})
                        break
                except Exception:
                    break
            is_gen = val.get("isGenerating", False)
            text = val.get("latestText", "")
            out_file = "COPILOT_OPUS_LATEST_RAW.md" if agent_id == "98cead10" else "COPILOT_ASTRA_LATEST_RAW.md"
            out_path = TRADE_PLANS_DIR / out_file
            if text and len(text) > 100:
                out_path.write_text(text, encoding="utf-8")
            return {
                "name": f"Copilot_{name}_{agent_id[:8]}",
                "is_generating": is_gen,
                "text_len": len(text),
                "file": str(out_path),
                "preview": text[:300] if text else "",
                "done": (not is_gen) and len(text) > 200
            }
    except Exception as e:
        return {"name": f"Copilot_{name}", "error": str(e), "done": False}

async def harvest_all() -> dict:
    from Terminal.arena_bridge import get_all_arena_tab_ws_urls, get_all_copilot_tabs
    arena_tabs = await get_all_arena_tab_ws_urls()
    copilot_tabs = await get_all_copilot_tabs()
    
    tasks = []
    for name, ws in arena_tabs:
        tasks.append(check_arena_tab(name, ws))
    for tab in copilot_tabs:
        tasks.append(check_copilot_tab(tab))
        
    results = await asyncio.gather(*tasks)
    return {r["name"]: r for r in results}

if __name__ == "__main__":
    res = asyncio.run(harvest_all())
    print(json.dumps(res, indent=2))
