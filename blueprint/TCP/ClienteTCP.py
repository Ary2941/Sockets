import socket,threading, os

class TCPclient:
    def __init__(self,address):
        self.socket_name = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ('localhost',int(address))

    def connect(self):
        while 1:
            try:
                self.socket.connect(self.address)
                return
            except(ConnectionRefusedError):
                pass

    def send_message(self):
        while 1:
            try:
                message = input("").encode()
                self.socket.send(message)
            except:
                os._exit(0)

    def run(self):
        self.connect()
        thread1 = threading.Thread(target=self.send_message, args=())
        thread1.start()


