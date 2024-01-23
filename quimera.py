from blueprint import Cliente, Servidor


serveraddress = input("my address: ")
clientaddress = input("their address: ")

Servidor.server(serveraddress).run()
Cliente.client(clientaddress).run()
