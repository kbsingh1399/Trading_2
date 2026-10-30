from pathlib import Path

p = Path("Terminal/rock_hard_dual_watchdog.py")
text = p.read_text(encoding="utf-8")

old_code = """                # Consider complete if: (not is_gen and has_anchor) OR (cur_len >= 10000 and text is stable and has cycle)
                is_text_complete = (not is_gen and has_anchor) or (len(cur_text) >= 10000 and ("Final Execution" in cur_text or "Candidate Trade" in cur_text or "COUNCIL REPORT" in cur_text))
                if has_cycle and is_text_complete and len(cur_text) > 50:"""

new_code = """                # Must be a model response (NOT the user prompt)
                is_user_prompt = cur_text.strip().startswith("# 🏛️ AUTONOMOUS") or "Dossier-Centric Multi-Agent Squad Audit & Full-Length Forensic Candidate Discovery Specification" in cur_text[:400]
                is_text_complete = not is_user_prompt and ((not is_gen and has_anchor) or (len(cur_text) >= 20000 and ("Final Execution Summary" in cur_text or "COUNCIL REPORT" in cur_text)))
                if has_cycle and not is_user_prompt and is_text_complete and len(cur_text) > 1000:"""

text_norm = text.replace("\r\n", "\n")
old_norm = old_code.replace("\r\n", "\n")

if old_norm in text_norm:
    text_norm = text_norm.replace(old_norm, new_code)
    p.write_text(text_norm, encoding="utf-8")
    print("SUCCESS: Fixed prompt vs response detection in rock_hard_dual_watchdog.py")
else:
    print("FAILED: Target condition not found")
