import PySimpleGUI as sg


class TelaPersonalTrainer:
    def __init__(self):
        self.__window = None
        self.layout_tela_aba_personal()
        #self.layout_tela_alterar_dados()
        self.layout_mexer_personal()

    def close(self):
        self.__window.Close()

    def mostrar_msg(self, msg):
        sg.popup("", msg)

    def mostrar_personal_trainer(self, dados_personal):
        infos_personal = "NOME: " + dados_personal["nome"] + '\n'
        infos_personal = infos_personal + "LOGIN: " + dados_personal["login"] + '\n'
        infos_personal = infos_personal + "SENHA: " + dados_personal["senha"] + '\n'
        infos_personal = infos_personal + "CPF:" + dados_personal["cpf"] + '\n'
        infos_personal = infos_personal + "HABILITAÇÃO: " + dados_personal["habilitacao"] + '\n'
        sg.popup("------ INFORMAÇÕES PERSONAL ------", infos_personal)

    def layout_tela_aba_personal(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("----- ABA PERSONAL -----", font=("Helvica", 20))],
            [sg.Text('O que você deseja fazer hoje ?', font=("Helvica", 15))],
            [sg.Radio('Consultar seus dados', "RD1", key='1')],
            [sg.Radio('Alterar seus dados', "RD1", key='2')],
            [sg.Button('Confirmar'), sg.Button('Retornar')]
        ]
        self.__window = sg.Window('Personal').Layout(layout)

    def tela_aba_personal(self):
        self.layout_tela_aba_personal()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif button == 'Retornar':
            opcao = 0
        self.close()
        return opcao

    def layout_tela_alterar_dados(self, personal):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
                [sg.Text('Olá, Renove seus Dados:', font=("Helvica", 20))],
                [sg.Text('Digite o nome: ', font=("Helvica", 15))],
                [sg.InputText(personal.nome, key='nome')],
                [sg.Text('Digite o cpf:', font=("Helvica", 15))],
                [sg.InputText(personal.cpf, key='cpf')],
                [sg.Text('Digite o login:', font=("Helvica", 15))],
                [sg.InputText(personal.login, key='login')],
                [sg.Text('Digite a senha:', font=("Helvica", 15))],
                [sg.InputText(personal.senha, key='senha')],
                [sg.Text('Digite a habilitação:', font=("Helvica", 15))],
                [sg.InputText(personal.habilitacao, key='habilitacao')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]
        self.__window = sg.Window('Renovação dos dados, personal').Layout(layout)

    def tela_alterar_dados(self, personal):  # alterando personal
        self.layout_tela_alterar_dados(personal)
        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            nome = None
            cpf = None
            login = None
            senha = None
            habilitacao = None
        else:
            nome = values["nome"]
            cpf = values["cpf"]
            login = values["login"]
            senha = values["senha"]
            habilitacao = values["habilitacao"]
        self.close()
        return {"cpf": cpf, "nome": nome, "login": login, "senha": senha, "habilitacao": habilitacao}

    def layout_mexer_personal(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("------ INÍCIO ------", font=("Helvica", 20))],
            [sg.Text("------ ABA PERSONAL ------", font=("Helvica", 20))],
            [sg.Text('Seja bem vindo, personal! O que você deseja fazer hoje?', font=("Helvica", 15))],
            [sg.Radio('ABA Personal', "RD3", key='1')],
            [sg.Radio('ABA Alunos', "RD3", key='2')],
            [sg.Radio('ABA Treinos', "RD3", key='3')],
            [sg.Radio('Sair', "RD3", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.__window = sg.Window('Personal').Layout(layout)

    def mexer_personal(self):
        while True:
            opcao = 0
            self.layout_mexer_personal()
            button, values = self.__window.Read()
            if values['1']:
                opcao = 1
            elif values['2']:
                opcao = 2
            elif values['3']:
                opcao = 3
            # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
            if values['0'] or button in (None, 'Retornar'):
                opcao = 0
            self.close()
            return opcao
