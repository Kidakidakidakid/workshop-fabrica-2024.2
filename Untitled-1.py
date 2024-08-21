import random

def ataqueTotal(atributo,bonus,arma):
    atributo = random.randint(0,10)
    bonus = random.randint(0,5)
    arma = random.randint(10,20)
    return atributo + bonus

def armaduraTotal(atributo,bonus,armadura):
    atributo = random.randint(0,10)
    bonus = random.randint(0,5)
    armadura = random.randint(0,10)
    return atributo+bonus+armadura

def danoFinal(ataqueTotal,armaduraTotal):
    if ataqueTotal > armaduraTotal:
        dano = random.randint(1,12)
        return dano
    else:
        return "Nao acertou"
print(danoFinal)