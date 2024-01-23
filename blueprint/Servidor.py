import socket, threading,os

class server:
    def __init__(self,address):
        self.socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ('localhost',int(address))
        self.clients = dict()

    def listen(self):
        self.socket.bind(self.address)
        self.socket.listen()
        
        while 1:

            cliente, cliente_sitio = self.socket.accept()
            
            cliente_thread = threading.Thread(target=self.get_messages, args=(cliente,str(cliente_sitio[1]))).start()
            self.clients[str(cliente_sitio[1])] = (cliente, )            
            print(f"connection {len(self.clients)} stablished with {cliente_sitio[1]}")

    def get_messages(self,entity,entity_name):
        while 1:
            try:
                input = entity.recv(self.address[1]).decode()
                print(f"they:{input}")
            except(ConnectionResetError):
                os._exit(0)

    def run(self):
        transfer_messageThread = threading.Thread(target=self.listen)
        transfer_messageThread.start()
