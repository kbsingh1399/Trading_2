import sys
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['docs/trade_plans/ARENA_LATEST_RAW.md', 'docs/trade_plans/ZAI_LATEST_RAW.md', 'docs/trade_plans/GEMINI_WEB2API_LATEST_RAW.md']:
    print(f"\n=================== {fname} ===================")
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    print("Length:", len(text))
    # Look for Section 4, 5, 6 or conclusion
    for line in text.split('\n'):
        if any(keyword in line.lower() for keyword in ['verdict', 'ruling', 'recommendation', 'ticket 19490051', 'let run', 'should i let it run', 'concur']):
            print("  ", line.strip()[:120])
