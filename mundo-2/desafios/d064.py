
p = True
r = 0
qn = -1
s = 0
while p != False:
    if r == 999:
        print('No total foram digitados {} números e a soma deles é {}'.format(qn,s))
        p = False
    else:
        qn += 1
        s += r
        r = int(input('Digite um número: '))
