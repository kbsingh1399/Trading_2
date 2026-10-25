# Alias module for 22_Forced_Liquidations_MTF
import importlib

_mod = importlib.import_module("Data.Excel_Modules.22_Forced_Liquidations_MTF")
dump_forced_liquidations_to_excel = _mod.dump_forced_liquidations_to_excel
SHEET_NAME = _mod.SHEET_NAME
