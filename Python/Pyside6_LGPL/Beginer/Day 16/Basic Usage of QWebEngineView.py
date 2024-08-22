import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView

# Step 1: Create the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QWebEngineView Example')
        self.resize(800, 600)

        layout = QVBoxLayout()

        # Create a QWebEngineView and load a URL
        self.web_view = QWebEngineView()
        self.web_view.setUrl('https://www.iiuc.software')

        layout.addWidget(self.web_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

# Step 2: Create the main application object and run the event loop
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
