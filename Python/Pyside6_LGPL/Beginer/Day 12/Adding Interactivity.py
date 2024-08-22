import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView,  QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem

# Step 1: Create the tree view model
class TreeModel(QStandardItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setHorizontalHeaderLabels(['Name', 'Description'])

        rootItem = self.invisibleRootItem()

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
        self.setWindowTitle('Interactive Tree View Example')
        self.resize(600, 400)

        layout = QVBoxLayout()

        self.tree_view = QTreeView()
        self.tree_model = TreeModel()
        self.tree_view.setModel(self.tree_model)

        self.detail_label = QLabel("Select an item to see details")

        self.tree_view.selectionModel().selectionChanged.connect(self.on_selection_changed)

        layout.addWidget(self.tree_view)
        layout.addWidget(self.detail_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_selection_changed(self, selected, deselected):
        index = self.tree_view.selectionModel().currentIndex()
        if index.isValid():
            item = self.tree_model.itemFromIndex(index)
            details = item.child(index.row()).text() if item.hasChildren() else 'No details'
            self.detail_label.setText(f"Selected Item: {item.text()}\nDetails: {details}")

# Step 3: Create the main application object and run the event loop
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
