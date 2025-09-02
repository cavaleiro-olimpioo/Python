import random

a1 = str(input('primeiro aluno: '))
a2 = str(input('segundo aluno: '))
a3 = str(input('terceiro aluno: '))
a4 = str(input('quarto aluno: '))

ae = random.choice([a1,a2,a3,a4])

print('O aluno escolhido para apagar o quadro foi o(a) {}'.format(ae))