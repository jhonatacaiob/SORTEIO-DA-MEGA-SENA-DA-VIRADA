#DECLARÇÃO DAS VARIAVEIS
from random import randint, sample
resultado = []
vezes = int ( input ( "Quantos números você quer sortear?: " ) )
#vezes = 6

l = [x for x in range(1,61)]

print(l)
sampl = sample(l,vezes)
print(sampl)
result_cres = sorted(sampl)
print(result_cres)
result_cres = list(map(str,result_cres))
print(result_cres)
#CONVERSÃO DA LISTA EM STRING
rc = ", ".join(result_cres)


#IMPRESSÃO DOS NUMEROS PARA O USUÁRIO
print("Os numeros sorteados foram %s, PARABENS AOS GANHADORES" %(rc))


#PEGA PORRA, CONSEGUI SEUS ARROMBADO
