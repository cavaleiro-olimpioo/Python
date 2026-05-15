class Mission:
    def __init__(self, name, description, dificuty, reward):
        self.name = name
        self.description = description
        self.dificuty = dificuty
        self.reward = reward
        self.finished = False

    def concluir_missao(self):
        self.finished = True
        print('Tarefa concluida com sucesso')
