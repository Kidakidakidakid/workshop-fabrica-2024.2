jogador1 = input("\nPedra Papel ou Tesoura? ").lower()
jogador2 = input("\nPedra Papel ou Tesoura? ").lower()
jogo = True
continuarJogo = "sim".lower()
while continuarJogo == "sim":
    if jogador1 == "pedra":
        if jogador2 == "pedra":
            print("Empate")
        if jogador2 == "papel":
            print("Jogador 2 ganhou")
        if jogador2 == "tesoura":
            print("Jogador 1 ganhou")
    elif jogador1 == "tesoura":
        if jogador2 == "pedra":
            print("Jogador 2 ganha")
        if jogador2 == "papel":
            print("Jogador 1 ganhou")
        if jogador2 == "tesoura":
            print("Empate")
    elif jogador1 == "papel":
        if jogador2 == "pedra":
            print("Jogador 1 ganha")
        if jogador2 == "papel":
            print("Empate")
        if jogador2 == "tesoura":
            print("Jogador 2 ganha")
    continuarJogo = input("Deseja continuar o jogo? Sim/Nao ")
    if continuarJogo == "sim":
        jogo = True