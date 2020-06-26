# EJERCICIOS CICLO FOR

# EUP que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.
"""
num1 = int(input("Escribe un número: "))
num2 = int(input(f"Escribe un número mayor o igual a {num1}: "))
while num2 < num1:
    num2 = int(input(f"Escribe por favor un número mayor o igual a {num1}: "))

for i in range(num1, num2 + 1):
    if i%2 == 0:
        print(f"El número {i} es par")
    else:
        print(f"El número {i} es impar")
"""
"""
for indice in range(5):
    for indice2 in range(3):
        print(indice, indice2)
"""
# EUP que pida un número entero mayor que cero y que escriba sus divisores.
# Mi manera
"""
num1 = int(input("Escribe un número mayor que 0: "))
while num1 <= 0:
    num1 = int(input("Escribe un número mayor que 0 por favor: "))
divisores = []
contador = 0
for i in range(1, (num1//2) + 1):
    if num1%i == 0:
        divisores.append(i)
        contador += 1


print(f"Los divisores de {num1} son: {divisores}")
print(f"En total son: {contador}")"""
"""
# Otra manera
num1 = int(input("Escribe un número mayor que 0: "))
while num1 <= 0:
    num1 = int(input("Escribe un número mayor que 0 por favor: "))
print(f"Los divisores de {num1} son: ", end="")
for i in range(1, num1 + 1):
    if num1 % i == 0:
        print(i, end=" ")"""

# EUP que pregunte cuántos números se van a introducir,
# pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el primero.

"""num = int(input("Introduce cuántos valores escribirás: "))
if num <= 0:
    print("¡Imposible!")
else:
    wrande = int(input("Escribe un número: "))
    for i in range(num - 1):
        valores = int(input(f"Escribe un número mayor a {wrande}: "))
        if valores <= wrande:
            print(f"{valores} no es mayor que {wrande}")

print("Gracias por su colaboración")

# EUP  que pregunte cuántos números se van a introducir, pida esos números,
# y muestre un mensaje cada vez que un número no sea mayor que el anterior.

num = int(input("Introduce cuántos valores escribirás: "))
if num <= 0:
    print("¡Imposible!")
else:
    wrande = int(input("Escribe un número: "))
    for i in range(num - 1):
        valores = int(input(f"Escribe un número mayor a {wrande}: "))
        if valores <= wrande:
            print(f"{valores} no es mayor que {wrande}")
        wrande = valores

    print("Gracias por su colaboración")
"""
"""
# EUP que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

num = int(input("Cuántos números vas a introducir? "))

if num < 0:
    print("Imposible!")
elif num == 0:
    print("No ha escrito ningún número negativo")
else:
    contador = 0
    for i in range(num):
        valor = int(input("Introduza un número"))
        if valor < 0:
            contador += 1

    if contador == 1:
        print(f"Ha escrito 1 número negativo")
    else:
        print(f"Ha escrito {contador} números negativos")
"""
# EUP que pregunte cuántos números se van a introducir, pida esos números,
# y diga al final cuántos han sido pares y cuántos impares.
"""
num = int(input("¿Cuántos números escribirá? "))

if num < 0:
    print("Imposible!")
elif num == 0:
    print(" Ha escrito 0 pares y 0 impares")
else:
    pares = 0
    impares = 0
    for i in range(num):
        valores = int(input("Escribe un número: "))
        if valores%2 == 0:
            pares += 1
        else:
            impares += 1
    if pares == 1 and impares == 1:
        print(f"Ha escrito 1 par y 1 impar")
    elif pares == 1:
        print(f"Ha escrito 1 par y {impares} impares")
    elif impares == 1:
        print(f"Ha escrito {pares} pares y 1 impar")
    else:
        print(f"Ha escrito {pares} pares y {impares} impares")
"""

# EUP  que pida un número entero mayor que 1 y que escriba si el número es un número primo o no
"""
from math import sqrt
num = int(input("Escriba un número mayor a 1: "))
# ROUND sirve para redondear al número más próximo (numero, cuantos_decimales_a_tomar)
redondeo = round(sqrt(num))
if num <= 1:
    print("Escriba un número mayor a 1")
else:
    divisores = []
    for i in range(1, redondeo + 1):
        if  num%i == 0:
            divisores.append(i)
    print(divisores)
    if divisores == [1]:
        print(f"{num} es primo.")
    else:
        print(f"{num} no es primo.")
"""
# EUP que pregunte cuantos números se van a introducir, pida esos números (que puedan ser decimales) y calcule su suma.
"""
num = int(input("¿Cuántos números va a introducir? "))

if num < 0:
    print("Imposible!")
elif num == 0:
    print("No introdujo números, la suma es 0")
else:
    suma = 0
    for i in range(num):
        valores = float(input("Introduzca un número: "))
        suma += valores

    print("La suma es: ", suma)
"""

# EUP que pida dos números enteros y escriba la suma de todos los enteros desde el primer número hasta el segundo.
"""
num1 = int(input("Escriba un número entero positivo: "))
if num1 < 0:
    print("imposible!")
else:
    num2 = int(input(f"Escribe un número mayor que {num1}: "))
    if num2 <= num1:
        print(f"He pedido un entero mayor a {num1}")
    else:
        suma = 0
        sumandos = []
        for i in range(num1, num2 + 1):
            suma += i
            sumandos.append(i)
        print(f"La suma desde {num1} hasta {num2} es {suma}")
# Un detalle importante es que el bucle no debe llegar al último número
# (para que no escriba un + después del último número)
        for i in range(num1, num2):
            print(f"{i} + ", end="")
        print(f"{num2} = {suma}"
              " otra linea"
              )
        
"""
# EUP que pregunte cuántos números se van a introducir, pida esos números,
# y escriba el mayor, el menor y la media aritmética.
"""
numeros = int(input("Cuántos valores va a introducir? "))
if numeros <= 0:
    print("imposible!!")
else:
    valores = float(input("Escribe un número 1: "))
    mayor = menor = suma = valores
    for i in range(2, numeros + 1):
        valores = float(input(f"Escribe un número {i}: "))
        if valores > mayor:
            mayor = valores
        if valores < menor:
            menor = valores

        suma += valores
    media = suma/numeros

    print(f"El número más pequeño que se introdujo fué: {menor}:")
    print(f"El número más grande que se introdujo fué: {mayor}:")
    print(f"La media de los números introducidos es: {suma/numeros}")
"""
# EUP que pida un número entero mayor que cero y calcule su factorial.
"""
num = int(input("Ingrese un número para saber su factorial: "))
if num < 0:
    print("IMPOSIBLE!!!")
elif num == 0:
    print("El factorial de 0, (0!) es:  1")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i

    print(f"El factorial de {num}, ({num}!) es: {factorial}")

"""



