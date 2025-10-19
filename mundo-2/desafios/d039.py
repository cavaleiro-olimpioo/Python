from datetime import datetime
nasc = int(input('Em que ano você nasceu? '))
idade = datetime.now().year - nasc

if idade == 18:
    print('Você tem {} anos, já está ma hora de se alistar ao serviço militar!'.format(idade))
elif idade > 18:
    print('Você tem {} anos, ja deveria ter feito o alistamento militar!'.format(idade))
else:
    print('Você tem {} anos, fique tranquilo quanto ao alistamento militar'.format(idade))