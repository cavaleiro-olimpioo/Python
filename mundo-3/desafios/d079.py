valores = []
r = 's'
while True:
    if r == 's':
        val = int(input('Adicione um valor a lista: '))
        if val not in valores:
            valores.append(val)
            print('Valor adicionado com sucesso...')

        else:
            print('Valor já digitado!')
        while True:
            r = str(input('Gostaria de continuar? [S/N]: ')).lower()
            if r not in ('s', 'n'):
                print('[ERRO] Responda entre [S/N]')
            else:
                break
    else:
        break
print(f'Os valores digitados em ordem crescente foram {sorted(valores)}')