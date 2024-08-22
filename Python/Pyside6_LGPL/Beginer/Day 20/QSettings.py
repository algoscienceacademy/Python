import sys
from PySide6.QtCore import QSettings, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class SettingsExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = QSettings('YourCompany', 'YourApp')
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QSettings Example")
        
        # Retrieve the stored window position and size
        self.restoreGeometry(self.settings.value("geometry", b''))
        
        button_save = QPushButton("Save Settings")
        button_save.clicked.connect(self.save_settings)
        
        button_load = QPushButton("Load Settings")
        button_load.clicked.connect(self.load_settings)
        
        layout = QVBoxLayout()
        layout.addWidget(button_save)
        layout.addWidget(button_load)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
    def save_settings(self):
        # Save window position and size
        self.settings.setValue("geometry", self.saveGeometry())
        
    def load_settings(self):
        # Retrieve and apply the saved window position and size
        self.restoreGeometry(self.settings.value("geometry", b''))

    def closeEvent(self, event):
        # Save settings when the application is closed
        self.save_settings()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SettingsExample()
    window.show()
    sys.exit(app.exec())
