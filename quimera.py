from blueprint import Cliente, Servidor


serveraddress = input("server address: ")
clientaddress = input("client address: ")

Servidor.server(serveraddress).run()
Cliente.client(clientaddress).run()