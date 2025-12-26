def player(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {0} gol(s) no campeonato')


print('-'*50)

player(str(input('Nome do jogador: ')), input('Número de gols: '))
