from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from widgets.LeftSide.DataButton import DataButton


class BranchesButton(QWidget):
    def __init__(self, branches=[]):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.Branches = branches
        self._addToLayout()

    def connectBranchsignal(self, function):
        for branch in self.Branches:
            branch.branchsignal.connect(function)

    def connectButtonsignal(self, function):
        for branch in self.Branches:
            branch.buttonsignal.connect(function)

    def addToLayout(self):
        for branch in self.Branches:
            self.layout.addWidget(branch)
            branch.show()

    def removeFromLayout(self):
        for branch in self.Branches:
            self.layout.removeWidget(branch)
            branch.hide()

    def setprevBranch(self, prevBranch):
        for branch in self.Branches:
            branch.prevBranch = prevBranch

    def addBranch(self, branch):
        self.Branches.append(branch)
        if self.Branches[0].prevBranch is not None:
            branch.setprevBranch(self.Branches[0].prevBranch)

    def setBranchesAt(self, index, branches):
        self.Branches[index].setBranches(branches)

