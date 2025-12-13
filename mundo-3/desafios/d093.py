jogador = dict()
gols = list()
ttg = 0

jogador['nome'] = str(input('Nome do jogador: '))
pj = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(pj):
    gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
jogador['gols'] = gols
for i in gols:
    ttg += i
jogador['total'] = ttg
print(f'{"-="*50}')
print(jogador)
print(f'{"-="*50}')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'{"-="*50}')
print(f'O jogador {jogador["nome"]} jogou {pj} partidas')
for en, p in enumerate(gols):
    print(f'     => Na partida {en+1}, fez {p} gols')
print(f'Foi um total de {ttg} gols')
