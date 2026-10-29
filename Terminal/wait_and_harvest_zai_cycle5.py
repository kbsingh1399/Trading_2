import asyncio
import hashlib
import json
import pathlib
import sys
import time
import websockets
from Terminal.rock_hard_dual_watchdog import find_ws_url, save_zai_output

ROOT = pathlib.Path(__file__).resolve().parents[1]
ZAI_RAW_FILE = ROOT / "docs" / "trade_plans" / "ZAI_LATEST_RAW.md"

async def check():
    ws_url = find_ws_url("chat.z.ai")
    if not ws_url:
        return None
    async with websockets.connect(ws_url, max_size=50_000_000) as ws:
        js = """(() => {
            const stopBtn = document.querySelector('button[aria-label*="Stop"], button[title*="Stop"], button.stop-button, button:has(span.size-3.rounded-xs)');
            const stopSquare = document.querySelector('button span.size-3.rounded-xs, button span.block.size-3');
            const sendBtn = document.querySelector('button#send-message-button, button[aria-label="Send"], button[aria-label*="Send"]');
            const isGenerating = Boolean(stopBtn) || Boolean(stopSquare) || !sendBtn;
            
            // Try to find the markdown text
            const allChatMsgs = Array.from(document.querySelectorAll('.chat-assistant.markdown-prose, div.prose'));
            let chatText = '';
            for (let i = allChatMsgs.length - 1; i >= 0; i--) {
                const t = (allChatMsgs[i].innerText || '').trim();
                if (t.includes('Cycle_005') || t.includes('COUNCIL REPORT')) {
                    chatText = t;
                    break;
                }
            }

            // Fallback to body text from Cycle_005
            const body = document.body.innerText;
            const cIdx = body.lastIndexOf('# [COUNCIL REPORT');
            let bodyReport = '';
            if (cIdx !== -1) {
                bodyReport = body.substring(cIdx);
            }

            let text = chatText.length > bodyReport.length ? chatText : bodyReport;
            if (!text && body.lastIndexOf('Cycle_005') !== -1) {
                text = body.substring(body.lastIndexOf('Cycle_005'));
            }

            return {
                isGenerating,
                sendEnabled: Boolean(sendBtn && !sendBtn.disabled),
                textLen: text.length,
                text: text,
                hasEnd: text.includes('[END OF REPORT')
            };
        })()"""
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        res = json.loads(await ws.recv())
        return res.get('result', {}).get('result', {}).get('value')

async def main():
    print("Surveillance started for Z.ai Cycle_005...", flush=True)
    last_len = 0
    stable_ticks = 0
    for tick in range(150): # up to 300 seconds
        state = await check()
        if not state:
            print("Z.ai tab not reachable", flush=True)
            await asyncio.sleep(2.0)
            continue
        is_gen = state.get('isGenerating', True)
        t_len = state.get('textLen', 0)
        has_end = state.get('hasEnd', False)
        
        print(f"t={tick*2}s: isGen={is_gen}, textLen={t_len}, hasEnd={has_end}", flush=True)
        
        if (not is_gen and t_len > 1000) or has_end:
            if t_len == last_len:
                stable_ticks += 1
            else:
                stable_ticks = 1
                last_len = t_len
            
            if stable_ticks >= 2 or has_end:
                full_text = state.get('text', '')
                ZAI_RAW_FILE.write_text(full_text, encoding='utf-8')
                print(f"SUCCESS! Z.ai Cycle_005 harvested ({len(full_text)} chars) to {ZAI_RAW_FILE}", flush=True)
                return 0
        else:
            stable_ticks = 0
            last_len = t_len
            
        await asyncio.sleep(2.0)
    print("Timeout waiting for Z.ai", flush=True)
    return 1

if __name__ == '__main__':
    sys.exit(asyncio.run(main()))
