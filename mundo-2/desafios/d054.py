from datetime import datetime

print('Digite o ano nascimento de 7 pessoas')
p = 1

maid = 0
for i in range(7):
    a = int(input('{} pessoa: '.format(p)))
    if (datetime.now().year-a) >= 18:
        maid += 1
    p+=1

print('Ao total, {} pessoas são miores de idade'.format(maid))