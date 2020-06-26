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

