v = int(input('Digite a velocidade do carro: '))

m = (v-80)*7

if v > 80:
    print('Você foi multado em {},00R$ por andar a {}km'.format(m, v))
else:
    print('Você esta dentro dos limites de velocidade! Continue assim... Gay')