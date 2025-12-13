jogador = dict()
jogadores = list()
gols = list()
ttg = 0

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    pj = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for i in range(pj):
        gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
    jogador['gols'] = gols[:]
    for i in gols:
        ttg += i
    jogador['total'] = ttg
    jogadores.append(jogador.copy())
    jogador = {}
    gols = []
    ttg = 0
    while True:
        r = str(input('Gostaria de continuar? [S/N]: '))
        if r not in ('s', 'n'):
            print('[ERRO] Resposta inválida')
        else:
            break
    if r == 'n':
        break
    else:
        print(f'{"-"*25}')
print(f'{"-="*50}')
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total":<5}')
print(f'{"-"*39}')
for pos, i in enumerate(jogadores):
    gols_txt = ','.join(map(str, i["gols"]))
    print(f'{pos+1:<4}{i["nome"]:<15}{gols_txt:<15}{i["total"]:<5}')
print(f'{"-"*39}')
while True:
    while True:
        rc = int(input('Mostrar dados de qual jogador? (999 para) '))-1
        if rc not in range(len(jogadores)):
            print('[ERRO] Jogador não encontrado')
        else:
            break
    if rc == 998:
        break
    else:
        print(f'-- levantamento do jogador {jogadores[rc]["nome"]}')
        for i in range(len(jogadores[rc]['gols'])):
            print(f'     No jogo {i+1} fez {jogadores[rc]['gols'][i]}')

print('<< VOLTE SEMPRE >>')