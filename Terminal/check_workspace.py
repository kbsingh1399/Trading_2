import asyncio, json
import websockets
from Terminal.rock_hard_dual_watchdog import find_ws_url

async def main():
    ws_url = find_ws_url("chat.z.ai")
    async with websockets.connect(ws_url) as ws:
        js = """(() => {
            const cm = document.querySelector('.cm-content');
            let text = '';
            if (cm && cm.cmView) {
                let v = cm.cmView;
                while (v && !v.state && v.parent) v = v.parent;
                if (v && v.view && v.view.state) text = v.view.state.doc.toString();
                else if (v && v.state) text = v.state.doc.toString();
            }
            if (!text) {
                const wsProse = document.querySelector('.workspaceContent .markdown-prose, .workspace .markdown-prose, .workspaceContent pre');
                if (wsProse) text = (wsProse.innerText || '').trim();
            }
            const header = Array.from(document.querySelectorAll('.text-sm.flex-1.truncate.line-clamp-1')).map(e => (e.innerText || '').trim()).find(t => t.endsWith('.md') || t.endsWith('.json')) || '';
            return {
                header,
                len: text.length,
                preview: text.slice(0, 500),
                tail: text.slice(-500)
            };
        })()"""
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        res = json.loads(await ws.recv())
        val = res.get('result', {}).get('result', {}).get('value')
        print("Header:", val.get("header"))
        print("Length:", val.get("len"))
        print("Preview:\n", val.get("preview"))
        print("Tail:\n", val.get("tail"))

if __name__ == '__main__':
    asyncio.run(main())
