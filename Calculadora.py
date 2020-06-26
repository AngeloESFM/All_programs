# 24 CALCULADORA BÁSICA
# Solicitar al usuario número y realizar la operación

# Declaramos las variables
# utilizamos input, para guardar lo que el usuario escriba
num1 = input("ingresa un número:")
num2 = input("ingresa otro número:")
if num1 and num2 is float or int:
# Hacemos la suma y guardamos el resultado
    print (type(num1))   # Sirve para saber el tipo de la variable
    suma = float(num1) + float(num2)
# Imprimimos el resultado de la suma
    print("La suma es: ",suma)
# Hacemos la resta y guardamos el resultado
    resta = float(num1) - float(num2)
# Imprimimos el resultado de la resta
    print("La resta es: ",resta)
# Hacemos la multiplicación y guardamos el resultado
    producto = float(num1) * float(num2)
# Imprimimos el resultado
    print("El producto es: ",producto)
# Hacemos la división y guardamos el resultado
    div = float(num1) / float(num2)
# Imprimimos el resultado
    print("La división es: ",div)

# Hacemos la potencia y guardamos el resultado
    potencia = float(num1)**float(num2)
# Imprimimos el resultado
    print("La potencia es: ", potencia)

else:
    print("no ingreso un número, intente de nuevo")
