# Tests/Test_Sheet_Socratic_Extractor.py
import pytest
from Terminal.Data_Factory.sheet_socratic_extractor import build_socratic_audit_table, get_sheet_socratic_insights

def test_socratic_insights_dictionary():
    insights = get_sheet_socratic_insights()
    assert len(insights) >= 30
    assert "00_MT5_Account_Telemetry" in insights
    assert "22_Forced_Liquidations_MTF" in insights
    assert "Can I improve trading process more with data from this excel sheet?" in insights["00_MT5_Account_Telemetry"]["question"]

def test_socratic_audit_table_generation():
    table_md, records = build_socratic_audit_table()
    assert len(records) >= 30
    assert "Index & Sheet Name" in table_md
    assert "Can I improve trading process more" in table_md

    # Check that 22_Forced_Liquidations_MTF is included
    liq_sheet = next((r for r in records if "22_Forced_Liquidations_MTF" in r["sheet_name"]), None)
    assert liq_sheet is not None
    assert "READ" in liq_sheet["status"]
