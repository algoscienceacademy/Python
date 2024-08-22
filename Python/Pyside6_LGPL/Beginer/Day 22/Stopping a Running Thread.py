import sys
from PySide6.QtCore import QThread, Signal, QMutex, QWaitCondition,QMutexLocker
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget

class WorkerThread(QThread):
    update_signal = Signal(str)
    stop_signal = Signal()

    def __init__(self):
        super().__init__()
        self.mutex = QMutex()
        self._is_running = True

    def run(self):
        count = 0
        while self._is_running:
            with QMutexLocker(self.mutex):
                count += 1
                self.update_signal.emit(f"Working... {count}")
                self.sleep(1)

    def stop(self):
        with QMutexLocker(self.mutex):
            self._is_running = False

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Press to start")
        self.start_button = QPushButton("Start Thread")
        self.stop_button = QPushButton("Stop Thread")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)

        self.start_button.clicked.connect(self.start_thread)
        self.stop_button.clicked.connect(self.stop_thread)

    def start_thread(self):
        self.thread = WorkerThread()
        self.thread.update_signal.connect(self.update_label)
        self.thread.start()

    def stop_thread(self):
        self.thread.stop()

    def update_label(self, text):
        self.label.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
