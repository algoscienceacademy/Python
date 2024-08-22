import sys
from PySide6.QtWidgets import QApplication, QSlider, QLabel, QHBoxLayout, QWidget, QVBoxLayout
from PySide6.QtCore import Qt

class LabeledSlider(QWidget):
    def __init__(self):
        super().__init__()
        self.slider = QSlider(Qt.Horizontal)
        self.label = QLabel("0")
        self.slider.valueChanged.connect(self.update_label)
        
        layout = QHBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def update_label(self, value):
        self.label.setText(str(value))

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        labeled_slider = LabeledSlider()
        layout.addWidget(labeled_slider)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
