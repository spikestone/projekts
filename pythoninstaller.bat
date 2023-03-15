@echo off

echo Suche nach der neuesten Version von Python...
powershell -Command "$html = Invoke-WebRequest https://www.python.org/downloads/windows/; $url = ($html.Links | Where-Object href -like '*python-3.*.exe' | Select-Object -First 1).href; $url" > latest.txt

set /p latest=<latest.txt
del latest.txt

echo Herunterladen der neuesten Version von Python: %latest% ...
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%latest%', 'python-latest.exe')"

echo Installieren von Python...
start /wait python-latest.exe /quiet InstallAllUsers=1 PrependPath=1

echo Python wurde installiert!


pip install PySide6
pip install request