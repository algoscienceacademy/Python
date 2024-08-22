import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtGui import QSurfaceFormat
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL.GL import glClear, glClearColor, GL_COLOR_BUFFER_BIT


# Step 1: Create a custom widget for OpenGL rendering
class OpenGLWidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.setFormat(QSurfaceFormat.defaultFormat())  # Set default format

    def initializeGL(self):
        # Set up OpenGL settings
        glClearColor(0.0, 0.0, 0.0, 1.0)  # Set clear color to black

    def paintGL(self):
        # Clear the screen with the clear color
        glClear(GL_COLOR_BUFFER_BIT)

# Step 2: Create the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QOpenGLWidget Example')
        self.resize(800, 600)

        layout = QVBoxLayout()

        # Create the OpenGL widget
        self.opengl_widget = OpenGLWidget()
        
        layout.addWidget(self.opengl_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

# Step 3: Create the main application object and run the event loop
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
