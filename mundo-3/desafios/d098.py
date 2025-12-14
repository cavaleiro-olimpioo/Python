import time

def linha():
    print('-='*50)

def contagem(i, f, p):
    time.sleep(1)
    linha()
    if p <= 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    vt = i
    if i < f:
        while vt < f:
            print(vt, end=' ')
            time.sleep(.5)
            vt += p
    else:
        while vt > f:
            print(vt, end=' ')
            time.sleep(.5)
            vt -= p
    if vt <= f:
        print(vt, end=' ')
    time.sleep(.5)
    print('FIM!')

contagem(1, 10, 1)
contagem(10, 0, 2)
linha()
print(f'Agora é sua vez de personalizar a contagem!')
contagem(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))

