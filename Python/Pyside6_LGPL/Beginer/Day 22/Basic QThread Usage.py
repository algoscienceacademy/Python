import sys
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class WorkerThread(QThread):
    update_signal = Signal(str)

    def run(self):
        for i in range(5):
            self.update_signal.emit(f"Count: {i}")
            self.sleep(1)  # Simulate a long-running task

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Starting...")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.thread = WorkerThread()
        self.thread.update_signal.connect(self.update_label)
        self.thread.start()

    def update_label(self, text):
        self.label.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
