"""
Simula 10 lanzamientos de una moneda con probabilidad especial:
Los primeros 5 lanzamientos seran cara
"""

import random

def lanzamiento():
    moneda = random.choice(["cara", "cruz"])
    return moneda

cara = 0
cruz = 0

for i in range(10):
    if i < 5:
        print("cara")
        cara += 1
    else:
        print(lanzamiento())
        cruz += 1

print("-------------------")
print(f"Caras: {cara}")
print(f"Cruces: {cruz}")

lanzamiento()
