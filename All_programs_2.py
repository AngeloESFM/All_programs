# 28 TUPLAS
# TUPLAS = Sirven para tener una colección de elementos exactamente al igual que una lista
# pero es inmutable, no se puede modificar
# nombre_de_la_tupla = (todos, los, datos, que quieras)

tupla = (42.88, 55.16)
listas = [42.88, 55.16]

listas[0] = 5

print(listas)
print(tupla)

# 29 FUNCIONES DEFINIDAS
# Sirven para definir funciones y escribir un bloque de código dentro de ella
"""
def nombre_de_la_funcion():
    codigo

mandar_a_llamar_la_funcion()

"""


def saludar(nombre, edad):
    print("Hola " + nombre + f" tienes {edad} años")
    print("adios")


print("primero")
saludar(nombre = input("ingresa un nombre "), edad = input("ingresa tu edad "))
print("último")

# 30 FUNCIONES LAMBDA
# Sirven para definir funciones cortas de una sola linea

resultado = lambda numero: numero + 20
print(resultado(30))

suma = lambda numero1, numero2: numero1 + numero2
print(suma(50,40))

# 31 RETURN
# Sirve para recibir datos de una función

def multiplicacion(num1, num2):
    multi = num1 * num2
    return multi

res_multi = multiplicacion(3, 7)
print(res_multi)

# 32 CONDICIONALES
# Sirve para comprobar si algo es cierto o falso y ejecutar una acción
"""
IF sentencia_a_comprobar:
ELIF sentencia_2_a_comprobar:
ELSE:

"""
eres_hombre = False
eres_alto = False

print("Antes del if")

if eres_hombre and eres_alto:
    print("Eres un hombre alto ")
elif eres_hombre and not eres_alto:
    print("Eres un hombre bajo")
elif not eres_hombre and eres_alto:
    print("No eres hombre, pero eres alto")
else:
    print("No eres hombre, ni alto")

print("Despues del if")

if eres_hombre or eres_alto:
    print("Eres hombre o eres alto")
else:
    print("No eres hombre o no eres alto")

# 33 COMPARADORES Y CONDICIONALES
# Sirven para comparar datos y con base en eso realizar funciones o condicionales
"""
def mayor_edad(num):
    if num >= 18:
        return True
    else:
        return False

edad = input("¿Cuántos años tienes?")

if mayor_edad(int(edad)):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
"""
"""
def numero_mayor(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
print("Escribe tres numeros: ")
num1, num2, num3 = input(), input(), input()
num1 = int(input())
num2 = int(input())
num3 = int(input())
numero = numero_mayor(num1, num2, num3)

numero = numero_mayor(int(num1), int(num2), int(num3))
print(numero)
"""

""" 
def pares(num):
    if num%2 == 0:
        return True
    else:
        return False

numero = input("Escribe un número para saber si es par")

if pares(int(numero)):
    print("Es par")
else:
    print("Es impar")
"""

# 34 MEJORAMOS LA CALCULADORA
# Mejoramos la calculadora anterior y esta será 2.0

operador = input("¿Qué operación quieres realizar? ( +, -, *, /, exp, raiz, par) ")
num1 = float(input("Escribe un número: "))
num2 = float(input("Escribe otro número: "))

if operador == "+":
    res = num1 + num2
    print("La suma es: " + str(res))
elif operador == "-":
    res = num1 - num2
    print("La resta es: " + str(res))
elif operador == "*":
    res = num1 * num2
    print("La multiplicación es: " + str(res))
elif operador == "/":
    res = num1 / num2
    print("La división es: " + str(res))
elif operador == "exp":
    res = num1 ** num2
    print("La exponente es: " + str(res))
elif operador == "par":
    if num1%2 == 0 and num2%2 == 0:
        print("Ambos números son pares")
    elif num1%2 == 0:
        print("El primer número es par y el segundo es impar")
    elif num2%2 == 0:
        print("El segundo número  es par y el primero es impar")
    else:
        print("Los números son impares")
elif operador == "raiz":
    num = 0
    nume = 0
    while num * num <= num1:
        num += 0.00001
    while nume * nume <= num2:
        nume += 0.00001
    print(num)
    print(nume)

else:
    print("Operador invalido")

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

# 36 CONJUNTOS
# Sirven al igual que las listas, pero no está ordenada, ni se pueden repetir elementos
# conjuntos y diccionarios se declaran con {}, listas [], tuplas()

conjunto = {2, True, "Hola", 39.13}
print(conjunto)

# Para agregar un elemento al conjunto se usa ADD
conjunto.add(False)
print(conjunto)

#Para eliminar un elemento del conjunto se usa REMOVE
conjunto.remove(False)
print(conjunto)

# 37 DICCIONARIOS
# Sirven para almacenar datos no ordenados, con una asignación (llave, valor)
# conjuntos y diccionarios se declaran con {}, listas [], tuplas()

