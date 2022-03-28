from PyQt5.QtWidgets import QWidget, QVBoxLayout
from widgets.DataButton import DataButton


class Buttontree(QWidget):
    def __init__(self):
        super().__init__(self)

        self.layout = QVBoxLayout()
        self.Tree = {}

    def addButton(self):
        btn = DataButton("Name", "None")
        self.layout.addWidget(btn)
        self.Tree