#\n da enters entre líneas
print("¡Hola mundo!\nCreaste tú primer linea de código")

#palabras reservadas que no se pueden utilizar en variables
#help("keywords")
# 9 DECLARAR VARIABLES,
numero= 10;
print(numero)
# ASIGNAR VALORES
numero1, numero2, numero3= 1, 2, 3
print(numero1)
print(numero2)
print(numero3)
#ver el espacio de memoria ocupado por variables
#  id(numero)
#ver las variables
#  dir()
#borrar variable o desocupar espacio en la memoria
#  del(variable)
# Existen dos tipos de datos "NÚMERICOS Y CADENAS" aunque también existen los booleanos (TRUE, FALSE)

# 10 NÚMERICOS
#Enteros (int)
entero = 10
print(entero)

#Flotante (float)
flotante= 10.05
print(flotante)

#Complejo (complex)
Complejo= (10.05+0j)

#para saber que tipo de dato es
# type(variable)= int, float, complex

#para convertir un tipo de dato en otro
#al tipo que se convertira (la variable a convertir)
# flotante = 10.05 ahora
#int(flotante) será igual a 10

# 11 BOOLEANOS (bool)
#verdadero (True) y falso (False)
verdadero= True
falso= False
# bool(0) da false
#bool(algo diferente a 0) da True

# 12 CADENA DE TEXTO (str)
cadena= "Hola mundo"
cadena2= 'Hola mundo'
cadena3= "Esto es una cadena\nestoy en otra 'linea'"
cadena4= "Esto es una cadena\nestoy en otra \"linea\""


print(cadena)
print(cadena2)
print(cadena3)
print(cadena4)

# 13 OPERADORES MATEMATICOS
"""
+ SUMA
- RESTA
* MULTIPLICACIÓN
** EXPONENTE
/ DIVISIÓN
// DIVISIÓN QUE DEVUELVE SOLO ENTEROS
% MODULO O RESIDUO
"""

#REGLAS DE PRECEDENCIA
"""
1. Paréntesis
2. Exponentes
3. MUltiplicación
4. División
5. Suma
6.-Resta
"""

resultado = 12 * 5 + 2 / 3 ** 2
#print (resultado)
resultado1 = (12 * 5) + (2 / (3 ** 2))
#print (resultado1)
resultado2 = (12 * 5) + (2 / 3) ** 2
#print (resultado2)

# 14 OPERADORES DE CADENAS

cadena1 = "Hola "
cadena2 = "mundo"
cadenas_unidas= cadena1 + cadena2
#print(cadenas_unidas)

cadenas_repetidas = cadena1 * 3
#print(cadenas_repetidas)

# 15 OPERADORES DE RELACIÓN
#Cumplen con una evaluación de 2 valores que cumplan con una condición, y el resultado es booleano
"""
== Igual a
!= Distinto a 
> Mayor que
< Menor que
>= Mayor o igual
<= Menor o igual
"""
numero10 = 10
numero_diez = "10"
#int(variable) la convierte en int, float, str
mayor_igual = numero10 >= int(numero_diez)
print(mayor_igual)
# 16 OPERADORES DE ASIGNACIÓN= Para asignar valores a una variable
"""
= Asignación simple x = y
+= Asignación suma x += y equivale a x = x + y
-= Asignación resta x -= y equivale a x = x - y
*= Asignación multiplicación x *= y equivale a x = x * y
**= Asignación exponente x **= y equivale a x = x ** y
/= Asignación división x /= y equivale a x = x / y
//= Asignación división entera x //= y equivale a x = x // y
%= Asignación modulo x %= y equivale a x = x % y
"""
numero1 = 1
numero2 = 2
#Podemos asignar valores en una misma linea
numero3, numero4, numero5 = 3, 4, 5

#ASIGNACIÓN SUMA
numero1 = numero1 + numero2
print(numero1)
numero1 = 1
numero1 += numero2
print(numero1)

#ASIGNACIÓN RESTA
numero1 = 1
numero1 = numero1 - numero2
print(numero1)
numero1 = 1
numero1 -= numero2
print(numero1)
# EScribir las asignaciones restantes

#¿Cómo funciona esta línea de código?
# a, b = b, a + b
a = 1
b = 2
a, b = b, a + b
print (a,b, '"código en una línea"')
# diferente resultado cuando se escribe en lineas separadas, ya que da los valores de lineas anteriores

a = 1
b = 2
print(a, "valor de a")
a = b
print(a, "valor de a despues de asignarle b")
b = a + b
print(a, b, '"código en dos líneas"')

#OPERADORES LÓGICOS Y DE PERTENENCIA

# 17 OPERADORES LÓGICOS
# Nos permiten comprobar si se cumplen comparaciones lógicas
"""
or -> a or b -> ¿ Se cumple a o b? sólo es falso si ninguna se cumple
and -> a & b -> ¿ Se cumplen a y b? sólo es verdadero si todas se cumplen
not -> not x -> contrario de x
"""
verdadero = True
falso = False
print("comparador OR:")
print(verdadero or falso, "\n")
print("comparador AND:")
print(verdadero and falso)

