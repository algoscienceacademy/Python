import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout

# Step 1: Create the main application object
app = QApplication(sys.argv)

# Step 2: Create the main window (QWidget)
window = QWidget()
window.setWindowTitle('QMessageBox Example')

# Step 3: Create a button that will trigger the message box
button = QPushButton('Show Message')

# Step 4: Define a function to show a message box when the button is clicked
def show_message():
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Information")
    msg_box.setText("This is an information message.")
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    
    # Show the message box and capture the response
    response = msg_box.exec()

    # Check the response
    if response == QMessageBox.Ok:
        print("OK clicked")
    else:
        print("Cancel clicked")

# Step 5: Connect the button's clicked signal to the show_message function
button.clicked.connect(show_message)

# Step 6: Create a layout and add the button
layout = QVBoxLayout()
layout.addWidget(button)

# Step 7: Set the layout for the main window
window.setLayout(layout)

# Step 8: Show the window
window.show()

# Step 9: Run the application's event loop
sys.exit(app.exec())
