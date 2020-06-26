# 19, 20 GENERADORES I y II
# Se obtiene con la instrucción YIELD y se recorre con un búcle
# SIrve para obtener una lista de uno por uno los datos, es más eficiente que un método normal
# Su útildad más exacta es cuando se tenga que generar una lista infiníta

# Comando YIELD FROM
# Sirve para obtener información de las listas y sublistas de búcles anidados



# Para obtener una lista de números pares podemos hacerlo :
"""
def numerosPares(limite):

    num = 1
    
    listanum = []

    while num<=limite:
        par = num*2
        listanum.append(par)
        num += 1

    return listanum

limite = int(input("Escribe cuantos pares quieres: "))
print(numerosPares(limite))
"""
# como se hace con un GENERADOR
"""
def generaNumeros(limite):  
    
    num = 1

    while num <= limite:
        yield num*2
        num += 1


#--Objeto GENERADOR
devuelveNumeros = generaNumeros(int(input("Cuantos números pares quieres: "))) 
"""
# Imprimimos toda la lista
"""
for i in devuelveNumeros:
    print(str(i), end=', ')
"""
# Otra forma de usarlo, es para obtener valores despues de hacer otra parte de código
# El comando NEXT, sirve para llamar el siguiente número que saldría del objeto generador
"""
print(next(devuelveNumeros))

print("Aqui podria ir muchas lineas de código")

print(next(devuelveNumeros))

print("Aquí otras mil lineas...")

print(next(devuelveNumeros))
"""
# Ahora usaremos el comando YIELD FROM
# Sirve para obtener información de las listas y sublistas de búcles anidados

# el * en un argumento, indica  qeu no se sabe cuantos elementos va a recibir ese argumento pueden ser muchos o pocos
# además los convierte en túpla
def ciudades(*nomciu):
    #De esta forma accedemos a los sub elementos "M" & "a"
    """for elemento in nomciu: 
        for subElemento in elemento:
            yield subElemento"""

    # de esta forma accedemos a los mismos sub elementos pero con el comando YIELD FROM
    for elemento in nomciu:
        yield from elemento


dev_ciu = ciudades("Madrid", "CDMX") 

print(next(dev_ciu))
print("y...")
print(next(dev_ciu))