import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout

class LabeledLineEdit(QWidget):
    def __init__(self, label_text, parent=None):
        super().__init__(parent)
        self.label = QLabel(label_text)
        self.line_edit = QLineEdit()
        
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

    def text(self):
        return self.line_edit.text()

    def set_text(self, text):
        self.line_edit.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create an instance of the custom widget
    labeled_line_edit = LabeledLineEdit("Enter your name:")
    labeled_line_edit.set_text("John Doe")
    
    labeled_line_edit.show()
    sys.exit(app.exec())
