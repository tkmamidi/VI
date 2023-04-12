from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit
import sys
from utils.file_dialog import select_file
from utils.data_parser import parse_data
from utils.page_viewer import show_page, prev_page, next_page


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.file_path = None
        self.parsed_data = {}
        self.table_header = []
        self.current_page = 0

        self.upload_button = QPushButton("Upload", self)
        self.upload_button.setGeometry(10, 10, 80, 30)
        self.upload_button.clicked.connect(self.select_file)

        self.text = QTextEdit(self)
        self.text.setGeometry(10, 50, 780, 540)
        self.text.setReadOnly(True)

        self.prev_button = QPushButton("Prev", self)
        self.prev_button.setGeometry(10, 600, 80, 30)
        self.prev_button.clicked.connect(self.prev_page)
        self.prev_button.setEnabled(False)

        self.next_button = QPushButton("Next", self)
        self.next_button.setGeometry(110, 600, 80, 30)
        self.next_button.clicked.connect(self.next_page)
        self.next_button.setEnabled(False)

    def select_file(self):
        self.file_path = select_file(self)
        if self.file_path:
            self.parse_data()

    def parse_data(self):
        if self.file_path:
            self.parsed_data, self.table_header = parse_data(self.file_path)
            self.current_page = 0
            show_page(
                self.parsed_data, self.current_page, self.text, self.prev_button, self.next_button
            )

    def prev_page(self):
        self.current_page -= 1
        prev_page(
            self.parsed_data, self.current_page, self.text, self.prev_button, self.next_button
        )

    def next_page(self):
        self.current_page += 1
        next_page(
            self.parsed_data, self.current_page, self.text, self.prev_button, self.next_button
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 800, 640)
    window.show()
    sys.exit(app.exec_())
