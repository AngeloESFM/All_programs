import math
num1 = input("inserte número para sacarle raiz cuadrada:")
num1 = float(num1)
print(math.sqrt(num1))

def raiz_c(n):
    num1 = 0
    while num1 * num1 <= n:
        num1 += 0.00001
    return num1
print(raiz_c(num1))
