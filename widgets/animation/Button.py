from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QPropertyAnimation, QSize, QMargins
from PyQt5.QtCore import QAbstractAnimation


class AnimCategoryButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text=text, parent=parent)
        self.ui()
        self.initEnterAnimation()



    def initEnterAnimation(self):
        self.enterEventAnimation = QPropertyAnimation(self, b"geometry")
        self.enterEventAnimation.setDuration(250)


    def enterEvent(self, event):
        self.enterEventAnimation.setDirection(QAbstractAnimation.Forward)
        if self.enterEventAnimation.state() == self.enterEventAnimation.State.Stopped:
            rect = self.geometry()
            self.enterEventAnimation.setStartValue(rect)
            rect+=QMargins(10,10,10,10)
            self.enterEventAnimation.setEndValue(rect)
            self.enterEventAnimation.start()
        QPushButton.enterEvent(self, event)

    def leaveEvent(self, event):
        self.enterEventAnimation.setDirection(QAbstractAnimation.Backward)
        if self.enterEventAnimation.state() == self.enterEventAnimation.State.Stopped:
            self.enterEventAnimation.start()
        QPushButton.leaveEvent(self, event)

    def ui(self):
        self.setMinimumSize(QSize(95, 0))
        self.setMaximumSize(QSize(150, 50))
        font = QFont()
        font.setFamily(u"Gill Sans MT Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.setFont(font)
        self.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 191, 255, 255), stop:1 rgba(11, 71, 89, 168));\n"
            "\n"
            "color: rgb(234, 234, 234);"
            "\n"
            "border-radius:0.9em;"
        )

