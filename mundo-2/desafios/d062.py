r = int(input('Digite a razão da PA: '))
pt = int(input('Digite o primeiro termo da PA: '))
t = 10
p = True
while p == True:
    print('Aqui estão os primeiros {} termos da PA:'.format(t))
    for i in range(t):
        print(pt, end=' ')
        pt += r
    ta = int(input('\nGostaria de mostrar mais quantos termos? '))
    if ta == 0:
        print('Você escolheu sair')
        p = False
    else:
        t += ta