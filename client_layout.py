import PySimpleGUI as sg

layout = [ 
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
