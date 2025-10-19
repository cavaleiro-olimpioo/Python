a = int(input('Digite o tamanho da primeira reta: '))
b = int(input('Digite o tamanho da segunda reta: '))
c = int(input('Digite o tamanho da terceira reta: '))

if not ((a+b) > c and (a+c) > b and (b+c) > a):
    print('Não forma um triângulo :(')
else:
    if a == b == c:
        tp = 'Equilátero'
    elif a == b or b == c or a == c:
        tp = 'Isósceles'
    else:
        tp = 'Escaleno'
    print('Forma um triângulo {}!'.format(tp))
