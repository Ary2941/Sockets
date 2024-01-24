import socket
import threading
import os

class UDPserver:
    def __init__(self, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = ('localhost', int(port))
        self.clients = dict()
        self.port = port

    def listen(self):
        self.socket.bind(self.address)

        while True:
            data, client_address = self.socket.recvfrom(int(self.port))

            client_thread = threading.Thread(target=self.get_messages, args=(data, client_address))
            client_thread.start()

            self.clients[str(client_address[1])] = client_address

    def get_messages(self, data, client_address):
        print(f"{self.port}: {data.decode()}")

    def run(self):
        transfer_message_thread = threading.Thread(target=self.listen)
        transfer_message_thread.start()

