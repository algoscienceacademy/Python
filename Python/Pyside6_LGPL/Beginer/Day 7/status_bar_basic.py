import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar, QLabel

# Step 1: Create the main application object
app = QApplication(sys.argv)

# Step 2: Create the main window (QMainWindow)
window = QMainWindow()
window.setWindowTitle('Status Bar Example')
window.resize(600, 400)

# Step 3: Create a status bar and set it to the main window
status_bar = QStatusBar()
window.setStatusBar(status_bar)

# Step 4: Create a label and add it to the status bar
status_label = QLabel("Ready")
status_bar.addWidget(status_label)

# Step 5: Create a function to update the status message
def update_status(message):
    status_label.setText(message)

# Step 6: Simulate updating the status after some operations
window.statusBar().showMessage("Loading data...", 2000)  # Message for 2 seconds
window.statusBar().showMessage("Data loaded successfully", 3000)  # Message for 3 seconds

# Step 7: Show the main window
window.show()

# Step 8: Run the application's event loop
sys.exit(app.exec())
