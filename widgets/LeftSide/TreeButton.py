from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from widgets.Item import Item


class TreeButton(QWidget):
    choiced = pyqtSignal(Item)
    def __init__(self, branches):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.Tree = branches
        self.CurrentBranches = self.Tree.copy()

        self.viewBranches()

    def viewBranches(self):
        for branch in self.CurrentBranches:
            branch.branchsignal.connect(self.moveIn)
            branch.buttonsignal.connect(self.info)
            self.layout.addWidget(branch)
            #branch.show()

    def info(self, arg):
        itm = Item()
        itm.addParagraph(arg.text())
        itm.addLabel(arg.Data)
        self.choiced.emit(itm)
    def moveIn(self,arg):
        self.refreshLayout()
        self.CurrentBranches = arg
        self.viewBranches()

    def refreshLayout(self):
        for w in self.CurrentBranches:
            self.layout.removeWidget(w)
            w.hide()

