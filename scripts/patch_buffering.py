from pathlib import Path

p = Path("Terminal/rock_hard_dual_watchdog.py")
t = p.read_text(encoding="utf-8")
t = t.replace('sys.stdout.reconfigure(encoding="utf-8", errors="replace")', 'sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)')
t = t.replace('sys.stderr.reconfigure(encoding="utf-8", errors="replace")', 'sys.stderr.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)')
p.write_text(t, encoding="utf-8")
print("Updated line buffering in rock_hard_dual_watchdog.py")
