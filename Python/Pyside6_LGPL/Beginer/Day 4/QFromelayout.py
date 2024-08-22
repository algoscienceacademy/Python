import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFormLayout

# Step 1: Create the main application object
app = QApplication(sys.argv)

# Step 2: Create the main window (QWidget)
window = QWidget()
window.setWindowTitle('Form Layout Example')

# Step 3: Create widgets
name_label = QLabel('Name:')
name_edit = QLineEdit()

email_label = QLabel('Email:')
email_edit = QLineEdit()

submit_button = QPushButton('Submit')

# Step 4: Create a form layout and add widgets
layout = QFormLayout()
layout.addRow(name_label, name_edit)
layout.addRow(email_label, email_edit)
layout.addRow(submit_button)

# Step 5: Set the layout for the main window
window.setLayout(layout)

# Step 6: Show the window
window.show()

# Step 7: Run the application's event loop
sys.exit(app.exec())
