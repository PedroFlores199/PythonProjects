"""
Cuenta las vocales que tiene una palabra
"""

def contarVocales(palabra):
    vocales = "aeiou"
    contador = 0

    for letra in palabra:
        if letra in vocales:
            contador += 1

    print(f"Tiene {contador} vocales")
    return contador


contarVocales("Hola")