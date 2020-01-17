from PyQt5.QtCore import QThread, pyqtSignal
import socket
import errno


class ClientThread(QThread):
    oppo = pyqtSignal(str)
    rply = pyqtSignal(str)
    error = pyqtSignal(str)
    rematch = pyqtSignal(str)
    draw = pyqtSignal(str)

    def __init__(self, username, ip, parent=None):
        super(ClientThread, self).__init__(parent)
        self.username = username
        self.ip = ip

    def run(self):
        rcv = False
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((self.ip, 1234))
            self.s.sendall(bytes(self.username, 'utf-8'))
        except ConnectionRefusedError as e:
            self.error.emit("nTarget Refused to Connect")

        try:
            while True:
                msg = self.s.recv(10)
                msg = msg.decode('utf-8')

                if not rcv:
                    self.oppo.emit(msg)
                    rcv = True

                elif msg == "D":
                    self.draw.emit(msg)

                elif msg == "R":
                    self.rematch.emit(msg)

                else:
                    self.rply.emit(msg)

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                if rcv:
                    self.error.emit("yOpponent Disconnected")

        except Exception as e:
            self.error.emit('yUnknown Error: {}'.format(str(e)))

    def send(self, data):
        self.s.sendall(bytes(data, "utf-8"))
