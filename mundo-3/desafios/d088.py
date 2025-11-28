import random
import time
ms = []
jgs = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {jgs} JOGOS =-=-=-')
for pal in range(jgs):
    jogo = []
    for i in range(6):
        while True:
            val = random.randint(1, 60)
            if val not in jogo:
                jogo.append(val)
                break
    ms.append(jogo[:])
    print(f'Jogo {pal+1}: {ms[pal]}')
    time.sleep(0.5)
print('-=-=-=-=-= < BOA SORTE! > =-=-=-=-=-')


