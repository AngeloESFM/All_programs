# EJERCICIOS PARA DEFINIR FUNCIONES

# EUP que devuelva el área del rectangulo a partir de una base y una altura
"""
def area_rectangulo(base, altura):
    are = float(base) * float(altura)
    return are

arear = area_rectangulo(base = input("Introduce la base del rectángulo: "),
                       altura = input("Introduce la altura del rectángulo: "))
print(f"El área del rectángulo es: {arear}")
"""
# EUP que devuelva el área de un círculo a partir de un radio. (R^2)* PI
"""
import math

def area_circulo(radio):
    area = (float(radio)**2)*math.pi
    return area
areac = area_circulo(radio = input("Introduce el radio del círculo: "))
print(f"El área del circulo es {areac}")
"""
# EUP que a partir de dos números cumpla lo siguiente:
# Si el primer número es mayor que el segundo, debe devolver 1.
# Si el primer número es menor que el segundo, debe devolver -1.
# Si ambos números son iguales, debe devolver un 0.
"""
def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

relab = relacion(a = input("Escribe un número: "), b = input("Escribe otro número: "))
print (relab)
"""
# EUP  que a partir de dos números, devuelva su punto intermedio.
# Cuando lo tengas comprueba el punto intermedio entre -12 y 24:
"""
def intermedio(a, b):
    inte = (float(a) + float(b)) / 2
    return inte

int = intermedio(a = input("Escribe un número: "), b = input("Escribe otro número: "))
print(int)
"""
# EUP que tome una lista de números enteros y devuelva dos listas ordenadas.
# La primera con los números pares y la segunda con los números impares.

# Definimos una lista vacia y se le van pidiendo valores al usuario
"""
list = []
n = int(input("Introduzca una lista de números, indica cuántos números ingresaras: "))
for x in range(n):
    valor = int(input("Ingrese un valor entero:"))
    list.append(valor)

def separar(lista):
    lista.sort()                 #SORT sirve para ordenar una lista de menor a mayor
    pares = []
    impares = []
    for l in lista:
        if l%2 == 0:
            pares.append(l)
        else:
            impares.append(l)
    return pares, impares
#imprimimos las listas
print("La lista es: ", list)
pares, impares = separar(list)
print("Los pares son: ", pares)
print("Los impares son: ", impares)
"""
# Definición como una función para obtener un factorial

"""
def factorial(num):
    if num > 1:
        num = num * factorial(num-1)
    print("valor final ->", num)
    return num

print(factorial(int(input("Ingresa un número para obtener su factorial: "))))
"""
# EUP que calcule el área de un círculo y otra que calcule el volúmen de un cilindro usando la primera función.
# A= pi (r**2) v = pi(r**2)(h)

"""
import math

def area_circulo(radio):
    area = math.pi * (radio**2)
    return area
def volumen_cilindro(altura, area):
    volumen = area * altura
    return volumen

radio = area_circulo(int(input("Introduce el radio del circulo: ")))
print("El área del circulo es:", radio)
altura = volumen_cilindro(int(input("Introduce la altura del cilindro: ")), radio)
print("El volúmen del cilindro es:", altura)
"""
# EUP que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
"""
def cuadrados(lista):
    cuadra = []
    for l in lista:
        l = l ** 2
        cuadra.append(l)        # Tambien se puede cuadra.append(l**2) y eliminamos la linea anterior
    return cuadra

list = []
n = int(input("Cuántos números ingresará?: "))
for x in range(n):
    valores = int(input("Introduzca un número: "))
    list.append(valores)

res = cuadrados(list)
print(res)
"""

