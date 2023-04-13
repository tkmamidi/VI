from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QTextBrowser,
    QFileDialog,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
    QToolBar,
    QStatusBar,
    QWidget,
)
import sys
from utils.file_dialog import select_file
from utils.page_viewer import show_page
from utils.prediction import predict
import csv
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set the title of the main window
        self.setWindowTitle("DITTO.ai")

        self.file_path = None
        self.parsed_data = {}
        self.table_header = []
        self.current_page = 0
        self.flagged_rows = set()

        # Set central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.upload_button = QPushButton("Upload csv", self)
        self.upload_button.clicked.connect(self.select_file)

        self.upload_text = QLabel(self)
        self.upload_text.setText("Upload openCravat annotated file:")

        # Add status bar
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)

        self.text = QTextBrowser(self)
        self.text.setReadOnly(True)
        self.text.setOpenExternalLinks(True)

        # Create QLineEdit widget for user input
        self.user_input_line_text = QLabel(self)
        self.user_input_line_text.setText("Notes:")
        self.user_input_line_edit = QLineEdit(self)
        self.user_input_line_edit.textChanged.connect(self.update_user_input)

        self.prev_button = QPushButton("Prev", self)
        self.prev_button.clicked.connect(self.prev_page)
        self.prev_button.setEnabled(False)

        self.next_button = QPushButton("Next", self)
        self.next_button.clicked.connect(self.next_page)
        self.next_button.setEnabled(False)

        self.flag_button = QPushButton("Flag", self)
        self.flag_button.clicked.connect(self.flag_row)
        self.flagged_rows = set()

        self.download_button = QPushButton("Download", self)
        self.download_button.clicked.connect(self.download_flagged_rows)
        self.download_button.setEnabled(False)

        # Create layout and add widgets
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.upload_text)
        top_layout.addWidget(self.upload_button)

        middle_layout = QHBoxLayout()
        middle_layout.addWidget(self.user_input_line_text)
        middle_layout.addWidget(self.user_input_line_edit)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.prev_button)
        bottom_layout.addWidget(self.next_button)
        bottom_layout.addWidget(self.flag_button)
        bottom_layout.addWidget(self.download_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.text)
        main_layout.addLayout(middle_layout)
        main_layout.addLayout(bottom_layout)

        # Set widget layout
        central_widget.setLayout(main_layout)

        # self.setGeometry(100, 100, 800, 900)

    def resizeEvent(self, event):
        # Override resizeEvent to adjust widget sizes and positions
        self.text.setGeometry(10, 60, self.width() - 20, self.height() - 70)

    def select_file(self):
        self.file_path = select_file(self)
        if self.file_path:
            self.flagged_rows.clear()
            self.download_button.setEnabled(False)
            self.predict_parse_data()

    def predict_parse_data(self):
        if self.file_path:
            df = predict(self.file_path)
            # Add new column for user input values
            df["notes"] = ""
            self.parsed_data = df.to_dict("index")
            self.current_page = 0
            show_page(
                self.parsed_data, self.current_page, self.text, self.prev_button, self.next_button
            )

    def update_user_input(self, text):
        # Get current row index
        row_idx = list(self.parsed_data.keys())[self.current_page]
        # page_data = list(self.parsed_data.values())[self.current_page]

        # Update user input value in DataFrame
        self.parsed_data[row_idx]["notes"] = text

    def prev_page(self):
        # Save current user input before navigating to next page
        self.update_user_input(self.user_input_line_edit.text())

        self.current_page -= 1
        row_idx = list(self.parsed_data.keys())[self.current_page]
        self.user_input_line_edit.setText(str(self.parsed_data[row_idx]["notes"]))
        show_page(
            self.parsed_data, self.current_page, self.text, self.prev_button, self.next_button
        )

    def next_page(self):
        # Save current user input before navigating to next page
        self.update_user_input(self.user_input_line_edit.text())

        self.current_page += 1
        row_idx = list(self.parsed_data.keys())[self.current_page]
        self.user_input_line_edit.setText(str(self.parsed_data[row_idx]["notes"]))

        show_page(
            self.parsed_data, self.current_page, self.text, self.prev_button, self.next_button
        )

    def flag_row(self):
        if self.parsed_data:
            selected_row = list(self.parsed_data.keys())[self.current_page]
            if selected_row not in self.flagged_rows:
                self.flagged_rows.add(selected_row)
            self.download_button.setEnabled(len(self.flagged_rows) > 0)

    def download_flagged_rows(self):
        if self.flagged_rows:
            file_path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "CSV files (*.csv)")
            if file_path:
                with open(file_path, "w", newline="") as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow(self.parsed_data[0])
                    for row in self.flagged_rows:
                        csv_writer.writerow(self.parsed_data[row].values())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 800, 640)
    window.show()
    sys.exit(app.exec_())
