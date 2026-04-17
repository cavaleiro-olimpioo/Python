while True:
    print('\033[1;30;42m~'*50)
    print(f'{"SISTEMA DE AJUDA PyHELP":^50}')
    print('~' * 50)

    fb = str(input('\033[mFunção ou biblioteca > '))


    try:
        print('\033[1;30;46m~'*50)
        print(f'{"Acessando o manual do comando '" + fb + "'":^50}')
        print('~' * 50)
        print('\033[;;m')
        help(fb)
    except:
        print('Biblioteca não encontrada')