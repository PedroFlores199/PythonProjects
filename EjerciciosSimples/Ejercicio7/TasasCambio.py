"""
Comvierte una cantidad de divisa a otra usando una API de tasas de cambio en tiempo real
"""

import requests

tasas = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()

origen = input("Introduce la divisa de origen: ").upper()
destino = input("Introduce la divisa de destino: ").upper()
cantidad = float(input("Introduce la cantidad de divisa a convertir: "))

tasa = cantidad * tasas["rates"][destino] / tasas["rates"][origen]

print(f"{cantidad} {origen} son {tasa:.2f} {destino}")