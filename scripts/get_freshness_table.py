import json
with open('Data/metadata/parquet_all_feeds_checklist.json', encoding='utf-8') as f:
    data = json.load(f)
checklist = data.get('checklist', [])
lines = []
lines.append('Idx  | Feed Name                      | Tier          | Rows   | Banner (IST)             | Age (min)  | Status')
lines.append('-------------------------------------------------------------------------------------------------------------------')
for item in checklist[:33]:
    idx = f"{item['idx']:02d}"
    name = f"{item['feed_name']:<30}"
    tier = f"{item['tier']:<13}"
    rows = f"{item['rows']:<6}"
    banner = f"{item['banner_ist']:<24}"
    age = f"{item['age_str']:<10}"
    status = item['status']
    lines.append(f"{idx}   | {name} | {tier} | {rows} | {banner} | {age} | {status}")
print('\n'.join(lines))
