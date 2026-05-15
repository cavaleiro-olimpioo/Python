from rich.panel import Panel
from rich.console import Console

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def etiqueta(self):
        console = Console()
        conteudo = f"{self.nome:^45}\n\n{'-'*45}\n\n{f'R${self.preco}':.^45}"
        
        panel = Panel(
            conteudo,
            title="Produto",
            width=50
        )

        console.print(panel)

p1 = Produto("iPhone 17 Pro Max", "25,000.85")
p2 = Produto("Notebook Gamer", "8,000.00")
p1.etiqueta()