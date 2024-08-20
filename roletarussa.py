jogador1 = input("Pedra Papel ou Tesoura? ").lower()
jogador2 = input("Pedra Papel ou Tesoura? ").lower()
continuarJogo = "sim".lower()
while continuarJogo == "sim":
    if jogador1 == "pedra" and jogador2 == "papel":
        print("Jogador 2 ganhou")
    elif jogador1 == "pedra" and jogador2 == "tesoura":
        print("Jogador 1 ganhou")
    elif jogador1 == "pedra" and jogador2 == "pedra":
        print("Empate")
    elif jogador1 == "tesoura" and jogador2 == "papel":
        print("Empate")
    elif jogador1 == "tesoura" and jogador2 == "tesoura":
        print("Empate")
    elif jogador1 == "papel" and jogador2 == "papel":
        print("Empate")
continuarJogo =