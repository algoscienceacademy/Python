import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer, Qt

# Step 1: Create the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTimer Example')
        self.resize(300, 200)

        layout = QVBoxLayout()

        # Create a QLabel to display the timer's elapsed time
        self.label = QLabel("Elapsed Time: 0 seconds")
        layout.addWidget(self.label)

        # Create a QTimer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Timer interval in milliseconds (1000 ms = 1 second)

        self.elapsed_time = 0

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_time(self):
        self.elapsed_time += 1
        self.label.setText(f"Elapsed Time: {self.elapsed_time} seconds")

# Step 2: Create the main application object and run the event loop
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
