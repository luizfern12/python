from random import randint
from time import sleep
import os

while True:
    chances = 3
    print("você consegue adivinhar o número que eu escolhi?")
    print("obs:você tem 3 chances")
    print("")
    while chances > 0:
        cpu = randint(0,10)
        player = int(input("Digite um número de 0 a 10:"))
        print("")
        if player == cpu:
            print("Parabens você acertou!!!")
            break
        else:
            print("Você errou :(")
            print("")
            chances -= 1
        if chances <= 0:
            print("todas as suas chances acabaram :(")
            break
    sleep(3)
    os.system('clear') or None