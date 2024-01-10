import socket,threading,sys,os

try:
    server_address=('localhost',int(sys.argv[1]))
except(IndexError):
    print("para rodar o aquivo favor executar no formato: python client.py *coloque aqui o servidor*")
    sys.exit()

print("link start!")

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client_socket.connect(server_address)
    they, their_address = client_socket,server_address  
    mensagem = they.recv(2143).decode()
    my_address = (mensagem.split(" ")[2],mensagem.split(" ")[1])
    print(f"we ({my_address[1]}) are in localhost:{server_address[1]} talking with {my_address[0]}")

except(ConnectionRefusedError):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except(KeyboardInterrupt):
        print("!quit")
        sys.exit()

    server_socket.bind(server_address)
    server_socket.listen()    
    client_socket.connect(server_address)
    me, my_address = server_socket.accept()
    they, their_address = server_socket.accept()
    they.send(f"MYADDRESS {their_address[1]} {my_address[1]}".encode())
    print(f"we ({my_address[1]}) are in localhost:{server_address[1]} talking with {their_address[1]}")


def send_message():
    try:
        while 1:
            mensagem = input("")
            if mensagem == "!quit":
                they.send("!quit".encode())
                os._exit(0)
            they.send(f"MESSAGE {my_address[1]}: {mensagem}".encode())
    
    except Exception as e:
        print("!quit")
        they.send("!quit".encode())
        os._exit(0)

thread1 = threading.Thread(target=send_message, args=())
thread1.start()

def get_message():
    while 2:
        try:
            mensagem = they.recv(2143).decode()
            if mensagem.split(" ")[0] == "MESSAGE":
                print(" ".join(mensagem.split(" ")[1:]) )
           
            if mensagem == "!quit":
                print("!quit")
                os._exit(0)
 
        except (ConnectionError,OSError):
            pass

thread2 = threading.Thread(target=get_message, args=())

thread2.start()