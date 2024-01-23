import socket
import threading
import os

class UDPclient:
    def __init__(self, address):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = ('localhost', int(address))

    def send_message(self):
        while True:
            try:
                message = input("").encode()
                self.socket.sendto(message, self.address)
            except:
                os._exit(0)

    def run(self):
        thread1 = threading.Thread(target=self.send_message, args=())
        thread1.start()