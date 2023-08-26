from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QFileDialog
)
from PySide6.QtCore import QUrl

from gui import Ui_MainWindow
from downloader import QDownloader

import os

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setFixedSize(self.size())

        self.set_buttons()
        self.downloader = QDownloader()
        self.downloader.progress.connect(self.update_progress_bar)
        self.downloader.finished.connect(self.download_finished)
        self.downloader.speed.connect(self.update_speed)
        self.downloader.elapsed.connect(self.time_passed)
        self.downloader.error_occured.connect(self.handle_error)

        self.ui.download_btn.clicked.connect(self.start_download)
        self.ui.stop_btn.clicked.connect(self.stop_download)
        self.ui.file_path_browse_btn.clicked.connect(self.browse_file_path)
        self.ui.download_url_line.textChanged.connect(self.set_file_path)
        
    def set_buttons(self, downloading: bool = False):
        self.ui.stop_btn.setEnabled(downloading)
        self.ui.resume_btn.setEnabled(downloading)
        self.ui.download_btn.setEnabled(not downloading)
        self.ui.download_url_line.setEnabled(not downloading)
        self.ui.file_path_line.setEnabled(not downloading)
        self.ui.file_path_browse_btn.setEnabled(not downloading)

    def time_passed(self, time):
        self.ui.elapsed_label.setText(f"{time / 10e2} s")

    def update_speed(self, speed: float):
        self.ui.speed_label.setText(f"{round(speed / 10e5, 2)} MB/s")

    def handle_error(self, error: str):
        QMessageBox.critical(self, "NetworkError", error)
        self.set_buttons(downloading=False)

    def set_file_path(self):
        path = os.getcwd()
        file_name = QUrl(self.ui.download_url_line.text()).fileName()

        if path and file_name:
            self.ui.file_path_line.setText(os.path.join(path, file_name))

    def browse_file_path(self):
        current_path = QUrl(self.ui.file_path_line.text()).path()

        file_path, _ = QFileDialog.getSaveFileName(self, dir=current_path)
        if file_path:
            self.ui.file_path_line.setText(file_path)

    def start_download(self):
        url = self.ui.download_url_line.text()
        file_path = self.ui.file_path_line.text()
        
        if url and file_path:
            self.set_buttons(downloading=True)
            self.downloader.start_download(url, file_path)
        else:
            self.set_buttons(downloading=False)
            QMessageBox.critical(self, "Error", "Please set url and file path first")
            
    def stop_download(self):
        self.downloader.stop_download()
        self.set_buttons(downloading=False)

    def download_finished(self):
        self.set_buttons(downloading=False)
        QMessageBox.information(self, "Download Completed", 
            f"Downloaded file saved to {self.ui.file_path_line.text()}")
            

    def update_progress_bar(self, value):
        self.ui.download_progressbar.setValue(value)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()