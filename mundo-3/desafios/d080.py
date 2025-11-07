lista = []
for i in range(5):
    val = int(input('Digite um valor: '))
    if i == 0:
        lista.append(val)
        print(f'{val} adicionado a posição 0')
    elif i == 1:
        if val > lista[0]:
            lista.append(val)
            print(f'{val} adicionado a posição 1')
        else:
            lista.insert(0, val)
            print(f'{val} adicionado a posição 0')
    else:
        for pos, num in enumerate(lista):
            if val > num:
                if val > lista[len(lista)-1]:
                    lista.append(val)
                    print(f'{val} adicionado ao final da lista')
                    break
            else:
                lista.insert(pos, val)
                print(f'{val} adicionado à posição {pos}')
                break

print(f'Os valores digitados em ordem foram {lista}')