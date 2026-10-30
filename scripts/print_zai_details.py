import sys
sys.stdout.reconfigure(encoding='utf-8')
txt = open('docs/trade_plans/ZAI_LATEST_RAW.md', encoding='utf-8').read()
print("Z.ai length:", len(txt))
print("--- Z.AI FIRST 1500 CHARS ---")
print(txt[:1500])
print("\n--- Z.AI LAST 2000 CHARS ---")
print(txt[-2000:])
