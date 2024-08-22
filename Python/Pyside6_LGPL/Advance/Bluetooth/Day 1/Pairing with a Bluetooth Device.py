import sys
from PySide6.QtBluetooth import QBluetoothDeviceDiscoveryAgent, QBluetoothLocalDevice, QBluetoothDeviceInfo
from PySide6.QtCore import Slot, QCoreApplication

class BluetoothPairer:
    def __init__(self):
        self.discovery_agent = QBluetoothDeviceDiscoveryAgent()
        self.local_device = QBluetoothLocalDevice()
        self.discovery_agent.deviceDiscovered.connect(self.device_discovered)
        self.discovery_agent.start()

    @Slot(QBluetoothDeviceInfo)
    def device_discovered(self, device_info):
        print(f"Pairing with device: {device_info.name()}")
        self.local_device.requestPairing(device_info.address())

if __name__ == "__main__":
    app = QCoreApplication(sys.argv)
    pairer = BluetoothPairer()
    sys.exit(app.exec())
