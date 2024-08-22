import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsRectItem, QVBoxLayout, QWidget
from PySide6.QtGui import QBrush, QPen, QPainter
from PySide6.QtCore import QRectF, Qt

# Step 1: Create custom graphical items with mouse event handling
class InteractiveEllipse(QGraphicsEllipseItem):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.setBrush(QBrush(Qt.red))
        self.setPen(QPen(Qt.black))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setBrush(QBrush(Qt.green))

class InteractiveRect(QGraphicsRectItem):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.setBrush(QBrush(Qt.blue))
        self.setPen(QPen(Qt.black))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setBrush(QBrush(Qt.yellow))

# Step 2: Create the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Interactive Graphics View Example')
        self.resize(600, 400)

        layout = QVBoxLayout()

        # Create a QGraphicsScene
        scene = QGraphicsScene()
        scene.setSceneRect(QRectF(0, 0, 800, 600))

        # Add interactive graphical items to the scene
        ellipse = InteractiveEllipse(0, 0, 100, 100)
        ellipse.setPos(50, 50)
        scene.addItem(ellipse)

        rect = InteractiveRect(0, 0, 150, 150)
        rect.setPos(200, 200)
        scene.addItem(rect)

        # Create a QGraphicsView
        view = QGraphicsView(scene)
        view.setRenderHint(QPainter.Antialiasing)
        view.setRenderHint(QPainter.SmoothPixmapTransform)

        layout.addWidget(view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

# Step 3: Create the main application object and run the event loop
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
