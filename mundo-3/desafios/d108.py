from uteis import d007pack
from uteis.d008pack import modulo

pr = float(input('Digite um preço: R$'))

print(f'A metade de {modulo(pr)} é {modulo(d007pack.metade(pr))}')
print(f'O dobro de {modulo(pr)} é {modulo(d007pack.dobro(pr))}')
print(f'Aumentando 10%, temos {modulo(d007pack.porcento(pr, 10))}')