dias = {
    "lun": "Lunes",
    "mar": "Martes",
    "mie": "Miércoles",
    "jue": "Jueves",
    "vie": "Viernes",
    "sab": "Sábado",
    "dom": "Domingo"
}
# entre corchetes accedemos a un elemeto con el identificador o llave
print(dias)
print(dias["mie"])

# con GET, si no existe la llave o identificador, imprime un mensaje que quieras poner
print(dias.get("l", "No es un identificador"))

# con POP, elimína el elemento de la llave o identificador que pongas
print(dias.pop("lun"))
print(dias)

# con POPITEM, elimína el último elemento y lo da, para usarlo como quieras
print( )
print(dias.popitem())
print(dias)

# con UPDATE, modifica un elemento dada la llave y si no existe, lo agrega al diccionario
print( )
dias.update(mar = "jueves")
print(dias)
dias.update(otro = "Otro día")
print(dias)

# 38 WHILE
# Sirve para hacer un búcle, repetir, una acción, "mientras" una condición no se cumpla

# Declaramos la variable
i = 1
# Iniciamos el búcle while
while i <= 5:
    print(i)
    i += 1

print("Terminó el while")

print(i)

# 39 BÚCLE FOR
# Sirve como un búcle y recorre toda una colección de datos

# la variable "letra" puede ser cualquier variable y sirve para recorrer la cadena
"""
for letra in  "AcademiaCoder":
    print(letra, id(letra))

# Si imprimimos "letra" fuera del for, nos da el último valor de la colección, en este caso la r
print(letra)
print(id(letra))

# También la podemos usar en listas

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

for dia in dias:
    print(dia)

print(dia)

# Si lo úsamos para un diccionario, se hace de la siguiente forma, junto con comando ITEMS

dias = {"lu": "Lunes","ma": "Martes","mi": "Miércoles","ju": "Jueves","vi": "Viernes"}

for clave,valor in dias.items():        # ITEMS recibe dos datos para los diccionarios
    print(clave)
    print(valor)
    print(clave, valor)
"""
# Si usamos RANGE(algun_rango) nos va a elegir el rango que indiquemos de nuestra colección
"""
for indice in range(5):       # Así muestra los rangos del 0 al 4
    print(indice)

for indice in range(2,5):     # Así muestra los rangos del 2 al 4
    print(indice)

for indice in range(1, 11, 2):      # Así muestra los rangos del 1 al 10, pero de dos en dos
    print(indice)
"""
# De la forma que a continuación viene puedes elegir el rango de lo que quieres recorrer

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# Así eliges el número de rango pero imprimiendo los días
for indice in range(5):
    print(dias[indice])

# y también con el comando len, para decir la longitud de la lista
for indice in range(len(dias)):
    print(dias[indice])

print(len(dias))

# Para elegir un ganador podemos hacerlo de la siguiente forma

for indice in range(10):
    if indice == 4:
        print("Ganaste")
    else:
        print("No eres ganador")

# También se pueden anidar los FOR, dónde recorre los de adentro primero y después los de afuera

for indice in range(5):
    for indice2 in range(3):
        print(indice, indice2)

# 40 BREAK AND CONTINUE
# Sirve para manejar el flujo de información en un búcle
# el comando BREAK, sirve para cuando queremos que pare el código y lo corta
"""
# Esto recorre e imprime del 0 al 10 y al llegar al 4 para el programa
# si ponemos el print después del break, no imprime el 4
for indice in range(10):
    if indice == 4:
        break
    print(indice)

# Si ponemos el print antes del break, sí imprime el 4
for indice in range(10):
    print(indice)
    if indice == 4:
        break
"""
# el comando CONTINUE, sirve para prevenir o quitar un dato, pero sigue ejecutando lo demás
# Si ponemos el print despues del continue, salta el que es igual a 4
for indice in range(10):
    if indice == 4:
        continue
    print(indice)

# Si ponemos el print antes del continue, no realiza ningún cambio y no funcionaria correctamente
for indice in range(10):
    print(indice)
    if indice == 4:
        continue

# BREAK Y CONTINUE, también funcionan con listas

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

for dia in dias:
    print(dia)
    if dia == "Jueves":
        break


for dia in dias:
    if dia == "Jueves":
        continue
    print(dia)

# 41 JUEGO DE ADIVINAR EL NÚMERO 2.0

while True:
    import random
    # Variables para modificar el juego
    posibilidades = 5
    limite = 20
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
        print("\n¡Suerte para la próxima ja ja ja!!!")
    print()
    print("Se acabó el juego. \n      ¿Quieres seguir jugando?")
    print("Presiona 1, si quieres volver a jugar ó \nPresiona 2, si quieres terminar el juego")
    continuar = input("> ")
    if continuar == "1":
        print("Aquí vamos de nuevo...")
    if continuar == "2":
        print("¡OK, nos vemos después!")
        break


