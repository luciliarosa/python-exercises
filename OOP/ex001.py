# Declaração de classes
class Gafanhoto:
    def __init__(self): # Método construtor
        self.nome = "" # Atributos de Instância
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "Luci"
g1.idade = 29

g1.aniversario()

print(g1.mensagem())
