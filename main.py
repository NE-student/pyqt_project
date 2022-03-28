from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout
from widgets.TreeButton import TreeButton
from widgets.BranchButton import BranchButton
import sys


class App(QMainWindow):
    def __init__(self, branches):
        super().__init__()
        self.layout = QHBoxLayout(self)

        self.treebtn = TreeButton(branches)
        self.layout.addWidget(self.treebtn)

        self.centerWidget = QWidget()
        self.centerWidget.setLayout(self.layout)
        self.setCentralWidget(self.centerWidget)
        self.setGeometry(40,40, 300, 450)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    games = [BranchButton("Grounded", "....", [BranchButton("Weapons", ".."), BranchButton("Npcs", "..")])]
    window = TreeButton(games)
    window.show()
    sys.exit(app.exec())