# EUP que pida la anchura y altura de un rectángulo y lo dibuje con caracteres producto (*):
"""
def rectangle(base, altura):
    for i in range(altura):
        for j in range(base):
            print("*", end="")
        print()

rec = rectangle(base = int(input("Introduce la base del rectángulo: ")),
                altura = int(input("Introduce la altura del ractángulo: ")))
"""
# EUP que pida la anchura y altura de un rectángulo y lo dibuje con caracteres que elija el usuario:
"""
def rectangle(base, altura, caracter):
    for i in range(altura):
        for j in range(base):
            print(f"{caracter}", end="")
        print()

base = int(input("Introduce la base del rectángulo: "))
altura = int(input("Introduce la altura del ractángulo: "))
caracter = input("Elija un caracter para dibujar el rectángulo: ")
rectangle(base, altura, caracter)
"""
# EUP que pida la anchura de un triángulo y lo dibuje con caracteres producto (*):
"""
def triangle(ancho):
    for i in range(1, ancho + 1):
        for j in range(i):
            print("* ", end="")
        print()

    for i in range(1, ancho):
        for j in range(ancho - i):
            print("* ", end="")
        print()

triangle(ancho = int(input("Introduzca el ancho del triángulo: ")))
"""
# EUP que pida la anchura de un triángulo y dibuje una sucesión de triángulos con caracteres producto (*):
"""
def ascendente(ancho):
    for i in range(1, ancho + 1):
        for j in range(i):
            print("* ", end="")
        print()
def descendente(ancho):
    for i in range(1, ancho):
        for j in range(ancho - i):
            print("* ", end="")
        print()

ancho = int(input("Introduzca el ancho del triángulo: "))
for i in range(ancho, 0, -1):
    ascendente(i)
    descendente(i)
"""
# EUP que pida un año y que escriba si es bisiesto o no.
"""
print("COMPROBADOR DE AÑOS BISIESTOS")
def bisiesto(fecha):
    if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
        print("El año", fecha, "es un año bisiesto.")
    else:
        print("El año", fecha, "no es un año bisiesto.")

fecha = int(input("Escriba un año y le diré si es bisiesto: "))
bisiesto(fecha)
#bisiesto(fecha = int(input("Escriba un año y le diré si es bisiesto: ")))
print(fecha % 400)
print(fecha % 100, fecha % 4)
"""

# EUP  que pida dos años y escriba cuántos años bisiestos hay entre esas dos fechas (incluidos los dos años):
"""
def bisiesto(fecha1, fecha2):
    contador = 0
    for i in range(fecha1, fecha2 + 1):
        if i % 400 == 0 or (i % 100 != 0 and i % 4 == 0):
            contador += 1
    print(f"De {fecha1} a {fecha2} hay {fecha2 - fecha1 + 1} años, {contador} de ellos son bisiestos")
fecha1 = int(input("Escriba un año: "))
fecha2 = int(input(f"Escriba un año posterior a {fecha1}: "))
while fecha2 <= fecha1:
    fecha2 = int(input(f"Escriba un año posterior a {fecha1} intenta de nuevo: "))

bisiesto(fecha1, fecha2)
"""
# EUP que permita crear una lista de palabras (que puede ser vacía).
# Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista.
# Por último, el programa tiene que escribir la lista.
"""
def lista(num):
    lista = []
    if num == 0:
        print(f"La lista está vacía {lista}")
    else:
        for i in range(num):
            palabras = input(f"Introduce la palabra {i + 1}: ")
            lista.append(palabras)   # Ó también se puede lista += [palabras]
        print(f"La lista creada es: {lista}")


num = int(input("¿Cuántas palabras quieres incluir en la lista? "))
lista(num)
"""
# EUP que pida cuántas listas se quieren crear y las solicite a continuación:
"""
def lista(num):
    lista1 = []
    if num == 0:
        print(f"La lista está vacía {lista1}")
    else:
        for i in range(1, num + 1):
            palabras = input(f"Introduce la palabra {i}: ")
            lista1.append(palabras)   # Ó también se puede lista += [palabras]
        return lista1


num2 = int(input("¿Cuántas listas quiere escribir? "))

for i in range(1 , num2 + 1):
    num = int(input("¿Cuántas palabras quieres incluir en la lista? "))
    res_lista = lista(num)
    print(f"La lista número {i} es: {res_lista}")
"""
# Modifique el programa anterior de manera que las listas se escriban al final del programa:
"""
def lista(num):
    lista1 = []
    if num == 0:
        print(f"La lista está vacía {lista1}")
    else:
        for i in range(1, num + 1):
            palabras = input(f"Introduce la palabra {i}: ")
            lista1.append(palabras)   # Ó también se puede lista += [palabras]
        return lista1
def imp_listas(num2):
    for i in range(1, num2 + 1):
        num = int(input(f"¿Cuántas palabras quieres incluir en la lista ? "))
        res_lista = lista(num)
        return res_lista
num2 = int(input("¿Cuántas listas quiere escribir? "))

listas = []
for j in range(1, num2 + 1):
    listas += [imp_listas(j)]
for j in range(num2):
    print(f"La lista número {j + 1} es: {listas[j]}")

"""
# OTRA FORMA MEJOR
"""
def lista(contador):
    num = int(input(f"¿Cuántas palabras quieres incluir en la lista {contador} ? "))
    lista1 = []
    if num == 0:
        print(f"La lista está vacía {lista1}")
    else:
        for i in range(1, num + 1):
            palabras = input(f"Introduce la palabra {i}: ")
            lista1.append(palabras)   # Ó también se puede lista += [palabras]
        return lista1


num2 = int(input("¿Cuántas listas quiere escribir? "))

listas = []
for j in range(1, num2 + 1):
    listas += [lista(j)]
for j in range(num2):
    print(f"La lista número {j + 1} es: {listas[j]}")
"""
# EUP que permita crear dos listas de palabras y que, a continuación,
# elimine de la primera lista los nombres de la segunda lista.

