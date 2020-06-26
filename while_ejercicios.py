# EJERCICIOS PARA PRACTICAR WHILE

# ESCRIBIR UN PROGRAMA QUE PIDA DOS NÚMEROS, EL PRIMERO MENOR QUE EL OTRO E IMPRIMIR LOS DOS
"""
num1 = float(input("Ingrese un número: "))
num2 = float(input("ingrese otro número, mayor al primero: "))

while num2 <= num1:
    num2 = float(input("Escribe un número mayor al primero, ¬¬ "))

print(f"Los números son {num1} y {num2}")
"""
# EUP(ESCRIBIR UN PROGRAMA) QUE PIDA DOS NÚMEROS, MIENTRAS EL SEGUNDO SEA MAYOR IMPRIMA LOS NÚMEROS
"""
num3 = float(input("Ingrese un número: "))
num4 = float(input("ingrese otro número, mayor al primero: "))

while num4 > num3:
    num4 = float(input(f"{num4} es mayor a {num3}, elige otro mayor: "))

print(f"{num4} no es mayor a {num3}")
"""

# EUP QUE PIDA UN NÚMERO MÁS GRANDE QUE EL ANTERIOR Y SE IMPRIMAN HASTA QUE PONGAN UNO MENOR
"""
num5 = float(input("Ingrese un número: "))
num6 = float(input("ingrese otro número, mayor al primero: "))

while num6 > num5:
    num5 = num6
    num6 = float(input(f"Elige otro más grande que {num6}: "))

print(f"{num6} no es mayor a {num5}")
"""
# EUP QUE PIDA NÚMEROS POSITIVOS A ESCRIBIR SI NO ES POSITIVO SIGA PIDIENDO NÚMEROS HASTA QUE \n
# ESCRIBA LOS NÚMEROS POSITIVOS INDICADOS
"""
print("NÚMEROS POSITIVOS")
objetivo = int(input("Escriba la cantidad de números positivos a escribir: "))
while objetivo < 1:
    objetivo = int(input("La cantidad debe ser mayor que 0. Inténtelo de nuevo: "))

print()
numero = int(input("Escriba un número: "))
total = 1
if numero > 0:
     cantidad = 1
else:
     cantidad = 0

while cantidad < objetivo:
    numero = int(input("Escriba otro número: "))
    if numero > 0:
        cantidad += 1
    total += 1

print()
if total == 1:
    print("Ha escrito 1 número positivo.")
elif objetivo == 1:
    print(f"Ha escrito {total} números, {objetivo} de ellos positivo.")
else:
    print(f"Ha escrito {total} números, {objetivo} de ellos positivos.")
"""
# EUP QUE PIDA NÚMEROS HASTA QUE SE INGRESE UN NEGATIVO. SE TERMINA HACIENDO LA SUMA DE LOS POSITIVOS
"""
num1 = float(input("Escribe un número: "))
suma = num1
while num1 >= 0:
    num1 = float(input("Escriba otro número: "))
    if num1 >= 0:
        suma += num1
    else:
        break
print()
print(f"La suma de números positivos es {suma}")
"""
"""
TAMBIEN SE PUEDE DE LA SIGUIENTE FORMA, AHORRANDO LINEAS DE CÓDIGO
print("SUMA DE NÚMEROS")
numero = int(input("Escriba un número: "))
suma = 0
while numero >= 0:
    suma += numero
    numero = int(input("Escriba otro número: "))
print()
print(f"La suma de los números positivos introducidos es {suma}.")

"""

# EUP QUE PIDA UN VALOR LIMITE Y PIDA NÚMEROS DE MODO QUE
# CUANDO LA SUMA DE ESTOS LLEGUEN A ESE LÍMITE, LOS MUESTRE Y SE TERMINE EL PROGRAMA
"""
limite = float(input("Introduce un límite: "))
suma = 0
while limite <= 0:
    limite = float(input("El límite debe ser mayor a 0, intente de nuevo: "))
num = float(input("Escribe un número: "))
suma += num
while suma < limite:
    num = float(input("Escribe otro número: "))
    suma += num
print(f"Has superado o alcanzado el límite. La suma de los números es: {suma}")
"""

# EUP que pida primero dos números enteros (mínimo y máximo) y que después pida números enteros situados entre ellos.
# El programa terminará cuando se escriba un número que no esté comprendido entre los dos valores iniciales.
# El programa termina escribiendo la cantidad de números escritos.
"""
print("Escribe un rango de números")
min = float(input("Escribe un número mínimo: "))
max = float(input("Escribe un número máximo: "))
contador = 0
while max <= min:
    max = float(input(f"Escribe un número que sea mayor que {min}: "))

num = float(input(f"Introduzca un número que esté entre {min} y {max}: "))
while  min <= num and num <= max:
    contador += 1
    num = float(input(f"Introduzca un número que esté entre {min} y {max}: "))

print(f"{num} no está entre {min} y {max}")
if contador == 1:
    print(f"Has escrito 1 número entre {min} y {max}")
elif contador == 0:
    print(f"No has escrito ningún número entre {min} y {max}")
else:
    print(f"Has escrito {contador} números entre {min} y {max}")

"""
# EUP que calcule la descomposición en factores primos de un número.

"""
num = int(input("Escriba un número mayor a 1: "))
while num <= 1:
    num = int(input(f"{num} no es mayor a 1,  Escriba otro número : "))

copia = num
print("Descomposición en números primos", end= " ")
i = 2
while copia > i * i:
    while copia % 1 == 0:
        copia = copia // i
        print(f"{i}", end= " ")
    i += 1
        
if copia != 1:
    print(f"{copia}")
print()
"""

def main():
    print("DESCOMPOSICIÓN EN NÚMEROS PRIMOS")
    numero = int(input("Escriba un número entero mayor que 1: "))
    while numero <= 1:
        numero = int(input(f"{numero} no es mayor que 1. Inténtelo de nuevo: "))
    copia = numero

    print("Descomposición en factores primos:", end="")
    i = 2
    while copia > i * i:
        while copia % i == 0:
            copia = copia // i
            print(f" {i}", end="")
        i += 1
    if copia != 1:
        print(f" {copia}")


if __name__ == "__main__":
    main()









