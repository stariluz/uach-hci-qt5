from first_screen_ui import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.label.setText("Haz clic en el botón")
        self.pushButton.setText("Presióname")
        
        # Conectamos los eventos con sus acciones
        self.pushButton.clicked.connect(self.update)

    def update(self):
        self.label.setText("¡Acabas de hacer clic en el botón!")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()