nome = ''
alunos = []
while True:
    notas = []
    aluno = []
    nome = str(input('Nome: '))
    for i in range(2):
        notas.append(float(input(f'Nota {i+1}: ')))
    aluno.append(nome)
    aluno.append(notas[:])
    alunos.append(aluno[:])
    while True:
        r = str(input('Gostaria de continuar? [S/N] ')).lower()
        if r not in ('s', 'n'):
            print('[ERRO] Digite uma resposta válida')
        else:
            break
    if r == 'n':
        break
print(f'{'-='*50}')
print(f'{'No.':<5}{'NOME':<20}{'MÉDIA':<5}')
print(f'{'-'*35}')
for num, al in enumerate(alunos):
    print(f'{num:<5}{al[0]:<20}{(al[1][0]+al[1][1])/2:<5}')
print(f'{'-'*35}')
while True:
    while True:
        con = int(input('Gostaria de mostar as notas de qual aluno? (999 interrompe): '))
        if 999 != con and not (0 <= con < len(alunos)):
            print('[ERRO] Aluno não encontrado')
        else:
            break
    if con == 999:
        break
    else:
        print(f'As notas de {alunos[con][0]} são {alunos[con][1][0]} e {alunos[con][1][1]}')
        print(f'{'-' * 35}')
print('Finalizando...')
print('<<< VOLTE SEMPRE! >>>')