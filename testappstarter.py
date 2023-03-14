import subprocess
import requests
import hashlib
import os
import shutil

result = subprocess.run(['pip', 'install', "PySide6"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if result.returncode == 0:
    print('Das Paket wurde erfolgreich installiert.')
else:
    print('Fehler beim Installieren des Pakets:', result.stderr.decode())


import subprocess
import os

# Setze das Git-Repository und den Pfad zum Skript
repo_url = 'https://github.com/spikestone/projekts'
script_path = 'projekts/testapp.py'

# Wechsle in das Verzeichnis, in dem sich das Skript befindet
os.chdir(os.path.dirname(script_path))

# Hole die neueste Version des Repositorys
subprocess.run(['git', 'fetch'])

# Überprüfe, ob es eine neue Version des Skripts gibt
result = subprocess.run(['git', 'rev-list', 'HEAD...origin/master', '--count'], stdout=subprocess.PIPE)
num_commits_behind = int(result.stdout.decode('utf-8').strip())
if num_commits_behind == 0:
    print('Das Skript ist auf dem neuesten Stand.')
    exit()

# Lade die neueste Version des Skripts herunter
subprocess.run(['git', 'pull'])

# Gib eine Meldung aus, dass das Skript aktualisiert wurde
print('Das Skript wurde aktualisiert.')
