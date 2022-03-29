from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from widgets.LeftSide.DataButton import DataButton


class BranchButton(QWidget):
    buttonsignal = pyqtSignal(DataButton)
    branchsignal = pyqtSignal(dict)

    def __init__(self, name="Name", data="None", branches=[], prevbranches=[]):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.Button = DataButton(name, data)
        self.layout.addWidget(self.Button)
        self.Branches = branches
        self.prevBranches = prevbranches
        self.Button.clicked.connect(self.choiceBranch)

    def addprevBranch(self, tmp):
        self.prevBranches = [tmp]

    def choiceBranch(self):
        self.buttonsignal.emit(self.Button)
        self.branchsignal.emit({"Branches":self.Branches, "prevBranches":self.prevBranches})

    def addBranch(self, name="Name", data="None", branches=[]):
        branch = BranchButton(name, data, branches, list(self))
        self.Branches.append(branch)

    def addBranches(self, branches=[]):
        for branch in branches:
            branch.addprevBranch(self)
        self.Branches = branches

    def __copy__(self):
        return BranchButton(self.Button.text(), self.Button.Data, self.Branches)
