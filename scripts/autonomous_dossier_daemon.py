#!/usr/bin/env python3
"""
scripts/autonomous_dossier_daemon.py
====================================
Canonical redirect to standalone_dossier_json_daemon.py (Pure-Parquet -> JSON).
Ensures 100% data extraction without generating legacy .md files.
"""
from __future__ import annotations
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.standalone_dossier_json_daemon import main

if __name__ == "__main__":
    main()
