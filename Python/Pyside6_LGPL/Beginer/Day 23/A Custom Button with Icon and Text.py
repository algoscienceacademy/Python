import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon

class IconButton(QPushButton):
    def __init__(self, icon_path, text):
        super().__init__(text)
        self.setIcon(QIcon(icon_path))
        self.setIconSize(self.sizeHint())

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        button = IconButton("path/to/icon.png", "Custom Button")
        layout.addWidget(button)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
