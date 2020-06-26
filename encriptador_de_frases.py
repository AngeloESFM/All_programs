# 43 PROGRAMA QUE CAMBIA LAS VOCALES POR X

# "Hola AcademiaCoder, ¿cómo están hoy?
# Caracter que pondrá x ó X
# "Hxlx XcxdxmxxCxdxr, ¿cxmx xstxn hxy?

# Variables para modificar el programa


def encriptar(frase, caracter):
    encriptada = ""
    for letra in frase:
        if letra.lower() in "aeiouáéíóú":
            if letra.isupper():
                encriptada = encriptada + caracter.upper()
            else:
                encriptada = encriptada + caracter
        else:
            encriptada = encriptada + letra
    return encriptada

while True:
    caracter_elegido = input("Escribe la letra que cambia las vocales: ")
    print(encriptar(input("Escriba una frase\n > "), caracter_elegido))
    print("Elige 1 si quieres encriptar otra frase")
    print("ó 2 si quieres terminar el programa")
    opcion = input(">")
    if opcion == "2":
        print("¡HASTA LUEGO!")
        break
    if opcion == "1":
        print("----0----")
