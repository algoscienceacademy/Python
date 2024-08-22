import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlError

# Step 1: Set up the SQLite database with error handling
def setup_database():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(':memory:')
    if not db.open():
        print("Unable to open database")
        return False

    query = QSqlQuery()
    query.exec('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
    if not query.exec("INSERT INTO users (name) VALUES ('Alice')"):
        print("Insert failed:", query.lastError().text())
        return False
    if not query.exec("INSERT INTO users (name) VALUES ('Bob')"):
        print("Insert failed:", query.lastError().text())
        return False
    return True

# Step 2: Create the main window with transactions
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Database Example with Transactions')
        self.resize(400, 300)

        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        self.query_button = QPushButton("Fetch Data")
        self.query_button.clicked.connect(self.fetch_data)
        layout.addWidget(self.query_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        if not setup_database():
            self.text_edit.setText("Failed to set up database.")

    def fetch_data(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        if not query.exec("SELECT * FROM users"):
            self.text_edit.setText(f"Query failed: {query.lastError().text()}")
            return
        
        model.setQuery(query)
        results = ""
        for row in range(model.rowCount()):
            id_item = model.data(model.index(row, 0))
            name_item = model.data(model.index(row, 1))
            results += f"ID: {id_item}, Name: {name_item}\n"
        
        self.text_edit.setText(results)

# Step 3: Create the main application object and run the event loop
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
