"""
Crea una tragamonedas simple con 3 ruedas de emogis
Si las 3 ruedas couinciden muestra el mensaje de "JACKPOT"
"""

import random

def tragamonedas():
    rueda1 = random.choice(["🍇", "🍉", "🍊", "🍋", "🍌"])
    rueda2 = random.choice(["🍇", "🍉", "🍊", "🍋", "🍌"])
    rueda3 = random.choice(["🍇", "🍉", "🍊", "🍋", "🍌"])

    resultado = []

    resultado.append(rueda1)
    print(f"{rueda1}")
    input (" ")
    resultado.append(rueda2)
    print(f"{rueda2}")
    resultado.append(rueda3)
    input (" ")
    print(f"{rueda3}")

    print("-------------------")


    if rueda1 == rueda2 == rueda3:
        print("JACKPOT")
        return False

while True:
    if tragamonedas() == False:
        break
