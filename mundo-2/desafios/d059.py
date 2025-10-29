p = True
while p == True:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do Programa')
    es = int(input('Escolha uma das opções acima: '))
    if es == 1:
        print('A soma de {} e {} é {}'.format(n1, n2, n1+n2))
    elif es == 2:
        print('A multiplicação de {} e {} é {}'.format(n1, n2, n1*n2))
    elif es == 3:
        if n1 > n2:
            m = n1
        else:
            m = n2
        print('O maior valor digitado foi {}'.format(m))
    elif es == 4:
        pass
    else:
        p = False
