@echo off
net session >nul 2>&1
if %errorlevel% == 0 (
    echo Success: Administrative permissions confirmed.
    python your_script.py
) else (
    echo Failure: This script must be run as an administrator.
    pause >nul
    exit /b %errorlevel%
)