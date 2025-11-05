t1 = ('Lápis', 1.75,
      'Borracha', 2.00,
      'Caderno', 15.90,
      'Estojo', 25.00,
      'Transferidor', 4.20,
      'Compasso', 9.99,
      'Mochila', 120.32,
      'Canetas', 22.30,
      'Livro', 34.90

)
print(f"{'-'*50}\033[1m")
print(f'{"LISTAGEM DE PREÇOS":^50}\033[1m')
print(f"{'-'*50}\033[1m")

for pos, i in enumerate(t1):
    if pos == 0 or pos%2==0:
        print(f'{i:.<40}R${t1[pos+1]:>8}')
print(f"{'-'*50}\033[1m")