import sys

from blueprint.TCP import ClienteTCP,ServidorTCP
from blueprint.UDP import ClienteUDP,ServidorUDP


type = sys.argv[1].upper()

print(f"protocolo usado: {type}")



serveraddress = input("minha porta: ")
clientaddress = input("porta do amigo: ")

if type == "TCP":
    ServidorTCP.TCPserver(serveraddress).run()
    ClienteTCP.TCPclient(clientaddress).run()

if type == "UDP":
    ServidorUDP.UDPserver(serveraddress).run()
    ClienteUDP.UDPclient(clientaddress).run()
