nf = 0
for i in range(6):
    n = int(input('Digite um número: '))
    if n%2 == 0:
        nf += n
print('A soma dos valores pares foi de {}'.format(nf))