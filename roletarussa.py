while(True):
   jogador1 = input("Pedra Papel ou Tesoura? \n").lower()
   jogador2 = input("Pedra Papel ou Tesoura? \n").lower()
   if jogador1 == "pedra":
      if jogador2 == "pedra":
         print("Empate")
      elif jogador2 == "papel":
         print("Jogador 2 ganhou")
      elif jogador2 == "tesoura":
         print("Jogador 1 ganhou")

   elif jogador1 == "tesoura":
      if jogador2 == "pedra":
         print("Jogador 2 ganha")
      elif jogador2 == "papel":
         print("Jogador 1 ganhou")
      elif jogador2 == "tesoura":
         print("Empate")
         
   elif jogador1 == "papel":
      if jogador2 == "pedra":
         print("Jogador 1 ganha")
      elif jogador2 == "papel":
         print("Empate")
      elif jogador2 == "tesoura":
         print("Jogador 2 ganha")
   else:
      print("Jogo invalido")
   jogo = input("Deseja continuar o jogo? s/n: " ).lower()
   if jogo != "s" or jogo != "sim":
      break