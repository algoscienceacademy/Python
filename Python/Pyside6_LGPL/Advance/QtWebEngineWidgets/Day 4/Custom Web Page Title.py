import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView

class CustomTitleExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Page Title Example")

        # Create QWebEngineView widget
        self.web_view = QWebEngineView()
        self.web_view.setUrl("https://www.example.com")

        # Create a QLabel to display the page title
        self.title_label = QLabel("Page Title: ")

        # Connect to the titleChanged signal
        self.web_view.titleChanged.connect(self.update_title)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        layout.addWidget(self.title_label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_title(self, title):
        self.title_label.setText(f"Page Title: {title}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomTitleExample()
    window.show()
    sys.exit(app.exec())
