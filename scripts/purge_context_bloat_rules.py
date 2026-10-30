import os
import shutil
import datetime

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
archive_dir = "archive/purged_agents_md"
os.makedirs(archive_dir, exist_ok=True)

targets = [
    # Local workspace rules
    r"c:\Users\SIGMA\Documents\Trading_2\.agents\AGENTS.md",
    r"c:\Users\SIGMA\Documents\Trading_2\.agents\rules\AGENTS.md",
    r"c:\Users\SIGMA\Documents\Trading_2\.agents\rules\UNIVERSAL_SKILL_ROUTER.md",
    r"c:\Users\SIGMA\Documents\Trading_2\.agents\rules\GEMINI.md",
    r"c:\Users\SIGMA\Documents\Trading_2\.agents\rules\FABLE5_CHECKLIST.md",
    r"c:\Users\SIGMA\Documents\Trading_2\.agents\rules\MASTER_RULES.md",
    
    # Global config rules that get injected into every turn
    r"C:\Users\SIGMA\.gemini\config\rules\AGENTS.md",
    r"C:\Users\SIGMA\.gemini\config\rules\UNIVERSAL_SKILL_ROUTER.md",
]

print("=== PURGING CONTEXT-BLOATING RULE & AGENT FILES ===")
purged_count = 0

for target in targets:
    if os.path.exists(target):
        base_name = os.path.basename(target)
        prefix = "global_" if ".gemini" in target else "workspace_"
        if "rules" in target and "workspace_" in prefix:
            prefix += "rules_"
        dest_name = f"{prefix}{base_name}_{timestamp}.bak"
        dest_path = os.path.join(archive_dir, dest_name)
        
        # Copy to archive
        shutil.copy2(target, dest_path)
        # Remove from active rules location
        os.remove(target)
        print(f"Purged & Archived: {target} -> {dest_path}")
        purged_count += 1
    else:
        print(f"Already absent: {target}")

print(f"\nTotal files successfully purged and archived: {purged_count}")
