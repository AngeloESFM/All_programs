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


