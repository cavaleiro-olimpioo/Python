n = input('Digite algo: ')

print('{} é um elemento de tipo primitivo {}'.format(n, type(n)))
print('{} é um número? {}'.format(n, n.isnumeric()))
print('{} é uma string? {}'.format(n, n.isascii()))
print('{} tem apenas caracteres minúsculos? {}'.format(n, n.islower()))
print('{} tem apenas caracteres maiúsculos? {}'.format(n,n.isupper()))
print('{} tem espaços? {}'.format(n, n.isspace()))
print('{} é alfanumerico? {}'.format(n, n.isalnum()))

