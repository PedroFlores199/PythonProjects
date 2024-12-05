
"""
Simula una ruleta de casino donde el 90% de los resultados son "Rojo"
Haz 10 giros y cuenta cuántas veces sale cada color
"""

import random

def ruleta():
    resultados = {"Rojo": 0, "Negro": 0}

    for i in range(10):
        aleatorio = random.random()
        if aleatorio <= 0.9:
            print("Rojo")
            resultados["Rojo"] += 1
        else:
            print("Negro")
            resultados["Negro"] += 1

    print(f"Rojo: {resultados['Rojo']} veces")
    print(f"Negro: {resultados['Negro']} veces")

ruleta()
