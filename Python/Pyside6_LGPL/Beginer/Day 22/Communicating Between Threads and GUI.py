import sys
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget

class WorkerThread(QThread):
    result_signal = Signal(int)

    def run(self):
        result = 0
        for i in range(10):
            result += i
            self.sleep(1)
        self.result_signal.emit(result)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Press to start")
        self.button = QPushButton("Start Calculation")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.button.clicked.connect(self.start_thread)

    def start_thread(self):
        self.thread = WorkerThread()
        self.thread.result_signal.connect(self.show_result)
        self.thread.start()

    def show_result(self, result):
        self.label.setText(f"Result: {result}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
