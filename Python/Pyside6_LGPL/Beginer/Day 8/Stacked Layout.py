import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout

# Step 1: Create the main application object
app = QApplication(sys.argv)

# Step 2: Create the main window (QMainWindow)
window = QMainWindow()
window.setWindowTitle('QStackedWidget Example')
window.resize(600, 400)

# Step 3: Create a QStackedWidget and set it as the central widget
stacked_widget = QStackedWidget()
window.setCentralWidget(stacked_widget)

# Step 4: Create the first page
page1 = QWidget()
layout1 = QVBoxLayout()
layout1.addWidget(QLabel("This is Page 1"))
page1.setLayout(layout1)

# Step 5: Create the second page
page2 = QWidget()
layout2 = QVBoxLayout()
layout2.addWidget(QLabel("This is Page 2"))
page2.setLayout(layout2)

# Step 6: Create the third page
page3 = QWidget()
layout3 = QVBoxLayout()
layout3.addWidget(QLabel("This is Page 3"))
page3.setLayout(layout3)

# Step 7: Add pages to the QStackedWidget
stacked_widget.addWidget(page1)
stacked_widget.addWidget(page2)
stacked_widget.addWidget(page3)

# Step 8: Create a layout with buttons to switch between pages
button_layout = QHBoxLayout()
button1 = QPushButton("Page 1")
button2 = QPushButton("Page 2")
button3 = QPushButton("Page 3")

# Step 9: Define functions to change the displayed page
def show_page1():
    stacked_widget.setCurrentIndex(0)

def show_page2():
    stacked_widget.setCurrentIndex(1)

def show_page3():
    stacked_widget.setCurrentIndex(2)

# Step 10: Connect the buttons to the functions
button1.clicked.connect(show_page1)
button2.clicked.connect(show_page2)
button3.clicked.connect(show_page3)

# Step 11: Add buttons to the button layout
button_layout.addWidget(button1)
button_layout.addWidget(button2)
button_layout.addWidget(button3)

# Step 12: Add the button layout to the main window's layout
main_layout = QVBoxLayout()
main_layout.addLayout(button_layout)
main_layout.addWidget(stacked_widget)

# Step 13: Set the layout to the central widget
central_widget = QWidget()
central_widget.setLayout(main_layout)
window.setCentralWidget(central_widget)

# Step 14: Show the main window
window.show()

# Step 15: Run the application's event loop
sys.exit(app.exec())
