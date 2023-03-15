@echo off

python --version >nul 2>&1
if %errorlevel% NEQ 0 (
    echo Python is not installed on this system.
    python
) else (
    echo Python is installed on this system.


)

python -c "import PySide6" >nul 2>&1
if %errorlevel% NEQ 0 (
    echo PySide6 is not installed on this system.
    python3 -m pip install PySide6
) else (
    echo PySide6 is installed on this system.
)

python -c "import requests" >nul 2>&1
if %errorlevel% NEQ 0 (
    echo requests is not installed on this system.
    python -m pip install requests
) else (
    echo requests is installed on this system.
)

start /B pythonw.exe testappstarter.py
exit
