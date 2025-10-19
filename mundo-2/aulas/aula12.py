nome = str(input('Digite seu nome: '))

if nome == "Guilherme":
    print("Que nome lindo!")
elif nome == 'Cleber':
    print('Que nome feio!')
else:
    print('Que nome comum!')

print('Bom dia {}!'.format(nome))