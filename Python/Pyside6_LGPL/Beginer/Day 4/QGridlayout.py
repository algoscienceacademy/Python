import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout

# Step 1: Create the main application object
app = QApplication(sys.argv)

# Step 2: Create the main window (QWidget)
window = QWidget()
window.setWindowTitle('Grid Layout Example')

# Step 3: Create widgets
name_label = QLabel('Name:')
name_edit = QLineEdit()

email_label = QLabel('Email:')
email_edit = QLineEdit()

submit_button = QPushButton('Submit')

# Step 4: Create a grid layout and add widgets to specific rows and columns
layout = QGridLayout()
layout.addWidget(name_label, 0, 0)    # Row 0, Column 0
layout.addWidget(name_edit, 0, 1)     # Row 0, Column 1
layout.addWidget(email_label, 1, 0)   # Row 1, Column 0
layout.addWidget(email_edit, 1, 1)    # Row 1, Column 1
layout.addWidget(submit_button, 2, 0, 1, 2)  # Row 2, spanning 2 columns

# Step 5: Set the layout for the main window
window.setLayout(layout)

# Step 6: Show the window
window.show()

# Step 7: Run the application's event loop
sys.exit(app.exec())
