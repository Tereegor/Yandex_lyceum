import os
import sys

import requests
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class MapApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Yandex Maps Viewer')
        self.setGeometry(100, 100, 600, 450)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.load_map()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def load_map(self):
        lat = "55.753215"
        lon = "37.622504"
        scale = "0.02"

        api_key = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
        url = f"https://static-maps.yandex.ru/v1?ll={lon},{lat}&spn={scale},{scale}&size=600,450&apikey={api_key}"

        response = requests.get(url)
        if response.status_code == 200:
            with open("map.png", "wb") as file:
                file.write(response.content)

            pixmap = QPixmap("map.png")
            self.label.setPixmap(pixmap)
        else:
            self.label.setText(f"Ошибка при загрузке карты. Код ответа: {response.status_code}")

    def closeEvent(self, event):
        if os.path.exists("map.png"):
            os.remove("map.png")
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapApp()
    window.show()
    sys.exit(app.exec())
