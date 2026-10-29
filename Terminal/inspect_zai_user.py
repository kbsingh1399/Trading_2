import asyncio, json
import websockets
from Terminal.rock_hard_dual_watchdog import find_ws_url

async def main():
    ws_url = find_ws_url('chat.z.ai')
    async with websockets.connect(ws_url) as ws:
        js = """(() => {
            const userMsgs = Array.from(document.querySelectorAll('.chat-user, [data-message-author-role="user"]'));
            const lastUser = userMsgs.length > 0 ? userMsgs[userMsgs.length - 1] : null;
            if (!lastUser) return 'no user msg';
            
            // Find container that holds both user and assistant items
            let parent = lastUser;
            while (parent && parent.parentElement && parent.parentElement.children.length < 2) {
                parent = parent.parentElement;
            }
            const wrapper = parent.parentElement;
            const items = Array.from(wrapper.children);
            const userIdx = items.indexOf(parent);
            return {
                totalInWrapper: items.length,
                userIdx: userIdx,
                subsequentItems: items.slice(userIdx + 1).map(it => ({
                    tag: it.tagName,
                    classes: it.className,
                    textLen: it.innerText.length,
                    preview: it.innerText.slice(0, 300)
                }))
            };
        })()"""
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        res = json.loads(await ws.recv())
        val = res.get('result', {}).get('result', {}).get('value')
        print(val)

if __name__ == '__main__':
    asyncio.run(main())
