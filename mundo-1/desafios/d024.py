c = str(input('Digite o nome da sua cidade: ')).title()

if c.find('Santo') != 0:
    print('Sua cidade não começa com santo :(, mas sim com {}'.format(c.split()[0]))
else:
    print('Sua cidade começa com Santo!!')