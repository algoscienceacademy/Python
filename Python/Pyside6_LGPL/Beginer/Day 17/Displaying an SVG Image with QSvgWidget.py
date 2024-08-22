import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtSvgWidgets import QSvgWidget

# Step 1: Create the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSvgWidget Example')
        self.resize(600, 400)

        layout = QVBoxLayout()

        # Create a QSvgWidget and load an SVG file
        self.svg_widget = QSvgWidget('src/images/svc.svg')
        
        layout.addWidget(self.svg_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

# Step 2: Create the main application object and run the event loop
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
