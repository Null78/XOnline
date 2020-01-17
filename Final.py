# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\finale.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import Qt

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(422, 300)
        Dialog.setMinimumSize(QtCore.QSize(422, 300))
        Dialog.setMaximumSize(QtCore.QSize(422, 300))
        Dialog.setBaseSize(QtCore.QSize(422, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\img/o.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.Rematch = QtWidgets.QPushButton(Dialog)
        self.Rematch.setMinimumSize(QtCore.QSize(30, 35))
        self.Rematch.setObjectName("Rematch")
        self.gridLayout.addWidget(self.Rematch, 1, 0, 1, 1)
        self.Exit = QtWidgets.QPushButton(Dialog)
        self.Exit.setMinimumSize(QtCore.QSize(0, 35))
        self.Exit.setObjectName("Exit")
        self.gridLayout.addWidget(self.Exit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(400, 219))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./img/lose.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Game Over"))
        self.Rematch.setText(_translate("Dialog", "Rematch"))
        self.Exit.setText(_translate("Dialog", "Exit"))

class MyDialog(QDialog):
    def closeEvent(self, event):
        event.ignore()
        x = QMessageBox.warning(self, "Warning", "Are You Sure?",
                                QMessageBox.Yes | QMessageBox.No)
        if x == QMessageBox.Yes:
            sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = MyDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
