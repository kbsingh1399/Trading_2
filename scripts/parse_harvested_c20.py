import re
import pathlib

r = pathlib.Path("docs/trade_plans")
arena_text = (r / "ARENA_LATEST_RAW.md").read_text(encoding="utf-8")
zai_text = (r / "ZAI_LATEST_RAW.md").read_text(encoding="utf-8")

print("=== ARENA EXCERPTS ===")
for match in re.finditer(r"(?i)(AUDUSD|19490051|verdict|recommendation|consensus|tier_0|let run|cut|hold)", arena_text):
    start = max(0, match.start() - 50)
    end = min(len(arena_text), match.end() + 150)
    # print small sample
    print(arena_text[start:end].replace("\n", " "))
    print("-" * 40)
    if match.start() > 10000:
        break

print("\n=== ZAI EXCERPTS ===")
for match in re.finditer(r"(?i)(AUDUSD|19490051|verdict|recommendation|consensus|tier_0|let run|cut|hold)", zai_text):
    start = max(0, match.start() - 50)
    end = min(len(zai_text), match.end() + 150)
    print(zai_text[start:end].replace("\n", " "))
    print("-" * 40)
    if match.start() > 10000:
        break
