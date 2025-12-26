def intinput(v):
    while True:
        n = input(v)
        if int(n):
            return n
            break
        else:
            print('[ERRO] Digite um número inteiro válido!\033[1;31m')


n = intinput('digite um número: ')
print(f'Você acabou de digitar {n}')