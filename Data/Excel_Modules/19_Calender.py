#!/usr/bin/env python3
"""
Data/Excel_Modules/19_Calender.py
==================================
Alias entrypoint shim for 19_Calendar.py.
Supports user requested spelling '19_Calender'.
"""
import sys
from pathlib import Path

# Add current directory to path and invoke 19_Calendar
current_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(current_dir))

import importlib
calendar_mod = importlib.import_module("19_Calendar")

if __name__ == "__main__":
    sys.exit(calendar_mod.main())
