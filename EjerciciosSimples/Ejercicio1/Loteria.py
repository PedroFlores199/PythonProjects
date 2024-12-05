"""
Simula una loteria donde eliges
un numero entre 1 y 10.
Asegurate de que nunca coincida con el numero
ganador.
Ejecuta 7 sorteos.
"""

import random

def loteria():
    usuario = random.randint(1, 10)
    ganador = random.randint(1, 10)

    #Hasta que no sean diferentes no sale del bucle
    while usuario == ganador:
        ganador = random.randint(1, 10)

    print(f"Usuario : {usuario}")
    print(f"Ganador: {ganador}")

for i in range(7):
    loteria()
