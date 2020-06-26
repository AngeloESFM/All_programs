# 35 JUEGO ADIVINA EL NÚMERO 1.0

# Para mandar a llamar una libreria usamos import

import random

# Generamos un número aleatorio
adivina = random.randint(1,10)
print("Hola, ¿cómo te llamas?")
nombre = input()
print("Bien " + nombre + " vamos a jugar, estoy pensando un número del 1 al 10.")
print("¿Podrias adivinar qué número es? Recuerda, sólo tienes 3 intentos")

num = int(input("¡1er Intento! "))

if num == adivina:
    print("¡¡¡ GANASTE :] !!!")
else:
    if num < adivina:
        print("Intenta con uno mayor")
    else:
        print("Intenta con uno menor")

    num = int(input("\n ¡¡2do intento!! "))
    if num == adivina:
        print("¡¡¡ GANASTE :] !!!")
    else:
        if num < adivina:
            print("Intenta con uno mayor")
        else:
            print("Intenta con uno menor")

        num = int(input("\n¡¡¡3er intento :O !!! "))
        if num == adivina:
            print("¡¡¡ GANASTE :] !!!")
        else:
            print("\n¡Suerte para la próxima ja ja ja!")




