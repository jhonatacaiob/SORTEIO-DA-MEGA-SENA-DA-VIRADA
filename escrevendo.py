def cadastramento():
    from SignInUser import cadastramento2
    apostas, NomeJogador = cadastramento2()
    informaçoes = open("informaçoes.csv", 'a')
    texto = ""
    texto = '%s: %s'%(NomeJogador, apostas)
    informaçoes.write(texto)
    informaçoes.write("\n")
    informaçoes.close()
