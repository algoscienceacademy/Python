from PySide6.QtCore import QUrl
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtWidgets import QApplication
import sys

class NetworkExample(QApplication):
    def __init__(self, *args):
        super().__init__(*args)
        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self.on_finished)
        self.make_request()

    def make_request(self):
        url = QUrl("https://jsonplaceholder.typicode.com/posts/1")
        request = QNetworkRequest(url)
        self.manager.get(request)

    def on_finished(self, reply: QNetworkReply):
        data = reply.readAll().data().decode()
        print(data)
        reply.deleteLater()
        self.quit()

if __name__ == "__main__":
    app = NetworkExample(sys.argv)
    sys.exit(app.exec())
