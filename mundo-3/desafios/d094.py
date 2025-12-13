pessoa = dict()
pessoas = list()

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).lower()
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    pessoa = {}
    while True:
        r = str(input('Gostaria de continuar? [S/N] '))
        if r not in ('s', 'n'):
            print('[ERRO] Resposta inválida')
        else:
            break
    if r == 'n':
        break
print(f'{"-="*50}')
print(f'- O número de pessoas cadastradas é de {len(pessoas)}')
it = 0
for i in pessoas:
    it += i['idade']

med = it/len(pessoas)
print(f'- A média de idade é de {med} anos')
print(f'- As mulheres cadastradas foram:', end=' ')
for i in pessoas:
    if i['sexo'] == 'f':
        print(f'{i["nome"]}', end=' ')
print(f'\n- Lista de pessoas que são acima da média:')
for i in pessoas:
    if i['idade'] > med:
        for k, v in i.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')
