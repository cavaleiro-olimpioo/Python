s = 'h'
while s not in ('M', 'F'):
    s = str(input('Digite seu sexo [M/F]: ')).upper()
    if s not in ('M', 'F'):
        print('Erro, escolha entre masculino(M) e feminino(F)')
print('Fim')