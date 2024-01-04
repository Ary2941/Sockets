import socket,threading, sys

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

thread1 = threading.Thread(target=send_message, args=())
thread1.start()


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

thread2 = threading.Thread(target=get_message, args=())
thread2.start()