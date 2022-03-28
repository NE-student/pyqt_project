from PyQt5.QtWidgets import QPushButton


class DataButton(QPushButton):
    def __init__(self, text, data, parent=None):
        super().__init__(text=text, parent=parent)

        self._data = data

    @property
    def Data(self):
        return self._data

    @Data.setter
    def Data(self, data):
        self._data = data
