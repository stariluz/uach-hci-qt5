from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow()
main_window.setWindowTitle('Hello Qt6 with Poetry')
main_window.show()
sys.exit(app.exec())
