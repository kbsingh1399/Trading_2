import json
import sys

with open('docs/parquet_schema_audit.json', encoding='utf-8') as f:
    audit = json.load(f)

print(f"Loaded audit for {len(audit)} files.")

# Helper to format column table
def format_col_table(cols, sample):
    lines = ["| Column Name | Data Type | Sample Live Value | Description & Extraction Logic |"]
    lines.append("|---|---|---|---|")
    for col, dtype in cols.items():
        val = str(sample.get(col, ""))
        if len(val) > 40:
            val = val[:37] + "..."
        val = val.replace("\n", " ").replace("|", "\\|")
        lines.append(f"| `{col}` | `{dtype}` | `{val}` | Mapped to section extraction pipeline |")
    return "\n".join(lines)

print("Helper ready.")
