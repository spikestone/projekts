import sys
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
        Button1 = QPushButton("Taschenrechner")
        Button1.clicked.connect
        self.Button2 = QPushButton("Leer")

        #grid aka wie die ganzen widgets angeordnet sind
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.textlabel1,0,0)
        layout.addWidget(Button1,1,0)
        layout.addWidget(self.Button2,2,0)



        #action bei knopfdruck
    def on_Eingabe1_click(self):
        print("helloo")
        pass

if __name__ == __name__:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

