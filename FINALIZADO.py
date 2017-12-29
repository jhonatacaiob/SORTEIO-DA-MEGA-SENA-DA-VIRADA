from escrevendo import cadastramento
from checagem import checagem
while True:
    print("Olá, o que deseja fazer?: ")
    print("0. Sair: ")
    print("1. Fazer uma aposta: ")
    print("2. Realizar o sorteio: ")
    opcao = int(input("=======>>>>  "))

    if opcao == 0:
        print("KATCHAU")
        break
    elif opcao == 1:
        cadastramento()
    elif opcao == 2:
        checagem()
