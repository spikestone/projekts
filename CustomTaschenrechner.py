import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        #label
        self.label1 = QLabel()
        self.label1.setStyleSheet("border: 2px solid black;")
        self.label2 = QLabel("helo")
        self.label2.setStyleSheet("border: 2px solid black;")
        #eingabe
        self.Eingabe1 = QLineEdit()
        self.Eingabe2 = QLineEdit()


        # layout
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.label1,1,2)
        layout.addWidget(self.Eingabe1,1,1)
        layout.addWidget(self.Eingabe2,1,3)
        layout.addWidget(self.label2,2,1,1,3)



if __name__ == __name__:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

