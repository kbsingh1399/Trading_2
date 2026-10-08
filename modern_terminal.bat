@echo off
setlocal
REM Ensure UTF-8 console output for rich unicode rendering
chcp 65001 >nul 2>&1
python "%~dp0Terminal\modern_terminal.py" %*
endlocal
