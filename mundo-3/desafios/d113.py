def intinput(v):
    while True:
        n = input(v)
        if int(n):
            return n
            break
        else:
            print('[ERRO] Digite um número inteiro válido!\033[1;31m')

def floatinput(vr):
    while True:
        n = input(vr)
        if float(n):
            return n
            break
        else:
            print('[ERRO] Digite um número inteiro válido!\033[1;31m')




ni = intinput('Digite um número inteiro: ')
nr = intinput('Digite um número real: ')

print(f'O valor inteiro digitado foi {ni} e o real foi {nr}')