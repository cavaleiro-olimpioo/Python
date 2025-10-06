s = int(input('Digite seu salário: '))
a10 = s*10/100+s
a15 = s*15/100+s

if s >= 1250:
    print('Seu salário será de {}R$, com um aumento de {}R$'.format(a10, a10-s))
else:
    print('Seu salário será de {}R$, com um aumento de {}R$'.format(a15, a15-s))