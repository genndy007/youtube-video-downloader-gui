from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QMainWindow, QLineEdit, QLabel, QPushButton, QWidget,
    QGridLayout, QFileDialog
)
from backend.Downloader import download_video, download_audio



class MainWindow(QMainWindow):
    def __init__(self, icon_path):
        QMainWindow.__init__(self)
        self.language = 'ru'
        # Window settings
        self.setMinimumSize(400, 200)
        self.setWindowIcon(QtGui.QIcon(icon_path))
        # Creating layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)

        self.to_russian_button = QPushButton('По-русски', self)
        self.to_russian_button.clicked.connect(self.set_russian_text)

        self.to_english_button = QPushButton('In english')
        self.to_english_button.clicked.connect(self.set_english_text)
        # Line 1
        self.prompt_text = QLabel(self)

        self.url_prompt = QLineEdit(self)
        # Line 2
        self.directory_text = QLineEdit(self)

        self.choose_directory_button = QPushButton(self)
        self.choose_directory_button.clicked.connect(self.choose_directory_button_action)

        # Line 3
        self.download_video_button = QPushButton(self)
        self.download_video_button.clicked.connect(self.download_video_button_action)

        self.download_audio_button = QPushButton(self)
        self.download_audio_button.clicked.connect(self.download_audio_button_action)

        self.reset_button = QPushButton(self)
        self.reset_button.clicked.connect(self.reset_button_action)

        # Line 4
        self.result_text = QLabel(self)

        # By default russian language
        self.set_russian_text()

        # Translation buttons
        grid_layout.addWidget(self.to_russian_button, 0, 0)
        grid_layout.addWidget(self.to_english_button, 0, 1)

        # Show line 1
        grid_layout.addWidget(self.prompt_text, 1, 0)
        grid_layout.addWidget(self.url_prompt, 1, 1)
        # Show line 2
        grid_layout.addWidget(self.directory_text, 2, 0)
        grid_layout.addWidget(self.choose_directory_button, 2, 1)
        # Show line 3
        grid_layout.addWidget(self.reset_button, 3, 0)
        grid_layout.addWidget(self.result_text, 3, 1)
        # Show line 4
        grid_layout.addWidget(self.download_video_button, 4, 0)
        grid_layout.addWidget(self.download_audio_button, 4, 1)





    def choose_directory_button_action(self):
        text = ''
        if self.language == 'ru':
            text = 'Выберите папку'
        elif self.language == 'en':
            text = 'Choose directory'
        directory = QFileDialog.getExistingDirectory(self, text, '/home')
        self.directory_text.setText(directory)


    def download_video_button_action(self):
        # there could be some calling backend
        directory = self.directory_text.text()
        url = self.url_prompt.text()
        result = download_video(url, directory=directory)
        self.finish_downloading_text()


    def download_audio_button_action(self):
        directory = self.directory_text.text()
        url = self.url_prompt.text()
        result = download_audio(url, directory)
        self.finish_downloading_text()

    def reset_button_action(self):
        self.url_prompt.setText('')
        self.directory_text.setText('')
        if self.language == 'ru':
            self.result_text.setText('Статус: ')
        elif self.language == 'en':
            self.result_text.setText('Status: ')

    def finish_downloading_text(self):
        if self.language == 'ru':
            self.result_text.setText('Статус: ЗАКАЧАНО')
        elif self.language == 'en':
            self.result_text.setText('Status: Downloaded')


    def set_english_text(self):
        self.language = 'en'
        self.setWindowTitle("Downloader from YouTube")
        self.prompt_text.setText('Please paste your link:')
        self.choose_directory_button.setText('Choose directory...')
        self.download_video_button.setText('Download video')
        self.download_audio_button.setText('Download audio')
        self.reset_button.setText('Reset status etc')
        self.result_text.setText('Status: ')

    def set_russian_text(self):
        self.language = 'ru'
        self.setWindowTitle("Загрузчик с видео с ютуба")
        self.prompt_text.setText('Пожалуйста, вставьте ссылку:')
        self.choose_directory_button.setText('Выберите папку для закачки...')
        self.download_video_button.setText('Скачать видео (mp4)')
        self.download_audio_button.setText('Скачать аудио (mp4)')
        self.reset_button.setText('Сбросить статус и прочее')
        self.result_text.setText('Статус: ')








