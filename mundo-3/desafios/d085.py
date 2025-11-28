lista = []
par = []
imp = []
for i in range(7):
    val = int(input('Digite um valor: '))
    if val%2==0:
        par.append(val)
    else:
        imp.append(val)
lista.append(sorted(par))
lista.append(sorted(imp))
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores ímpares digitados foram {lista[1]}')