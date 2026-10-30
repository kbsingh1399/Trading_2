import sys

def main():
    path = "Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    old_header = "### ⏳ Cycle_017 Scorecard: PRE-INITIALIZED & ARMED\n**Target Interval**: `20 Minutes` | **Pacing Engine**: Dynamic AutoWake Timer"
    new_header = "### 🟢 Cycle_017 Scorecard: COMPLETED & FULLY VERIFIED\n**Target Interval**: `20 Minutes` | **Pacing Engine**: Dynamic AutoWake Timer | **Status**: Verified Consensus Achieved"

    if old_header not in text:
        print("old_header not found!")
        return

    # find the block between Cycle_017 and Cycle_018
    p1 = text.find(old_header)
    p2 = text.find("### ⏳ Cycle_018 Scorecard: PRE-INITIALIZED & ARMED")
    if p2 == -1:
        print("Cycle_018 not found!")
        return

    c17_block = text[p1:p2]
    
    # replace all '- [ ]' with '- [x]' in c17_block
    c17_block_new = c17_block.replace("- [ ]", "- [x]").replace(old_header, new_header)

    text_updated = text[:p1] + c17_block_new + text[p2:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(text_updated)
    print("Successfully updated Cycle_017 Scorecard to COMPLETED & FULLY VERIFIED!")

if __name__ == "__main__":
    main()
