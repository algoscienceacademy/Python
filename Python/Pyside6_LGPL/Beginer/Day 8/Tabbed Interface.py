import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

# Step 1: Create the main application object
app = QApplication(sys.argv)

# Step 2: Create the main window (QMainWindow)
window = QMainWindow()
window.setWindowTitle('QTabWidget Example')
window.resize(600, 400)

# Step 3: Create a QTabWidget and set it as the central widget
tab_widget = QTabWidget()
window.setCentralWidget(tab_widget)

# Step 4: Create the first tab
tab1 = QWidget()
layout1 = QVBoxLayout()
layout1.addWidget(QLabel("This is the content of Tab 1"))
tab1.setLayout(layout1)

# Step 5: Create the second tab
tab2 = QWidget()
layout2 = QVBoxLayout()
layout2.addWidget(QLabel("This is the content of Tab 2"))
tab2.setLayout(layout2)

# Step 6: Create the third tab
tab3 = QWidget()
layout3 = QVBoxLayout()
layout3.addWidget(QLabel("This is the content of Tab 3"))
tab3.setLayout(layout3)

# Step 7: Add tabs to the QTabWidget
tab_widget.addTab(tab1, "Tab 1")
tab_widget.addTab(tab2, "Tab 2")
tab_widget.addTab(tab3, "Tab 3")

# Step 8: Show the main window
window.show()

# Step 9: Run the application's event loop
sys.exit(app.exec())
