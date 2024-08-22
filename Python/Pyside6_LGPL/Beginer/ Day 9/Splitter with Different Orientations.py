import sys
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QSplitter, QTextEdit, QVBoxLayout, QWidget

# Step 1: Create the main application object
app = QApplication(sys.argv)

# Step 2: Create the main window (QMainWindow)
window = QMainWindow()
window.setWindowTitle('Vertical QSplitter Example')
window.resize(600, 400)

# Step 3: Create a vertical QSplitter
splitter = QSplitter(Qt.Vertical)

# Step 4: Create widgets to add to the splitter
text_edit1 = QTextEdit()
text_edit1.setPlainText("This is the first text edit.")

text_edit2 = QTextEdit()
text_edit2.setPlainText("This is the second text edit.")

# Step 5: Add widgets to the splitter
splitter.addWidget(text_edit1)
splitter.addWidget(text_edit2)

# Step 6: Set the splitter as the central widget
window.setCentralWidget(splitter)

# Step 7: Show the main window
window.show()

# Step 8: Run the application's event loop
sys.exit(app.exec())
