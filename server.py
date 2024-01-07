import socket, threading , sys

class server:
    def __init__(self,address):
        self.socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ('localhost',int(address))
        self.clients = dict()


    def avise_todos(self,message):
        for all_clients in self.clients.keys():
            self.clients[all_clients][0].send(message.encode())

    def avise_todos_menos_ele(self,ele,message):
        for all_clients in self.clients.keys()-[ele]:
            self.clients[all_clients][0].send(message.encode())



    def transfer_message(self,entity,entity_name):
        while 1:
            try:
                input = entity.recv(self.address[1]).decode()
                channel = (input.split(" ")[0])
                input = input.split(" ")[1:]

                input = " ".join(input)

                if channel == 'todos':
                    entity_response = f"{entity_name} disse para todos no server: {input}"
                    input = f"{entity_name} disse para todos: "+input
                    self.avise_todos_menos_ele(entity_name,input) #envie para todos os clientes menos o emissor

                elif entity_name != channel:
                    try:
                        entity_response = f"{entity_name} disse para {channel}: {input}"
                        input = f"{entity_name} disse: "+input 
                        self.clients[channel][0].send(input.encode()) #envie só pra um cliente

                    except(KeyError):
                        
                        entity_response = f'{input} para {channel} mas a mensagem foi perdida.'
                        entity.send(f"{channel} quem?".encode()) #não envie a mensagem

                else:
                    entity_response = f'{entity_name} disse para sim mesmo: {input}.'
                    input = f"{entity_name}: "+input
                    self.clients[channel][0].send(input.encode()) #devolva ao emissor
                
                print(entity_response)
            
            except(ConnectionResetError):
                input =f"{entity_name} saiu!!"
                print (input)
                del self.clients[entity_name]
                self.avise_todos(input)
                sys.exit()


    def listen(self):
        self.socket.bind(self.address)
        self.socket.listen()
        
        while 1:
            cliente, cliente_sitio = self.socket.accept() 
            self.clients[str(cliente_sitio[1])] = (cliente, threading.Thread(target=self.transfer_message, args=(cliente,str(cliente_sitio[1]))).start())            
            cliente.send(f"você entrou no servidor como {cliente_sitio[1]}".encode())
            print(f"connection {len(self.clients)} stablished with {cliente_sitio[1]}")
            
            whoishere = ""

            for all_clients in self.clients.keys()-[str(cliente_sitio[1])]:
                whoishere += ", "+ all_clients
                self.clients[all_clients][0].send(f"{cliente_sitio[1]} entrou.".encode())
            
            if len(self.clients) > 1:
                cliente.send(f"\nestão na sala:{whoishere[1:]}".encode())
            else:
                cliente.send(f"\nfora você, não há ninguém na sala.".encode())

    def broadcast(self):
        while 1:
            try:
                mensagem = input("")

                self.avise_todos(mensagem)
            except(EOFError,KeyboardInterrupt):
                self.socket.close()
                sys.exit()
                
    def run(self):
        transfer_messageThread = threading.Thread(target=self.listen)
        broadcastThread = threading.Thread(target=self.broadcast)

        transfer_messageThread.start()
        broadcastThread.start()

server(2143).run()
