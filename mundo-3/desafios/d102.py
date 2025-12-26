import time

def fatorial(n, show=False):
    """
    :param n: O número a ser calculado
    :param show: (opicional) Mostrar ou não a conta
    :return: O valor Fatorial
    """
    f = n
    for i in range(n, 0, -1):
        f *= i
    if show:
        for i in range (n, 0, -1):
            print(i, end=' ')
            if i != 1:
                print('x', end=' ')
            else:
                print(f'=', end=' ')
    return f



print(fatorial(5, True))