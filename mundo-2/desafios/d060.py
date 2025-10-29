import math
n = int(input('Digite um número: '))
nf = math.factorial(n)
print('O fatorial de {} é:'.format(n))
while n != 0:
    if n == 1:
        print('{} = {}'.format(n, nf), end='')
    else:
        print('{}x'.format(n), end='')
    n -= 1