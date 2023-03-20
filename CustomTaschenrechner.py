import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MainWindow(QWidget):
    def __init__(self):

        super().__init__()

        #styles
        schlank = "border: 1px solid black;"
        breit = "border: 2px solid black;"
        #label
        self.label1 = QLabel()
        self.label1.setStyleSheet(schlank)
        self.label2 = QLabel()
        self.label2.setStyleSheet("border: 2px solid black;")
        #eingabe
        self.Eingabe1 = QLineEdit()
        self.Eingabe1.setStyleSheet(schlank)
        self.Eingabe1.setValidator(QDoubleValidator())
        self.Eingabe2 = QLineEdit()
        self.Eingabe2.setStyleSheet(schlank)
        self.Eingabe2.setValidator(QDoubleValidator())
        #Knoepfe
        self.Plusbutton = QPushButton("Plus +")
        self.Plusbutton.clicked.connect(self.on_Plus_clicked)
        self.Minusbutton = QPushButton("Minus -")
        self.Minusbutton.clicked.connect(self.on_Minus_clicked)
        self.Malbutton = QPushButton("Mal *")
        self.Malbutton.clicked.connect(self.on_Mal_clicked)
        self.Geteiltbutton = QPushButton("Geteilt /")
        self.Geteiltbutton.clicked.connect(self.on_Geteilt_clicked)


        # layout
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.label1,1,2)
        layout.addWidget(self.Eingabe1,1,1)
        layout.addWidget(self.Eingabe2,1,3)
        layout.addWidget(self.label2,2,1,1,3)
        layout.addWidget(self.Plusbutton, 3, 1)
        layout.addWidget(self.Minusbutton,3,2)
        layout.addWidget(self.Malbutton,3,3)
        layout.addWidget(self.Geteiltbutton,4,1)
    def on_Plus_clicked(self):
        self.label1.setText("+")
        input1_text = self.Eingabe1.text()
        try:
            input_number1 = int(input1_text)
        except ValueError:
            input_number1 = float(input1_text)
        input2_text = self.Eingabe2.text()
        try:
            input_number2 = int(input2_text)
        except ValueError:
            input_number2 = float(input2_text)
        result = input_number1 + input_number2
        self.label2.setText(f'Das Ergebnis ist: {result}')
    def on_Minus_clicked(self):
        self.label1.setText("-")
        input1_text = self.Eingabe1.text()
        try:
            input_number1 = int(input1_text)
        except ValueError:
            input_number1 = float(input1_text)
        input2_text = self.Eingabe2.text()
        try:
            input_number2 = int(input2_text)
        except ValueError:
            input_number2 = float(input2_text)
        result = input_number1 - input_number2
        self.label2.setText(f'Das Ergebnis ist: {result}')
    def on_Mal_clicked(self):
        self.label1.setText("*")
        input1_text = self.Eingabe1.text()
        try:
            input_number1 = int(input1_text)
        except ValueError:
            input_number1 = float(input1_text)
        input2_text = self.Eingabe2.text()
        try:
            input_number2 = int(input2_text)
        except ValueError:
            input_number2 = float(input2_text)
        result = input_number1 * input_number2
        self.label2.setText(f'Das Ergebnis ist: {result}')
    def on_Geteilt_clicked(self):
        self.label1.setText("/")
        input1_text = self.Eingabe1.text()
        try:
            input_number1 = int(input1_text)
        except ValueError:
            input_number1 = float(input1_text)
        input2_text = self.Eingabe2.text()
        try:
            input_number2 = int(input2_text)
        except ValueError:
            input_number2 = float(input2_text)
        result = input_number1 / input_number2
        self.label2.setText(f'Das Ergebnis ist: {result}')

if __name__ == __name__:
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

