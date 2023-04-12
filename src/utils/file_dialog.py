from PyQt5.QtWidgets import QFileDialog


def select_file(window):
    file_path, _ = QFileDialog.getOpenFileName(window, "Open file", "", "CSV files (*.csv)")
    return file_path
