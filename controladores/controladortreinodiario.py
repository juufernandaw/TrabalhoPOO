from TrabalhoPOO.entidades.treinodiario import TreinoDiario
from TrabalhoPOO.telas.telatreinodiario import TelaTreinoDiario
from TrabalhoPOO.controladores.controladorsistema import ControladorSistema
from TrabalhoPOO.entidades.treino import Treino
from TrabalhoPOO.controladores.controladoraluno import ControladorAluno


class ControladorTreinoDiario():
    def __init__(self, controlador_sistema):
        self.__treinos_diarios = []
        self.__treinos = []
        self.__tela_treinoDiario = TelaTreinoDiario()
        self.__manter_tela = bool
        self.__controlador_sistema = controlador_sistema

    # @property
    # def treino_diarios(self):
    #     return self.__treinos_diarios
    #
    # def adc_treinos_diarios(self, treino_diario: TreinoDiario):
    #     self.__treinos_diarios.append(treino_diario)

    def incluir_treino(self, treino: Treino):
        if isinstance(treino, Treino):
            self.__treinos.append(treino)

    def mostrar_tela_treino_diario(self):
        return self.__tela_treinoDiario.mostrar_tela_desempenho()

    def desempenho_aluno(self):
        if self.__tela_treinoDiario.mostrar_tela_desempenho() == 1:
            self.__tela_treinoDiario.mostrar_desempenho()
            self.__tela_treinoDiario.checkin()
            self.checkin()

    def checkin(self):
        checkin = 0
        if self.__controlador_sistema.controladorsistema.abre_logins() == \
                self.__controlador_sistema.controladoraluno.abre_tela_funcoes_aluno():
            checkin += 1

        return checkin
