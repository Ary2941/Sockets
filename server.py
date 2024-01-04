import socket, threading , sys

myself = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost',2143)

myself.bind(address)
myself.listen()

print(f'{address[0]} waiting connections on {address[1]}...')

conexao1, endereco_cliente1 = myself.accept()
print(f"connection stablished with {endereco_cliente1[1]}")

conexao2, endereco_cliente2 = myself.accept()
print(f"connection stablished with {endereco_cliente2[1]}")

conexao1.send(f"you are now taling with {endereco_cliente2[1]}".encode())
conexao2.send(f"you are now taling with {endereco_cliente1[1]}".encode())

def end():
    mensagem = input()
    if mensagem:
        conexao1.close()
        conexao2.close()
        return

def get_message(prov,provAdress,rece):
    while 2143:
        try:
            message = prov.recv(2143)
            print(f"{provAdress[1]} diz: {message.decode()}")
            try:
                rece.send(f'{provAdress[1]} disse: {message.decode()}'.encode())
            
            except(ConnectionResetError):
                prov.send('Se uma árvore cai na floresta e ninguém está perto para ouvir, ela fez barulho?'.encode())
            

        except(ConnectionResetError):
            message = f'{provAdress[1]} caiu!'
            print(message)
            
            try: #mande mensagem para o outro avisando que caiu
                rece.send(message.encode())
            except(ConnectionResetError):
                pass
            
            sys.exit()

        except(ConnectionAbortedError):
            print(f"bye bye {provAdress[1]}!")
            sys.exit()





thread1 = threading.Thread(target=end, args=())
thread1.start()

thread2 = threading.Thread(target=get_message, args=(conexao1,endereco_cliente1,conexao2))
thread2.start()

thread3 = threading.Thread(target=get_message, args=(conexao2,endereco_cliente2,conexao1))
thread3.start()

thread2.join()
thread3.join()







