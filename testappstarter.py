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



# Setze die URL des GitHub-Repositorys und den Namen des Skripts
repo_url = 'https://github.com/spikestone/projekts'
script_name = 'testapp.py'

# Erstelle den vollständigen Download-URL des Skripts
download_url = f'{repo_url}/raw/master/{script_name}'

# Lade den Inhalt des Skripts vom GitHub-Repository herunter
response = requests.get(download_url)
new_script_content = response.text

# Erstelle einen Hash des neuen Skriptinhalts
new_script_hash = hashlib.md5(new_script_content.encode()).hexdigest()

# Prüfe, ob das lokale Skript aktualisiert werden muss
if os.path.exists(script_name):
    with open(script_name, 'r') as f:
        current_script_content = f.read()
    current_script_hash = hashlib.md5(current_script_content.encode()).hexdigest()
    if current_script_hash == new_script_hash:
        print('Das lokale Skript ist auf dem neuesten Stand.')
        exit()
    else:
        print('Es gibt eine neue Version des Skripts. Das lokale Skript wird aktualisiert.')
else:
    print('Das lokale Skript wurde nicht gefunden. Es wird heruntergeladen.')

# Speichere den Inhalt des neuen Skripts in einer temporären Datei
temp_script_name = f'{script_name}.temp'
with open(temp_script_name, 'w') as f:
    f.write(new_script_content)

# Ersetze das lokale Skript durch das neue Skript
os.replace(temp_script_name, script_name)

# Gib eine Meldung aus, dass das Skript aktualisiert wurde
print('Das Skript wurde aktualisiert.')
