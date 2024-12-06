"""
EJERCICIO:
¡Ha comenzado diciembre! Es hora de montar nuestro
árbol de Navidad...

Desarrolla un programa que cree un árbol de Navidad
con una altura dinámica definida por el usuario por terminal.

Ejemplo de árbol de altura 5 (el tronco siempre será igual):

    *
   ***
  *****
 *******
*********
   |||
   |||

El usuario podrá seleccionar las siguientes acciones:

- Añadir o eliminar la estrella en la copa del árbol (@)
- Añadir o eliminar bolas de dos en dos (o) aleatoriamente
- Añadir o eliminar luces de tres en tres (+) aleatoriamente
- Apagar (*) o encender (+) las luces (conservando su posición)
- Una luz y una bola no pueden estar en el mismo sitio

Solo puedes añadir una estrella, y tantas luces o bolas
como tengan cabida en el árbol. El programa debe notificar
cada una de las acciones (o por el contrario, cuando no
se pueda realizar alguna).
"""
import random

arbol = []
arbol_luces = []

def crear_arbol_navidad(altura):

     # Se multiplican cuantos espacios se van a necesitar y cuantos * se van a necesitar
    for i in range (altura):
        arbol.append(" " * (altura - i) + "*" * (i * 2 + 1))
        arbol_luces.append(" " * (altura - i) + "*" * (i * 2 + 1))
    # Si por ejemplo la altura fuera 5 se dejaria un espacio de 4 alineandolo con el * del principio
    arbol.append(" " * (altura - 1) + "|||")
    arbol_luces.append(" " * (altura - i) + "*" * (i * 2 + 1))
    #Iteramos el array
    for i in arbol:
        print(i)

def anadir_estrella(altura):
    arbol [0] = " " * (altura) + "@" + " " * (altura - 1)
    for i in arbol:
        print(i)
    return arbol



def anadir_bolas():
    # Evitamos la estrella y el tronco
    for i in range(1, len(arbol) - 1):
        linea = list(arbol[i])
        contador = 0
        for j in range(len(linea)):
            if linea[j] == "*" and contador % 2 == 0 and random.choice([True, False]):
                linea[j] = "0"
                contador += 1
            elif linea[j] == "*":
                contador += 1
        arbol[i] = "".join(linea)

    for i in arbol:
        print(i)
    return arbol

def anadir_luces():
    # Evitamos la estrella y el tronco
    for i in range(1, len(arbol) - 1):
        linea = list(arbol[i])
        contador = 0
        for j in range(len(linea)):
            if linea[j] == "*" and contador % 3 == 0 and random.choice([True, False]):
                linea[j] = "+"
                contador += 1
            elif linea[j] == "*":
                contador += 1
        arbol[i] = "".join(linea)
        arbol_luces[i] = "".join(linea)
    for i in arbol:
        print(i)

    return arbol

def apagar_encender_luces ():
    # Evitamos la estrella y el tronco
    opcion = int(input("Introduce 1 para apagar las luces y 2 para encenderlas: "))
    if opcion == 1:
        for i in range(1, len(arbol) - 1):
            linea = list(arbol_luces[i])
            contador = 0
            for j in range(len(linea)):
                if linea[j] == "+":
                    linea[j] = "*"
            arbol[i] = "".join(linea)
    elif opcion == 2:
        for i in range(len(arbol)):
            arbol_luces [i] = arbol [i]

    for i in arbol:
        print(i)
    return arbol



def main ():
    altura = int(input("Introduce la altura del árbol: "))
    crear_arbol_navidad(altura)

    while True:
        print("Opciones:")
        print("1. Añadir o eliminar la estrella en la copa del árbol (@)")
        print("2. Añadir o eliminar bolas (o) aleatoriamente")
        print("3. Añadir o eliminar luces (+) aleatoriamente")
        print("4. Apagar (*) o encender (+) las luces (conservando su posición)")
        print("5. Salir")
        opcion = int(input("Introduce una opción: "))

        if opcion == 1:
            anadir_estrella(altura)
        elif opcion == 2:
            anadir_bolas()
        elif opcion == 3:
            anadir_luces()
        elif opcion == 4:
            apagar_encender_luces()
        elif opcion == 5:
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()


