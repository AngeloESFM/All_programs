# 44 LISTAS ANIDADAS

grilla_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# Para mostrar todas las listas
for num in grilla_numeros:
    print(num)

# Para mostrar los números uno por uno
for filas in grilla_numeros:
    for columnas in filas:
        print(columnas)
