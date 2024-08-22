import sys
from PySide6.QtGui import QStandardItemModel, QStandardItem 
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget

# Step 1: Create the tree view model
class TreeModel(QStandardItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setHorizontalHeaderLabels(['Name', 'Description'])

        # Add root items
        rootItem = self.invisibleRootItem()

        # Create some items for the tree
        item1 = QStandardItem('Item 1')
        item1.appendRow([QStandardItem('Subitem 1.1'), QStandardItem('Details about Subitem 1.1')])
        item1.appendRow([QStandardItem('Subitem 1.2'), QStandardItem('Details about Subitem 1.2')])
        rootItem.appendRow([item1, QStandardItem('Description for Item 1')])

        item2 = QStandardItem('Item 2')
        item2.appendRow([QStandardItem('Subitem 2.1'), QStandardItem('Details about Subitem 2.1')])
        rootItem.appendRow([item2, QStandardItem('Description for Item 2')])

# Step 2: Create the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tree View Example')
        self.resize(400, 300)

        layout = QVBoxLayout()

        # Create the tree view and set the model
        tree_view = QTreeView()
        tree_model = TreeModel()
        tree_view.setModel(tree_model)

        layout.addWidget(tree_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

# Step 3: Create the main application object and run the event loop
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
