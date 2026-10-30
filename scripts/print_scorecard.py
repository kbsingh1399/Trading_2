import json

with open('Data/metadata/parquet_all_feeds_checklist.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print(f"Total: {d['total_canonical_feeds']} | Passed: {d['passed_feeds']} | Failed: {d['failed_or_stale_count']}")
print("Idx  | Feed Name                      | Tier          | Rows   | Banner (IST)             | Age (min)  | Status")
print("-" * 105)
for item in d['checklist']:
    idx_str = f"{item['idx']:02d}"
    print(f"{idx_str:<4} | {item['feed_name']:<30} | {item['tier']:<13} | {item['rows']:<6} | {item['banner_ist']:<24} | {item['age_str']:<10} | {item['status']}")
