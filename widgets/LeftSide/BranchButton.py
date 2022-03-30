from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from widgets.LeftSide.DataButton import DataButton
from widgets.LeftSide.BranchesButton import BranchesButton


class BranchButton(QWidget):
    buttonsignal = pyqtSignal(DataButton)
    branchsignal = pyqtSignal(dict)

    def __init__(self, name="Name", data="None", branches=BranchesButton(), prevbranch=None):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.Button = DataButton(name, data)
        self.layout.addWidget(self.Button)
        self.Branches = branches
        self.prevBranch = prevbranch
        self.Button.clicked.connect(self.choiceBranch)

    def setprevBranch(self, prevBranch):
        self.prevBranch = prevBranch

    def setBranches(self, branches=BranchesButton()):
        branches.setprevBranch(self)
        self.Branches = branches

    def choiceBranch(self):
        self.buttonsignal.emit(self.Button)
        self.branchsignal.emit({"Branches":self.Branches, "prevBranch":self.prevBranch})

    def isHighRank(self):
        if self.prevBranch is None:
            return True
        return False
