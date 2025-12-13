import random
import time

jogadores = dict()
jogadoresorder = list()

while True:
    c = str(input('Aperte Enter para começar '))
    print('Valores sorteados:')
    for i in range(4):
        val = random.randint(1, 6)
        jogadores[f'Jogador {i+1}'] = val
    for k, v in jogadores.items():
        print(f'     O jogador {k} tirou {v}')
        time.sleep(1)
    print('Ranking dos jogadores:')


    # Resposta final
    r = ''
    while True:
        r = str(input('Gostaria de jogar novamente? [S/N] ')).lower()
        if r not in ('s', 'n'):
            print('[ERRO] Responda entre [S/N]')
        else:
            break
    if r == 'n':
        break
    print()