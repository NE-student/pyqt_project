from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import  QFont


class Item(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

    def addParagraph(self, text, font=QFont("Times", 24, QFont.Bold)):
        lbl = QLabel(text)
        lbl.setFont(font)
        self.layout.addWidget(lbl)

    def addLabel(self, text, font=QFont("Arial", 14, QFont.Bold)):
        lbl = QLabel(text)
        lbl.setFont(font)
        self.layout.addWidget(lbl)