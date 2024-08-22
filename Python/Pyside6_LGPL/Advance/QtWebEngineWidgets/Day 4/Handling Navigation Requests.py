import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView

class NavigationExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Navigation Example")

        # Create QWebEngineView widget
        self.web_view = QWebEngineView()
        self.web_view.setUrl("https://www.example.com")

        # Create UI elements
        self.back_button = QPushButton("Back")
        self.forward_button = QPushButton("Forward")

        self.back_button.clicked.connect(self.web_view.back)
        self.forward_button.clicked.connect(self.web_view.forward)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        layout.addWidget(self.back_button)
        layout.addWidget(self.forward_button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NavigationExample()
    window.show()
    sys.exit(app.exec())
