::@echo off
::net session >nul 2>&1
::if %errorlevel% == 0 (
::    echo Success: Administrative permissions confirmed.
::    python .\main.py
::) else (
::    echo Failure: This script must be run as an administrator.
::    pause >nul
::    exit /b %errorlevel%
::)
@echo off
:: Wait...
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Wait...
    PowerShell -Command "Start-Process '%~dpnx0' -Verb RunAs"
    exit /b
)

:: 以下是你的实际批处理命令
echo Wait...
:: 在这里添加你的实际命令
start "" python "%~dp0main.py"
exit /b
pause