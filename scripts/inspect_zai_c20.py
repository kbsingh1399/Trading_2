import pathlib, re, sys

sys.stdout.reconfigure(encoding="utf-8")
z_text = pathlib.Path("docs/trade_plans/ZAI_LATEST_RAW.md").read_text(encoding="utf-8")

print("=== Z.AI LENGTH:", len(z_text))
print("=== Z.AI START ===")
print(z_text[:1000])

print("\n=== Z.AI TAIL ===")
print(z_text[-2000:])
