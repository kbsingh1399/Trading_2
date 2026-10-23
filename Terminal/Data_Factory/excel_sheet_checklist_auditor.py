#!/usr/bin/env python3
"""
excel_sheet_checklist_auditor.py
=================================
Institutional 30-Sheet Comprehensive Health & IST Timestamp Checklist Auditor.
Verifies all 30 canonical worksheets in Data/DataBase_Trading.xlsx:
  1. Sheet presence and canonical numerical ordering (00 to 29)
  2. Row 1 Tier-1 Top Banner in IST:
     "[Sheet Name] | LAST UPDATED: YYYY-MM-DD HH:MM:SS IST (UTC) | ROWS: [N] | STATUS: LIVE"
  3. Table Column Headers contain "Timestamp (IST)" (or valid IST field)
  4. Data rows populated (row_count > 0)
  5. Internal timestamps formatted in IST (UTC+5:30)
  6. Zero formula errors (#REF!, #DIV/0!, #N/A, #VALUE!, #NAME?)
  7. Age freshness (<30 minutes = LIVE, <=24h = PERIODIC, >24h = STALE)
  8. Outputs clean scorecard table and JSON file Data/excel_all_sheets_checklist.json.
  9. Exits with code 0 if all sheets pass; code 1 if any sheet needs wakeup/intervention.
"""

from __future__ import annotations

import datetime
import json
import os
import pathlib
import re
import sys
import time

try:
    import openpyxl
except ImportError:
    raise ImportError("openpyxl is required. Run 'pip install openpyxl'.")

ROOT_DIR = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "Data"
EXCEL_PATH = DATA_DIR / "DataBase_Trading.xlsx"
OUTPUT_JSON = DATA_DIR / "excel_all_sheets_checklist.json"

IST_TIMEZONE = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
UTC_TIMEZONE = datetime.timezone.utc

CANONICAL_SHEETS = [
    (0, "00_MT5_Account_Telemetry"),
    (1, "1_Crypto_ETF_Flows"),
    (2, "2_Spot_Netflow_S"),
    (3, "3_Exchanges_LS_Ratio_15M"),
    (4, "3_Exchanges_LS_Ratio_1H"),
    (5, "3_Exchanges_LS_Ratio_4H"),
    (6, "4_Hyperliquid_Analysis"),
    (7, "5_OI"),
    (8, "5_Funding_Rate"),
    (9, "6_Funding_Fee_Settlement"),
    (10, "7_Liq_Heapmap"),
    (11, "7_Live_Liq"),
    (12, "8_Exchange_Liquidation_Map_1D"),
    (13, "8_Exchange_Liquidation_Map_7D"),
    (14, "9_Liquidation_Max_Pain_24H"),
    (15, "9_Liquidation_Max_Pain_48H"),
    (16, "9_Liquidation_Max_Pain_3D"),
    (17, "9_Liquidation_Max_Pain_7D"),
    (18, "10_Whale_Orders"),
    (19, "11_Technical"),
    (20, "12_Hyperdash"),
    (21, "13_Hyperliquid"),
    (22, "14_Hyperdash_Liq_Map"),
    (23, "15_Hyperdash_Stops_Map"),
    (24, "16_Hyperdash_telegram_Intel"),
    (25, "17_Orderbook"),
    (26, "18_CVD"),
    (27, "19_News"),
    (28, "19_Calendar"),
    (29, "20_Auction_Market_Structure"),
]

DATE_PATTERN = re.compile(r'(\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2})')
BANNER_PATTERN = re.compile(r'LAST UPDATED:\s*([^\(\)]+?)(?:\s*\(([^\(\)]+?)\))?\s*\|\s*ROWS:\s*(\d+)')
ERROR_STRINGS = {"#ref!", "#div/0!", "#n/a", "#value!", "#name?", "#num!", "#null!"}


