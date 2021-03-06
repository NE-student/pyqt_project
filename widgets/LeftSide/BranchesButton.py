from PyQt5.QtWidgets import QWidget, QVBoxLayout


class BranchesButton(QWidget):
    def __init__(self, branches=[]):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.Branches = branches
        self.addToLayout()

    def connectBranchsignal(self, function):
        for branch in self.Branches:
            branch.branchsignal.choiced.connect(function)

    def connectButtonsignal(self, function):
        for branch in self.Branches:
            branch.buttonsignal.choiced.connect(function)

    def disconnectBranchsignal(self, function):
        try:
            for branch in self.Branches:
                branch.branchsignal.choiced.disconnect(function)
        except:
            pass

    def disconnectButtonsignal(self, function):
        try:
            for branch in self.Branches:
                branch.buttonsignal.choiced.disconnect(function)
        except:
            pass

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

