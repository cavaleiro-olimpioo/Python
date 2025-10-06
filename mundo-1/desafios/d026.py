f = str(input('Digite uma frase: ')).lower()
print('Nesta frase, a letra A aparece {} vezes, a primeira está na posição {} e a última está na posição {}'.format(f.count('a'), f.find('a')+1, f))