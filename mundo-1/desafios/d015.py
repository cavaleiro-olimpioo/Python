d = float(input('Por quantos dias ele foi alugado? '))
km = float(input('Quantos kilometros foram rodados com o carro? '))
dp = d*60
kmp = km*0.15
pt = dp+kmp
print('O total a ser pago é {}'.format(pt))