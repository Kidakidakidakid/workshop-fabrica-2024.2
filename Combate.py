import random

def ataqueTotal():
    atributo = random.randint(0,10)
    bonus = random.randint(0,5)
    arma = random.randint(0,10)
    return atributo + bonus + arma

def armaduraTotal():
    atributo = random.randint(0,10)
    bonus = random.randint(0,5)
    armadura = random.randint(0,10)
    return atributo+bonus+armadura

def danoFinal():
    ataque = ataqueTotal()
    armadura = armaduraTotal()
    print(ataque,armadura)
    
    if ataque > armadura:
        dano = random.randint(1,12)
        print(dano)
        return f"Ataque acertou! Dano causado: {dano}"
    else:
        return "Nao acertou"
    
    
print(danoFinal())