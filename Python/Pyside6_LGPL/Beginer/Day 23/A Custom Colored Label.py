import sys
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor

class ColoredLabel(QLabel):
    def __init__(self, text, bg_color, text_color):
        super().__init__(text)
        self.setAlignment(Qt.AlignCenter)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(bg_color))
        palette.setColor(QPalette.WindowText, QColor(text_color))
        self.setPalette(palette)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        colored_label = ColoredLabel("Custom Colored Label", "lightblue", "red")
        layout.addWidget(colored_label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
