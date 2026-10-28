import urllib.request
import json
import asyncio
import websockets

async def probe():
    tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json', timeout=5).read())
    arena = next(t for t in tabs if 'arena.ai' in t.get('url', ''))
    async with websockets.connect(arena['webSocketDebuggerUrl']) as ws:
        js = """(() => {
            const allButtons = Array.from(document.querySelectorAll('button')).map((b, idx) => ({
                idx,
                aria: b.getAttribute('aria-label') || '',
                title: b.getAttribute('title') || '',
                classes: b.className,
                rect: { w: Math.round(b.getBoundingClientRect().width), h: Math.round(b.getBoundingClientRect().height) },
                text: (b.innerText || '').trim(),
                html: b.innerHTML.slice(0, 150)
            }));
            
            // Check composer / footer buttons
            const composerArea = document.querySelector('div[data-perf-target="composer"]') || document.querySelector('form') || document.querySelector('.composer');
            const composerButtons = Array.from(document.querySelectorAll('button')).filter(b => {
                const rect = b.getBoundingClientRect();
                return rect.bottom > window.innerHeight - 150 && rect.right > window.innerWidth - 300;
            }).map(b => ({
                aria: b.getAttribute('aria-label') || '',
                classes: b.className,
                rect: { w: Math.round(b.getBoundingClientRect().width), h: Math.round(b.getBoundingClientRect().height) },
                html: b.innerHTML.slice(0, 150)
            }));

            // Check running indicators
            const runningTexts = Array.from(document.querySelectorAll('*')).filter(e => {
                const t = (e.innerText || '').trim();
                return t.includes('Running command') || t.includes('Deployed thread') || t === '●';
            }).map(e => ({ tag: e.tagName, text: (e.innerText || '').trim().slice(0, 40) }));

            return {
                url: location.href,
                composerButtons,
                runningTexts: runningTexts.slice(0, 6),
                stopCandidates: allButtons.filter(b => 
                    b.aria.toLowerCase().includes('stop') || 
                    b.html.includes('rect') || 
                    b.html.includes('square') ||
                    (b.rect.w >= 28 && b.rect.w <= 50 && b.rect.h >= 28 && b.rect.h <= 50 && b.html.includes('<svg'))
                )
            };
        })()"""
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        res = json.loads(await ws.recv())
        print(json.dumps(res.get('result', {}).get('result', {}).get('value'), indent=2))

if __name__ == '__main__':
    asyncio.run(probe())
