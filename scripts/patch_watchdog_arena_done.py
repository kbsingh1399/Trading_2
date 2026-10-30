from pathlib import Path

p = Path("Terminal/rock_hard_dual_watchdog.py")
text = p.read_text(encoding="utf-8")

old_condition = "                if has_cycle and not is_gen and has_anchor and len(cur_text) > 50:"
new_condition = """                is_text_complete = (not is_gen and has_anchor) or (len(cur_text) >= 10000 and ("Final Execution" in cur_text or "Candidate Trade" in cur_text or "COUNCIL REPORT" in cur_text))
                if has_cycle and is_text_complete and len(cur_text) > 50:"""

text_norm = text.replace("\r\n", "\n")
old_norm = old_condition.replace("\r\n", "\n")

if old_norm in text_norm:
    text_norm = text_norm.replace(old_norm, new_condition)
    p.write_text(text_norm, encoding="utf-8")
    print("SUCCESS: Patched Arena completion condition in rock_hard_dual_watchdog.py")
else:
    print("FAILED: Target condition not found")
