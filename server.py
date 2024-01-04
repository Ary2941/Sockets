import socket, threading , sys

myself = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost',2143)

myself.bind(address)
myself.listen()

print('waiting port connections 1', address[1])
conexao1, endereco_cliente1 = myself.accept()
print("connection stablished avec",  endereco_cliente1)

print('waiting port connections 2', address[1])
conexao2, endereco_cliente2 = myself.accept()
print("connection stablished avec",  endereco_cliente2)

def end():
    mensagem = input()
    if mensagem:
        conexao1.close()
        conexao2.close()

        threading.Event()

        return

def get_message(prov,provAdress,rece):
    print("getMessage")
    while 2143:
        try:
            message = prov.recv(2143)
            print(f"{provAdress[1]} diz: {message.decode()}")
            rece.send(f' {provAdress[1]} disse: {message.decode()}'.encode())
        except(ConnectionAbortedError):
            print(f"bye bye {provAdress[1]}!")
            return

thread2 = threading.Thread(target=get_message, args=(conexao1,endereco_cliente1,conexao2))
thread2.start()

thread3 = threading.Thread(target=get_message, args=(conexao2,endereco_cliente2,conexao1))
thread3.start()

thread1 = threading.Thread(target=end, args=())
thread1.start()
thread2.join()
thread3.join()





