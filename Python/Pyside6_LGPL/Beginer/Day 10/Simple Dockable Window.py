import sys
from PySide6.QtGui  import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QWidget, QVBoxLayout, QLabel

# Step 1: Create the main application object
app = QApplication(sys.argv)

# Step 2: Create the main window (QMainWindow)
window = QMainWindow()
window.setWindowTitle('QDockWidget Example')
window.resize(800, 600)

# Step 3: Create a central widget and set it as the central widget of the main window
central_widget = QWidget()
layout = QVBoxLayout()
layout.addWidget(QLabel("This is the central widget"))
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

# Step 4: Create a QDockWidget
dock_widget = QDockWidget("Dockable", window)
dock_widget.setWidget(QTextEdit())

# Step 5: Add the QDockWidget to the main window
window.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)

# Step 6: Show the main window
window.show()

# Step 7: Run the application's event loop
sys.exit(app.exec())
