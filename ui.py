import PyQt5  # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tictac.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(259, 300)
        Dialog.setStyleSheet("\n"
                             "")
        self.pb_3 = QtWidgets.QPushButton(Dialog)
        self.pb_3.setGeometry(QtCore.QRect(172, 62, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.pb_3.setFont(font)
        self.pb_3.setStyleSheet("")
        self.pb_3.setText("")
        self.pb_3.setObjectName("pb_3")
        self.pb_2 = QtWidgets.QPushButton(Dialog)
        self.pb_2.setGeometry(QtCore.QRect(91, 62, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.pb_2.setFont(font)
        self.pb_2.setText("")
        self.pb_2.setObjectName("pb_2")
        self.pb_5 = QtWidgets.QPushButton(Dialog)
        self.pb_5.setGeometry(QtCore.QRect(91, 121, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.pb_5.setFont(font)
        self.pb_5.setText("")
        self.pb_5.setObjectName("pb_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(8, 21, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pb_1 = QtWidgets.QPushButton(Dialog)
        self.pb_1.setGeometry(QtCore.QRect(10, 62, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.pb_1.setFont(font)
        self.pb_1.setText("")
        self.pb_1.setObjectName("pb_1")
        self.pb_6 = QtWidgets.QPushButton(Dialog)
        self.pb_6.setGeometry(QtCore.QRect(172, 120, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.pb_6.setFont(font)
        self.pb_6.setText("")
        self.pb_6.setObjectName("pb_6")
        self.pb_4 = QtWidgets.QPushButton(Dialog)
        self.pb_4.setGeometry(QtCore.QRect(10, 120, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.pb_4.setFont(font)
        self.pb_4.setText("")
        self.pb_4.setObjectName("pb_4")
        self.pb_7 = QtWidgets.QPushButton(Dialog)
        self.pb_7.setGeometry(QtCore.QRect(10, 181, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pb_7.setFont(font)
        self.pb_7.setText("")
        self.pb_7.setObjectName("pb_7")
        self.pb_9 = QtWidgets.QPushButton(Dialog)
        self.pb_9.setGeometry(QtCore.QRect(170, 180, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.pb_9.setFont(font)
        self.pb_9.setText("")
        self.pb_9.setCheckable(False)
        self.pb_9.setFlat(False)
        self.pb_9.setObjectName("pb_9")
        self.pb_8 = QtWidgets.QPushButton(Dialog)
        self.pb_8.setGeometry(QtCore.QRect(90, 180, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.pb_8.setFont(font)
        self.pb_8.setText("")
        self.pb_8.setObjectName("pb_8")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(18, 250, 221, 25))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(-55, -19, 341, 381))
        self.graphicsView.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.pb_3.raise_()
        self.pb_2.raise_()
        self.pb_5.raise_()
        self.label.raise_()
        self.pb_1.raise_()
        self.pb_6.raise_()
        self.pb_4.raise_()
        self.pb_7.raise_()
        self.pb_9.raise_()
        self.pb_8.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate(
            "Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Tic Tac Toe</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tictac.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(259, 300)
        Dialog.setStyleSheet("\n"
"")
        self.pb_3 = QtWidgets.QPushButton(Dialog)
        self.pb_3.setGeometry(QtCore.QRect(172, 62, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.pb_3.setFont(font)
        self.pb_3.setStyleSheet("")
        self.pb_3.setText("")
        self.pb_3.setObjectName("pb_3")
        self.pb_2 = QtWidgets.QPushButton(Dialog)
        self.pb_2.setGeometry(QtCore.QRect(91, 62, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.pb_2.setFont(font)
        self.pb_2.setText("")
        self.pb_2.setObjectName("pb_2")
        self.pb_5 = QtWidgets.QPushButton(Dialog)
        self.pb_5.setGeometry(QtCore.QRect(91, 121, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.pb_5.setFont(font)
        self.pb_5.setText("")
        self.pb_5.setObjectName("pb_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(8, 21, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pb_1 = QtWidgets.QPushButton(Dialog)
        self.pb_1.setGeometry(QtCore.QRect(10, 62, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.pb_1.setFont(font)
        self.pb_1.setText("")
        self.pb_1.setObjectName("pb_1")
        self.pb_6 = QtWidgets.QPushButton(Dialog)
        self.pb_6.setGeometry(QtCore.QRect(172, 120, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.pb_6.setFont(font)
        self.pb_6.setText("")
        self.pb_6.setObjectName("pb_6")
        self.pb_4 = QtWidgets.QPushButton(Dialog)
        self.pb_4.setGeometry(QtCore.QRect(10, 120, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.pb_4.setFont(font)
        self.pb_4.setText("")
        self.pb_4.setObjectName("pb_4")
        self.pb_7 = QtWidgets.QPushButton(Dialog)
        self.pb_7.setGeometry(QtCore.QRect(10, 181, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pb_7.setFont(font)
        self.pb_7.setText("")
        self.pb_7.setObjectName("pb_7")
        self.pb_9 = QtWidgets.QPushButton(Dialog)
        self.pb_9.setGeometry(QtCore.QRect(170, 180, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.pb_9.setFont(font)
        self.pb_9.setText("")
        self.pb_9.setCheckable(False)
        self.pb_9.setFlat(False)
        self.pb_9.setObjectName("pb_9")
        self.pb_8 = QtWidgets.QPushButton(Dialog)
        self.pb_8.setGeometry(QtCore.QRect(90, 180, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.pb_8.setFont(font)
        self.pb_8.setText("")
        self.pb_8.setObjectName("pb_8")
        self.pb_reset = QtWidgets.QPushButton(Dialog)
        self.pb_reset.setGeometry(QtCore.QRect(18, 250, 221, 25))
        self.pb_reset.setObjectName("pb_reset")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(-55, -19, 341, 381))
        self.graphicsView.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.pb_3.raise_()
        self.pb_2.raise_()
        self.pb_5.raise_()
        self.label.raise_()
        self.pb_1.raise_()
        self.pb_6.raise_()
        self.pb_4.raise_()
        self.pb_7.raise_()
        self.pb_9.raise_()
        self.pb_8.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Tic Tac Toe</span></p></body></html>"))
        self.pb_reset.setText(_translate("Dialog", "Reset"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
