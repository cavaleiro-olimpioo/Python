p = True
mb = 0
mai = 0
nr = 0
while p:
    n = int(input('Digite um número: '))
    nr += 1
    brk = str(input('Gostaria de digitar mais algum número [S/N]: ')).lower()
    if nr == 1:
        men = n
    if brk == 'n':
        p = False
        m = mb/nr
        print('A média dos valores escolhidos foi de {}, o maior valor digitado foi {} e o menor foi {}'.format(m,mai,men))
    else:
        mb += n
        if n > mai:
            mai = n
        elif n < men:
            men = n