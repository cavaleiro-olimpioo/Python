valores = []
r = 's'
while True:
    val = int(input('Digite um valor: '))
    valores.append(val)
    while True:
        r = str(input('Quer continuar? [S/N] ')).lower()
        if r not in ('s', 'n'):
            print('[ERRO] Digite uma resposta válida')
        else:
            break
    if r == 'n':
        break
print(f'Você digitou {len(valores)} elementos\nOs valores em ordem decrescente são {sorted(valores, reverse=True)}')
if 5 in valores:
    print('O valor 5 está dentro da lista!')
else:
    print('O valor 5 não está na lista')