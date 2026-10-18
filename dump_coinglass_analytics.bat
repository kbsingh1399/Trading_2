@echo off
chcp 65001 >nul
echo ==============================================================================
echo CoinGlass Institutional Deep Excel Analytics Pipeline
echo Target: Data/DataBase_Trading.xlsx
echo ==============================================================================
python -u Terminal/Data_Factory/coinglass_deep_excel_dumper.py %*
echo.
echo Pipeline execution finished. Press any key to close.
pause >nul
