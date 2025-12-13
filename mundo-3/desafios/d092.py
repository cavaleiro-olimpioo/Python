from datetime import datetime

pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
anonasc = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - anonasc
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - anonasc
print(f'{"-="*50}')
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')