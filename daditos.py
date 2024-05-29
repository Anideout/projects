import random
import os

valor_minimo = 1
valor_maximo = 6

juega_otra_vez = "si"

while juega_otra_vez == "si" or juega_otra_vez == "s":
    print("tirando los dados....")
    print("los numeros son....")
    print(random.randint(valor_minimo, valor_maximo))
    print(random.randint(valor_minimo, valor_maximo))
    juega_otra_vez = input("Tirar los dados otra vez uwu ?\n")
    os.system("clear")
    if juega_otra_vez == "no" or juega_otra_vez == "n":
        print("hasta la proximaaaaa uwu")

