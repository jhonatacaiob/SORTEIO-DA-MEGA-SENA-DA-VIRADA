def cadastramento2():
    from CARTELAS3 import cadastramento1
    NomeJogador = input("Qual seu nome?: ")
    preco = 0
    total = []
    comece = 's'
    todas_apostas = []
    while comece == "sim" or comece == "s":
        printavel, Apostas = cadastramento1()
        if Apostas == 6:
            preco += 3.5
            total += [preco]
        elif Apostas == 7:
            preco += 24.5
            total += [preco]
        elif Apostas == 8:
            preco += 98
            total += [preco]
        elif Apostas == 9:
            preco += 294
            total += [preco]
        elif Apostas == 10:
            preco += 735
            total += [preco]
        elif Apostas == 11:
            preco += 1617
            total += [preco]
        elif Apostas == 12:
            preco += 3234
            total += [preco]
        elif Apostas == 13:
            preco += 6006
            total += preco
        elif Apostas == 14:
            preco += 10510.5
            total += [preco]
        elif Apostas == 15:
            preco += 17517.5
            total += [preco]
        print("Sr(a). %s, vocÃª apostou nos numeros %s" %(NomeJogador, printavel))
        print("Essa aposta deu R$:",preco)
        todas_apostas += [printavel]
        preco = 0
        comece = input("gostaria de jogar novamente?: ")
    else:
        print("Pague R$:",sum(total),"antes de sair")
        print("OBRIGADO POR USAR NOSSOS SERVIÃ‡OS")
    apostas = '|'.join(todas_apostas)
    return apostas, NomeJogador
