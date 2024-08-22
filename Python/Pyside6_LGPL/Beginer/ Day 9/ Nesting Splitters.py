import sys
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QSplitter, QTextEdit, QWidget, QVBoxLayout

# Step 1: Create the main application object
app = QApplication(sys.argv)

# Step 2: Create the main window (QMainWindow)
window = QMainWindow()
window.setWindowTitle('Nested QSplitter Example')
window.resize(600, 400)

# Step 3: Create the main horizontal splitter
main_splitter = QSplitter(Qt.Horizontal)

# Step 4: Create the first vertical splitter
vertical_splitter = QSplitter(Qt.Vertical)
text_edit1 = QTextEdit()
text_edit1.setPlainText("This is the first text edit.")
text_edit2 = QTextEdit()
text_edit2.setPlainText("This is the second text edit.")
vertical_splitter.addWidget(text_edit1)
vertical_splitter.addWidget(text_edit2)

# Step 5: Create the second vertical splitter
text_edit3 = QTextEdit()
text_edit3.setPlainText("This is the third text edit.")
text_edit4 = QTextEdit()
text_edit4.setPlainText("This is the fourth text edit.")

vertical_splitter2 = QSplitter(Qt.Vertical)
vertical_splitter2.addWidget(text_edit3)
vertical_splitter2.addWidget(text_edit4)

# Step 6: Add the vertical splitters to the main horizontal splitter
main_splitter.addWidget(vertical_splitter)
main_splitter.addWidget(vertical_splitter2)

# Step 7: Set the main splitter as the central widget
window.setCentralWidget(main_splitter)

# Step 8: Show the main window
window.show()

# Step 9: Run the application's event loop
sys.exit(app.exec())
