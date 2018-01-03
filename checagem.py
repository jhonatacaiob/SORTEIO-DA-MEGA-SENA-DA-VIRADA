def checagem():
    from SORTEIO import result_cres
    premio = 306
    lis_win = []
    for h in range(len(result_cres)):
        result_cres[h] = int(result_cres[h])
    informaçoes = open('informaçoes.csv', 'r')
    for i in informaçoes:
        lis = i.split(": ")
        n = lis[1]
        n = n.split("|")
        for a in range(len(n)):
            contador = 0
            n1 = n[a].split(",")
            for j in range(len(n1)):
                n1[j] = int(n1[j])
            for l in result_cres:
                for g in n1:
                    if l == g:
                        contador += 1
            lis_win += [contador]
    informaçoes.closed
    nom_win = ''
    maxi = max(lis_win)
    informaçoes = open('informaçoes.csv', 'r')
    for i in informaçoes:
        lis = i.split(": ")
        m = lis[0]
        n = lis[1]
        n = n.split("|")
        for a in range(len(n)):
            contador = 0
            n1 = n[a].split(",")
            for j in range(len(n1)):
                n1[j] = int(n1[j])
            for l in result_cres:
                for g in n1:
                    if l == g:
                        contador += 1
            if contador == maxi:
                nom_win += m + ','
    nom_win = nom_win.split(',')
    del nom_win[-1]
    nom_winS = ", ".join(nom_win)
    le = len(nom_win)
    div = premio/le
    if len(nom_win) == 1 and maxi == 1:
        print("%s acertou %i dezena"% (nom_winS, maxi))
        print('%s ganhou %i milhões de reais' %(nom_winS, premio))
    elif len(nom_win) > 1 and maxi > 1 :
        print("%s acertaram %i dezenas" %(nom_winS, maxi))
        print("Cada um ganhou aproximadamente %i milhões de reais"%(div)) 
    elif len (nom_win)  > 1 and maxi == 1:   
        print("%s acertaram %i dezena" %(nom_winS, maxi))
        print("Cada um ganhou aproximadamente %i milhões de reais"%(div))
    else:
        print("%s acertou %i dezenas"% (nom_winS, maxi))
        print('%s ganhou %i milhões de reais' %(nom_winS, premio))
    informaçoes.close()
