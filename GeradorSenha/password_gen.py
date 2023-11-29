import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        sg.theme('DarkPurple4')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
             sg.Input(key='site', size=(20,1))],
             [sg.Text('Email/Usuário', size=(10, 1)),
             sg.Input(key='usuario', size=(20, 1))],
             [sg.Text('Quantidade caracteres'), sg.Combo(values=list(
                 range(5, 31)), key='total_chars', default_value=5, size=(3, 1))],
                 [sg.Output(size=(32, 5))],
                 [sg.Button('Gerar Senha'), sg.Button('Close', pad=((115, 0), 5))]
                 
        ]
        # Declarar janela
        self.janela = sg.Window('Password Generator', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Close':
                sg.popup('Obrigado por usar! :)', pad=(10, 0))
                break
            
            if evento == 'Gerar Senha':
                if valores['site'] and valores['usuario']:
                    nova_senha = self.gerar_senha(valores)
                    print(nova_senha)
                    self.salvar_senha(nova_senha, valores)
                else:
                    sg.popup('Os campos site/usuário são obrigatórios.', button_color=('white', 'red'))

            

    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*?+-='
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass
    
    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"site: {valores['site']}, usuario: {valores['usuario']}, nova senha: {nova_senha}\n\n")
        print('Arquivo Salvo')

gen = PassGen()
gen.Iniciar()