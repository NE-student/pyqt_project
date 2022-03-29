from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal
from widgets.Item import Item


class TreeButton(QWidget):
    choiced = pyqtSignal(Item)

    def __init__(self, branches):
        super().__init__()

        self.depthLevel = 0

        self.layout = QVBoxLayout(self)
        self.Tree = branches
        self.backbuttons = []
        self.CurrentBranches = self.Tree.copy()

        self.backbtn = QPushButton("<-")
        self.backbtn.setDisabled(True)
        self.backbtn.clicked.connect(self.moveBack)
        self.layout.addWidget(self.backbtn)

        self.viewBranches()

    def viewBranchesAfterBack(self):
        self.backbtn.setDisabled(True)
        if self.depthLevel != 0:
            self.backbtn.setDisabled(False)

        for branch in self.CurrentBranches:
            self.layout.addWidget(branch)
            branch.show()

    def viewBranches(self):
        self.backbtn.setDisabled(True)
        if self.depthLevel != 0:
            self.backbtn.setDisabled(False)

        for branch in self.CurrentBranches:
            branch.branchsignal.connect(self.moveForward)
            branch.buttonsignal.connect(self.info)
            self.layout.addWidget(branch)
            branch.show()


    def info(self, arg):
        itm = Item()
        itm.addParagraph(arg.text())
        itm.addLabel(arg.Data)
        self.choiced.emit(itm)

    def moveBack(self):
        self.depthLevel -= 1
        self.refreshLayout()
        if len(self.prevBranches) == 0:
            self.CurrentBranches = self.Tree
            self.prevBranches = self.Tree
            self.depthLevel = 0
        else:
            self.CurrentBranches = self.prevBranches[0].Branches
            self.prevBranches = self.prevBranches[0].prevBranches

        self.viewBranchesAfterBack()


    def moveForward(self, arg):
        self.depthLevel +=1
        self.prevBranches = arg["prevBranches"]
        #if self.depthLevel == 1:
            #self.prevBranches = self.Tree

        self.refreshLayout()
        self.CurrentBranches = arg["Branches"]
        self.viewBranches()

    def refreshLayout(self):
        for w in self.CurrentBranches:
            self.layout.removeWidget(w)
            w.hide()
