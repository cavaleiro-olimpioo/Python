t1 = ('Aprender', 'magica', 'programar', 'linguagem', 'curso', 'gratis', 'trabalhar', 'estudar', 'escola', 'futuro')
for i in t1:
    print(f'\nNa palavra {i} temos ', end='')
    for v in i:
        if v in 'aeiou':
            print(v, end=' ')
