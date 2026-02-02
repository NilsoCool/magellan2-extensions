@echo off
chcp 65001 > nul
setlocal

:: Check for Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python to use this tool: https://www.python.org/downloads/
    pause
    exit /b
)

:: Run the script
python auto_merge.py
