import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QPushButton
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QIODevice

class SerialPortConfigExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Port Config Example")

        # Create serial port
        self.serial_port = QSerialPort()

        # Create UI elements
        self.port_combo = QComboBox()
        self.baudrate_combo = QComboBox()
        self.baudrate_combo.addItems(["9600", "19200", "38400", "57600", "115200"])
        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect_serial)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.port_combo)
        layout.addWidget(self.baudrate_combo)
        layout.addWidget(self.connect_button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Populate port combo
        self.update_ports()

    def update_ports(self):
        self.port_combo.clear()
        ports = QSerialPortInfo.availablePorts()
        for port in ports:
            self.port_combo.addItem(port.portName())

    def connect_serial(self):
        port_name = self.port_combo.currentText()
        baud_rate = int(self.baudrate_combo.currentText())

        self.serial_port.setPortName(port_name)
        self.serial_port.setBaudRate(baud_rate)
        self.serial_port.setDataBits(QSerialPort.Data8)
        self.serial_port.setParity(QSerialPort.NoParity)
        self.serial_port.setStopBits(QSerialPort.OneStop)
        self.serial_port.setFlowControl(QSerialPort.NoFlowControl)

        if self.serial_port.open(QIODevice.ReadWrite):
            print(f"Connected to {port_name} at {baud_rate} baud.")
        else:
            print("Failed to connect.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SerialPortConfigExample()
    window.show()
    sys.exit(app.exec())
