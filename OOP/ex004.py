"""
Crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo.
Crie também um método que permita ao funcionário se apresentar.
"""
from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        print(f":+1: Olá, sou {self.nome}, e sou {self.cargo} do setor {self.setor} da empresa Luci's Tech ")

f1 = Funcionario("Lucilia", "TI", "Analista de Sistemas")
f2 = Funcionario("Vini", "Contabilidade", "Contador")
f1.apresentar()
f2.apresentar()
    