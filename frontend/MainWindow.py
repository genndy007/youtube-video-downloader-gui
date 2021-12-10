from PyQt5.QtWidgets import (
    QMainWindow, QLineEdit, QLabel, QPushButton, QWidget,
    QGridLayout, QFileDialog
)
from backend.Downloader import download_video
# from .ElementsParameters import (
#     COORDS_PROMPT_URL,
#     COORDS_PROMPT_TEXT,
#     COORDS_CONFIRM_BUTTON,
#
#     SIZE_PROMPT_URL,
# )


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(200, 200)
        self.setWindowTitle("Downloader from YouTube")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)

        self.prompt_text = QLabel(self)
        self.prompt_text.setText('Please paste your link:')

        self.url_prompt = QLineEdit(self)

        self.confirm_button = QPushButton('Confirm', self)
        self.confirm_button.clicked.connect(self.confirm_button_action)

        self.choose_directory_button = QPushButton('Choose directory...', self)
        self.choose_directory_button.clicked.connect(self.choose_directory_button_action)

        self.directory_text = QLineEdit(self)

        self.result_text = QLabel(self)
        self.result_text.setText('Status: ')

        self.reset_button = QPushButton('Reset', self)
        self.reset_button.clicked.connect(self.reset_button_action)



        grid_layout.addWidget(self.prompt_text, 0, 0)
        grid_layout.addWidget(self.url_prompt, 0, 1)
        grid_layout.addWidget(self.confirm_button, 0, 2)
        grid_layout.addWidget(self.directory_text, 1, 0)
        grid_layout.addWidget(self.choose_directory_button, 1, 1)
        grid_layout.addWidget(self.reset_button, 1, 2)
        grid_layout.addWidget(self.result_text, 2, 0)


    def choose_directory_button_action(self):
        directory = QFileDialog.getExistingDirectory(self, 'Choose directory', '/home')
        self.directory_text.setText(directory)


    def confirm_button_action(self):
        # there could be some calling backend
        directory = self.directory_text.text()
        url = self.url_prompt.text()
        result = download_video(url, directory=directory)
        self.result_text.setText('Status: Downloaded')

    def reset_button_action(self):
        self.url_prompt.setText('')
        self.directory_text.setText('')
        self.result_text.setText('Status: ')



