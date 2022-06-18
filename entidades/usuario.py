from abc import ABC, abstractmethod


class Usuario(ABC):
    @abstractmethod
    def __init__(self, nome: str, login: str, senha: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__login = login
        self.__senha = senha

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha: str):
        self.__senha = senha

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf


