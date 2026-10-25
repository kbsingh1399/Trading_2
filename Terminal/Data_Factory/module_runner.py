#!/usr/bin/env python3
"""
Terminal/Data_Factory/module_runner.py
=======================================
Dedicated execution wrapper for individual Excel harvester modules.
Automatically imports excel_lock_hook to guarantee cross-process FileLock protection
on Data/DataBase_Trading.xlsx before delegating to the target harvester script.
"""

import pathlib
import runpy
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
MODULES_DIR = ROOT / "Data" / "Excel_Modules"
if str(MODULES_DIR) not in sys.path:
    sys.path.insert(0, str(MODULES_DIR))

try:
    import excel_lock_hook  # noqa: F401
except ImportError:
    pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] module_runner.py requires target script path.")
        sys.exit(1)
    target_script = pathlib.Path(sys.argv[1]).resolve()
    # Replace sys.argv so target script receives its original arguments
    sys.argv = [str(target_script)] + sys.argv[2:]
    runpy.run_path(str(target_script), run_name="__main__")
