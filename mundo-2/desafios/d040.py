m = float(input('Quanto você tirou em matemática? '))
p = float(input('Quanto você tirou em português? '))

med = (p+m)/2

if med < 5:
    print('Você foi reprovado, com a média de {}'.format(med))
elif 5 <= med <= 6.9:
    print('Você está de recuperação! Com a média {}'.format(med))
else:
    print('Parabéns, você passou de ano! Com nota {}'.format(med))