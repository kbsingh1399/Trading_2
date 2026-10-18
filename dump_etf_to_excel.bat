@echo off
setlocal
cd /d "%~dp0"
echo =====================================================================
echo CoinGlass Spot ETF Excel Automation & Tabular Storage Pipeline
echo Target: Data\DataBase_Trading.xlsx
echo =====================================================================
python Terminal\Data_Factory\etf_excel_dumper.py %*
echo.
echo Process complete.
pause
