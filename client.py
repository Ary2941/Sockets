import socket,threading, sys
import PySimpleGUI as sg


class client:
    def __init__(self,address):
        self.socket_name = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ('localhost',int(address))
        self.socket.connect(self.address)
        self.messages = []
        self.channels = {"todos":[]}

        ## interface
        self.column1 = []
        self.current_channel = "todos"
        self.channel_to_send = "todos"
        
        layout = [ 
            [
                [sg.Text(f"Usuário{self.socket_name}",key="USERNAME")],
            ],
            
            [ 
                sg.Table(
                    self.column1,
                    headings=["Conversas"],
                    size=(5, 6),
                    enable_events=True,
                    justification='center',
                    enable_click_events=True,
                    key ="CONVERSAS",
                    ),
                                    
                sg.Column([
                        [sg.Text("Canal atual: todos",key="CURRENTCHANNELNAME")],
                        [sg.Listbox(self.channels[self.current_channel],key='CHANNELVIEW',size=(30, 4), font=('Arial Bold', 14))]
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
                            
        self.view = sg.Window(title="Cliente",layout=layout, margins=(100, 50))

    def send_message(self):

        while 1:
            event, values = self.view.read()

            if event == sg.WIN_CLOSED:
                self.socket.close()
                sys.exit()
                break
            if event == "OK":
                
                message = values['INPUT']

                self.view['STATUS'].update(f"enviando a mensagem para o canal {self.channel_to_send}")
                
                self.channels[self.channel_to_send].append(f"eu: {message}")
                
                self.socket.send(f'{self.channel_to_send} {message}'.encode())

                self.view['INPUT'].update("")
                self.view['CHANNELVIEW'].update(self.channels[self.channel_to_send])
                print(self.channels)
                

            if '+CLICKED+' in event:
                if event[2][0] is not None: 
                    print("changing channel to:{} ".format(self.column1[event[2][0]]))
                    self.current_channel = self.column1[event[2][0]]
                    self.channel_to_send = self.column1[event[2][0]]
                    self.view['INPUT'].update("")
                    self.view['CHANNELVIEW'].update(self.channels[self.current_channel])
                    self.view['CURRENTCHANNELNAME'].update(f"Canal atual: {self.column1[event[2][0]]}")

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
                        self.channels[channel] = []
                        self.column1.append(channel)
                    print(self.channels)
                
                    ### 

                # algum cliente entrou
                elif mensagem.decode().split(" ")[0] == "link_start":
                    self.channels[mensagem.decode().split(" ")[1]] = []
                    self.column1.append(mensagem.decode().split(" ")[1])

                    self.view['CONVERSAS'].update(self.column1)
                    self.current_channel = "todos"
                    self.view['CHANNELVIEW'].update(self.channels[self.current_channel])


                    print(self.channels)

                # algum cliente saiu
                elif mensagem.decode().split(" ")[0] == "link_lost":
                    print(mensagem.decode()) #printa mensagem de perda de link
                    del self.channels[mensagem.decode().split(" ")[1]]
                    
                    if self.current_channel == mensagem.decode().split(" ")[1]:
                        self.current_channel = 'todos'
                        self.view['CHANNELVIEW'].update(self.channels[self.current_channel])
                    
                    self.column1.remove(mensagem.decode().split(" ")[1])
                    
                    self.view['CONVERSAS'].update(self.column1)

                    print(self.channels)

                # recebeu alguma mensagem em alguns do channels
                elif mensagem.decode().split(": ")[0] in self.channels.keys():
                    self.channels[mensagem.decode().split(": ")[0]].append(": ".join(mensagem.decode().split(": ")[1:]))
                    
                    print(": ".join(mensagem.decode().split(": ")[1:]))

                    att = mensagem.decode().split(": ")[0]

                    print(f"Cchanel{self.current_channel}")

                    if self.current_channel == mensagem.decode().split(": ")[0]:
                        self.view['CHANNELVIEW'].update(self.channels[mensagem.decode().split(": ")[0]])


                    print(self.channels)

                else:
                    print(f"servidor: {mensagem.decode()}")

            except(ConnectionAbortedError):
                break        
            except ConnectionError:
                print("connection lost")
                sys.exit()

    def run(self):
        thread1 = threading.Thread(target=self.send_message, args=())
        thread2 = threading.Thread(target=self.get_message, args=())


        thread1.start()
        thread2.start()

client(2143).run()

