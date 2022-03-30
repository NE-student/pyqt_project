from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal
from widgets.Item import Item


class TreeButton(QWidget):
    choiced = pyqtSignal(Item)

    def __init__(self, branches):
        super().__init__()

        self.backMovable = False

        self.layout = QVBoxLayout(self)
        self.Tree = branches
        self.CurrentBranches = self.Tree
        self.prevBranch = None

        self.backbtn = QPushButton("<-")
        self.backbtn.setDisabled(True)
        self.backbtn.clicked.connect(self.moveBack)
        self.layout.addWidget(self.backbtn)

        self.viewBranches()

    def viewBranchesAfterBack(self):
        self.backbtn.setDisabled(self.backMovable)

        self.CurrentBranches.addToLayout()
        self.layout.addWidget(self.CurrentBranches)

    def viewBranches(self):
        self.backbtn.setDisabled(self.backMovable)

        self.CurrentBranches.addToLayout()
        self.layout.addWidget(self.CurrentBranches)
        self.CurrentBranches.connectBranchsignal(self.moveForward)
        self.CurrentBranches.connectButtonsignal(self.info)

    def info(self, arg):
        itm = Item()
        itm.addParagraph(arg.text())
        itm.addLabel(arg.Data)
        self.choiced.emit(itm)

    def moveBack(self):
        self.refreshLayout()
        if self.prevBranch is None:
            self.CurrentBranches = self.Tree
            self.prevBranch = self.Tree
            self.backMovable = False
        else:
            self.CurrentBranches = self.prevBranch[0].Branches
            self.prevBranch = self.prevBranch[0].prevBranch

        self.viewBranchesAfterBack()


    def moveForward(self, arg):
        self.backMovable = True
        self.refreshLayout()
        self.prevBranch = arg["prevBranch"]
        self.CurrentBranches = arg["Branches"]
        self.viewBranches()

    def refreshLayout(self):
        self.CurrentBranches.removeFromLayout()
        self.layout.removeWidget(self.CurrentBranches)

