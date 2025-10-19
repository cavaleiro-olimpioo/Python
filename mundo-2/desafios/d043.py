import math

p = float(input('Quanto você pesa? '))
a = float(input('Quanto de altura você tem? '))

imc = p/(math.pow(a,2))

if imc < 18.5:
    print('seu IMC é de {}. você está abaixo do peso!'.format(imc))
elif 18.5 >= imc < 25:
    print('seu IMC é de {}. você está no peso ideal!'.format(imc))
elif 25 >= imc < 30:
    print('seu IMC é de {}. você está sobrepeso!'.format(imc))
else:
    print('Você está em obesidade mórbita! com {} de IMC'.format(imc))