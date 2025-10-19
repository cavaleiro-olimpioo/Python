from datetime import datetime

idade = datetime.now().year-int(input('Em que ano você nasceu? '))

if idade <= 9:
    print('Você é um nadador mirim de {} anos!'.format(idade))
elif idade >= 10 and idade <= 14:
    print('Você é um nadador infantil de {} anos!'.format(idade))
elif idade >= 15 and idade <= 19:
    print('Você é um nadador junior de {} anos!'.format(idade))
elif idade == 20:
    print('Você é um nadador sênior de {} anos!'.format(idade))
else:
    print('Você é um nadador mestre de {} anos!'.format(idade))
