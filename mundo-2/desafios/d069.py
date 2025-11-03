from numbers import Number

md = h = mv = 0
while True:
    i = 0
    s = 0
    print(f'\033[1m{'-'*25}\n\033[1m{'CADASTRE UMA PESSOA':^25}\n\033[1m{'-'*25}')
    i = int(input('Digite a idade de uma pessoa: '))
    while s not in ('m', 'f'):
        s = str(input('digite o sexo de uma pessoa [M/F]: ')).lower()
    print(f'\033[1m{'-'*20}')
    if i > 18:
        md += 1
    if s == 'm':
        h += 1
    if s == 'f' and i > 20:
        mv += 1
    cont = ''
    while cont not in ('s', 'n'):
        cont = str(input('Gostaria de continuar? [S/N]: ')).lower()
    if cont == 'n':
        break

print(f'No total de pessoas cadastradas, {md} pessoas tem mais de 18 anos, {h} homens foram cadastrados, e {mv} mulheres tem mais de 20 anos')