@echo off
setlocal
REM Ensure UTF-8 console output
chcp 65001 >nul 2>&1
python "%~dp0Terminal\live_data_terminal.py" %*
endlocal
