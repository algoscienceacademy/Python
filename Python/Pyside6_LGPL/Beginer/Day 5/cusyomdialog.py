import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox

# Step 1: Create the main application object
app = QApplication(sys.argv)

# Step 2: Create the main window (QWidget)
window = QWidget()
window.setWindowTitle('QDialog Example')

# Step 3: Create a button that will trigger the custom dialog
button = QPushButton('Open Dialog')

# Step 4: Define a custom dialog class
class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Dialog")
        
        # Create widgets for the dialog
        self.label = QLabel("Enter your name:")
        self.line_edit = QLineEdit()

        # Add dialog buttons
        self.dialog_buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.dialog_buttons.accepted.connect(self.accept)
        self.dialog_buttons.rejected.connect(self.reject)
        
        # Create a layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.dialog_buttons)
        
        # Set the layout for the dialog
        self.setLayout(layout)

# Step 5: Define a function to show the custom dialog
def show_dialog():
    dialog = CustomDialog()
    if dialog.exec():
        print(f"Name entered: {dialog.line_edit.text()}")
    else:
        print("Dialog canceled")

# Step 6: Connect the button's clicked signal to the show_dialog function
button.clicked.connect(show_dialog)

# Step 7: Create a layout and add the button
layout = QVBoxLayout()
layout.addWidget(button)

# Step 8: Set the layout for the main window
window.setLayout(layout)

# Step 9: Show the window
window.show()

# Step 10: Run the application's event loop
sys.exit(app.exec())
