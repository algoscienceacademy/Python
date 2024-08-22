import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QHBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QWebEngineView Navigation Example')
        self.resize(800, 600)

        layout = QVBoxLayout()

        # Create QWebEngineView first
        self.web_view = QWebEngineView()
        self.web_view.setUrl('https://www.example.com')

        # Create navigation controls
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL and press Enter")
        self.url_input.returnPressed.connect(self.load_url)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.web_view.back)

        self.forward_button = QPushButton("Forward")
        self.forward_button.clicked.connect(self.web_view.forward)

        self.reload_button = QPushButton("Reload")
        self.reload_button.clicked.connect(self.web_view.reload)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self.back_button)
        nav_layout.addWidget(self.forward_button)
        nav_layout.addWidget(self.reload_button)
        nav_layout.addWidget(self.url_input)

        layout.addLayout(nav_layout)
        layout.addWidget(self.web_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_url(self):
        url = self.url_input.text()
        if url:
            self.web_view.setUrl(url)

# Create the main application object and run the event loop
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