# 17 OPERADORES DE PERTENENCIA
# Los operadores de pertenencia evaluan si un objeto se encuentra dentro de otro
"""
in -> se encuentra en
not in -> no se encuentra en
"""
cadena = "Angelo"
print('An' in cadena)
print('Z' not in cadena)

# 18 FUNCIONES IDENTIDAD
# Los operadores comprueban si un objeto es igual a otro
# is & is not
a = 10
b = 10
print(a is float)
print(a is not int)

# la diferencia entre mutable en inmutable es que los vectores son mutables osea que no cambian su lugar en memoria
# inmutable es que se modifica su lugar en memoria, osea que se borra y se reescribe de nuevo

# 19 TRABAJAMOS CON CADENAS DE TEXTO

# Las cadenas pueden ser tratadas como listas
cadena = "Hola AcademiaCoder"

# H o l a   A c a d e  m  i  a  C  o  d  e  r
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
#                               ... -3  -2  -1

# Se escoge la posición que queremos mostrar entre corchetes
# nombre_de_la_cadena [número de la posición a mostar]
letra = cadena[5]
print(letra)
# Para ir de adelante hacía atrás se empieza en -1 y se ponen números negativos
letra = cadena[-18]
print(letra)

# Para darle un intervalo de posiciones es
# nombre de la cadena[número de la posición inicial:número de la posición final obtendra una posición anterior]
letras = cadena[2:13]
print(letras)
# Si no se le indica el rango, regresa todos los datos siguientes o anteriores
letras = cadena[5:]
print(letras)
letras = cadena[:13]
print(letras)

#no pueden ser modificadas como las listas, osea no son mutables

# 20 FUNCIONES DE LAS CADENAS DE TEXTO
# Todas las funciones están en https://docs.python.org/3/library/stdtypes.html#string-methods
# nombre de la cadena.nombre de la función a utilizar. otra función ----> puede concatenar las funciones
modificada = cadena.capitalize()
print(modificada)
modificada = cadena.upper().isupper()
print(modificada)
modificada = cadena.split()
print(modificada)
cadena_comas = "Marcos,Natalia,Rosa"
lista_nombres = cadena_comas.split(',')
print(lista_nombres)

# 21 UNIR VARIABLES A CADENAS
# Sirve para concatenar variables y cadenas, transformar los números en letras

alumnos = 3600
academia = "Academia Angelo"
cadena = "Los " + str(alumnos) + " alumnos de la " + academia + " son muy listos"
print (cadena)

# El más práctico es poner f al principio de la cadena para que detecte los formatos de las variables entre corchetes
cadena = f"Los {alumnos} alumnos de la {academia} son muy listos"
print (cadena)

# .FORMAT = tambien convierte automaticamente tod o en cadena, tomando las variables que sean sustituyendolas por {}
# .FORMAT(variable1, variable2, ... )
cadena = "Los {} alumnos de la {} son muy listos".format(alumnos,academia)
print (cadena)

# Tambien puedes renombrar los corchetes, para que no importe el orden de los parámetros
cadena = "Los {a} alumnos de la {b} son muy listos".format(b=academia, a=alumnos)
print (cadena)

# 22 INGRESAR O PEDIR TEXTO AL USUARIO
# INPUT() = Sirve para introducir texto al programa

# Puede ser de la manera
print ("Ingresa tu nombre: ")
nombre = input()
print (f"El nombre del alumno es {nombre}")

# O también puede ser de esta forma MÁS ELEGANTE
nombre = input("Ingresa tu nombre: ")
print (f"El nombre del alumno es {nombre}")

# 23 COMENTARIOS EN PYTHON
# Para comentar una linea utilizamos el signo # y en las lineas permite 80 caractéres segun la reglas PEP8
# Los comentarios sirven para tener más ordenado nuestro código
# y tener una ayuda que explique que función realiza cada código
# EJEMPLO

# Declaramos nuestras variables
numero1 = 10
numero2 = 5
numero1, numero2 = 10, 5  # Ahorramos una línea de código haciendo una declaración multiple
# Sumamos ambas variables
suma = numero1 + numero2
# Imprimimos el resultado en pantalla
print(suma)

