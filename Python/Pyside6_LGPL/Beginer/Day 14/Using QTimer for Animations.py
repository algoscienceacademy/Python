import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer, Qt, QRect
from PySide6.QtGui import QPainter, QColor

# Step 1: Create a custom widget for animation
class AnimatedWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: white;")
        self.x_pos = 0
        self.y_pos = 100
        self.direction = 1  # 1 for right, -1 for left

        # Create a QTimer for animation
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(10)  # Interval in milliseconds

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor('blue'))
        painter.drawEllipse(self.x_pos, self.y_pos, 50, 50)

    def animate(self):
        # Update the position of the animated item
        self.x_pos += 1 * self.direction
        if self.x_pos > self.width() - 50 or self.x_pos < 0:
            self.direction *= -1
        self.update()  # Trigger a repaint

# Step 2: Create the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTimer Animation Example')
        self.resize(600, 400)

        layout = QVBoxLayout()
        self.animated_widget = AnimatedWidget()
        layout.addWidget(self.animated_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

# Step 3: Create the main application object and run the event loop
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
