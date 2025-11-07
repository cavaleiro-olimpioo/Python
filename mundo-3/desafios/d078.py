val = []
for i in range(5):
    val.append(int(input(f'Digite um valor para a posição {i}: ')))

for pos, valor in enumerate(val):
    if pos == 0:
        men = valor
        mai = valor
        posmen = 0
        posmai = 0
    else:
        if valor < men:
            men = valor
            posmen = pos
        if valor > mai:
            mai = valor
            posmai = pos
print(f'{"-="*50}')
print(f'os valores digitados foram {val}\n O maior valor digitado foi {mai} na posição {posmai}...\n O menor valor digitado foi {men} na posição {posmen}')

