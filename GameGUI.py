# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\XOPGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox


class Ui_PlayWindow(object):
    def setupUi(self, PlayWindow):
        PlayWindow.setObjectName("PlayWindow")
        PlayWindow.resize(320, 393)
        PlayWindow.setMinimumSize(QtCore.QSize(320, 393))
        PlayWindow.setMaximumSize(QtCore.QSize(320, 393))
        self.centralwidget = QtWidgets.QWidget(PlayWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(20, 20))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/x.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(20, 20))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(".\\img/o.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\img/o.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PlayWindow.setWindowIcon(icon)
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setMinimumSize(QtCore.QSize(0, 94))
        self.btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_4.setStyleSheet("border-top-style: solid;\n"
                                    "border-right-style: solid;\n"
                                    "border-bottom-style: solid;\n"
                                    "border-left-style: none;\n"
                                    "border-color: black;\n"
                                    "border-width: 1.5px;")
        iconz = QtGui.QIcon()
        iconz.addPixmap(QtGui.QPixmap("img/z.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_4.setIcon(iconz)
        self.btn_4.setIconSize(QtCore.QSize(94, 80))
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setMinimumSize(QtCore.QSize(0, 94))
        self.btn_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_7.setStyleSheet("border-top-style: solid;\n"
                                    "border-right-style: solid;\n"
                                    "border-bottom-style: none;\n"
                                    "border-left-style: none;\n"
                                    "border-color: black;\n"
                                    "border-width: 1.5px;")
        self.btn_7.setIcon(iconz)
        self.btn_7.setIconSize(QtCore.QSize(94, 80))
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 2, 0, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setMinimumSize(QtCore.QSize(0, 94))
        self.btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1.setStyleSheet("border-top-style: none;\n"
                                    "border-right-style: solid;\n"
                                    "border-bottom-style: solid;\n"
                                    "border-left-style: none;\n"
                                    "border-color: black;\n"
                                    "border-width: 1.5px;")
        self.btn_1.setIcon(iconz)
        self.btn_1.setIconSize(QtCore.QSize(94, 80))
        self.btn_1.setFlat(True)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 0, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setEnabled(True)
        self.btn_2.setMinimumSize(QtCore.QSize(0, 94))
        self.btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2.setStyleSheet("border-top-style: none;\n"
                                    "border-right-style: solid;\n"
                                    "border-bottom-style: solid;\n"
                                    "border-left-style: solid;\n"
                                    "border-color: black;\n"
                                    "border-width: 1.5px;\n"
                                    "")

        self.btn_2.setIcon(iconz)
        self.btn_2.setIconSize(QtCore.QSize(94, 80))
        self.btn_2.setFlat(True)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 0, 1, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setMinimumSize(QtCore.QSize(0, 94))
        self.btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_3.setStyleSheet("border-top-style: none;\n"
                                    "border-right-style: none;\n"
                                    "border-bottom-style: solid;\n"
                                    "border-left-style: solid;\n"
                                    "border-color: black;\n"
                                    "border-width: 1.5px;")
        self.btn_3.setIcon(iconz)
        self.btn_3.setIconSize(QtCore.QSize(94, 80))
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 0, 2, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setMinimumSize(QtCore.QSize(0, 94))
        self.btn_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_5.setStyleSheet("border-color: black;\n"
                                    "border-style: solid;\n"
                                    "border-width: 1.5px;")
        self.btn_5.setIcon(iconz)
        self.btn_5.setIconSize(QtCore.QSize(94, 80))
        self.btn_5.setDefault(False)
        self.btn_5.setFlat(True)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setMinimumSize(QtCore.QSize(0, 94))
        self.btn_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_6.setStyleSheet("border-top-style: solid;\n"
                                    "border-right-style: none;\n"
                                    "border-bottom-style: solid;\n"
                                    "border-left-style: solid;\n"
                                    "border-color: black;\n"
                                    "border-width: 1.5px;")
        self.btn_6.setIcon(iconz)
        self.btn_6.setIconSize(QtCore.QSize(94, 80))
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setMinimumSize(QtCore.QSize(0, 94))
        self.btn_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_8.setStyleSheet("border-top-style: solid;\n"
                                    "border-right-style: solid;\n"
                                    "border-bottom-style: none;\n"
                                    "border-left-style: solid;\n"
                                    "border-color: black;\n"
                                    "border-width: 1.5px;")
        self.btn_8.setIcon(iconz)
        self.btn_8.setIconSize(QtCore.QSize(94, 80))
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 2, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setMinimumSize(QtCore.QSize(0, 94))
        self.btn_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_9.setStyleSheet("border-top-style: solid;\n"
                                    "border-right-style: none;\n"
                                    "border-bottom-style: none;\n"
                                    "border-left-style: solid;\n"
                                    "border-color: black;\n"
                                    "border-width: 1.5px;")
        self.btn_9.setIcon(iconz)
        self.btn_9.setIconSize(QtCore.QSize(94, 80))
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        PlayWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PlayWindow)
        QtCore.QMetaObject.connectSlotsByName(PlayWindow)

    def retranslateUi(self, PlayWindow):
        _translate = QtCore.QCoreApplication.translate
        PlayWindow.setWindowTitle(_translate("PlayWindow", "XO"))
        self.label.setText(_translate("PlayWindow", "Player 1:"))
        self.label_2.setText(_translate("PlayWindow", "Player 2:"))


class MyWindow(QMainWindow):
    def closeEvent(self, event):
        event.ignore()
        x = QMessageBox.warning(self, "Warning", "Are You Sure?",
                                QMessageBox.Yes | QMessageBox.No)
        if x == QMessageBox.Yes:
            sys.exit()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    PlayWindow = MyWindow()
    ui = Ui_PlayWindow()
    ui.setupUi(PlayWindow)

    PlayWindow.show()
    sys.exit(app.exec_())
