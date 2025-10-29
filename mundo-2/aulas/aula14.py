n = 1
p = -1
while n != 0:
    n = int(input('Digite um valor: '))
    if n%2 == 0:
        p += 1
print('Você digitou {} números pares'.format(p))