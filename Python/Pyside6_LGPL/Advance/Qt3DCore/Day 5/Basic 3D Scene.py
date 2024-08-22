import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.Qt3DCore import QEntity, QTransform
from PySide6.Qt3DExtras import Qt3DWindow, QPhongMaterial, QSphereMesh
from PySide6.QtGui import QVector3D

class Basic3DScene(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic 3D Scene")

        # Create a Qt3DWindow
        self.view = Qt3DWindow()
        self.container = self.createWindowContainer(self.view)
        self.setCentralWidget(self.container)

        # Root entity
        self.root_entity = QEntity()

        # Create a sphere mesh entity
        self.sphere = QEntity(self.root_entity)
        sphere_mesh = QSphereMesh()
        sphere_mesh.setRadius(1)
        self.sphere.addComponent(sphere_mesh)
        
        # Apply material
        material = QPhongMaterial()
        self.sphere.addComponent(material)

        # Transform entity
        transform = QTransform()
        transform.setTranslation(QVector3D(0, 0, 0))
        self.sphere.addComponent(transform)

        # Set the root entity
        self.view.setRootEntity(self.root_entity)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Basic3DScene()
    window.show()
    sys.exit(app.exec())
