n = int(input('Digite um número: '))
nt = 1
ntf = 0
for i in range(10):
    ntf = nt*n
    print('{} x {} = {}'.format(nt, n, ntf))
    nt += 1