import json
import os

path = "Data/metadata/parquet_all_feeds_checklist.json"
if not os.path.exists(path):
    path = "Data/parquet_all_feeds_checklist.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

feeds = data.get("checklist", [])
print(f"Total feeds: {len(feeds)}, all_passed: {data.get('all_passed')}")
print(f"{'Idx':<4} | {'Feed Name':<32} | {'Tier':<14} | {'Rows':<8} | {'Banner (IST)':<24} | {'Age (min)':<10} | {'Status'}")
print("-" * 105)
for f in feeds:
    idx = f.get("idx", 0)
    name = f.get("feed_name", f.get("sheet_name", "N/A"))
    tier = f.get("tier", "Standard")
    rows = f.get("rows", 0)
    banner = f.get("banner_ist", "N/A")
    age = f.get("age_minutes", 0.0)
    status = f.get("status", "PASS")
    print(f"{idx:02d}   | {name:<32} | {tier:<14} | {rows:<8} | {banner:<24} | {age:<10.1f}m | {status}")
