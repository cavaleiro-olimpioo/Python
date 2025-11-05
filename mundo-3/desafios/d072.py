ne = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
      'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um número entre 0 e 20: '))
while True:
    if 0 > n or n > 20:
        n = int(input('[ERRO] Tente novamente. Digite um número entre 0 e 20: '))
    else:
        print(f'O número digitado foi {ne[n]}')
        break