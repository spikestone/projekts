import subprocess

result = subprocess.run(['pip', 'install', "PySide6"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if result.returncode == 0:
    print('Das Paket wurde erfolgreich installiert.')
else:
    print('Fehler beim Installieren des Pakets:', result.stderr.decode())
