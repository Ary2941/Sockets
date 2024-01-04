import socket,threading, sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address=('localhost',2143)

try:
    client_socket.connect(server_address)
    they, their_address = client_socket,server_address

except(ConnectionRefusedError):
    server_socket.bind(server_address)
    server_socket.listen()
    print(f'{server_address[0]} waiting connections on {server_address[1]}...')
    
    client_socket.connect(server_address)
    me, my_address = server_socket.accept()

    they, their_address = server_socket.accept()
    print(f"({server_address[1]}) we ({my_address[1]}) are talking with ({their_address[1]})")

    they.send(f"we ({their_address[1]}) are talking with ({my_address[1]})".encode())

def send_message():
    while 1:
        mensagem = input("")
        if mensagem == "!quit":
            client_socket.close()
            they.close()
            sys.exit()
        try:
            they.send(mensagem.encode())

        except(ConnectionResetError):
            client_socket.close()
            sys.exit()

thread1 = threading.Thread(target=send_message, args=())
thread1.start()


def get_message():
    while 1:
        try:
            mensagem = they.recv(2143)
            print(f'({server_address[1]})',mensagem.decode())
        except(ConnectionAbortedError):
            break        
        except ConnectionError:
            print("a conversa se encerrou!")
            sys.exit()

thread2 = threading.Thread(target=get_message, args=())
thread2.start()

thread1.join()