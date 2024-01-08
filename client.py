import socket,threading, sys
import PySimpleGUI as sg


class client:
    def __init__(self,address):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ('localhost',int(address))
        self.socket.connect(self.address)
        self.messages = []
        self.channels = []

    def send_message(self):
        while 1:
            try:
                mensagem = input("")
                if mensagem == "!quit":
                    self.socket.close()
                    sys.exit()
                try:
                    self.socket.send(mensagem.encode())

                except(ConnectionResetError,EOFError):
                    self.socket.close()
                    sys.exit()
            except(ConnectionResetError,EOFError,KeyboardInterrupt):
                    self.socket.close()
                    sys.exit()


    def get_message(self):
        while 1:
            try:
                mensagem = self.socket.recv(2143)
                print(mensagem.decode())
                self.messages.append(mensagem.decode())
                if mensagem.decode().split(",")[0] == "todos":
                    for channel in mensagem.decode().split(","):
                        if channel not in self.channels:
                            self.channels.append(channel)

                if mensagem.decode().split(" ")[0] == "link_lost":
                    print(mensagem.decode().split(" ")[0])
                    self.channels.remove(mensagem.decode().split(" ")[1])

                print(self.channels)

            except(ConnectionAbortedError):
                break        
            except ConnectionError:
                print("connection lost")
                sys.exit()

    def run(self):
        thread1 = threading.Thread(target=self.send_message, args=())
        thread2 = threading.Thread(target=self.get_message, args=())


        thread1.start()
        thread2.start()

client(2143).run()

