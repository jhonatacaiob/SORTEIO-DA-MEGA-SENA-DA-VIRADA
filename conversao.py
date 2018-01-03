def conversao(valor):
    valor = str(valor)
    valor = ' ' + valor
    valor = valor.split(" ")
    valor = valor[1]
    valor_nac = ''
    if '.' in valor:
        for i in valor:
            if '.' == i:
                valor_nac += ','
            else:
                valor_nac += i
    else:
        for i in valor:
            valor_nac += i
    valor_naclis = valor_nac.split(',')
    decimal = len(valor_naclis[1])
    v = valor_naclis[1]
    if decimal == 1:
        valor_nac += '0'
    elif decimal == 0:
        valor_nac += '00'
    valor_nac = 'R$ '+valor_nac
    return valor_nac
