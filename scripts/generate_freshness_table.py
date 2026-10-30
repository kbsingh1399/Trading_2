import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('Data/metadata/parquet_all_feeds_checklist.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print(f"Idx  | Feed Name                      | Tier          | Rows   | Banner (IST)             | Age (min)  | Status")
print("-" * 115)
for item in d.get('checklist', []):
    idx = item['idx']
    feed_name = item['feed_name']
    tier = item['tier']
    rows = item['rows']
    banner_ist = item['banner_ist']
    age_str = item['age_str']
    status = item['status']
    print(f"{idx:02d}   | {feed_name:<30} | {tier:<13} | {rows:<6} | {banner_ist:<24} | {age_str:<10} | {status}")
