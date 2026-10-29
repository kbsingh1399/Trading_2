import asyncio
import sys
import time

sys.path.insert(0, 'Terminal')
from rock_hard_dual_watchdog import probe_zai, save_zai_output

async def main():
    for i in range(10):
        z = await probe_zai()
        text = z.get('lastText', '')
        is_gen = z.get('isGenerating', False)
        print(f"Check {i}: len={len(text)}, isGen={is_gen}, has_Cycle_005={'Cycle_005' in text}", flush=True)
        if 'Cycle_005' in text:
            print(f"FOUND Cycle_005! Text length: {len(text)}", flush=True)
            if not is_gen:
                save_zai_output(z)
                print("Saved Z.ai output to docs/trade_plans/ZAI_LATEST_RAW.md!", flush=True)
                return
        await asyncio.sleep(4.0)

if __name__ == '__main__':
    asyncio.run(main())
