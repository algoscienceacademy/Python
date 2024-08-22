import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QClipboard

class ClipboardExample(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("QClipboard Example")
        self.setGeometry(300, 300, 400, 300)

        # Create a QTextEdit widget for text input
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Type some text here...")

        # Create buttons for copy and paste
        self.copy_button = QPushButton("Copy", self)
        self.paste_button = QPushButton("Paste", self)

        # Connect buttons to their respective methods
        self.copy_button.clicked.connect(self.copy_text)
        self.paste_button.clicked.connect(self.paste_text)

        # Arrange widgets in a vertical layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.paste_button)

        # Set the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def copy_text(self):
        # Get the current text from the QTextEdit
        text = self.text_edit.toPlainText()

        # Access the system clipboard and copy the text
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

    def paste_text(self):
        # Access the system clipboard and paste the text
        clipboard = QApplication.clipboard()
        text = clipboard.text()

        # Insert the text into the QTextEdit
        self.text_edit.setPlainText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClipboardExample()
    window.show()
    sys.exit(app.exec())
