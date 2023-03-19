import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton

class App1(QWidget):
    def __init__(self):
        super().__init__()

        # Create UI elements
        label = QLabel("This is App 1")
        button = QPushButton("Click me")

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        # Set layout for the widget
        self.setLayout(layout)

class App2(QWidget):
    def __init__(self):
        super().__init__()

        # Create UI elements
        label = QLabel("This is App 2")
        button = QPushButton("Click me")

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        # Set layout for the widget
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up main window
        self.setWindowTitle("Multi-App Example")

        # Set up tab widget
        tab_widget = QTabWidget()
        self.setCentralWidget(tab_widget)

        # Add tabs to the tab widget
        app1_widget = App1()
        app2_widget = App2()
        tab_widget.addTab(app1_widget, "App 1")
        tab_widget.addTab(app2_widget, "App 2")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
