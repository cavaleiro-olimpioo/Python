import random

print('Vamos jogar ímpar ou par!')

v = 0
while True:
    nj = int(input('Digite um valor: '))
    nm = random.randint(0, 10)
    ns = nj + nm
    while True:
        ip = str(input('Ímpar ou par [P/I]: ')).lower()
        if 'p' != ip != 'i':
            print('Digite entre ímpar ou par!')
        else:
            break
    if ns%2 == 0:
        print(f'Você escolheu {nj} e o computador escolheu {nm}. Total de {ns}, deu par!')
    else:
        print(f'Você escolheu {nj} e o computador escolheu {nm}. Total de {ns}, deu ímpar!')
    if ip == 'i' and ns%2 == 0:
        print(f'Você perdeu! Com um total de {v} vitórias!')
        break
    elif ip == 'p' and ns%2 != 0:
        print(f'Você perdeu! Com um total de {v} vitórias!')
        break
    else:
        print('Você venceu!')
        v += 1
        print('Vamos jogar novamente!')

