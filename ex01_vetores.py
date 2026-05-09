#OP.VET_LT.1
#Declaração de variáveis

#Início

import random

def func_somaimp (vetor):
    soma: int = 0
    for i in vetor:
        if (i % 2 != 0):
            soma += i
    print ("A soma dos ímpares do vetor equivale a:", soma)


def func_media (vetor, count):
    soma: int = 0
    for i in vetor:
        if (i >= 10 and i <= 200):
            if (count >= 0):
                soma += i
                count += 1
    med = (soma / count)
    print (f"A média dos números entre 10 e 200 é igual a: {med: .2f}")



def main ():
    vet = []
    tam = 50
    cont: int = 0

    for i in range (tam):
        vet.append (random.randint (0, 300))
    
    func_media (vet, cont)

    func_somaimp (vet)

if (__name__ == "__main__"):
    main ()