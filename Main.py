import LoginGUI
import sys, socket
import Final
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon


class MainUIClass(QMainWindow, LoginGUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainUIClass, self).__init__(parent)
        self.setupUi(self)
        self.ConnectButton.clicked.connect(self.start)


    def start(self):
        self.ConnectButton.setDisabled(True)
        if self.UsernameEdit.text() == "" or self.UsernameEdit.text().strip() == "":
            QMessageBox.warning(self, "Error", "Username Cannot be Empty")
            self.ConnectButton.setDisabled(False)

        elif len(self.UsernameEdit.text()) > 8:
            QMessageBox.warning(self, "Error", "Username Cannot be More than 8 Charecters")
            self.ConnectButton.setDisabled(False)

        else:
            if self.HostBox.isChecked():
                self.server()

            else:
                import validip
                if not validip.check(self.ServerEdit.text().strip()):
                    QMessageBox.warning(self, "Error", "Invalid IP Address")
                    self.ConnectButton.setDisabled(False)
                else:
                    self.client()

    def server(self):
        import Server
        self.host = True
        self.serverclass = Server.ServerThread()
        self.serverclass.oppo.connect(self.senduser)
        self.serverclass.rply.connect(self.updates)
        self.serverclass.error.connect(self.errors)
        self.serverclass.draw.connect(self.draw)
        self.serverclass.rematch.connect(self.accepted)
        self.serverclass.start()
        self.roll()

    def client(self):
        import Client
        self.host = False
        self.clientclass = Client.ClientThread(self.UsernameEdit.text(), self.ServerEdit.text().strip())
        self.clientclass.oppo.connect(self.buildui)
        self.clientclass.rply.connect(self.updates)
        self.clientclass.error.connect(self.errors)
        self.clientclass.draw.connect(self.draw)
        self.clientclass.rematch.connect(self.rematch)
        self.clientclass.start()

    def errors(self, er):
        self.ConnectButton.setDisabled(False)
        QMessageBox.critical(self, "Error", er[1:])
        if er[0] == "y":
            sys.exit()

    def roll(self):
        try:
            if self.me == "X":
                self.me = "O"

            elif self.me == "O":
                self.me = "X"

            self.buildui()

        except:
            from random import choice
            self.me = choice(["X", "O"])
            self.getip()


    def getip(self):
        self.ip = self.serverclass.ip()
        self.mbox = QMessageBox(self)
        self.mbox.setIcon(QMessageBox.Information)
        self.mbox.setText("Waiting for Opponent to join\n\nLocal IP: {}\nExternal IP: {}".format(socket.gethostbyname(socket.gethostname()), self.ip))
        self.mbox.setWindowTitle("Waiting")
        self.mbox.setStandardButtons(QMessageBox.Cancel)
        self.mbox.setTextInteractionFlags(Qt.TextSelectableByMouse)
        if self.mbox.exec() == QMessageBox.Cancel:
            del self.me
            self.serverclass.close()
            self.ConnectButton.setDisabled(False)


    def senduser(self, oppo):
        self.mbox.done(1)
        self.oppo = oppo
        self.serverclass.send(self.me + self.UsernameEdit.text())
        self.buildui()

    def buildui(self, oppo=""):
        import GameGUI

        self.PlayWindow = GameGUI.MyWindow()
        self.gui = GameGUI.Ui_PlayWindow()
        self.gui.setupUi(self.PlayWindow)

        if self.host:
            if self.me == "X":
                self.turn = True
                self.gui.label.setText("Player 1: " + self.UsernameEdit.text())
                self.gui.label_2.setText("Player 2: " + self.oppo)
            else:
                self.turn = False
                self.gui.label.setText("Player 1: " + self.oppo)
                self.gui.label_2.setText("Player 2: " + self.UsernameEdit.text())
        else:
            try:
                if oppo[0] == "X":
                    self.me = "O"
                else:
                    self.me = "X"
                self.oppo = oppo[1:]
            except:
                pass
            if self.me == "O":
                self.turn = False
                self.gui.label.setText("Player 1: " + self.oppo)
                self.gui.label_2.setText("Player 2: " + self.UsernameEdit.text())
            else:
                self.turn = True
                self.gui.label.setText("Player 1: " + self.UsernameEdit.text())
                self.gui.label_2.setText("Player 2: " + self.oppo)

        for letter in ["x", "o", "z"]:
            exec("self.icon{} = QIcon()".format(letter))
            exec("self.icon{}.addPixmap(QPixmap(\"img/{}.png\"), QIcon.Normal, QIcon.Off)".format(letter, letter))
            exec("self.icon{}.addPixmap(QPixmap(\"img/{}.png\"), QIcon.Disabled, QIcon.Off)".format(letter, letter))

        self.play = 0
        self.order = "ZZZZZZZZZ"

        for i in range(1, 10):
            eval("self.gui.btn_{}.clicked.connect(self.btn{})".format(i, i))

        self.hide()
        self.PlayWindow.show()

    def btn1(self):
        if self.turn and self.order[0] == "Z":
            self.turn = False
            self.play += 1
            if self.me == "X":
                self.gui.btn_1.setIcon(self.iconx)
                self.order = "X" + self.order[1:]
            else:
                self.gui.btn_1.setIcon(self.icono)
                self.order = "O" + self.order[1:]

            if self.play >= 3:
                if self.order[0::4] == 3 * self.order[0]:
                    self.order = "W" + self.order
                elif self.order[:3] == 3 * self.order[0]:
                    self.order = "W" + self.order
                elif self.order[0::3] == 3 * self.order[0]:
                    self.order = "W" + self.order
                elif "Z" not in self.order:
                    self.order = "D" + self.order


            if self.host:
                self.serverclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()
            else:
                self.clientclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()


    def btn2(self):
        if self.turn and self.order[1] == "Z":
            self.turn = False
            self.play += 1
            if self.me == "X":
                self.gui.btn_2.setIcon(self.iconx)
                self.order = self.order[0] + "X" + self.order[2:]
            else:
                self.gui.btn_2.setIcon(self.icono)
                self.order = self.order[0] + "O" + self.order[2:]

            if self.play >= 3:
                if self.order[:3] == 3 * self.order[0]:
                    self.order = "W" + self.order
                elif self.order[1::3] == 3 * self.order[1]:
                    self.order = "W" + self.order
                elif "Z" not in self.order:
                    self.order = "D" + self.order

            if self.host:
                self.serverclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()
            else:
                self.clientclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()

    def btn3(self):
        if self.turn and self.order[2] == "Z":
            self.turn = False
            self.play += 1
            if self.me == "X":
                self.gui.btn_3.setIcon(self.iconx)
                self.order = self.order[:2] + "X" + self.order[3:]
            else:
                self.gui.btn_3.setIcon(self.icono)
                self.order = self.order[:2] + "O" + self.order[3:]

            if self.play >= 3:
                if self.order[:3] == 3 * self.order[0]:
                    self.order = "W" + self.order
                elif self.order[2::3] == 3 * self.order[2]:
                    self.order = "W" + self.order
                elif self.order[2::2][0:3] == 3 * self.order[2]:
                    self.order = "W" + self.order
                elif "Z" not in self.order:
                    self.order = "D" + self.order

            if self.host:
                self.serverclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()
            else:
                self.clientclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()

    def btn4(self):
        if self.turn and self.order[3] == "Z":
            self.turn = False
            self.play += 1
            if self.me == "X":
                self.gui.btn_4.setIcon(self.iconx)
                self.order = self.order[:3] + "X" + self.order[4:]
            else:
                self.gui.btn_4.setIcon(self.icono)
                self.order = self.order[:3] + "O" + self.order[4:]

            if self.play >= 3:
                if self.order[3:6] == 3 * self.order[3]:
                    self.order = "W" + self.order
                elif self.order[0::3] == 3 * self.order[0]:
                    self.order = "W" + self.order
                elif "Z" not in self.order:
                    self.order = "D" + self.order

            if self.host:
                self.serverclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()
            else:
                self.clientclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()

    def btn5(self):
        if self.turn and self.order[4] == "Z":
            self.turn = False
            self.play += 1
            if self.me == "X":
                self.gui.btn_5.setIcon(self.iconx)
                self.order = self.order[:4] + "X" + self.order[5:]
            else:
                self.gui.btn_5.setIcon(self.icono)
                self.order = self.order[:4] + "O" + self.order[5:]

            if self.play >= 3:
                if self.order[3:6] == 3 * self.order[3]:
                    self.order = "W" + self.order
                elif self.order[0::4] == 3 * self.order[0]:
                    self.order = "W" + self.order
                elif self.order[1::3] == 3 * self.order[1]:
                    self.order = "W" + self.order
                elif self.order[2::2][0:3] == 3 * self.order[2]:
                    self.order = "W" + self.order
                elif "Z" not in self.order:
                    self.order = "D" + self.order

            if self.host:
                self.serverclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()
            else:
                self.clientclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()

    def btn6(self):
        if self.turn and self.order[5] == "Z":
            self.turn = False
            self.play += 1
            if self.me == "X":
                self.gui.btn_6.setIcon(self.iconx)
                self.order = self.order[:5] + "X" + self.order[6:]
            else:
                self.gui.btn_6.setIcon(self.icono)
                self.order = self.order[:5] + "O" + self.order[6:]

            if self.play >= 3:
                if self.order[3:6] == 3 * self.order[3]:
                    self.order = "W" + self.order
                elif self.order[2::3] == 3 * self.order[2]:
                    self.order = "W" + self.order
                elif "Z" not in self.order:
                    self.order = "D" + self.order

            if self.host:
                self.serverclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()
            else:
                self.clientclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()

    def btn7(self):
        if self.turn and self.order[6] == "Z":
            self.turn = False
            self.play += 1
            if self.me == "X":
                self.gui.btn_7.setIcon(self.iconx)
                self.order = self.order[:6] + "X" + self.order[7:]
            else:
                self.gui.btn_7.setIcon(self.icono)
                self.order = self.order[:6] + "O" + self.order[7:]

            if self.play >= 3:
                if self.order[0::3] == 3 * self.order[0]:
                    self.order = "W" + self.order
                elif self.order[2::2][0:3] == 3 * self.order[2]:
                    self.order = "W" + self.order
                elif self.order[-3:] == 3 * self.order[6]:
                    self.order = "W" + self.order
                elif "Z" not in self.order:
                    self.order = "D" + self.order

            if self.host:
                self.serverclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()
            else:
                self.clientclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()

    def btn8(self):
        if self.turn and self.order[7] == "Z":
            self.turn = False
            self.play += 1
            if self.me == "X":
                self.gui.btn_8.setIcon(self.iconx)
                self.order = self.order[:7] + "X" + self.order[8:]
            else:
                self.gui.btn_8.setIcon(self.icono)
                self.order = self.order[:7] + "O" + self.order[8:]

            if self.play >= 3:
                if self.order[1::3] == 3 * self.order[1]:
                    self.order = "W" + self.order
                elif self.order[-3:] == 3 * self.order[6]:
                    self.order = "W" + self.order
                elif "Z" not in self.order:
                    self.order = "D" + self.order

            if self.host:
                self.serverclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()
            else:
                self.clientclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()

    def btn9(self):
        if self.turn and self.order[8] == "Z":
            self.turn = False
            self.play += 1
            if self.me == "X":
                self.gui.btn_9.setIcon(self.iconx)
                self.order = self.order[:-1] + "X"
            else:
                self.gui.btn_9.setIcon(self.icono)
                self.order = self.order[:-1] + "O"


            if self.play >= 3:
                if self.order[-3:] == 3 * self.order[6]:
                    self.order = "W" + self.order
                elif self.order[0::4] == 3 * self.order[0]:
                    self.order = "W" + self.order
                elif self.order[2::3] == 3 * self.order[2]:
                    self.order = "W" + self.order
                elif "Z" not in self.order:
                    self.order = "D" + self.order


            if self.host:
                self.serverclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()
            else:
                self.clientclass.send(self.order)
                if self.order[0] == "W":
                    self.win()
                elif self.order[0] == "D":
                    self.draw()

    def updates(self, rply):
        lose = False
        draw = False
        if rply[0] == "W":
            rply = rply[1:]
            lose = True
        elif rply[0] == "D":
            rply = rply[1:]
            draw = True

        self.order = rply
        for i, n in zip(rply, range(1,10)):
            exec("self.gui.btn_{}.setIcon(self.icon{})".format(str(n), i.lower()))
        self.turn = True

        if lose:
            self.lose()
        if draw:
            self.draw()

    def win(self):
        import Final

        self.Form = Final.MyDialog()
        self.fui = Final.Ui_Dialog()
        self.fui.setupUi(self.Form)
        self.fui.Exit.clicked.connect(self.out)
        self.fui.Rematch.clicked.connect(self.rematch)
        self.fui.label.setPixmap(QPixmap(".\\img/win.png"))
        self.Form.exec()

    def lose(self):
        import Final

        self.Form = Final.MyDialog()
        self.fui = Final.Ui_Dialog()
        self.fui.setupUi(self.Form)
        self.fui.Exit.clicked.connect(self.out)
        self.fui.Rematch.clicked.connect(self.rematch)
        self.Form.exec()

    def draw(self):
        import Final

        self.Form = Final.MyDialog()
        self.fui = Final.Ui_Dialog()
        self.fui.setupUi(self.Form)
        self.fui.Exit.clicked.connect(self.out)
        self.fui.label.setPixmap(QPixmap(".\\img/draw.png"))
        self.fui.Rematch.clicked.connect(self.rematch)
        self.Form.exec()


    def out(self):
        self.Form.reject()
        sys.exit()

    def rematch(self, data=""):
        if self.host:
            self.serverclass.send("R")
            self.fui.Rematch.setDisabled(True)
        else:
            if data == "R":
                self.orem = True
            else:
                self.rem = True
                self.fui.Rematch.setDisabled(True)
            try:
                if self.rem and self.orem:
                    self.clientclass.send("A")
                    self.accepted()
            except:
                pass

    def accepted(self):
        self.rem = False
        self.orem = False
        self.Form.reject()
        self.PlayWindow.hide()
        self.roll()

    def closeEvent(self, event):
        event.ignore()
        x = QMessageBox.warning(self, "Warning", "Are You Sure?",
                                QMessageBox.Yes | QMessageBox.No)
        if x == QMessageBox.Yes:
            sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUIClass()
    window.show()
    app.exec_()
