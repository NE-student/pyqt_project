from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSignal, QObject
from widgets.LeftSide.DataButton import DataButton
from widgets.LeftSide.BranchesButton import BranchesButton

class ButtonSignal(QObject):
    choiced = pyqtSignal(DataButton)

class BranchSignal(QObject):
    choiced = pyqtSignal(dict)

class BranchButton(QWidget):
    def __init__(self, name="Name", data="None", branches=None, prevbranch=None):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.Button = DataButton(name, data)
        self.layout.addWidget(self.Button)
        self.Branches = branches
        self.prevBranch = prevbranch
        self.Button.clicked.connect(self.choiceBranch)

        self.buttonsignal = ButtonSignal()
        self.branchsignal = BranchSignal()

    def setprevBranch(self, prevBranch):
        self.prevBranch = prevBranch

    def setBranches(self, branches=None):
        branches.setprevBranch(self)
        self.Branches = branches

    def choiceBranch(self):
        self.buttonsignal.choiced.emit(self.Button)
        self.branchsignal.choiced.emit({"Branches":self.Branches, "prevBranch":self.prevBranch})

    def isHighRank(self):
        if self.prevBranch is None:
            return True
        return False
