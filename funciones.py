# 29 FUNCIONES
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
