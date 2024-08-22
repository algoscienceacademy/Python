import sys

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QWidget, QVBoxLayout, QLabel

# Step 1: Create the main application object
app = QApplication(sys.argv)

# Step 2: Create the main window (QMainWindow)
window = QMainWindow()
window.setWindowTitle('Multiple QDockWidget Example')
window.resize(800, 600)

# Step 3: Create a central widget and set it as the central widget of the main window
central_widget = QWidget()
layout = QVBoxLayout()
layout.addWidget(QLabel("This is the central widget"))
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

# Step 4: Create multiple QDockWidgets
dock_widget1 = QDockWidget("Dockable 1", window)
dock_widget1.setWidget(QTextEdit())

dock_widget2 = QDockWidget("Dockable 2", window)
dock_widget2.setWidget(QTextEdit())

dock_widget3 = QDockWidget("Dockable 3", window)
dock_widget3.setWidget(QTextEdit())

# Step 5: Add QDockWidgets to different areas
window.addDockWidget(Qt.LeftDockWidgetArea, dock_widget1)
window.addDockWidget(Qt.RightDockWidgetArea, dock_widget2)
window.addDockWidget(Qt.BottomDockWidgetArea, dock_widget3)

# Step 6: Show the main window
window.show()

# Step 7: Run the application's event loop
sys.exit(app.exec())
