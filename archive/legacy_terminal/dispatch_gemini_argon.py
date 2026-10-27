import json
import urllib.request
import asyncio
import websockets
from pathlib import Path

CDP_HTTP_URL = "http://127.0.0.1:9222"

async def dispatch_argon(prompt_text: str):
    req = urllib.request.urlopen(f"{CDP_HTTP_URL}/json")
    pages = json.loads(req.read().decode())
    target = next((p for p in pages if "gemini.google.com" in p.get("url", "")), None)
    if not target:
        print("ERROR: Google Gemini Argon tab not found in Chrome!")
        return False
        
    print(f"Connecting to Gemini Argon tab: {target.get('title')}")
    ws_url = target.get("webSocketDebuggerUrl")
    
    async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
        # Focus and select all existing text in editor
        js_focus_clear = """
        (() => {
            const editor = document.querySelector('.ql-editor');
            if (!editor) return false;
            editor.focus();
            document.execCommand('selectAll', false, null);
            document.execCommand('delete', false, null);
            return true;
        })()
        """
        await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js_focus_clear, "returnByValue": True}}))
        await ws.recv()
        await asyncio.sleep(0.5)
        
        # Use native CDP Input.insertText
        print(f"Pasting prompt ({len(prompt_text)} chars) into Gemini via CDP Input.insertText...")
        # If prompt is very large, chunk it in 8k pieces to avoid websocket buffer issues
        chunk_size = 8000
        for i in range(0, len(prompt_text), chunk_size):
            chunk = prompt_text[i:i+chunk_size]
            await ws.send(json.dumps({
                "id": 100 + i,
                "method": "Input.insertText",
                "params": {"text": chunk}
            }))
            await ws.recv()
            await asyncio.sleep(0.05)
            
        print("Prompt text successfully entered into editor!")
        await asyncio.sleep(1.0)
        
        # Click the send button or press Enter
        js_click_or_enter = """
        (() => {
            const sendBtn = document.querySelector('button[aria-label*="Send" i], button.send-button, [data-test-id*="send" i]');
            if (sendBtn && !sendBtn.disabled && sendBtn.offsetParent !== null) {
                sendBtn.click();
                return "CLICKED_SEND_BUTTON";
            }
            return "NO_BUTTON_FOUND";
        })()
        """
        await ws.send(json.dumps({"id": 2, "method": "Runtime.evaluate", "params": {"expression": js_click_or_enter, "returnByValue": True}}))
        btn_resp = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value")
        print("Send button status:", btn_resp)
        
        # Also dispatch Enter key
        print("Dispatching Enter key...")
        await ws.send(json.dumps({
            "id": 3,
            "method": "Input.dispatchKeyEvent",
            "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 13, "text": "\r", "unmodifiedText": "\r"}
        }))
        await ws.send(json.dumps({
            "id": 4,
            "method": "Input.dispatchKeyEvent",
            "params": {"type": "keyUp", "windowsVirtualKeyCode": 13, "text": "\r", "unmodifiedText": "\r"}
        }))
        
        await asyncio.sleep(2.0)
        
        # Check if generating
        js_check = """
        (() => {
            const isGen = !!document.querySelector('.stop-generating-button, [aria-label*="Stop" i], mat-progress-bar');
            return { isGen, textLen: document.querySelector('.ql-editor')?.innerText?.length || 0 };
        })()
        """
        await ws.send(json.dumps({"id": 5, "method": "Runtime.evaluate", "params": {"expression": js_check, "returnByValue": True}}))
        res = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value")
        print("Argon status after dispatch:", res)
        return True

async def main():
    import glob, re
    files = glob.glob("docs/prompts/ARENA_CYCLE_*_FABLE_PROMPT.txt")
    if not files:
        print("No cycle prompts found!")
        return
    # Sort by cycle number
    def cycle_num(fn):
        m = re.search(r"CYCLE_(\d+)_", fn)
        return int(m.group(1)) if m else 0
    latest_file = sorted(files, key=cycle_num)[-1]
    print(f"Loading latest prompt: {latest_file}...")
    prompt = Path(latest_file).read_text(encoding="utf-8")
    await dispatch_argon(prompt)

if __name__ == "__main__":
    asyncio.run(main())
