def contavel():
    from conversao import conversao
    total = 0
    informaçoes = open('informaçoes.csv', 'r')
    for i in informaçoes:
        lis = i.split(": ")
        n = lis[1]
        n = n.split("|")
        for a in range(len(n)):
            n1 = n[a].split(",")
            tam_apo = len(n1)
            Apostas = tam_apo
            if Apostas == 6:
                total += 3.5
            elif Apostas == 7:
                total += 24.5
            elif Apostas == 8:
                total += 98
            elif Apostas == 9:
                total += 294
            elif Apostas == 10:
                total += 735
            elif Apostas == 11:
                total += 1617
            elif Apostas == 12:
                total += 3234
            elif Apostas == 13:
                total += 6006
            elif Apostas == 14:
                total += 10510.5
            elif Apostas == 15:
                total += 17517.5
    total = conversao(total)
    print("Você tem",total,"no caixa")
    informaçoes.close()
