import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

# Step 1: Set up the SQLite database
def setup_database():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(':memory:')  # Use an in-memory database for this example
    if not db.open():
        print("Unable to open database")
        return False

    query = QSqlQuery()
    query.exec('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
    query.exec("INSERT INTO users (name) VALUES ('Alice')")
    query.exec("INSERT INTO users (name) VALUES ('Bob')")
    return True

# Step 2: Create the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Database Example')
        self.resize(400, 300)

        layout = QVBoxLayout()

        # Create a QTextEdit to display query results
        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        # Create a QPushButton to trigger the database query
        self.query_button = QPushButton("Fetch Data")
        self.query_button.clicked.connect(self.fetch_data)
        layout.addWidget(self.query_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Set up the database
        if not setup_database():
            self.text_edit.setText("Failed to set up database.")

    def fetch_data(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.exec("SELECT * FROM users")
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
