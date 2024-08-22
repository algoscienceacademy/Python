import sys
from PySide6.QtBluetooth import QBluetoothDeviceDiscoveryAgent, QBluetoothSocket, QBluetoothDeviceInfo
from PySide6.QtCore import Slot, QCoreApplication

class BluetoothConnector:
    def __init__(self):
        self.discovery_agent = QBluetoothDeviceDiscoveryAgent()
        self.socket = QBluetoothSocket(QBluetoothSocket.RfcommSocket)
        self.discovery_agent.deviceDiscovered.connect(self.device_discovered)
        self.discovery_agent.start()

    @Slot(QBluetoothDeviceInfo)
    def device_discovered(self, device_info):
        print(f"Connecting to device: {device_info.name()}")
        self.socket.connectToService(device_info, QBluetoothSocket.RfcommService)
        if self.socket.waitForConnected(5000):
            print("Connected successfully")
        else:
            print("Failed to connect")

if __name__ == "__main__":
    app = QCoreApplication(sys.argv)
    connector = BluetoothConnector()
    sys.exit(app.exec())
