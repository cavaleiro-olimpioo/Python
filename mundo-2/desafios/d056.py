mi = 0
medi = 0
fmv = 0
hv = ''
idhv = 0
for i in range(1, 5):
    print('----------{} pessoa----------'.format(i))
    n = str(input('Nome: '))
    id = int(input('Idade: '))
    s = str(input('Sexo [M/F]: '))
    mi += id
    if i == 4:
        medi = mi/4
    if s == 'f':
        if id > 20:
            fmv += 1
    if s == 'm':
        if id > idhv:
            idhv = id
            hv = n.capitalize()
print('A média de idade das 4 pessoas é de {} anos, ao total {} mulher(es) tem mais de 20 anos e o homem mais velho é o {}'.format(medi, fmv, hv))