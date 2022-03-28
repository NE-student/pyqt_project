from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from widgets.DataButton import DataButton


class BranchButton(QWidget):
    buttonsignal = pyqtSignal(DataButton)
    branchsignal = pyqtSignal(list)

    def __init__(self, name="Name", data="None", branches=[]):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.Button = DataButton(name, data)
        self.layout.addWidget(self.Button)
        self.Branches = branches
        self.Button.clicked.connect(self.choiceBranch)

    def choiceBranch(self):
        self.buttonsignal.emit(self.Button)
        self.branchsignal.emit(self.Branches)

    def addBranch(self):
        branch = BranchButton()
        self.Branches.append(branch)

    def __copy__(self):
        newBranchButton = BranchButton(self.Button.text(), self.Button.Data, self.Branches)
