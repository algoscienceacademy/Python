import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar, QLabel, QPushButton, QVBoxLayout, QWidget

# Step 1: Create the main application object
app = QApplication(sys.argv)

# Step 2: Create the main window (QMainWindow)
window = QMainWindow()
window.setWindowTitle('Status Bar Interaction Example')
window.resize(600, 400)

# Step 3: Create a central widget and layout
central_widget = QWidget()
layout = QVBoxLayout()
central_widget.setLayout(layout)

# Step 4: Create a status bar and set it to the main window
status_bar = QStatusBar()
window.setStatusBar(status_bar)

# Step 5: Create a label for the status bar
status_label = QLabel("Ready")
status_bar.addWidget(status_label)

# Step 6: Create buttons that will update the status bar
button_1 = QPushButton('Start Process')
button_2 = QPushButton('Stop Process')

# Step 7: Define functions to update the status bar based on button clicks
def start_process():
    status_label.setText("Process started...")

def stop_process():
    status_label.setText("Process stopped.")

# Step 8: Connect the buttons to the functions
button_1.clicked.connect(start_process)
button_2.clicked.connect(stop_process)

# Step 9: Add buttons to the layout
layout.addWidget(button_1)
layout.addWidget(button_2)

# Step 10: Set the central widget of the main window
window.setCentralWidget(central_widget)

# Step 11: Show the main window
window.show()

# Step 12: Run the application's event loop
sys.exit(app.exec())
