import random

n = int(input('Escolha um número entre 0 e 5: '))
na = random.randint(0,5)

print('o número escolhido foi {}'.format(na))
if n > 5:
    print('Você é burro? Eu disse entre 0 e 5')
else:
    if n == na:
        print('Parabéns você venceu!')
    else:
        print('infelizmente você perdeu, agora seus bens pertencem ao governo')