"""Resilient Graphify AST Watcher Daemon for Windows.

Uses watchdog.observers.polling.PollingObserver to prevent Win32
ReadDirectoryChangesW buffer overflow/handle exhaustion in large repositories,
and wraps execution in a persistent supervisor loop.
"""

import sys
import time
from pathlib import Path
import watchdog.observers
import watchdog.observers.polling

# Force unbuffered standard output
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True)

# Monkeypatch Observer to use robust PollingObserver on Windows
watchdog.observers.Observer = watchdog.observers.polling.PollingObserver

from graphify.watch import watch


def main():
    watch_path = Path(".").resolve()
    print(f"[graphify-supervisor] Starting resilient AST watcher on {watch_path}")
    while True:
        try:
            watch(watch_path, debounce=3.0)
        except KeyboardInterrupt:
            print("\n[graphify-supervisor] Shutting down on user interrupt.")
            break
        except Exception as exc:
            print(f"[graphify-supervisor] Watcher encountered error: {exc}. Restarting in 2s...")
            time.sleep(2.0)


if __name__ == "__main__":
    main()