"""def lista_original():
    num = int(input("Cuántas palabras tiene la lista? "))
    lista = []
    if num <= 0:
        print(f"La lista es vacia:", str(lista) + ".")
    else:
        for i in range(1, num + 1):
            print("Escribe la palabra", str(i) + ": ", end="")
            palabras = input()
            lista.append(palabras)
        print("La lista es:", str(lista) +".")
        return lista


def lista_a_eliminar():
    num2 = int(input("Cuántas palabras tiene la lista de palabras a eliminar? "))
    lista2 = []
    if num2 <= 0:
        print("La lista es vacía", str(lista2) + ".")
    else:
        for i in range(1, num2 + 1):
            print("Escribe la palabra", str(i) + ": ", end="")
            palabra = input()
            lista2.append(palabra)
        print("La lista de palabras a eliminar es:", str(lista2) + ".")
        return lista2


imp_lista_original = lista_original()
imp_lista_a_eliminar = lista_a_eliminar()
for i in imp_lista_a_eliminar:
    for j in range(len(imp_lista_original)-1, -1, -1):
        if imp_lista_original[j] == i:
            del(imp_lista_original[j])
print("La lista es ahora", imp_lista_original)
"""

# Modifique el programa anterior de manera que se escriban varias listas
# y el programa elimine de las listas anteriores las palabras que aparecen en las siguientes:

def lista_original(j):
    num = int(input("Cuántas palabras tiene la lista? "))
    lista = []
    if num <= 0:
        print(f"La lista es vacia:", str(lista) + ".")
    else:
        for i in range(1, num + 1):
            print("Escribe la palabra", str(i) + ": ", end="")
            palabras = input()
            lista.append(palabras)
        return lista


def lista_a_eliminar(listas):
    lista2 = []
    lista2.append(listas)

    return lista2


def eliminacion(imp_lista_a_eliminar):
    for i in imp_lista_a_eliminar:
        for j in range(len(imp_lista_original) - 1, -1, -1):
            if imp_lista_original[j] == i:
                del (imp_lista_original[j])
    return imp_lista_original

num2 = int(input("¿Cuántas listas quiere escribir? "))

listas = []
borradas = []
for j in range(1, num2 + 1):
    listas += [lista_original(j)]
    borradas += [lista_original(j + 1)]
imp_lista_original = listas
imp_lista_a_eliminar = borradas
imp = eliminacion(imp_lista_a_eliminar)

for j in range(num2):
    print(f"La lista número {j + 1} es: {listas[j]}")
print(imp)
