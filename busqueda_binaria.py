# 56 BUSQUEDAS BINARIAS
# SIRVE PARA ENCONTRAR NÚMEROS EN LAS LISTAS

# Mi forma de hacer la busqueda del 40
"""lista = [2, 4, 8, 14, 16, 25, 31, 40, 53, 86, 40, 70, 40]
for i in lista:
    if i == 40:
        print(lista.index(40))      # con .INDEX encuentras el número de índice de un array o lista

# De la siguiente forma se hace, para ver cuántas veces está un dato en la lista
m = [i for i, x in enumerate(lista) if x == 40]
print(m)
"""
# 1ro. Buscar el punto medio (puntero)
# 2do. Comprobar si el punto medio es el valor que buscamos
# 3ro. Si el número es menor al que buscamos, aumentamos el inicio + 1 sobre el puntero
# 4to. Si el número es mayor al que buscamos, disminuimos el final - 1 debajo del puntero
# 5to. Si inicio mayor o igual que final, entonces el número no se encuentra en la lista

lista = [0, 88, 72, 21, 14, 16, 90, 35, 47, 6, 68, 12, 10, 54, 41]
# con .SORT() ordenamos las listas de menor a mayor
lista.sort()
print(lista)

def busqueda_binaria(valor):
    inicio = 0
    final = len(lista) - 1
    while inicio <= final:
        puntero = (inicio + final) // 2
        print(puntero)
        print(lista[puntero])
        if valor == lista[puntero]:
            return puntero
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            final = puntero - 1
    return None

def buscar_valor(valor):
    res_busqueda = busqueda_binaria(valor)
    if res_busqueda is None:
        return f"El número {valor} no está en la lista"
    else:
        return f"El número {valor} está en el lugar {res_busqueda} "

while True:
    busq = (buscar_valor(int(input("Introduce un número: "))))
    print(busq)

    print("Deseas hacer otra comprobación?")
    print("Presiona 1 para seguir, presiona 2 para terminar")
    opcion = input(">")
    if opcion == "1":
        continue
    elif opcion == "2":
        print("Bye")
        break
# LO MISMO SIN FUNCIONES
lista = [0, 88, 72, 21, 14, 16, 90, 35, 47, 6, 68, 12, 10, 54, 41]
# con .SORT() ordenamos las listas de menor a mayor
lista.sort()
print(lista)
valor = int(input("Ingresa un valor"))
inicio = 0
final = len(lista)
print(final)
while inicio <= final:
    puntero = (inicio + final) // 2
    print(puntero)
    print(lista[puntero])
    if valor == lista[puntero]:
        print("El número está en " + str(puntero))
        break
    elif valor > lista[puntero]:
        inicio = puntero + 1
    else:
        final = puntero - 1
print("El número no está en la lista")