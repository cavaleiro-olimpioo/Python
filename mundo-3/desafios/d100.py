import time
import random

val = list()

def sort():
    print('Sorteando 5 valores da lista:', end=' ')
    for i in range(5):
        na = random.randint(1, 10)
        print(na, end=' ')
        val.append(na)
        time.sleep(.3)
    print('PRONTO!')

def somp():
    soma = 0
    for i in val:
        if i%2==0:
            soma += i
    print(f'Somando os valores pares de {val}, temos {soma}')


sort()
somp()
