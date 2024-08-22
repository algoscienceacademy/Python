import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView

class BasicWebView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic WebView Example")

        # Create a QWebEngineView widget
        self.web_view = QWebEngineView()
        self.web_view.setUrl("https://www.example.com")

        self.setCentralWidget(self.web_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BasicWebView()
    window.show()
    sys.exit(app.exec())
