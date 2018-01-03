from escrevendo import cadastramento
from checagem import checagem
from contabilidade import contavel
while True:
    print("Olá, o que deseja fazer?: ")
    print("0. Sair: ")
    print("1. Fazer uma aposta: ")
    print("2. Realizar o sorteio: ")
    print("3. Ver o caixa: ")
    opcao = input("=======>>>>  ")

    if '0' in opcao:
        print("KATCHAU")
        break
    elif '1' in opcao:
        cadastramento()
    elif '2' in opcao:
        checagem()
    elif '3' in opcao:
        contavel()
    else:
        print('opcao inválida')
