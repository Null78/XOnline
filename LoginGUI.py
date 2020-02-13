# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\xoGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(320, 393)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(320, 393))
        MainWindow.setMaximumSize(QtCore.QSize(320, 393))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.UsernameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UsernameEdit.setObjectName("UsernameEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.UsernameEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.ServerEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ServerEdit.setObjectName("ServerEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ServerEdit)
        self.HostBox = QtWidgets.QCheckBox(self.centralwidget)
        self.HostBox.setObjectName("HostBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.HostBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.ConnectButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConnectButton.sizePolicy().hasHeightForWidth())
        self.ConnectButton.setSizePolicy(sizePolicy)
        self.ConnectButton.setMinimumSize(QtCore.QSize(0, 35))
        self.ConnectButton.setObjectName("ConnectButton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.ConnectButton)
        self.StatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.StatusLabel.setText("")
        self.StatusLabel.setObjectName("StatusLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.StatusLabel)
        self.gridLayout.addLayout(self.formLayout, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.XOLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.XOLabel.sizePolicy().hasHeightForWidth())
        self.XOLabel.setSizePolicy(sizePolicy)
        self.XOLabel.setText("")
        self.XOLabel.setPixmap(QtGui.QPixmap("./img/xo.png"))
        self.XOLabel.setScaledContents(True)
        self.XOLabel.setObjectName("XOLabel")
        self.gridLayout.addWidget(self.XOLabel, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\img/o.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.retranslateUi(MainWindow)
        self.HostBox.clicked['bool'].connect(self.ServerEdit.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XO: Login"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Server IP"))
        self.HostBox.setText(_translate("MainWindow", "I\'m the host"))
        self.ConnectButton.setText(_translate("MainWindow", "Start"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
