import socket, threading , sys

# canal 0 = todos
# canal numero específico = cliente específico

class server:
    def __init__(self,address):
        self.socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ('localhost',int(address))
        self.clients = dict()

    def transfer_message(self,entity,entity_name):
        while 1:
            input = entity.recv(self.address[1]).decode()

            channel = (input.split(" ")[0])
            input = input.split(" ")[1:]

            input = " ".join(input)

            entity_response = f"{entity_name} disse para o canal {channel}: {input}"
            input = f"{entity_name}: "+input

            if channel == 'all':
                 for all_clients in self.clients.keys()-[entity_name]:
                    self.clients[all_clients][0].send(input.encode())

            else:
                self.clients[channel][0].send(input.encode())
            

            print(entity_response)
            


    def listen(self):
        self.socket.bind(self.address)
        self.socket.listen()
        
        while 1:
            cliente, cliente_sitio = self.socket.accept() 
            self.clients[str(cliente_sitio[1])] = (cliente, threading.Thread(target=self.transfer_message, args=(cliente,str(cliente_sitio[1]))).start())            
            cliente.send(f"você entrou no servidor como {cliente_sitio[1]}".encode())
            print(f"connection {len(self.clients)} stablished with {cliente_sitio[1]}")

    def broadcast(self):
        while 1:
            mensagem = input("")
            if mensagem == "!quit":
                pass

            for client in self.clients.keys():
                self.clients[client][0].send(mensagem.encode())


    def run(self):
        transfer_messageThread = threading.Thread(target=self.listen)
        broadcastThread = threading.Thread(target=self.broadcast)

        transfer_messageThread.start()
        broadcastThread.start()

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