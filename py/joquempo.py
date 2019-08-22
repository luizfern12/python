from random import randint
from time import sleep
def QuemGanhou(cpu,cpu1):
  if cpu == 0: # cpu pedra
    if cpu1 == 0: # player pedra
      print("Empate")
    elif cpu1 == 1: # player papel
      print("Player vence")
    elif cpu1 == 2: # player tesoura
      print("Cpu vence")
    else:
      print("Jogada invalida")

  elif cpu == 1: # cpu papel
    if cpu1 == 0: # player pedra
      print("Cpu vence")
    elif cpu1 == 1: # player papel
      print("Empate")
    elif cpu1 == 2: # player tesoura
      print("Player vence")
    else:
      print("Jogada invalida")

  elif cpu == 2: # cpu tesoura
    if cpu1 == 0: # player pedra
      print("Player Vence")
    elif cpu1 == 1: # player papel
      print("Cpu vence")
    elif cpu1 == 2: # player tesoura
      print("Empate") 
    else:
      print("Jogada invalida")
      
itens = ("Pedra", "Papel", "Tesoura")
while True:
  print('''
  Suas opcoes:

  [ 0 ] Pedra
  [ 1 ] Papel
  [ 2 ] Tesoura
  [ 3 ] Sair
  ''')

  player = int(input("qual a sua escolha? "))
  
  if player == 3:
  	break
  
  cpu = int(randint(0, 2))

  print()
  print("Jo")
  sleep(1)
  print("Kem")
  sleep(1)
  print("Po")
  print()

  QuemGanhou(cpu,player)
                                                
  print()
  print("Cpu jogou " + itens[cpu])
  print()
  print("Player jogou " + itens[player])
  print()