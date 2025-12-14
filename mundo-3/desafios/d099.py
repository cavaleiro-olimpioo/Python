import time

def maior(*nuns):
    print('-='*50)
    print('Analisando os valores passados...')
    for n in nuns:
        print(n, end=' ')
        time.sleep(.5)
    print(f'Foram informados {len(nuns)} valores ao todo.')
    nunst = sorted(nuns)
    print(f'o maior valor informado foi {nunst[len(nuns)-1]}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)