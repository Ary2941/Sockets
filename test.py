import PySimpleGUI as sg
'''
channels = {"todos":[""], "123":[""]}
column1 = [
    [f'{x}'] for x in channels.keys() 
]

current_channel      = channels["todos"]
channel_to_send      = "todos"

layout=[
            [
                [sg.Text("Client Side")],
            ],
            [ 
                sg.Table(
                    column1,
                    headings=["Conversas"],
                    size=(5, 6),
                    enable_events=True,
                    justification='center',
                    enable_click_events=True,
                    key ="table",
                ),
                
                sg.Column([
                            [sg.Text("Canal atual: todos",key="CURRENTCHANNELNAME")],
                            [sg.Listbox(current_channel,key='CHANNELVIEW',size=(30, 4), font=('Arial Bold', 14))]
                            ]
                        
                        )
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

view = sg.Window(title="Hello World",layout=layout, margins=(100, 50))


while True:
    event, values = view.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    if event == "OK":
        view['STATUS'].update(f"enviando a mensagem para o canal {channel_to_send}")
        channels[channel_to_send].append(values['INPUT'])
        view['INPUT'].update("")
        view['CHANNELVIEW'].update(current_channel)
        

    if '+CLICKED+' in event:
        if event[2][0] is not None: 
            print("You clicked row:{} Column: {}".format(event[2][0], event[2][1]))
            current_channel = channels[column1[event[2][0]][0]]
            channel_to_send = column1[event[2][0]][0]
            view['INPUT'].update("")
            view['CHANNELVIEW'].update(current_channel)
            view['CURRENTCHANNELNAME'].update(f"Canal atual: {column1[event[2][0]][0]}")

    if event == "L1":
        channel_to_send = values[event][0][0]
    print(event)
'''

class view:
    def __init__(self,channels):
        self.channels   = channels
        self.column1    = [ [f'{x}'] for x in channels.keys() ]
        self.current_channel = channels["todos"]
        self.channel_to_send = self.current_channel
        
        layout=[
                    [
                        [sg.Text("Client Side")],
                    ],
                    [ 
                        sg.Table(
                            self.column1,
                            headings=["Conversas"],
                            size=(5, 6),
                            enable_events=True,
                            justification='center',
                            enable_click_events=True,
                            key ="table",
                        ),
                        
                        sg.Column([
                                    [sg.Text("Canal atual: todos",key="CURRENTCHANNELNAME")],
                                    [sg.Listbox(self.current_channel,key='CHANNELVIEW',size=(30, 4), font=('Arial Bold', 14))]
                                    ]
                                
                                )
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
    
    def show(self):
        while True:
            event, values = self.view.read()
            # End program if user closes window or
            # presses the OK button
            if event == sg.WIN_CLOSED:
                break
            if event == "OK":
                self.view['STATUS'].update(f"enviando a mensagem para o canal {channel_to_send}")
                self.channels[channel_to_send].append(values['INPUT'])
                self.view['INPUT'].update("")
                self.view['CHANNELVIEW'].update(current_channel)
                

            if '+CLICKED+' in event:
                if event[2][0] is not None: 
                    print("You clicked row:{} Column: {}".format(event[2][0], event[2][1]))
                    current_channel = self.channels[self.column1[event[2][0]][0]]
                    channel_to_send = self.column1[event[2][0]][0]
                    self.view['INPUT'].update("")
                    self.view['CHANNELVIEW'].update(current_channel)
                    self.view['CURRENTCHANNELNAME'].update(f"Canal atual: {self.column1[event[2][0]][0]}")

            if event == "L1":
                channel_to_send = values[event][0][0]
            print(event)

view({"todos":[""], "123":[""]}).show()