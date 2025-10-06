d = int(input('Qual a distânca da viagem? '))

if d > 200:
    p = d*0.45
else:
    p = d*0.45
print('Sua viagem de {}km vai dar entorno de {}R$'.format(d,p))
