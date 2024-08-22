import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QDrag, QDropEvent, QDragEnterEvent, QDragMoveEvent, QPixmap
from PySide6.QtWidgets import QStyle

# Step 1: Create a custom draggable widget with a custom drag icon
class CustomDraggableLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        # Use QStyle to get a standard pixmap
        self.setPixmap(QPixmap(self.style().standardPixmap(QStyle.SP_MessageBoxInformation)))
        self.setStyleSheet("background-color: lightblue;")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            drag = QDrag(self)
            mime_data = QMimeData()
            mime_data.setText(self.text())
            drag.setMimeData(mime_data)
            drag.setHotSpot(event.pos())
            drag.exec(Qt.CopyAction | Qt.MoveAction)

# Step 2: Create a custom drop target widget with visual feedback
class CustomDropTargetLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAcceptDrops(True)
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: lightyellow;")

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText():
            self.setStyleSheet("background-color: lightgreen;")
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        self.setStyleSheet("background-color: lightyellow;")

    def dropEvent(self, event: QDropEvent):
        self.setText(event.mimeData().text())
        self.setStyleSheet("background-color: lightyellow;")
        event.acceptProposedAction()

# Step 3: Create the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Custom Drag and Drop Example')
        self.resize(400, 300)

        layout = QVBoxLayout()
        self.draggable_label = CustomDraggableLabel("Drag me with custom icon!")
        self.drop_target_label = CustomDropTargetLabel("Drop here with visual feedback!")

        layout.addWidget(self.draggable_label)
        layout.addWidget(self.drop_target_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

# Step 4: Create the main application object and run the event loop
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
