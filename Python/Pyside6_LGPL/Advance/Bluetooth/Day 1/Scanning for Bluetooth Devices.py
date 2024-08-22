import sys
from PySide6.QtBluetooth import QBluetoothDeviceDiscoveryAgent, QBluetoothDeviceInfo
from PySide6.QtCore import Slot, QCoreApplication

class BluetoothScanner:
    def __init__(self):
        self.discovery_agent = QBluetoothDeviceDiscoveryAgent()
        self.discovery_agent.deviceDiscovered.connect(self.device_discovered)
        self.discovery_agent.start()

    @Slot(QBluetoothDeviceInfo)
    def device_discovered(self, device_info):
        print(f"Discovered device: {device_info.name()} - {device_info.address().toString()}")

if __name__ == "__main__":
    app = QCoreApplication(sys.argv)
    scanner = BluetoothScanner()
    sys.exit(app.exec())
