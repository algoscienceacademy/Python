import sys
from PySide6.QtWidgets import QApplication, QWidget

# Step 1: Create an application object
app = QApplication(sys.argv)

# Step 2: Create a main window
window = QWidget()
window.setWindowTitle('My First PySide6 Application')
window.setGeometry(100, 100, 600, 400)  # x, y, width, height

# Step 3: Show the window
window.show()

# Step 4: Run the application's event loop
sys.exit(app.exec())
