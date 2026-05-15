from rich.console import Console
from rich.panel import Panel
from rich.text import Text

class Churrasco:
    def __init__(self, nome, pessoas):
        self.nome = nome
        self.pessoas = pessoas
        self.carneTotal = self.pessoas * 0.4
        self.precoTotal = self.carneTotal * 82.40

    def analisar(self):
        console = Console()
        conteudo = (
            f"Analisando [green]{self.nome}[/] com [blue]{self.pessoas} pessoas[/]\n"
            f"Cada participante comerá 0.4kg — R$82,40/kg\n"
            f"Comprar: [blue]{self.carneTotal:.1f}kg[/] de carne\n"
            f"Custo total: [green]R${self.precoTotal:.2f}[/]\n"
            f"Por pessoa: [yellow]R${self.precoTotal / self.pessoas:.2f}[/]"
        )
        console.print(Panel(conteudo, title=self.nome, width=100))

c1 = Churrasco('Churras dos amigos', 15)
c1.analisar()