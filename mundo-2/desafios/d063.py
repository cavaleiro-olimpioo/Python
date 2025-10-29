print('Sequência de Fibonacci')

n = int(input('Digite um da saquência: '))
s1 = 0
s2 = 1

while n != 0:
    print(s1)
    soma = s1+s2
    s1 = s2
    s2 = soma

    n-=1