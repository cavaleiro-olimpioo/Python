print(f'\033[1m{'-'*50}\n\033[1m{'Caixa Eletrônico':^50}\n\033[1m{'-'*50}')
valor = int(input('Qual o valor do seu saque? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced} ')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break