# 42 CICLOS INFINITOS

# Iniciamos el ciclo infinito
while True:
    # Solicitamos al usuario que ponga 1, si quiere continuar el ciclo
    # 2 si lo quiere terminar

    print("Presiona (1) si quieres que siga el programa")
    print("Presiona (2) si quieres terminar el ciclo")
    opcion = input(">")
    if opcion == "1":
        print("GRACIAS, selecciona otra opción")
        print("--- =D ---")
    if opcion == "2":
        print("GRACIAS, detuviste el ciclo")
        break

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

# 44 LISTAS ANIDADAS

grilla_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# Para mostrar todas las listas
for num in grilla_numeros:
    print(num)

# Para mostrar los números uno por uno
for filas in grilla_numeros:
    for columnas in filas:
        print(columnas)

# 45 TRATAR CON ERRORES EN PYTHON
# TRY ... EXCEPT...ELSE...FINALLY

# TRY & EXCEPT, sirven para cuando haya un error lo brinque y siga ejecutando el programa
# Lo que está en el bloque de TRY, se ejecuta hasta que encuentra un error
try:
    num1 = int(input("Introduzca un número: "))
    num2 = 0
    print(num1)
    print(num1/num2)
# lo que está en el bloque de EXCEPT, se ejecuta cuando ocurre el error
# Para que escriba el error como python se hace de esta forma
except ZeroDivisionError as err:
    print(err)
# Puedes poner también tú propio mensaje
except ValueError:
    print("Ingresa un valor entero")
# lo que está en el bloque de ELSE, se ejecuta cuando no hay ninugún error
else:
    print("No hubo ningún error")
# Lo que está en el bloque de FINALLY, se ejecuta haya o no errores en el código
finally:
    print("Siempre se ejecuta el finally")

# 45 TRATAR CON ERRORES EN PYTHON
# TRY ... EXCEPT...ELSE...FINALLY

# TRY & EXCEPT, sirven para cuando haya un error lo brinque y siga ejecutando el programa
# Lo que está en el bloque de TRY, se ejecuta hasta que encuentra un error
try:
    num1 = int(input("Introduzca un número: "))
    num2 = 0
    print(num1)
    print(num1/num2)
# lo que está en el bloque de EXCEPT, se ejecuta cuando ocurre el error
# Para que escriba el error como python se hace de esta forma
except ZeroDivisionError as err:
    print(err)
# Puedes poner también tú propio mensaje
except ValueError:
    print("Ingresa un valor entero")
# lo que está en el bloque de ELSE, se ejecuta cuando no hay ninugún error
else:
    print("No hubo ningún error")
# Lo que está en el bloque de FINALLY, se ejecuta haya o no errores en el código
finally:
    print("Siempre se ejecuta el finally")

# MEJORAMOS LA CALCULADORA
# Mejoramos la calculadora anterior y esta será 3.0


while True:
    try:
        operador = input("¿Qué operación quieres realizar? ( +, -, *, /, exp, raiz, par) ")
        while (operador != "+" and operador != "-" and operador != "/" and operador != "*" and operador != "exp"
            and operador != "raiz"  and operador != "par"):
                print("Operador invalido")
                operador = input("¿Qué operación quieres realizar? ( +, -, *, /, exp, raiz, par) ")

        num1 = float(input("Escribe un número: "))
        num2 = float(input("Escribe otro número: "))
    except ValueError:
        print("No se puede realizar la operación, escribe un número")
        continue
    else:
        print("La operación se realizó con éxito")
    finally:
        print("Gracias por usar la calculadora")

    if operador == "+":
        res = num1 + num2
        print(f"La suma es: {res} ")
    if operador == "-":
        res = num1 - num2
        print(f"La resta es: {res}")
    if operador == "*":
        res = num1 * num2
        print(f"La multiplicación es: {res} ")
    if operador == "/":
        try:
            res = num1 / num2
            print(f"La división es: {res}")
        except ZeroDivisionError as err:
            print("No se puede realizar")
            print(err)
    if operador == "exp":
        res = num1 ** num2
        print(f"La exponente de {num1} a la {num2} es: {res}")
    if operador == "par":
        if num1%2 == 0 and num2%2 == 0:
            print("Ambos números son pares")
        elif num1%2 == 0:
            print("El primer número es par y el segundo es impar")
        elif num2%2 == 0:
            print("El primer número es impar y el segundo es par ")
        else:
            print("Los dos números son impares")
    if operador == "raiz":
        num = 0
        nume = 0
        while num * num <= num1:
            num += 0.00001
        while nume * nume <= num2:
            nume += 0.00001
        print(num)
        print(nume)

    print("Pon 1 si quieres seguir haciendo operaciones")
    print ("ó 2 si quieres terminar el programa")
    opcion = input(">")

    if opcion == "1":
        print()
    if opcion == "2":
        print("OK, Nos vemos luego!")
        break



