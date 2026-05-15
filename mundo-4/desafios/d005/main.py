import rich
from rich.console import Console
from rich.panel import Panel

class Gamer:
    def __init__(self, name, nick):
        self.name = name
        self.nick = nick
        self.games = list()

    def add_favorito(self, game):
        self.games.append(game)

    def all_games(self):
        for i in self.games:
            rich.print(f':alien_monster: [blue]{i}[/]')

    def ficha(self):
        console = Console()
        panel = Panel(
            f'Nome real: [blue] {self.name} [/]',
            'Jogos favoritos: ',
            self.all_games(),
            title=f'Jogador <{self.nick}>',
            width=100
        )
        console.print(panel)

j1 = Gamer('Gui', 'nps')
j1.ficha()