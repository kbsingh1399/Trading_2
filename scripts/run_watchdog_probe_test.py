import asyncio
import json
import sys
import pathlib

ROOT = pathlib.Path('.').resolve()
sys.path.insert(0, str(ROOT / 'Terminal'))
import rock_hard_dual_watchdog as rdw

async def test_probes():
    a = await rdw.probe_arena()
    print('ARENA PROBE:')
    print(f"Connected: {a.get('connected')}, isGen: {a.get('isGenerating')}, len: {a.get('lastLen')}, hash: {a.get('textHash')}")
    if a.get('lastText'):
        print('Arena Preview:', a['lastText'][:300])
        rdw.save_arena_output(a)

    z = await rdw.probe_zai()
    print('\nZAI PROBE:')
    print(f"Connected: {z.get('connected')}, isGen: {z.get('isGenerating')}, len: {z.get('lastLen')}, hash: {z.get('textHash')}")
    if z.get('lastText'):
        print('Zai Preview:', z['lastText'][:300])
        rdw.save_zai_output(z)

if __name__ == '__main__':
    asyncio.run(test_probes())
