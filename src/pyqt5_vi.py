from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QTextEdit
import sys
import csv


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
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "CSV files (*.csv)")
        if self.file_path:
            self.parse_data()

    def parse_data(self):
        if self.file_path:
            with open(self.file_path, "r") as f:
                self.parsed_data = {}
                csv_reader = csv.reader(f)
                self.table_header = next(csv_reader)
                cols_to_display = list(range(1, 8)) + [11, 12, 23]  # Select columns 1, 3, and 5
                for row in csv_reader:
                    selected_data = [row[i] for i in cols_to_display]
                    selected_header = [self.table_header[i] for i in cols_to_display]
                    parsed_line = {
                        selected_header[i]: selected_data[i] for i in range(len(selected_data))
                    }
                    self.parsed_data[",".join(row)] = parsed_line

            self.current_page = 0
            self.show_page()

    def show_page(self):
        self.text.clear()
        if self.parsed_data:
            page_data = list(self.parsed_data.values())[self.current_page]
            page_text = ""
            for key, value in page_data.items():
                page_text += f"<p><b>{key}: </b>{value}</p>"
            self.text.setHtml(page_text)

        self.prev_button.setEnabled(self.current_page > 0)
        self.next_button.setEnabled(self.current_page < len(self.parsed_data) - 1)

    def prev_page(self):
        self.current_page -= 1
        self.show_page()

    def next_page(self):
        self.current_page += 1
        self.show_page()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 800, 640)
    window.show()
    sys.exit(app.exec_())