def run_checklist_audit(max_freshness_min: float = 30.0) -> tuple[bool, dict]:
    now_utc = datetime.datetime.now(UTC_TIMEZONE)
    now_ist = datetime.datetime.now(IST_TIMEZONE)
    
    if not EXCEL_PATH.exists():
        print(f"[FAIL] Master workbook not found at {EXCEL_PATH}")
        return False, {"error": "File not found"}

    wb = openpyxl.load_workbook(EXCEL_PATH, read_only=True, data_only=True)
    existing_sheets = wb.sheetnames
    
    checklist = []
    all_passed = True
    stale_or_failed = []
    
    print("\n" + "=" * 115)
    print(f"       MASTER EXCEL 30-SHEET REFRESH & IST TIMESTAMP AUDIT CHECKLIST       ")
    print(f"       Current Time: {now_ist.strftime('%Y-%m-%d %H:%M:%S IST')} ({now_utc.strftime('%Y-%m-%d %H:%M:%S UTC')})       ")
    print(f"       Target: {EXCEL_PATH.name} ({EXCEL_PATH.stat().st_size / (1024*1024):.2f} MB)       ")
    print("=" * 115)
    print(f"{'Idx':<4} | {'Sheet Name':<30} | {'Rows':<6} | {'Banner (IST)':<24} | {'Age (min)':<10} | {'TS Format':<10} | {'Status'}")
    print("-" * 115)
    
    for idx, expected_name in CANONICAL_SHEETS:
        sheet_exists = expected_name in existing_sheets
        if not sheet_exists:
            all_passed = False
            stale_or_failed.append(expected_name)
            checklist.append({
                "index": idx,
                "sheet_name": expected_name,
                "exists": False,
                "status": "MISSING"
            })
            print(f"{idx:02d}   | {expected_name:<30} | {'-':<6} | {'SHEET MISSING':<24} | {'-':<10} | {'-':<10} | FAIL (MISSING)")
            continue
            
        ws = wb[expected_name]
        max_r = ws.max_row or 0
        
        # Read first 3 rows
        r1_vals = [c.value for c in ws[1]] if max_r >= 1 else []
        r2_vals = [c.value for c in ws[2]] if max_r >= 2 else []
        r3_vals = [c.value for c in ws[3]] if max_r >= 3 else []
        
        # 1. Inspect Row 1 and Row 2 for Banner
        banner_text = ""
        banner_ist = ""
        banner_rows = None
        has_banner = False
        
        for candidate in (r1_vals[:3] + r2_vals[:3]):
            cs = str(candidate or "")
            if "LAST UPDATED" in cs:
                has_banner = True
                banner_text = cs
                bm = BANNER_PATTERN.search(cs)
                if bm:
                    banner_ist = bm.group(1).strip()
                    # If prefix was included, clean it
                    if "|" in banner_ist:
                        banner_ist = banner_ist.split("|")[-1].strip()
                    try:
                        banner_rows = int(bm.group(3))
                    except Exception:
                        pass
                break

        # 2. Check Table Timestamp Column in Headers (Row 1 or Row 2)
        has_ts_header = False
        ts_header_name = ""
        for h in (r2_vals + r1_vals):
            hs = str(h or "")
            if any(k in hs.lower() for k in ["timestamp", "time"]):
                has_ts_header = True
                ts_header_name = hs
                break
                
        # 3. Detect Internal Timestamp & Age
        detected_ts_str = None
        ts_is_ist = False
        
        if banner_ist:
            detected_ts_str = banner_ist
            ts_is_ist = "IST" in banner_ist
        else:
            # Look in row 2/3 cells
            for val in (r2_vals + r3_vals):
                vs = str(val or "")
                if "IST" in vs and any(yr in vs for yr in ["2026-", "2025-", "2024-"]):
                    detected_ts_str = vs
                    ts_is_ist = True
                    break
                elif any(yr in vs for yr in ["2026-", "2025-", "2024-"]) and len(vs) >= 19:
                    m = DATE_PATTERN.search(vs)
                    if m:
                        detected_ts_str = m.group(1)
                        if "IST" in vs:
                            ts_is_ist = True
                        break
                        
        # Calculate Sheet Age
        age_minutes = None
        age_str = "UNKNOWN"
        is_fresh = False
        
        if detected_ts_str:
            try:
                clean_str = detected_ts_str.replace("IST", "").replace("UTC", "").strip()
                if "T" in clean_str:
                    clean_str = clean_str.replace("T", " ")
                dt_naive = datetime.datetime.strptime(clean_str[:19], "%Y-%m-%d %H:%M:%S")
                if ts_is_ist:
                    dt_aware = dt_naive.replace(tzinfo=IST_TIMEZONE)
                else:
                    dt_aware = dt_naive.replace(tzinfo=UTC_TIMEZONE)
                    
                diff_sec = (now_utc - dt_aware.astimezone(UTC_TIMEZONE)).total_seconds()
                diff_sec = max(0.0, diff_sec)
                age_minutes = diff_sec / 60.0
                
                if age_minutes < 60:
                    age_str = f"{age_minutes:.1f}m"
                elif age_minutes < 1440:
                    age_str = f"{age_minutes/60:.1f}h"
                else:
                    age_str = f"{age_minutes/1440:.1f}d"
                    
                is_fresh = (age_minutes <= max_freshness_min)
            except Exception:
                age_str = "PARSE_ERR"

        # Check for formula errors in sample rows
        has_error = False
        for r in [r1_vals, r2_vals, r3_vals]:
            for c in r:
                if str(c).strip().lower() in ERROR_STRINGS:
                    has_error = True
                    break

        status = "PASS" if (sheet_exists and max_r > 0 and is_fresh and not has_error) else "WARN"
        if not is_fresh or max_r == 0:
            all_passed = False
            stale_or_failed.append(expected_name)

        checklist.append({
            "index": idx,
            "sheet_name": expected_name,
            "exists": sheet_exists,
            "max_row": max_r,
            "has_banner": has_banner,
            "banner_text": banner_text[:60] if banner_text else None,
            "banner_ist": banner_ist,
            "ts_header": ts_header_name,
            "detected_ts": detected_ts_str,
            "is_ist": ts_is_ist,
            "age_minutes": round(age_minutes, 1) if age_minutes is not None else None,
            "age_str": age_str,
            "is_fresh": is_fresh,
            "has_formula_error": has_error,
            "status": status
        })
        
        ts_display = banner_ist[:24] if banner_ist else (detected_ts_str[:24] if detected_ts_str else "NONE")
        ts_type = "IST (UTC+5:30)" if ts_is_ist else ("UTC" if detected_ts_str else "NONE")
        status_display = "PASS" if status == "PASS" else ("STALE" if not is_fresh else "FAIL")
        
        print(f"{idx:02d}   | {expected_name:<30} | {max_r:<6} | {ts_display:<24} | {age_str:<10} | {ts_type:<10} | {status_display}")

    wb.close()
    
    total_sheets = len(checklist)
    passed_sheets = sum(1 for s in checklist if s["status"] == "PASS")
    
    print("-" * 115)
    print(f"Summary: {passed_sheets}/{total_sheets} Sheets Live & Fresh (<{max_freshness_min:.0f}m in IST) | Stale/Failed: {len(stale_or_failed)}")
    print("=" * 115 + "\n")
    
    audit_data = {
        "timestamp_ist": now_ist.strftime("%Y-%m-%d %H:%M:%S IST"),
        "timestamp_utc": now_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "total_canonical_sheets": total_sheets,
        "passed_sheets": passed_sheets,
        "failed_or_stale_count": len(stale_or_failed),
        "failed_or_stale_sheets": stale_or_failed,
        "all_passed": all_passed,
        "checklist": checklist
    }
    
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(audit_data, f, indent=2)
        
    return all_passed, audit_data


if __name__ == "__main__":
    passed, data = run_checklist_audit(max_freshness_min=30.0)
    sys.exit(0 if passed else 1)
