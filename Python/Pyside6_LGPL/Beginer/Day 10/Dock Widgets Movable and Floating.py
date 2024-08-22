import sys
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QWidget, QVBoxLayout, QLabel

# Step 1: Create the main application object
app = QApplication(sys.argv)

# Step 2: Create the main window (QMainWindow)
window = QMainWindow()
window.setWindowTitle('Movable and Floating QDockWidget Example')
window.resize(800, 600)

# Step 3: Create a central widget and set it as the central widget of the main window
central_widget = QWidget()
layout = QVBoxLayout()
layout.addWidget(QLabel("This is the central widget"))
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

# Step 4: Create a QDockWidget with different features
dock_widget = QDockWidget("Movable Dock", window)
dock_widget.setWidget(QTextEdit())

# Step 5: Allow the dock widget to be floated and moved
dock_widget.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)

# Step 6: Add the QDockWidget to the main window
window.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)

# Step 7: Show the main window
window.show()

# Step 8: Run the application's event loop
sys.exit(app.exec())
