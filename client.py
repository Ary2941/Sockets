import socket,threading, sys
import PySimpleGUI as sg


class client:
    def __init__(self,address):
        self.socket_name = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ('localhost',int(address))
        self.socket.connect(self.address)
        self.messages = []
        self.channels = {"todos":["",[]]}
        self.current_channel = "todos"
        self.channel_to_send = "todos"


    def send_message(self):

        while 1:
            event, values = self.view.read()

            if event == sg.WIN_CLOSED:
                self.socket.close()
                sys.exit()
                break
            if event == "OK":
                
                message = values['INPUT']

                self.channels[self.channel_to_send][1].append(f"eu: {message}")
                
                self.socket.send(f'{self.channel_to_send} {message}'.encode())

                self.view['INPUT'].update("")
                self.view['CHANNELVIEW'].update(self.channels[self.channel_to_send][1])
                self.view['CHANNELVIEW'].Widget.yview('moveto', '1.0')
                

            if '+CLICKED+' in event:
                if event[2][0] is not None: 
                    channel_clicked = list(self.channels.keys())[event[2][0]]
                    self.channels[channel_clicked][0] = ""
                    self.current_channel = channel_clicked
                    self.channel_to_send = channel_clicked
                    self.view['INPUT'].update("")
                    self.view['CHANNELVIEW'].update(self.channels[self.current_channel][1])
                    self.view['CURRENTCHANNELNAME'].update(f"Canal atual: {channel_clicked}")
                    self.view['CONVERSAS'].update([[channelname, self.channels[channelname][0]] for channelname in list(self.channels.keys())])


            if event == "L1":
                channel_to_send = values[event][0][0]




    def get_message(self):
        while 1:
            try:
                mensagem = self.socket.recv(2143)
                                
                # entramos
                if mensagem.decode().split(" ")[0] == "self_start":
                    self.socket_name = mensagem.decode().split(" ")[1].split(",")[0]

                    ## criando o channels da interface
                    for channel in mensagem.decode().split(" ")[1].split(",")[1:]:
                        self.channels[channel] = ["",[]]

                # algum cliente entrou
                elif mensagem.decode().split(" ")[0] == "link_start":
                    self.channels[mensagem.decode().split(" ")[1]] = ["",[]]

                    self.view['CONVERSAS'].update([[channelname, self.channels[channelname][0]] for channelname in list(self.channels.keys())])
                    self.current_channel = "todos"
                    self.view['CHANNELVIEW'].update(self.channels[self.current_channel][1])

                # algum cliente saiu
                elif mensagem.decode().split(" ")[0] == "link_lost":
                    print(mensagem.decode()) #printa mensagem de perda de link
                    del self.channels[mensagem.decode().split(" ")[1]]
                    
                    if self.current_channel == mensagem.decode().split(" ")[1]:
                        self.current_channel = 'todos'
                        self.view['CHANNELVIEW'].update(self.channels[self.current_channel][1])
                                        
                    self.view['CONVERSAS'].update([[channelname, self.channels[channelname][0]] for channelname in list(self.channels.keys())])

                # recebeu alguma mensagem em alguns do channels
                elif mensagem.decode().split(": ")[0] in self.channels.keys():
                    self.channels[mensagem.decode().split(": ")[0]][1].append(": ".join(mensagem.decode().split(": ")[1:]))
                    
                    print(": ".join(mensagem.decode().split(": ")[1:]))

                    att = mensagem.decode().split(": ")[0]

                    if self.current_channel == att:
                        self.view['CHANNELVIEW'].update(self.channels[att][1])
                        self.view['CHANNELVIEW'].Widget.yview('moveto', '1.0')

                    elif self.current_channel != att:
                        self.channels[att][0] = "+"
                        self.view['STATUS'].update(f"Mensagem recebida na conversa com {att}")
                    self.view['CONVERSAS'].update([[channelname, self.channels[channelname][0]] for channelname in list(self.channels.keys())])

                else:
                    print(f"servidor: {mensagem.decode()}")

            except(ConnectionAbortedError):
                break        
            except ConnectionError:
                print("connection lost")
                sys.exit()

    def run(self):


        layout = [ 
            [
                [sg.Text(f"Usuário{self.socket_name}",key="USERNAME")],
            ],
            
            [ 
                sg.Table(
                    self.channels,
                    headings=["Conversas"," + "],
                    size=(5, 6),
                    enable_events=True,
                    justification='center',
                    enable_click_events=True,
                    key ="CONVERSAS",
                    ),
                                    
                sg.Column([
                        [sg.Text("Canal atual: todos",key="CURRENTCHANNELNAME")],
                        [sg.Listbox(self.channels[self.current_channel][1],key='CHANNELVIEW',auto_size_text=True,size=(30, 10), font=('Arial Bold', 14))]
                    ])
            ], 

            [
                sg.Input(size=(20, 1), font=('Arial Bold', 14), expand_x=True, key='INPUT'),
                sg.Button("OK"),
            ],
                [
                                
                            ],
                            [
                                sg.Text("",key='STATUS'),
                            ],
        ]
        self.view = sg.Window(title="Cliente",layout=layout, margins=(1, 1))
        thread1 = threading.Thread(target=self.send_message, args=())
        thread2 = threading.Thread(target=self.get_message, args=())


        thread1.start()
        thread2.start()

client(2143).run()

