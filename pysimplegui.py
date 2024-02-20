# Criando uma tela de login em Python


import PySimpleGUI as sg

layout = [
    [sg.Text('Usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('', key='mensagem')]
]

window = sg.Window('Login',layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
     usuario = values['usuario']
     senha_correta = '123456'
     usuario_correto = 'camilla'
     usuario = values['usuario']
     senha =  values['senha']
     if senha == senha_correta and usuario == usuario_correto:
         window['mensagem'].update('Login feito com sucesso')
     else:
         window['mensagem'].update('Login ou senha incorreto')
