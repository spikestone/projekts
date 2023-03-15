@echo off

python --version >nul 2>&1
if %errorlevel% NEQ 0 (
    echo Python is not installed on this system.
    python
) else (
    echo Python is installed on this system.
)

python3 -m pip install PySide6
python -m pip install requests
python3 testappstarter.py
