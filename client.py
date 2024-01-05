import socket,threading, sys

class client:
    def __init__(self,address):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ('localhost',int(address))
        self.socket.connect(self.address)

    def send_message(self):
        while 1:
            mensagem = input("")
            if mensagem == "!quit":
                self.socket.close()
                sys.exit()
            try:
                self.socket.send(mensagem.encode())

            except(ConnectionResetError):
                self.socket.close()
                sys.exit()

    def get_message(self):
        while 1:
            try:
                mensagem = self.socket.recv(2143)
                print(f'({self.address[1]})',mensagem.decode())
            except(ConnectionAbortedError):
                break        
            except ConnectionError:
                print("servidor fechou!")
                sys.exit()


    def run(self):
        thread1 = threading.Thread(target=self.send_message, args=())
        thread2 = threading.Thread(target=self.get_message, args=())

        thread1.start()
        thread2.start()

'''
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

endereco_servidor=('localhost',2143)
server.connect(endereco_servidor)


def send_message():
    while 1:
        mensagem = input("")
        if mensagem == "!quit":
            server.close()
            sys.exit()
        try:
            server.send(mensagem.encode())

        except(ConnectionResetError):
            server.close()
            sys.exit()



def get_message():
    while 1:
        try:
            mensagem = server.recv(2143)
            print(f'({endereco_servidor[1]})',mensagem.decode())
        except(ConnectionAbortedError):
            break        
        except ConnectionError:
            print("servidor fechou!")
            sys.exit()


thread1 = threading.Thread(target=send_message, args=())


thread2 = threading.Thread(target=get_message, args=())

thread1.start()
thread2.start()

'''

client(2143).run()