# 31 RETURN
# Sirve para recibir datos de una función

def multiplicacion(num1, num2):
    multi = num1 * num2
    return multi                  # Despues de return en una función, se corta todo lo que está debajo

res_multi = multiplicacion(3, 7)
print(res_multi)