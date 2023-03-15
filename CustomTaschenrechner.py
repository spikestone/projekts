import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        #fesnter größe
        self.resize(100,100)
        #label
        self.label1 = QLabel("Taschenrechner")
        #eingabe
        self.Eingabe1 = QLineEdit()

        # layout
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.Eingabe1,1,1)
        layout.addWidget(self.label1,0,0,1,1)

if __name__ == __name__:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

