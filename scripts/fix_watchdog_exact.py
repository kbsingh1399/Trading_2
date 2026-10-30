from pathlib import Path

p = Path("Terminal/rock_hard_dual_watchdog.py")
text = p.read_text(encoding="utf-8")

old_line = 'is_text_complete = (not is_gen and has_anchor) or (len(cur_text) >= 10000 and ("Final Execution" in cur_text or "Candidate Trade" in cur_text or "COUNCIL REPORT" in cur_text))'
new_code = '''# Must be a model response (NOT the user prompt)
                is_user_prompt = cur_text.strip().startswith("# 🏛️ AUTONOMOUS") or "Dossier-Centric Multi-Agent Squad Audit" in cur_text[:400]
                is_text_complete = not is_user_prompt and ((not is_gen and has_anchor) or (len(cur_text) >= 20000 and ("Final Execution Summary" in cur_text or "COUNCIL REPORT" in cur_text)))'''

if old_line in text:
    text = text.replace(old_line, new_code)
    text = text.replace('if has_cycle and is_text_complete and len(cur_text) > 50:', 'if has_cycle and not is_user_prompt and is_text_complete and len(cur_text) > 1000:')
    p.write_text(text, encoding="utf-8")
    print("SUCCESS: Updated prompt vs response filter in watchdog.")
else:
    print("FAILED: old_line not found.")
