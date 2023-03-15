import sys
import subprocess
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        #name des Fensters
        self.setWindowTitle("Programm Hub")
        #labels
        self.textlabel1 = QLabel("Costum Programme")
        #Knöpfe zum drücken
        self.Button1 = QPushButton("Taschenrechner")
        self.Button1.clicked.connect(self.on_button_click)
        self.Button2 = QPushButton("Leer")

        #grid aka wie die ganzen widgets angeordnet sind
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.textlabel1,0,0)
        layout.addWidget(self.Button1,1,0)
        layout.addWidget(self.Button2,2,0)



    #action bei knopfdruck
    def on_button_click(self):
        subprocess.call(["python3", "CustomTaschenrechner.py"])

if __name__ == __name__:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

