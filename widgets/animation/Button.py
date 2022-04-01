from PyQt5.QtWidgets import QPushButton, QGraphicsColorizeEffect
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QSize, QMargins, QEasingCurve



class AnimCategoryButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text=text, parent=parent)
        self.ui()
        self.initEnterAnimationGroup()



    def initEnterAnimationGroup(self):
        sizeAnim = QPropertyAnimation(self, b"geometry")
        sizeAnim.setDuration(250)
        sizeAnim.setEasingCurve(QEasingCurve.InOutCubic)

        coloreffect = QGraphicsColorizeEffect()
        coloreffect.setStrength(0)
        coloreffect.setColor(QColor(220,75,222))
        self.setGraphicsEffect(coloreffect)
        coloranim = QPropertyAnimation(coloreffect, b"strength")
        coloranim.setDuration(200)

        self.enterEventAnimation = QParallelAnimationGroup()
        self.enterEventAnimation.addAnimation(sizeAnim)
        self.enterEventAnimation.addAnimation(coloranim)


    def _enterEventSizeAnimation(self):
        anim = self.enterEventAnimation.children()[0]
        rect = self.geometry()
        anim.setStartValue(rect)
        rect += QMargins(10, 10, 10, 10)
        anim.setEndValue(rect)

    def _enterEventColorAnimation(self):
        anim = self.enterEventAnimation.children()[1]
        anim.setStartValue(0)
        anim.setEndValue(1)

    def enterEvent(self, event):
        self.enterEventAnimation.setDirection(self.enterEventAnimation.Forward)
        if self.enterEventAnimation.state() == self.enterEventAnimation.State.Stopped:
            self._enterEventSizeAnimation()
            self._enterEventColorAnimation()
            self.enterEventAnimation.start()
        QPushButton.enterEvent(self, event)

    def leaveEvent(self, event):
        self.enterEventAnimation.setDirection(self.enterEventAnimation.Backward)
        if self.enterEventAnimation.state() == self.enterEventAnimation.State.Stopped:
            self.enterEventAnimation.start()
        QPushButton.leaveEvent(self, event)

    def ui(self):
        self.setMinimumSize(QSize(95, 0))
        self.setBaseSize(QSize(95, 30))
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
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 191, 255, 255), stop:1 rgba(11, 55, 66, 168));\n"
            "\n"
            "color: rgb(234, 234, 234);"
            "\n"
            "border-radius:0.9em;"
        )

