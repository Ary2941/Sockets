import socket,threading,sys,os

from datetime import datetime

import PySimpleGUI as sg

#####################################################################################################################################
try:
    server_address=('localhost',int(sys.argv[1]))
except(IndexError):
    print("para rodar o aquivo favor executar no formato: python client.py *coloque aqui o servidor*")
    sys.exit()

print("link start!")
#####################################################################################################################################

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client_socket.connect(server_address)
    they, their_address = client_socket,server_address  
    mensagem = they.recv(2143).decode()
    my_address = (mensagem.split(" ")[2],mensagem.split(" ")[1])
    print(f"we ({my_address[1]}) are in localhost:{server_address[1]} talking with {my_address[0]}")
    mytheme = 'DarkPurple1'

except(ConnectionRefusedError):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except(KeyboardInterrupt):
        print("!quit")
        sys.exit()

    server_socket.bind(server_address)
    server_socket.listen()    
    client_socket.connect(server_address)
    me, my_address = server_socket.accept()
    they, their_address = server_socket.accept()
    they.send(f"MYADDRESS {their_address[1]} {my_address[1]}".encode())
    print(f"we ({my_address[1]}) are in localhost:{server_address[1]} talking with {their_address[1]}")
    mytheme = 'DarkTeal1'

mensagens = []

#####################################################################################################################################



sg.theme(mytheme) 
layout = [  
            [sg.Text(f'Usuário {my_address[1]}')],
            [sg.Listbox(mensagens, size=(30, 4), font=('Arial Bold', 14), expand_y=True,expand_x=True, key='LIST')],
            [sg.InputText(key="MESSAGE INPUT"),sg.Button('mandar',key = "SEND")],
            [] 
        ]

# Create the Window
window = sg.Window('Window Title', layout)


#####################################################################################################################################
def send_message():
    try:
        while 1:
            mensagem = input("")
            if mensagem == "!quit":
                they.send("!quit".encode())
                os._exit(0)

            mensagens.append(f"Eu: {mensagem}" ) 
            they.send(f"MESSAGE {my_address[1]}: {mensagem}".encode())

            window["LIST"].update(mensagens) #interface
            window['LIST'].Widget.yview_moveto(1)

    
    except Exception as e:
        print("!quit")
        they.send("!quit".encode())
        os._exit(0)

#####################################################################################################################################
def get_message():
    while 2:
        try:
            mensagem = they.recv(2143).decode()
            if mensagem.split(" ")[0] == "MESSAGE":
                print(" ".join(mensagem.split(" ")[1:]) )
                mensagens.append(" ".join(mensagem.split(" ")[1:]) )

                window["LIST"].update(mensagens) #interface
                window['LIST'].Widget.yview_moveto(1)

            if mensagem == "!quit":
                print("!quit")
                os._exit(0)
        except(ConnectionResetError):
            print("!quit")
            os._exit(0)   


#####################################################################################################################################
thread1 = threading.Thread(target=send_message, args=())
thread1.start()

thread2 = threading.Thread(target=get_message, args=())
thread2.start()

#####################################################################################################################################


while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        print("!quit")
        they.send("!quit".encode())
        os._exit(0)

    if event == "SEND":
        mensagem = values["MESSAGE INPUT"]
        mensagens.append(f"Eu: {mensagem}")
        print(f"Eu: {mensagem}")
        they.send(f"MESSAGE {my_address[1]}: {mensagem}".encode())
        window["LIST"].update(mensagens)
        window["MESSAGE INPUT"].update("")

        window['LIST'].Widget.yview_moveto(1)
