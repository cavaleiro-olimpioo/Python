import random

t1 = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
print(f'Os valores sorteados foram {t1}')
for pos, i in enumerate(t1):
    if pos == 0:
        men = i
        mai = 0
    else:
        if i > mai:
            mai = i
        if i < men:
            men = i
print(f'O maior valor desta tupla foi {mai}, e o menor foi {men}')
