from PyQt5.QtCore import QThread, pyqtSignal
import socket, errno


class ServerThread(QThread):
    oppo = pyqtSignal(str)
    rply = pyqtSignal(str)
    error = pyqtSignal(str)
    rematch = pyqtSignal(str)
    draw = pyqtSignal(str)

    def __init__(self, parent=None):
        super(ServerThread, self).__init__(parent)

    def run(self):
        try:
            rcv = False
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind(('0.0.0.0', 1234))
            self.s.listen(1)
            self.clientsocket, self.address = self.s.accept()
            while True:
                while True:
                    msg = self.clientsocket.recv(10)
                    msg = msg.decode('utf-8')

                    if not rcv:
                        self.oppo.emit(msg)
                        rcv = True

                    elif msg == "D":
                        self.draw.emit(msg)

                    elif msg == "A":
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
        self.clientsocket.send(bytes(data, "utf-8"))

    def ip(self):
        try:
            from requests import get
            req = get('http://api.ipify.org', timeout=3)
            return req.text
        except:
            return ""

    def close(self):
        self.s.close()
