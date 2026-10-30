import asyncio
import json
import websockets

async def check_chart():
    ws_url = 'ws://127.0.0.1:9222/devtools/page/FDDB732749CF0371E914334A4F0AD4A7'
    async with websockets.connect(ws_url) as ws:
        js = """(() => {
            const canvases = Array.from(document.querySelectorAll('canvas')).map(c => ({ w: c.width, h: c.height }));
            const highcharts = document.querySelectorAll('.highcharts-container, .echarts, [class*="chart"]').length;
            const textNodes = document.body ? document.body.innerText.split('\\n').filter(t => t.trim().length > 0) : [];
            const liqMapSection = textNodes.filter(t => t.includes('Liq') || t.includes('BTC') || t.includes('Binance') || t.includes('Pain') || t.includes('Cumulative') || t.includes('Leverage'));
            return {
                canvases: canvases,
                chartContainers: highcharts,
                sampleText: liqMapSection.slice(0, 20)
            };
        })()"""
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        resp = json.loads(await ws.recv())
        print(json.dumps(resp.get('result', {}).get('result', {}).get('value'), indent=2))

asyncio.run(check_chart())
