
# Caça-níqueis fds kk

import random

print('===============ULTIMATE NIQUEL===============')
print('Escolha um niquel entre: \n 1)🍒 \n 2)💎 \n 3)🚀')
#  \n 4)🍊 \n 5)🌝
es = int(input(':'))
n1 = random.choices('🍒''💎''🚀')
n2 = random.choices('🍒''💎''🚀')
n3 = random.choices('🍒''💎''🚀')
if es !=1 and es !=2 and es !=3:
    print('Escolhe um desses números cabaço kkkkkk')
else:
    if es == '1':
        es = '🍒'
    elif es == '2':
        es = '💎'
    elif es == '3':
        es = '🚀'


    w = False
    if n1 == n2 and n2 == n3:
        if es == n1:
            w = True

    print('{}|{}|{}'.format(n1, n2, n3))


    if w == True:
        print('Parabéns! Você não ganhou porra nenhuma!!!')
    elif w == False and n1 == n2 and n2 == n3:
        print('Caralho tu é muito azarado kkkkkkkk')
    elif w == False:
        print('Não foi dessa vez, mas você pode estar perto')
