import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Dialog Example")
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.create_menu()

    def create_menu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        open_action = QAction("Open with Filter", self)
        open_action.triggered.connect(self.open_file_with_filter)
        file_menu.addAction(open_action)

    def open_file_with_filter(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "Images (*.png *.jpg);;Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            with open(file_name, 'r') as file:
                self.text_edit.setPlainText(file.read())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
