l1 = []
l2 = []
l3 = []
spar = 0
ster = 0
mais = 0
matriz = [l1,l2,l3]
for en, linha in enumerate(matriz):
    for i in range(3):
        val = int(input(f'Digite um valor para [{en+1}, {i+1}]: '))
        linha.append(val)
print(f'{'=-'*50}')
for col in range(3):
    for linh in range(3):
        if linh == 2:
            print(f'[  {matriz[col][linh]}  ]')
        else:
            print(f'[  {matriz[col][linh]}  ]', end='')

        if matriz[col][linh] % 2 == 0:
            spar += matriz[col][linh]
        if linh == 2:
            ster += matriz[col][linh]
        if col == 1:
            if col == 0:
                mais == matriz[col][linh]
            else:
                if matriz[col][linh] > mais:
                    mais = matriz[col][linh]
print(f'{'=-'*50}')
print(f'A soma dos valores pares é de {spar}')
print(f'A soma dos valores da terceira coluna é de {ster}')
print(f'o maior valor da segunda coluna é de {mais}')