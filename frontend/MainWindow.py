from PyQt5.QtWidgets import (
    QMainWindow, QLineEdit, QLabel, QPushButton, QWidget,
    QGridLayout, QFileDialog
)
from backend.Downloader import download_video, download_audio



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # Window settings
        self.setMinimumSize(400, 200)
        self.setWindowTitle("Downloader from YouTube")
        # Creating layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)
        # Line 1
        self.prompt_text = QLabel(self)
        self.prompt_text.setText('Please paste your link:')

        self.url_prompt = QLineEdit(self)
        # Line 2
        self.directory_text = QLineEdit(self)

        self.choose_directory_button = QPushButton('Choose directory...', self)
        self.choose_directory_button.clicked.connect(self.choose_directory_button_action)

        # Line 3
        self.download_video_button = QPushButton('Download video', self)
        self.download_video_button.clicked.connect(self.download_video_button_action)

        self.download_audio_button = QPushButton('Download audio', self)
        self.download_audio_button.clicked.connect(self.download_audio_button_action)

        self.reset_button = QPushButton('Reset', self)
        self.reset_button.clicked.connect(self.reset_button_action)

        # Line 4
        self.result_text = QLabel(self)
        self.result_text.setText('Status: ')

        # Show line 1
        grid_layout.addWidget(self.prompt_text, 0, 0)
        grid_layout.addWidget(self.url_prompt, 0, 1)
        # Show line 2
        grid_layout.addWidget(self.directory_text, 1, 0)
        grid_layout.addWidget(self.choose_directory_button, 1, 1)
        # Show line 3
        grid_layout.addWidget(self.reset_button, 2, 0)
        grid_layout.addWidget(self.result_text, 2, 1)
        # Show line 4
        grid_layout.addWidget(self.download_video_button, 3, 0)
        grid_layout.addWidget(self.download_audio_button, 3, 1)





    def choose_directory_button_action(self):
        directory = QFileDialog.getExistingDirectory(self, 'Choose directory', '/home')
        self.directory_text.setText(directory)


    def download_video_button_action(self):
        # there could be some calling backend
        directory = self.directory_text.text()
        url = self.url_prompt.text()
        result = download_video(url, directory=directory)
        self.result_text.setText('Status: Downloaded')


    def download_audio_button_action(self):
        directory = self.directory_text.text()
        url = self.url_prompt.text()
        result = download_audio(url, directory)
        self.result_text.setText('Status: Downloaded')

    def reset_button_action(self):
        self.url_prompt.setText('')
        self.directory_text.setText('')
        self.result_text.setText('Status: ')



