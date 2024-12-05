"""
Adivina cualquier contraseña de
letras y números de hasta 4 caracteres
Usando fuerza bruta
"""

import random

def fuerza_bruta():


    usuario = input("Ingrese la contraseña (máximo 4 caracteres): ")
    if len(usuario) > 4:
        print("La contraseña debe tener un máximo de 4 caracteres.")
        return fuerza_bruta()

    while True:
        contrasena = ""
        for i in range(len(usuario)):
            contrasena += random.choice("abcdefghijklmnopqrstuvwxyz0123456789")

        print(f"Contraseña: {contrasena}")

        if contrasena == usuario:
            print(f"La contraseña es: {contrasena}")
            break

fuerza_bruta()