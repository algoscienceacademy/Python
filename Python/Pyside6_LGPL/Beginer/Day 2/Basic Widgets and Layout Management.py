import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout

# Step 1: Create the main application object
app = QApplication(sys.argv)

# Step 2: Create the main window (QWidget)
window = QWidget()
window.setWindowTitle('Basic Widgets Example')

# Step 3: Create widgets
label = QLabel('Enter your name:')
line_edit = QLineEdit()
button = QPushButton('Click Me')

# Step 4: Create a layout and add widgets to it
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(line_edit)
layout.addWidget(button)

# Step 5: Set the layout for the main window
window.setLayout(layout)

# Step 6: Show the window
window.show()

# Step 7: Run the application's event loop
sys.exit(app.exec())
