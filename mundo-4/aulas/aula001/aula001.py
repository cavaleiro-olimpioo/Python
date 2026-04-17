# Declaração de classe
class Gafanhoto:
    def __init__(self): # Método construtor
        # Atributos
        self.nome = ""
        self.idade = 0
        # Métodos
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        return f'{self.nome} é um Gafanhoto(a), que tem {self.idade} anos'

# Declaração de objeto
g1 = Gafanhoto()
g1.nome = "Guilherme"
g1.idade = 15
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Thiago'
g2.idade = 14
print(g2.mensagem() )