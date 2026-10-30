import asyncio
import json
import sys
import websockets
from pathlib import Path

ROOT = Path("C:/Users/SIGMA/Documents/Trading_2")
ARENA_RAW_FILE = ROOT / "docs" / "trade_plans" / "ARENA_LATEST_RAW.md"
ZAI_RAW_FILE = ROOT / "docs" / "trade_plans" / "ZAI_LATEST_RAW.md"

sys.path.insert(0, str(ROOT))
from Terminal.rock_hard_dual_watchdog import find_ws_url, probe_zai

async def harvest_arena():
    ws_url = find_ws_url("arena.ai")
    if not ws_url:
        print("Arena tab not found")
        return False
        
    js = """(() => {
        function nodeToMd(node) {
            if (!node) return '';
            if (node.nodeType === Node.TEXT_NODE) return node.textContent;
            if (node.nodeType !== Node.ELEMENT_NODE) return '';

            const tag = node.tagName.toLowerCase();
            if (tag === 'pre') {
                const code = node.querySelector('code');
                const lang = code ? (code.className.match(/language-(\\w+)/) || ['', ''])[1] : '';
                return '\\n```' + lang + '\\n' + (code ? code.innerText : node.innerText) + '\\n```\\n';
            }
            if (tag === 'code' && node.parentElement.tagName.toLowerCase() !== 'pre') return '`' + node.innerText + '`';
            if (tag === 'h1') return '\\n# ' + node.innerText.trim() + '\\n\\n';
            if (tag === 'h2') return '\\n## ' + node.innerText.trim() + '\\n\\n';
            if (tag === 'h3') return '\\n### ' + node.innerText.trim() + '\\n\\n';
            if (tag === 'h4') return '\\n#### ' + node.innerText.trim() + '\\n\\n';
            if (tag === 'p') return '\\n' + Array.from(node.childNodes).map(nodeToMd).join('').trim() + '\\n';
            if (tag === 'br') return '\\n';
            if (tag === 'hr') return '\\n---\\n';
            if (tag === 'ul') return '\\n' + Array.from(node.children).map(li => '- ' + nodeToMd(li).trim()).join('\\n') + '\\n';
            if (tag === 'ol') return '\\n' + Array.from(node.children).map((li, idx) => (idx + 1) + '. ' + nodeToMd(li).trim()).join('\\n') + '\\n';
            if (tag === 'li') return Array.from(node.childNodes).map(nodeToMd).join('').trim();
            if (tag === 'strong' || tag === 'b') return '**' + Array.from(node.childNodes).map(nodeToMd).join('') + '**';
            if (tag === 'em' || tag === 'i') return '*' + Array.from(node.childNodes).map(nodeToMd).join('') + '*';
            if (tag === 'table') {
                const rows = Array.from(node.querySelectorAll('tr'));
                if (rows.length === 0) return '';
                const lines = [];
                let isHeader = true;
                for (const r of rows) {
                    const cells = Array.from(r.querySelectorAll('th, td')).map(c => nodeToMd(c).replace(/\\n/g, ' ').trim());
                    lines.push('| ' + cells.join(' | ') + ' |');
                    if (isHeader) {
                        lines.push('| ' + cells.map(() => '---').join(' | ') + ' |');
                        isHeader = false;
                    }
                }
                return '\\n' + lines.join('\\n') + '\\n\\n';
            }
            return Array.from(node.childNodes).map(nodeToMd).join('');
        }

        const allProses = Array.from(document.querySelectorAll('.prose')).filter(p => (p.innerText || '').trim().length > 50);
        const lastProse = allProses.length > 0 ? allProses[allProses.length - 1] : null;
        return lastProse ? nodeToMd(lastProse).trim() : '';
    })()"""

    async with websockets.connect(ws_url, max_size=50_000_000) as ws:
        await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
        res = json.loads(await ws.recv())
        text = res.get("result", {}).get("result", {}).get("value") or ""
        if len(text) > 500:
            ARENA_RAW_FILE.write_text(text, encoding="utf-8")
            print(f"SUCCESS: Harvested Arena.ai text ({len(text)} chars) to {ARENA_RAW_FILE}")
            return True
    return False

async def harvest_zai():
    z = await probe_zai()
    text = z.get("lastText", "")
    if len(text) > 500:
        ZAI_RAW_FILE.write_text(text, encoding="utf-8")
        print(f"SUCCESS: Harvested Z.ai text ({len(text)} chars) to {ZAI_RAW_FILE}")
        return True
    return False

async def main():
    await harvest_arena()
    await harvest_zai()

if __name__ == "__main__":
    asyncio.run(main())
