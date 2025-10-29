import random

print('Tente acertar o número que estou pensando!')
ne = random.randint(0,10)
t = 0
n = -1
while n != ne:
    n = int(input('Digite um número de 0 a 10: '))
    if n != ne:
        print('Errou, digite outro número')
    t += 1
if t > 1:
    print('Parabéns! Você acertou com {} tentativas'.format(t))
else:
    print('oloko, você acertou de primeira!')