def cadastramento2():
    from CARTELAS3 import cadastramento1
    NomeJogador = input("Qual seu nome?: ")
    preco = ''
    comece = 's'
    todas_apostas = []
    while comece == "sim" or comece == "s":
        printavel, Apostas = cadastramento1()
        if Apostas == 6:
            preco += '3,50'
        elif Apostas == 7:
            preco += '4,50'               
        elif Apostas == 8:
            preco += '98'
        elif Apostas == 9:
            preco += '294'
        elif Apostas == 10:
            preco += '735'
        elif Apostas == 11:
            preco += '1.617'
        elif Apostas == 12:
            preco += '3.234'
        elif Apostas == 13:
            preco += '6006'
        elif Apostas == 14:
            preco += '10.510,5'
        elif Apostas == 15:
            preco += '17.517,50'
        print("Sr(a). %s, você apostou nos numeros %s" %(NomeJogador, printavel))
        print("Pague R$: %s antes de sair" %(preco))
        todas_apostas += [printavel] 
        comece = input("gostaria de jogar novamente?: ")
        preco = ''
    else:
        print("OBRIGADO POR USAR NOSSOS SERVIÇOS")
    apostas = '|'.join(todas_apostas)
    return apostas, NomeJogador
