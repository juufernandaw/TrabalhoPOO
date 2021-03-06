import PySimpleGUI as sg


class TelaSistema:
    def __init__(self):
        self.__window = None
        self.layout_mostrar_menu_inicial()
        self.layout_logar_aluno()
        self.layout_logar_personal()

        # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado precisa chamar
        # self.init_components() aqui para o caso de chamar essa janela uma 2a vez. Não é possível reusar layouts de
        # janelas depois de fechadas.
    def logar(self, opcao_escolhida):
        if opcao_escolhida == 1:
            self.layout_logar_aluno()
        elif opcao_escolhida == 2:
            self.layout_logar_personal()
        button, values = self.__window.Read()
        login = values['login']
        senha = values['senha']
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if button == 'Retornar':
            self.close()
        self.close()
        return login, senha

    def mostrar_menu_inicial(self):
        self.layout_mostrar_menu_inicial()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        elif button == 'Sair':
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def layout_mostrar_menu_inicial(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Olá, bem vindo! Aqui começa sua jornada para superar seus limites!', font=("Helvica", 25))],
            [sg.Text('Faça o seu login', font=("Helvica", 15))],
            [sg.Radio('Aluno', "RD13", key='1')],
            [sg.Radio('Professor', "RD13", key='2')],
            [sg.Button('Confirmar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window('Sistema de login').Layout(layout)

    def layout_logar_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
                [sg.Text('Bem vindo ao login!', font=("Helvica", 25))],
                [sg.Text('Aluno, digite seu login', font=("Helvica", 15))],
                [sg.InputText('', key='login')],
                [sg.Text('Aluno, digite sua senha', font=("Helvica", 15))],
                [sg.InputText('', key='senha')],
                [sg.Button('Confirmar'), sg.Button('Retornar')]
                ]
        self.__window = sg.Window('Sistema de login!!').Layout(layout)

    def layout_logar_personal(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
             [sg.Text('Bem vindo ao login!', font=("Helvica", 25))],
             [sg.Text('Personal, digite seu login', font=("Helvica", 15))],
             [sg.InputText('', key='login')],
             [sg.Text('Personal, digite sua senha', font=("Helvica", 15))],
             [sg.InputText('', key='senha')],
             [sg.Button('Confirmar'), sg.Button('Retornar')]
         ]
        self.__window = sg.Window('Sistema de login!!').Layout(layout)

    def mostrar_msg(self, msg):
        sg.popup("", msg)
