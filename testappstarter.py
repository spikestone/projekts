import os , sys
import requests

# URL des Skripts auf GitHub
github_url = "https://raw.githubusercontent.com/spikestone/projekts/main/testapp.py"
# Pfad zur lokalen Datei des Skripts
current_directory = os.getcwd()
local_path = current_directory + "/testapp.py"

# Überprüfen, ob die lokale Datei existiert
if os.path.isfile(local_path):
    # Herunterladen des Skripts von GitHub
    response = requests.get(github_url)
    # Vergleichen der beiden Skripte
    if response.text != open(local_path, 'r').read():
        # Wenn die Skripte unterschiedlich sind, die neue Datei herunterladen
        with open(local_path, 'w') as file:
            file.write(response.text)
        print("Das Skript wurde aktualisiert!")
    else:
        print("Das Skript ist bereits auf dem neuesten Stand!")
else:
    # Wenn die lokale Datei nicht existiert, die Datei herunterladen
    response = requests.get(github_url)
    with open(local_path, 'w') as file:
        file.write(response.text)
    print("Das Skript wurde heruntergeladen!")

import subprocess

# Name der Datei des Skripts, das ausgeführt werden soll
script_file = "testapp.py"

# Ausführen des Skripts im selben Verzeichnis wie dieses Skript
subprocess.call(["python3", script_file])
