a = int(input('Digite o tamanho da primeira reta: '))
b = int(input('Digite o tamanho da segunda reta: '))
c = int(input('Digite o tamanho da terceira reta: '))

if (a+b) > c and (a+c) > b and (b+c) > a:
    print('Forma um triângulo!')
else:
    print('Não forma um triângulo :(')