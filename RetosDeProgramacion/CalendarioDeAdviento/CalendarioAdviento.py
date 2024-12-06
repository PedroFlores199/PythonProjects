"""
EJERCICIO:
¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
developers. Del 1 al 24 de diciembre: https://adviento.dev

Dibuja un calendario por terminal e implementa una
funcionalidad para seleccionar días y mostrar regalos.
- El calendario mostrará los días del 1 al 24 repartidos
  en 6 columnas a modo de cuadrícula.
- Cada cuadrícula correspondiente a un día tendrá un tamaño
  de 4x3 caracteres, y sus bordes serán asteríscos.
- Las cuadrículas dejarán un espacio entre ellas.
- En el medio de cada cuadrícula aparecerá el día entre el
  01 y el 24.

Ejemplo de cuadrículas:
**** **** ****
*01* *02* *03* ...
**** **** ****

- El usuario seleccioná qué día quiere descubrir.
- Si está sin descubrir, se le dirá que ha abierto ese día
  y se mostrará de nuevo el calendario con esa cuadrícula
  cubierta de asteríscos (sin mostrar el día).

Ejemplo de selección del día 1
**** **** ****
**** *02* *03* ...
**** **** ****

- Si se selecciona un número ya descubierto, se le notifica
  al usuario.
"""

calendario = [f"{i:02}" for i in range(1, 25)] #Explicacion: creamos una lista con los días del calendario, con un formato de dos dígitos, :02 lo que hace es que tenga 2 digitos pero se podria hacer asi tambien --> [str(i).zfill(2) for i in range(1, 25)]

def calendario_adviento():
    for i in range(0, 24, 6): #Explicacion: vamos a recorrer el calendario de 6 en 6 para que se muestre de forma ordenada
        print("**** " * 6)
        print(" ".join(f"*{calendario[j]}*" for j in range(i, i + 6)))  #Explicacion: como calendario es una cadena de texto tenemos que insertar la cadena de forma ordenada, por lo que vamos a tener un bucle con los rangos que queramos que recorra y insertándolo en la cadena de texto
        print("**** " * 6)
        print()

def descubrir_dia():
    global calendario
    try:
        dia = int(input("Introduce el día que quieres descubrir (1-24): "))
        if dia < 1 or dia > 24:
            print("Día no válido. Intenta de nuevo.")
            return

        if calendario[dia - 1] == "****":
            print("Ya has descubierto este día.")
        else:
            print(f"Has descubierto el día {dia}. ¡Aquí está tu regalo!")
            calendario[dia - 1] = "****"
            calendario_adviento()

    except ValueError:
        print("Por favor, introduce un número válido.")


calendario_adviento()

while True:
    descubrir_dia()
