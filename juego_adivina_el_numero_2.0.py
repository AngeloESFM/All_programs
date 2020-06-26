# 41 JUEGO DE ADIVINAR EL NÚMERO 2.0

while True:
    import random
    # Variables para modificar el juego
    posibilidades = 5
    limite = 100
    intentos = 0

    print("     Hola, ¿cómo te llamas?")
    nombre = input()
    print("Bien " + nombre + " vamos a jugar, estoy pensando un número del 1 al " + str(limite) + ".")
    print("¿Podrias adivinar qué número es? Recuerda, sólo tienes " + str(posibilidades) + " intentos.")

    # Generamos un número aleatorio
    adivina = random.randint(1,limite)

    while intentos < posibilidades:
        num = int(input("Escoge un número: "))
        if num == adivina:
            print("\nGANASTES!!!")
            break
        else:
            if num < adivina:
                if intentos == posibilidades - 1:
                    break
                print("Intenta con un número más grande")

            else:
                if intentos == posibilidades - 1:
                    break
                print("Intenta con un número más pequeño")
        intentos += 1

    if num != adivina:
        print("\n       PERDISTES!!")
        print("¡Suerte para la próxima ja ja ja!!!")
        print(f"El número era: {adivina}")
    print()
    print("Se acabó el juego. \n      ¿Quieres seguir jugando?")
    print("Presiona 1, si quieres volver a jugar ó \nPresiona 2, si quieres terminar el juego")
    continuar = input("> ")
    if continuar == "1":
        print("Aquí vamos de nuevo...")
    if continuar == "2":
        print("¡OK, nos vemos después!")
        break


