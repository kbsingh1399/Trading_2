import re
import json

arena_raw = open('docs/trade_plans/ARENA_LATEST_RAW.md', encoding='utf-8').read()

# find json in arena
start_idx = arena_raw.find('```json')
if start_idx != -1:
    end_idx = arena_raw.rfind('```')
    json_str = arena_raw[start_idx + len('```json'):end_idx].strip()
    try:
        data = json.loads(json_str)
        print("Arena JSON parsed successfully! Keys:", list(data.keys()))
        for k in data.keys():
            val = data[k]
            if isinstance(val, list):
                print(f"Key '{k}': {len(val)} items")
                for i, item in enumerate(val):
                    print(f"  Item {i+1}:", item)
            elif isinstance(val, dict):
                print(f"Key '{k}': dict with {len(val)} keys:", list(val.keys()))
    except Exception as e:
        print(f"JSON load error: {e}")
        # print around error
        print("Raw snippet:", json_str[:500])
else:
    print("```json not found in Arena")
