'''fbrut = str(input('Digite uma frase: '))'''
fbrut = 'abc'

f = fbrut.replace(' ', '').lower()

for i in range(len(f), 0):
    finv = f[i]
print(finv)