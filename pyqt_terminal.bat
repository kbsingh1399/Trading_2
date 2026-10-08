@echo off
setlocal
REM Ensure UTF-8 console output and launch PyQt6 Institutional Desktop Workstation
chcp 65001 >nul 2>&1
python "%~dp0Terminal\pyqt_terminal.py" %*
endlocal
