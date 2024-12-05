"""
Pedir al usuario que ingrese su año de nacimiento
y mostrar en pantalla la edad que tiene.
"""

anioNacimiento = int(input("Ingrese su año de nacimiento: "))
anioActual = int(input("Ingrese el año actual: "))

Edad = anioActual - anioNacimiento

print(f"Usted tiene {Edad} años.")