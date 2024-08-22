import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QByteArray, QIODevice, QTimer

class SerialPortTimeoutExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Port Timeout Example")

        # Create serial port
        self.serial_port = QSerialPort()
        self.available_ports = QSerialPortInfo.availablePorts()

        if self.available_ports:
            self.serial_port.setPortName(self.available_ports[0].portName()) 
            self.serial_port.setBaudRate(QSerialPort.Baud9600)
            self.serial_port.setDataBits(QSerialPort.Data8)
            self.serial_port.setParity(QSerialPort.NoParity)
            self.serial_port.setStopBits(QSerialPort.OneStop)
            self.serial_port.setFlowControl(QSerialPort.NoFlowControl)
            self.serial_port.open(QIODevice.ReadWrite)
        else:
            print("No available serial ports.")
            sys.exit()

        # Create UI elements
        self.text_edit = QTextEdit()
        self.read_button = QPushButton("Read")
        self.read_button.clicked.connect(self.read_data)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.read_button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Timer to handle timeout
        self.timer = QTimer()
        self.timer.setInterval(5000)  # 5 seconds
        self.timer.timeout.connect(self.handle_timeout)

    def read_data(self):
        if self.serial_port.waitForReadyRead(1000):  # Wait for 1 second
            data = self.serial_port.readAll()
            self.text_edit.append(f"Received: {data.data().decode()}")
        else:
            self.text_edit.append("No data received within the timeout period.")

    def handle_timeout(self):
        self.text_edit.append("Timeout occurred!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SerialPortTimeoutExample()
    window.show()
    sys.exit(app.exec())

