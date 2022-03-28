from PyQt5.QtWidgets import QWidget, QVBoxLayout
from widgets.BranchButton import BranchButton



class TreeButton(QWidget):
    def __init__(self, branches):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.Tree = branches
        self.CurrentBranches = self.Tree.copy()

        self.viewBranches()

    def viewBranches(self):
        for branch in self.CurrentBranches:
            branch.branchsignal.connect(self.moveIn)
            self.layout.addWidget(branch)
            #branch.show()


    def moveIn(self,arg):
        self.refreshLayout()
        self.CurrentBranches = arg
        self.viewBranches()

    def refreshLayout(self):
        for w in self.CurrentBranches:
            self.layout.removeWidget(w)
            w.hide()

