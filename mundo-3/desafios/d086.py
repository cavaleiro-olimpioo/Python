l1 = []
l2 = []
l3 = []
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
