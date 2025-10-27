print('Digite o peso de 5 pessoas')
c = 1
mai = 0
for i in range(5):
    p = int(input('Peso {}: '.format(i+1)))
    if p > mai:
        mai = p
    if i == 0:
        men = p
    else:
        if p < men:
            men = p

print('O maior peso digitado foi {}kg e o menos foi {}kg'.format(mai, men))
