from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout
from widgets.LeftSide.TreeButton import TreeButton
from widgets.LeftSide.BranchesButton import BranchesButton
from widgets.LeftSide.BranchButton import BranchButton
from widgets.RightSide.DescriptionWidget import DescriptionWidget
from widgets.Item import Item
import sys


class App(QMainWindow):
    def __init__(self, branches):
        super().__init__()
        self.layout = QHBoxLayout(self)

        self.treebtn = TreeButton(branches)
        self.description = DescriptionWidget(Item())

        self.treebtn.choiced.connect(self.viewDescription)

        self.layout.addWidget(self.treebtn)
        self.layout.addWidget(self.description)

        self.centerWidget = QWidget()
        self.centerWidget.setLayout(self.layout)
        self.setCentralWidget(self.centerWidget)
        self.setGeometry(40, 40, 300, 450)

    def viewDescription(self, arg):
        self.layout.removeWidget(self.description)
        self.description = DescriptionWidget(arg)
        self.layout.addWidget(self.description)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = BranchesButton([BranchButton("Grounded", "Grounded"), BranchButton("Rocket league", "aga")])
    children = BranchesButton([BranchButton("Weapons", "Weapons"), BranchButton("Npcs", "Npcs")])
    childrenchildren = BranchesButton([BranchButton("For far", "For far"), BranchButton("For near", "For near")])
    game.setBranchesAt(0, children)
    children.setBranchesAt(0, childrenchildren)
    window = App(game)
    window.show()
    sys.exit(app.exec())
