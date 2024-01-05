import socket, threading , sys



class server:
    def __init__(self,address):
        self.socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ('localhost',int(address))
        self.connections = []


    def hear(self,entity,entity_name,connections_index):
        while 1:
            entity_response = entity.recv(self.address[1])

            print(f"{entity_name} disse: {entity_response.decode()}")


    def listen(self):
        self.socket.bind(self.address)
        self.socket.listen()
        print(f'{self.address[0]} waiting connections on {self.address[1]}...')

        while 1:
            cliente, cliente_sitio = self.socket.accept()
            
            self.connections += [(cliente,cliente_sitio,threading.Thread(target=self.hear, args=(cliente,cliente_sitio[1],len(self.connections)-1)).start() )] #o socket, o endereço do mesmo, e uma thread que recebe as mensagens do socket
            print(f"connection {len(self.connections)} stablished with {self.connections[len(self.connections)-1][1]}")

    def broadcast(self):
        while 1:
            mensagem = input("")
            if mensagem == "!quit":
                pass

            for conexao in self.connections:
                conexao[0].send(mensagem.encode())


    def run(self):
        listenthread = threading.Thread(target=self.listen)
        broadcastthread = threading.Thread(target=self.broadcast)

        listenthread.start()
        broadcastthread.start()

server(2143).run()


'''
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







'''