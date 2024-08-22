import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout

# Step 1: Create the main application object
app = QApplication(sys.argv)

# Step 2: Create the main window (QWidget)
window = QWidget()
window.setWindowTitle('Signals and Slots Example')

# Step 3: Create widgets
label = QLabel('Enter your name:')
line_edit = QLineEdit()
button = QPushButton('Click Me')
message_label = QLabel('')  # Label to display a message

# Step 4: Create a layout and add widgets to it
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(line_edit)
layout.addWidget(button)
layout.addWidget(message_label)

# Step 5: Define a slot function
def on_button_click():
    name = line_edit.text()
    message_label.setText(f'Hello, {name}!')

# Step 6: Connect the button's clicked signal to the slot function
button.clicked.connect(on_button_click)

# Step 7: Set the layout for the main window
window.setLayout(layout)

# Step 8: Show the window
window.show()

# Step 9: Run the application's event loop
sys.exit(app.exec())
