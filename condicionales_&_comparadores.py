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

def numero_mayor(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
print("Escribe tres numeros: ")
"""
num1, num2, num3 = input(), input(), input()
numero = numero_mayor(int(num1), int(num2), int(num3))

num1 = int(input())
num2 = int(input())
num3 = int(input())
numero = numero_mayor(num1, num2, num3)
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