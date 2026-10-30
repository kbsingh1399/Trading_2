import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def parse_arena():
    with open('docs/trade_plans/ARENA_LATEST_RAW.md', 'r', encoding='utf-8') as f:
        raw = f.read()
    
    # Check if raw has escaped newlines
    if '\\n' in raw and '\n' not in raw[:200]:
        text = raw.replace('\\n', '\n').replace('\\"', '"')
    else:
        text = raw

    print("==================================================")
    print("ARENA.AI LATEST COUNCIL OUTPUT REVIEW")
    print(f"Total Characters: {len(text)}")
    print("==================================================")

    # Find main sections
    sections = re.findall(r'(##\s+[^\n]+)', text)
    print("Sections found:")
    for s in sections:
        print("  *", s)

    # Extract Table of Candidate Recommendations / Orders
    tables = re.findall(r'(\|.+?\|(?:\n\|.+?\|)+)', text)
    print(f"\nTables found: {len(tables)}")
    for idx, t in enumerate(tables):
        if any(w in t.lower() for w in ['ticket', 'symbol', 'candidate', 'recommendation', 'risk', 'spread', 'action', 'lot']):
            print(f"\n--- Relevant Table {idx+1} ---")
            lines = t.strip().split('\n')
            for l in lines[:15]:
                print(l)
            if len(lines) > 15:
                print(f"... ({len(lines)-15} more rows)")

def parse_zai():
    with open('docs/trade_plans/ZAI_LATEST_RAW.md', 'r', encoding='utf-8') as f:
        text = f.read()

    print("\n==================================================")
    print("Z.AI (GLM-5.3-Flash) LATEST COUNCIL OUTPUT REVIEW")
    print(f"Total Characters: {len(text)}")
    print("==================================================")

    sections = re.findall(r'(##?\s+[^\n]+)', text)
    print("Sections found:")
    for s in sections[:20]:
        print("  *", s)

    tables = re.findall(r'(\|.+?\|(?:\n\|.+?\|)+)', text)
    print(f"\nTables found: {len(tables)}")
    for idx, t in enumerate(tables):
        if any(w in t.lower() for w in ['ticket', 'symbol', 'candidate', 'recommendation', 'risk', 'spread', 'action', 'lot', 'entry']):
            print(f"\n--- Relevant Table {idx+1} ---")
            lines = t.strip().split('\n')
            for l in lines[:15]:
                print(l)
            if len(lines) > 15:
                print(f"... ({len(lines)-15} more rows)")

if __name__ == '__main__':
    parse_arena()
    parse_zai()
