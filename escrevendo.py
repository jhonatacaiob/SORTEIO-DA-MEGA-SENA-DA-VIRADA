def cadastramento():
    from SignInUser import cadastramento2
    apostas, NomeJogador = cadastramento2()
    informaçoes = open("informaçoes.csv", 'a')
    texto = ""
    texto = '%s: %s'%(NomeJogador, apostas)
    texto = texto + '\n'
    informaçoes.write(texto)
    informaçoes.close()
