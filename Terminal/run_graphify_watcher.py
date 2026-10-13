"""Lightweight, low-memory Graphify AST Watcher Daemon for Windows.

Scans only production Python directories (`Terminal/` and `Engine/`) every 15s
for `.py` mtime changes instead of recursively polling `.git/`, `.agents/`, and
`Data/` (reducing RAM footprint from ~850 MB to ~15 MB).
"""

import ctypes
import gc
import os
import subprocess
import sys
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True)


def _trim_working_set() -> None:
    if os.name == "nt":
        try:
            ctypes.windll.psapi.EmptyWorkingSet(ctypes.windll.kernel32.GetCurrentProcess())
        except Exception:
            pass


def _scan_py_mtimes(roots: list[Path]) -> dict[str, float]:
    state: dict[str, float] = {}
    for root in roots:
        if not root.exists():
            continue
        for p in root.rglob("*.py"):
            try:
                state[str(p)] = p.stat().st_mtime
            except OSError:
                continue
    return state


def main() -> None:
    repo_root = Path(".").resolve()
    watch_dirs = [repo_root / "Terminal", repo_root / "Engine"]
    print(f"[graphify-supervisor] Starting low-RAM AST watcher on {[str(d) for d in watch_dirs]}")
    prev = _scan_py_mtimes(watch_dirs)
    _trim_working_set()
    while True:
        try:
            time.sleep(15.0)
            curr = _scan_py_mtimes(watch_dirs)
            if curr != prev:
                prev = curr
                print("[graphify-supervisor] Detected Python AST change; running graphify update...")
                subprocess.run(
                    [sys.executable, "-m", "graphify", "update", "."],
                    cwd=str(repo_root),
                    timeout=60,
                    check=False,
                )
            gc.collect()
            _trim_working_set()
        except KeyboardInterrupt:
            print("\n[graphify-supervisor] Shutting down on user interrupt.")
            break
        except Exception as exc:
            print(f"[graphify-supervisor] Watcher error: {exc}. Continuing in 5s...")
            time.sleep(5.0)


if __name__ == "__main__":
    main()
