# it will be starting point for Program
import sys
from PyQt5 import QtWidgets
from frontend.MainWindow import MainWindow

icon_path = 'static/logo.png'

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow(icon_path)
main_window.show()

sys.exit(app.exec())