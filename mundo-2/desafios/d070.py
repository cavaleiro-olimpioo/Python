print(f'\033[1m{'='*50}\n\033[1m{'Loja super baratão':^50}\n\033[1m{'='*50}')
'''
p = preço
np = nome do produto
tg = total gasto
pb = produto mais barato
pmb = produto mais barato valor
pm = produto mais mil reais
cont = contagem
r = resposta
'''
tg = pb = pm = cont = 0
while True:
    np = str(input('Nome do produto: '))
    p = float(input('Preço: R$'))
    tg += p
    cont += 1
    if cont == 1:
        pb = np
        pmb = p
    elif p < pmb:
        pmb = p
        pb = np
    if p > 1000:
        pm += 1
    r = ''
    while r not in ('s', 'n'):
        r = str(input('Gostaria de continuar? [S/N]: ')).lower()
    if r == 'n':
        break
print(f'O valor total gasto foi de R${tg}, {pm} produtos custaram mais de R$1.000,00, e o produto mais barato foi o {pb}')