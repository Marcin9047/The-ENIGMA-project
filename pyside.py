from PySide2.QtWidgets import QApplication, QWidget, QPushButton
import sys

def MainApp():
    app = QApplication(sys.argv)
    window = QWidget()
    window = QPushButton("Push Me")
    window.show()
    app.exec_()

MainApp()