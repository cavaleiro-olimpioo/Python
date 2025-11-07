valores = []
valpar = []
valimp = []
r = 's'
while True:
    valores.append(int(input('Diigte um valor: ')))
    r = str(input('Gostaria de continuar? [S/N] ')).lower()
    while True:
        if r not in ('s', 'n'):
            print('[ERRO] Digite um valor válido')
        else:
            break
    if r == 'n':
        break
for val in valores:
    if val%2==0:
        valpar.append(val)
    else:
        valimp.append(val)
print(f'A lista completa é {valores}\n A lista com os valores pares é {valpar} \n E a lista com valores ímpares é {valimp}')

