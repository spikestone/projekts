import sys
import subprocess
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        #name des Fensters
        self.setWindowTitle("Programm Hub")
        #labels
        self.textlabel1 = QLabel("Costum Programme")
        #Knoepfe zum druecken
        self.Button1 = QPushButton("Taschenrechner")
        self.Button1.clicked.connect(self.on_button1_click)
        self.Button2 = QPushButton("in Arbeit")

        #grid aka wie die ganzen widgets angeordnet sind
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.textlabel1,0,0)
        layout.addWidget(self.Button1,1,0)
        layout.addWidget(self.Button2,2,0)



    #action bei knopfdruck
    def on_button1_click(self):
        subprocess.call(["python3", "CustomTaschenrechner.py"])

    def on_button2_click(self):
        subprocess.call(["python3", "inArbeit.py"])


if __name__ == __name__:
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

