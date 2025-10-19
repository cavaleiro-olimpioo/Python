import random

print('========== JOKENPÔ ==========')

escjog = str(input('Escolha entre pedra, papel, e tesoura: '))
escrob = random.choice(['pedra', 'papel', 'tesoura'])

if not (escjog == 'pedra', escjog == 'papel', escjog == 'tesoura'):
    print('Escolha entre pedra, papel ou tesoura!')
else:
    if escjog == 'papel' and escrob == 'pedra' or escjog == 'tesoura' and escrob == 'papel' or escjog == 'papel' and escrob == 'pedra' or escjog == 'pedra' and escrob == 'tesoura':
        win = 'venceu'
    elif escjog == 'pedra' and escrob == 'pedra' or escjog == 'papel' and escrob == 'papel' or escjog == 'tesoura' and escrob == 'tesoura':
        win = 'empatou'
    else:
        win = 'perdeu'

print('Você escolheu {} e o robô escolheu {}, você {}!'.format(escjog, escrob, win))