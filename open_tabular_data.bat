@echo off
echo ========================================================
echo   TRADING DATA VAULT - TABULAR DATABASE LAUNCHER
echo ========================================================
echo.
echo [1] Exporting latest SQLite tables to Excel workbook...
python Terminal\Data_Factory\export_db_to_excel.py
echo.
echo [2] Opening Data\trading_data_vault.xlsx in your default spreadsheet app...
start "" "Data\trading_data_vault.xlsx"
echo.
echo SQLite Database File: Data\history\time_series_index.db
echo (You can also open time_series_index.db directly in DB Browser for SQLite or DBeaver)
echo.
pause
