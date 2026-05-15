class Funcionarios:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentacao(self):
        return f'Olá! meu nome é {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa'

f1 = Funcionarios('Guilherme', 'TI', 'Dev Sênior')
print(f1.apresentacao())

f2 = Funcionarios('Manuella', 'repositora', 'atacadão')
print(f1.apresentacao())
