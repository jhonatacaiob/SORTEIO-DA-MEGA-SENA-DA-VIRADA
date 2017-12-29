#DECLARÇÃO DAS VARIAVEIS
from random import randint
resultado = []
vezes = int ( input ( "Quantos números você quer sortear?: " ) )
#vezes = 6




#SELEÇÃO DOS NUMEROS ALEATÓRIOS
while len(resultado) < vezes:
    contador = 0
    n = randint(1,60)
    for i in range(0,len(resultado)):
        if n == resultado[i]:
            contador += 1
    if contador == 0:
        resultado += [n]


#FORMATAÇÃO DOS NUMEROS EM ORDEM CRESCENTE

result_cres = []
for i in range(1,61):
    for r in resultado:
        if  i == r :
            i = str(i)
            result_cres += [i]
#CONVERSÃO DA LISTA EM STRING
rc = ", ".join(result_cres)


#IMPRESSÃO DOS NUMEROS PARA O USUÁRIO
print("Os numeros sorteados foram %s, PARABENS AOS GANHADORES" %(rc))


#PEGA PORRA, CONSEGUI SEUS ARROMBADO
