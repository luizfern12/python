from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
def QuemGanhou(cpu,player):

  def QuemJogouOque(cpu,player):
   print()
   print("Cpu jogou " + itens[cpu])
   print()
   print("Player jogou " + itens[player])
   print()

  if cpu == 0: # cpu pedra
    if player == 0: # player pedra
      print("Empate")
      QuemJogouOque(cpu,player)
    
    elif player == 1: # player papel
      print("Player vence")
      QuemJogouOque(cpu,player)
   
    elif player == 2: # player tesoura
      print("Cpu vence")
      QuemJogouOque(cpu,player)

    else:
      print("jogada invalida")
      print("")
      print("ninguem ganhou")


  elif cpu == 1: # cpu papel
    if player == 0: # player pedra
      print("Cpu vence")
      QuemJogouOque(cpu,player)
      
    elif player == 1: # player papel
      print("Empate")
      QuemJogouOque(cpu,player)
     
    elif player == 2: # player tesoura
      print("Player vence")
      QuemJogouOque(cpu,player)

    else:
      print("jogada invalida")
      print("")
      print("ninguem ganhou")


  elif cpu == 2: # cpu tesoura
    if player == 0: # player pedra
      print("Player Vence")
      QuemJogouOque(cpu,player)

    elif player == 1: # player papel
      print("Cpu vence")
      QuemJogouOque(cpu,player)

    elif player == 2: # player tesoura
      print("Empate")
      QuemJogouOque(cpu,player)
   
    else:
      print("jogada invalida")
      print("")
      print("ninguem ganhou")

while True:
  print('''
  Suas opcoes:

  [ 0 ] Pedra
  [ 1 ] Papel
  [ 2 ] Tesoura
  [ 3 ] Sair
  ''')

  player = int(input("qual a sua escolha?:"))
  
  if player == 3:
  	break

  cpu = int(randint(0, 2))

  print()
  print("Jo")
  sleep(1)
  print("Quem")
  sleep(1)
  print("Po")
  print()

  QuemGanhou(cpu,player)
