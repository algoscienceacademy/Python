import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QToolBar

# Step 1: Create the main application object
app = QApplication(sys.argv)

# Step 2: Create the main window (QMainWindow)
window = QMainWindow()
window.setWindowTitle('Toolbar Example')
window.resize(600, 400)

# Step 3: Create a central widget (QTextEdit) for the main window
text_edit = QTextEdit()
window.setCentralWidget(text_edit)

# Step 4: Create the menu bar
menu_bar = window.menuBar()

# Step 5: Add menus to the menu bar
file_menu = menu_bar.addMenu('File')
edit_menu = menu_bar.addMenu('Edit')

# Step 6: Create actions for the menus
new_action = QAction('New', window)
new_action.setShortcut('Ctrl+N')

open_action = QAction('Open...', window)
open_action.setShortcut('Ctrl+O')

save_action = QAction('Save', window)
save_action.setShortcut('Ctrl+S')

exit_action = QAction('Exit', window)
exit_action.setShortcut('Ctrl+Q')

undo_action = QAction('Undo', window)
undo_action.setShortcut('Ctrl+Z')

redo_action = QAction('Redo', window)
redo_action.setShortcut('Ctrl+Y')

# Step 7: Add actions to the File menu
file_menu.addAction(new_action)
file_menu.addAction(open_action)
file_menu.addAction(save_action)
file_menu.addSeparator()  # Adds a separator line
file_menu.addAction(exit_action)

# Step 8: Add actions to the Edit menu
edit_menu.addAction(undo_action)
edit_menu.addAction(redo_action)

# Step 9: Create a toolbar and add actions
toolbar = QToolBar("Main Toolbar")
window.addToolBar(toolbar)
toolbar.addAction(new_action)
toolbar.addAction(open_action)
toolbar.addAction(save_action)
toolbar.addSeparator()
toolbar.addAction(undo_action)
toolbar.addAction(redo_action)

# Step 10: Connect the Exit action to close the window
exit_action.triggered.connect(window.close)

# Step 11: Show the main window
window.show()

# Step 12: Run the application's event loop
sys.exit(app.exec())
