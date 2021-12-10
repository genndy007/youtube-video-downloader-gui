# it will be starting point for Program
import sys
from PyQt5 import QtWidgets
from frontend.MainWindow import MainWindow

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()

sys.exit(app.exec())