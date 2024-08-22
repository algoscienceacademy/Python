import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsRectItem, QVBoxLayout, QWidget
from PySide6.QtGui import QBrush, QPen, QPainter
from PySide6.QtCore import QRectF, Qt

# Step 1: Create the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Graphics View Example')
        self.resize(600, 400)

        layout = QVBoxLayout()

        # Create a QGraphicsScene
        scene = QGraphicsScene()
        scene.setSceneRect(QRectF(0, 0, 800, 600))

        # Add some graphical items to the scene
        ellipse = QGraphicsEllipseItem(0, 0, 100, 100)
        ellipse.setBrush(QBrush(Qt.red))
        ellipse.setPen(QPen(Qt.black))
        ellipse.setPos(50, 50)
        scene.addItem(ellipse)

        rect = QGraphicsRectItem(0, 0, 150, 150)
        rect.setBrush(QBrush(Qt.blue))
        rect.setPen(QPen(Qt.black))
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

# Step 2: Create the main application object and run the event loop
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
