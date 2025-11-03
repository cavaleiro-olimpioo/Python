n = s = r = 0

while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    else:
        s += n
        r+=1
print(f'Você digitou {r} e a soma entre todos foi {s}')