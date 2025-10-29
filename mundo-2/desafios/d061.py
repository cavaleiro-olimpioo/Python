r = int(input('Digite a razão da PA: '))
pt = int(input('Digite o primeiro termo da PA: '))
print('Aqui estão os primeiros 10 termos da PA:')
i = 1
while i != 10:
    print(pt, end=' ')
    pt += r
    i+=1