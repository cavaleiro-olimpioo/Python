import rich
from time import sleep

class Livro:
    def __init__(self, nome, paginas):
        self.nome = nome
        self.paginas = paginas
        self.pag_atual = 1

        rich.print(f'[blue]Você acabou de abrir o livro [red]{self.nome}[/red], que tem [green]{self.paginas} páginas[/green]')
        rich.print(f'[blue]Você está na página [orange]{self.pag_atual}[/orange][/blue]')

        

    def passar_paginas(self, np):
        if np + self.pag_atual > self.paginas:
            print()

        else:
            for i in range(1, np):

                self.pag_atual += 1
                
                print(f'Pág {self.pag_atual} >', end=' ', flush=True)

                sleep(.5)
                
            rich.print(f'\n[blue]Você avançou [bold]5[/bold] páginas, e agora está na [/blue][orange]página {self.pag_atual}[/orange]')

l1 = Livro('O Príncipe', 112)
l1.passar_paginas(10)