import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtGui import QPainter
from PySide6.QtSvg import QSvgRenderer

# Step 1: Create a custom widget for rendering SVG
class SvgRenderWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.renderer = QSvgRenderer('src/images/svc.svg')
        self.setMinimumSize(600, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.renderer.render(painter)

# Step 2: Create the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSvgRenderer Example')
        self.resize(600, 400)

        layout = QVBoxLayout()

        # Create the custom SVG render widget
        self.svg_render_widget = SvgRenderWidget()
        
        layout.addWidget(self.svg_render_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

# Step 3: Create the main application object and run the event loop
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
