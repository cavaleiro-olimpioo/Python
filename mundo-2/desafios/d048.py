n = 0
s = 0
for i in range(500):
    if not (n%2==0) and n%3==0:
        s += n
    n += 1
print('A soma de todos os números de 0 500 que são ímpares e múltiplos de 3 é {}'.format(s))