import socket,threading, sys

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

endereco_servidor=('localhost',2143)
cliente.connect(endereco_servidor)
quit_event = threading.Event()

def send_message(quit_event):
    while not quit_event.is_set():
        mensagem = input("")
        cliente.send(mensagem.encode())
    cliente.close()

thread1 = threading.Thread(target=send_message, args=(quit_event,))
thread1.start()



try:
    while not quit_event.is_set():
        mensagem = cliente.recv(2143)
        if not mensagem:
            print("conexão encerrada pelo server!")
            break
        print(f'({endereco_servidor[1]})',mensagem.decode())

except ConnectionError:
    print("Conexão perdida com o servidor!")
    quit_event.set()
    thread1.join()
    cliente.close() 
    sys.exit()