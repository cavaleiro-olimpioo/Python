aluno = dict()

def notas(*n, sit=False):
    """
    --> Função para análise de notas
    :param n: uma ou mais notas do aluno (aceita várias)
    :param sit: valor opicional, mostra a situação do aluno entre boa, razoável e ruim
    :return: retorna um dicionário com a mior, e a menor nota, o número de notas, a média e a situação (Se sit for True)
    """
    medi = 0
    for pos, i in enumerate(n):
        if pos == 0:
            mai = i
            men = i
        else:
            if i > mai:
                mai = i
            if i < men:
                men = i

        medi+=i
    med = medi/len(n)
    aluno['total:'] = len(n)
    aluno['maior:'] = mai
    aluno['menor:'] = men
    aluno['média'] = med
    if sit:
        if med < 5:
            situa = 'RUIM'
        elif med > 7:
            situa = 'BOA'
        else:
            situa = 'RAZOÁVEL'
        aluno['Situação'] = situa
    return aluno


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
help(notas)