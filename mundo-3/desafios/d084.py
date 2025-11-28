pessoas = list()
pes = list()
r = 's'
while True:
    pes.append(str(input('Nome: ')))
    pes.append(int(input('Peso: ')))
    pessoas.append(pes[:])
    pes.clear()
    while True:
        r = str(input('Quer continuar? [S/N]: ')).lower()
        if r not in ('s', 'n'):
            print('[ERRO] Digite uma resposta válida')
        else:
            break
    if r == 'n':
        break

for pos, i in enumerate(pessoas):
    if pos == 0:
        maip = i[1]
    else:
        if i[1] > maip:
            maip = i[1]

for pos, i in enumerate(pessoas):
    if pos == 0:
        menp = i[1]
    else:
        if i[1] < menp:
            menp = i[1]

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso cadastrado foi de {maip}Kg. Peso de', end=' ')
for pos, i in enumerate(pessoas):
    if i[1] == maip:
        print(i[0], end=' ')
print(f'\nO menor peso cadastrado foi de {menp}Kg. Peso de', end=' ')
for pos, i in enumerate(pessoas):
    if i[1] == menp:
        print(i[0], end=' ')