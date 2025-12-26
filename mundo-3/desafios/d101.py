from datetime import datetime

def voto(idade):
    if 18 <= idade < 60:
        return 'obrigatório'
    elif 15 < idade < 18 or idade > 60:
        return 'opicional'
    else:
        return 'negado'

print('-'*50)
i = datetime.now().year - int(input('Em que ano você nasceu? '))

print(f'Com {i} anos, seu voto é {voto(i)}')