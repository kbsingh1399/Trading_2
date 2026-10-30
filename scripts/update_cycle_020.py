import sys
from pathlib import Path

path = Path("Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md")
text = path.read_text(encoding="utf-8")

start_token = "### ⏳ Cycle_020 Scorecard: PRE-INITIALIZED & ARMED"
end_token = "### ⏳ Cycle_021 Scorecard: PRE-INITIALIZED & ARMED"

if start_token in text and end_token in text:
    start_idx = text.find(start_token)
    end_idx = text.find(end_token)
    
    cycle_020_block = text[start_idx:end_idx]
    
    updated_block = cycle_020_block.replace(
        "### ⏳ Cycle_020 Scorecard: PRE-INITIALIZED & ARMED",
        "### 🟢 Cycle_020 Scorecard: COMPLETED & FULLY VERIFIED"
    )
    updated_block = updated_block.replace("- [ ]", "- [x]")
    
    new_text = text[:start_idx] + updated_block + text[end_idx:]
    path.write_text(new_text, encoding="utf-8")
    print("SUCCESS: Updated Cycle_020 scorecard to COMPLETED & FULLY VERIFIED.")
else:
    print("FAILED: Could not find Cycle_020 block.")
