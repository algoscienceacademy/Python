import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QByteArray, QIODevice

class SerialPortExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Port Example")

        # Create serial port
        self.serial_port = QSerialPort()
        self.serial_port.setPortName(QSerialPortInfo.availablePorts()[0].portName())
        self.serial_port.setBaudRate(QSerialPort.Baud9600)
        self.serial_port.setDataBits(QSerialPort.Data8)
        self.serial_port.setParity(QSerialPort.NoParity)
        self.serial_port.setStopBits(QSerialPort.OneStop)
        self.serial_port.setFlowControl(QSerialPort.NoFlowControl)
        self.serial_port.open(QIODevice.ReadWrite)

        # Create UI elements
        self.text_edit = QTextEdit()
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_data)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.send_button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Connect serial port signal
        self.serial_port.readyRead.connect(self.read_data)

    def send_data(self):
        data = QByteArray(b"Hello, Serial Port!")
        self.serial_port.write(data)

    def read_data(self):
        data = self.serial_port.readAll()
        self.text_edit.append(f"Received: {data.data().decode()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SerialPortExample()
    window.show()
    sys.exit(app.exec())
