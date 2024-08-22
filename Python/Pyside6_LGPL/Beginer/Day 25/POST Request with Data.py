from PySide6.QtCore import QUrl, QByteArray
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
        url = QUrl("https://jsonplaceholder.typicode.com/posts")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")

        data = QByteArray(b'{"title": "foo", "body": "bar", "userId": 1}')
        self.manager.post(request, data)

    def on_finished(self, reply: QNetworkReply):
        data = reply.readAll().data().decode()
        print(data)
        reply.deleteLater()
        self.quit()

if __name__ == "__main__":
    app = NetworkExample(sys.argv)
    sys.exit(app.exec())
