t1 = (
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
    int(input('Digite um valor: '))
)
print(f'Você digitou os valores {t1}')
if 9 in t1:
    print(f'O valor 9 apareceu {t1.count(9)} vez')
else:
    print('Você não digitou nenhum 9 :(')
if 3 in t1:
    print(f'O valor 3 apareceu {t1.count(3)} vez')
else:
    print('Você não digitou nenhum 3 :(')

print('Os valores pares digitados foram', end=' ')
for i in t1:
    if i%2==0:
        print(f'{i}', end=' ')
