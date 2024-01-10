import socket,threading, sys

try:
    server_address=('localhost',int(sys.argv[1]))
except(IndexError):
    print("para rodar o aquivo favor executar no formato: python client.py *coloque aqui o servidor*")
    sys.exit()


run_send_message = True
run_get_message = True


try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    they, their_address = client_socket,server_address  

except(ConnectionRefusedError):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen()
    #print(f'{server_address[0]} waiting connections on {server_address[1]}...')
    
    client_socket.connect(server_address)
    me, my_address = server_socket.accept()
    they, their_address = server_socket.accept()

    they.send(f"MYADDRESS {their_address[1]} {my_address[1]}".encode())
    print(f"we ({my_address[1]}) are in localhost:{server_address[1]} talking with {their_address[1]}")


def send_message():
    while run_send_message:
        mensagem = input("")
        if mensagem == "!quit":
            client_socket.close()
            they.close()
            sys.exit()
        try:
            they.send(f"MESSAGE {my_address[1]}: {mensagem}".encode())

        except(ConnectionResetError,EOFError):
            client_socket.close()
            sys.exit()

def get_message():
    global run_send_message
    global run_get_message
    global my_address
    
    while run_get_message:
        try:
            mensagem = they.recv(2143).decode()
            if mensagem.split(" ")[0] == "MESSAGE":
                print(" ".join(mensagem.split(" ")[1:]) )

            if mensagem.split(" ")[0] == "MYADDRESS":
                my_address = (mensagem.split(" ")[2],mensagem.split(" ")[1])
                print(f"we ({my_address[1]}) are in localhost:{server_address[1]} talking with {my_address[0]}")
        
        except(ConnectionAbortedError):
            break        
        except ConnectionError:
            print("!quit")
            import os
            os._exit(0) 


thread1 = threading.Thread(target=send_message, args=())
thread1.start()

thread2 = threading.Thread(target=get_message, args=())
thread2.start()



thread1.join()