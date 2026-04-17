from uteis import d007pack

pr = int(input('Digite um preço: R$'))

print(f'A metade de R${pr} é {d007pack.metade(pr)}')
print(f'O dobro de R${pr} é {d007pack.dobro(pr)}')
print(f'Aumentando 10%, temos R${d007pack.dezpor(pr)}')