# Tambien se puede usar triple comilla para comentar, EJEMPLO
# LOS 12 MANDAMIENTOS DE PYTHON
"""
1. Los nombres de los módulos deben estar en minúsculas - hola.py
2. Los nombres de las clases deben usar CamelCase
3. Los métodos y funciones deben usar minúsculas_con_guión_bajo
4. Los métodos privados para uso interno, empiezan con _guión_bajo
5. Los atribútos de clase con __doble_guión_bajo
6. Las constantes en el primer nivel del código ( las que no se encuentran dentro de una función o una clase)
   deben usar LETRASMAYUSCULAS. Usar demasiadas constantes puede hacer que tú código sea menos reutilizable.
7. Si una variable en una función o método es tan temporal que no puedes darle un nombre, utiliza i para la 
   primera, j para la segunda, y k para la tercera.
8. Identa por 4 espacios por nivel. Sin tabuladores.
9. Las lineas no deberían tener nunca más de 80 caractéres. Divide las líneas usando una barra invertida.
   No necesitas hacerlo, si hay parentésis, llaves o corchetes.
10. Espacio despues de una coma ( huevos, con, jamón)
11. Espacio antes y despues de un operador i = i + 1
12. Escribe cadenas de documentación para todos los módulos, funciones, clases, y métodos públicos.
    Pyhton es una comunidad internacional, así que utiliza el inglés para cadenas de documentación
    los nombres de los objetos y los comentarios.
 """

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

# 25 JUEGO HISTORIA LOCA

# Declaramos las variables
# Utilizando input para que el usuario rellene los campos
print ("Crea tu historia loca")
print ("Ingresa las palabras que te solicitamos\n")
pal1 = input("Parte del cuerpo en plural: ")
pal2 = input("adjetivo en plural: ")
pal3 = input("adjetivo: ")
pal4 = input("adjetivo: ")
pal5 = input("Ingrese un nombre")
print(f"Antiguamente el hombre caminaba a cuatro {pal1.lower()},")  #hace toda la palabra en minúscula
print(f"se expresaba mediante gruñidos {pal2} y no sabia encender")
print(f"un {pal3} fuego. Esa es la historia del día en que la humanidad")
print(f"cambió para siempre( traducida del {pal4} idioma de las cavernas):")
# Completar la historia ...
# Como extra
print(f"Su nombre era {pal5.capitalize()}") #Sirve para hacer la primer letra mayúscula para nombres propios

# 26 Listas
# Sirven para tener elementos guardadados entre corchetes como vectores
# Colección de elementos, las listas están ordenadas y son mutables

frutas = ["Naranja", "Manzana", "Banana", "Kiwi", "Mandarina", "Uva"]
#              0            1         2       3            4       5

# Imprime toda la lista
print (frutas)
print (frutas[5])
# Imprime de atras hacía adelante
print (frutas[-6])
# usando los dos puntos ":" es para indicar un intervalo de las lista, cuantos elementos se muestran
print (frutas[1:4])
print (frutas[:3])
print (frutas[1:])


# 27 FUNCIONES DE LAS LISTAS O VECTORES
# Se verá que cosas se puede hacer con las listas o vectores

numeros = [5, 2, 23, 55, 1, 9, 6]
frutas = ["Naranja", "Manzana", "Banana", "Kiwi", "Mandarina", "Uva", "Naranja"]

print ("LISTA ORIGINAL DE FRUTAS")
print (frutas)
print ()

# FUNCIONES DE LAS LISTAS
# LEN, APPEND, EXTEND, INSERT, REMOVE, CLEAR, POP, INDEX, COUNT, SORT, REVERSE, COPY
# Para cambiar un elemento de la lista por otro, se hace lo siguiente, cambiar piña por manzana
frutas[1] = "Piña"
print (frutas)
# LEN = Sirve para ver el tamaño de la lista
print (len(frutas))
# APPEND = Sirve para agregar un elemento al final de la lista
frutas.append("Manzana")
print(frutas)
# EXTEND = Sirve para agregarle a una lista, otra lista, pero sin modificarla
# Sin modificarla
numeros.extend(frutas)
print(numeros)
# Modificándola
numeros = numeros + frutas
print(numeros)
# INSERT = Sirve para agregar un elemento a la lista en la posición que se quiera, y las otras se recorren
# lista.INSERT(lugar_donde_se_colocará, elemento_que_se_colocará)
frutas.insert(2, "Sandía")
print (frutas)
# REMOVE = Sirve para eliminar un elemento de la lista
frutas.remove("Kiwi")
print (frutas)
# CLEAR = Sirve para eliminar todos los elementos de la lista
#frutas.clear()
#print (frutas)
# POP = Sirve para eliminar el último elemento de la lista y se pueden hacer varios, elimina el último siempre
frutas.pop()
frutas.pop()
print(frutas)
# INDEX = Sirve para saber en que índice (o posición) esta el elemento dicho
print(frutas.index("Naranja"))
# COUNT = Sirve para contar cuantos elementos hay en la lista
print(frutas.count("Naranja"))
# SORT = Sirve para ordenar los datos de mayor a menor
#(para que de aqui en adelante funcione el programa, hay que comentar las anteriores)
frutas.sort()
print(frutas)
numeros.sort()
print(numeros)
# REVERSE = Sirve para voltear los indices ( o las posiciones) en las listas
frutas.reverse()
print(frutas)
# COPY = Sirve para dar una copia exacta de una lista y almacenarla en otra variable dandole otro lugar en la memoria la hace mutable
# si modificamos frutas2 no se modifica la original y viceversa
frutas2 = frutas.copy()
print (frutas2)

