def tit(txt):
    titl = len(txt)+4
    print('-'*titl)
    print(f'{txt:^{titl}}')
    print('-'*titl)
tit('Hello world!')
tit('Curso em Vídeo de Python')
tit('CeV')