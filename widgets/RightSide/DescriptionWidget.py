from PyQt5.QtWidgets import QWidget, QVBoxLayout


class DescriptionWidget(QWidget):

    def __init__(self, item):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(item)