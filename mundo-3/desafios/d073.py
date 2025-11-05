tb = (
'Palmeiras',
'Flamengo',
'Cruzeiro',
'Mirassol',
'Bahia',
'Botafogo',
'Fluminense',
'São Paulo',
'Vasco da Gama',
'Corinthians',
'Grêmio',
'Ceará SC',
'Atlético-MG',
'Bragantino',
'Internacional',
'Santos',
'EC Vitória',
'Fortaleza',
'Juventude',
'Sport Recife')

print(f'Lista de times do brasileirão: {tb}')
print(f'Os primeiros 5 colocados da tabela do brasileirão de 2025 são {tb[0:6]}')
print(f'Os últimos 4 colocados são {tb[-4:]}')
print(f'Os times em ordem alfabética são {sorted(tb)}')
if 'Chapecoense' in tb:
    print(f'O time da Chapecoense está na posição {tb.index('Chapecoense')+1}')
else:
    print('Infelizmente, o Chapecoense está abaixo da posição 20 :(')