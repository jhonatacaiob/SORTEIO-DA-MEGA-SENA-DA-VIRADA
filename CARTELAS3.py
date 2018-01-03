def cadastramento1():
    def teste(numeros):
        NomeUser = []
        while len (NomeUser) < numeros:
            contador = 0
            jogada = int(input("Qual a %i° dezena?: " %(len(NomeUser)+1) ))
            if jogada > 60 or jogada < 1 :
                print("Numero Invalido")
            else:
                for i in NomeUser:
                    if jogada == i:
                        contador += 1
                if contador == 0:
                    NomeUser += [jogada]
                else:
                    print("Voce já jogou esse número")

        return NomeUser


    #AQUI VAI COMEÇAR O CODIGO
    while True:
        Apostas = int(input("Quantos numeros voce quer apostar?: "))
        if Apostas < 6 or Apostas > 15:
            print("Jogada Inválida, escolha um numero de 6 a 15")
        else:
            ok = teste(Apostas)
            okp = []
            for j in range(1,61):
                for i in ok:
                    if j == i:
                        i = str(i)
                        okp += [i] 
            printavel = ",".join(okp)
            break
    return printavel, Apostas
