n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite mais um: '))

menor = n1

if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3