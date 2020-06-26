# 46 APRENDER A ABRIR Y CERRAR ARCHIVOS DE TEXTO

# Para abrir el archivo se hace de la siguiente forma
"""
# Para abrirlo sólo en lectura se pone una "r"
open("Alumnos.txt","r")
# Para abrirlo sólo en escritura se pone una "w"
open("Alumnos.txt","w")
# Para abrirlo sólo en escritura se pone una "a"
open("Alumnos.txt","a")
# Para abrirlo en escritura y lectura se pone una "r+"
open("Alumnos.txt","r+")
"""
# Para abrirlo sólo en lectura se pone una "r"
archivo_alumnos = open("estu.txt", "r")
# Para saber si es un archivo de lectura
print(archivo_alumnos)
# Para cerrar el archivo se hace de la siguiente forma, así debe ser la buena practica
archivo_alumnos.close()
# ^ Despues de cerrado el archivo ya no se puede hacer uso de él.


# 47 LEER ARCHIVOS DE TEXTO

# Para abrir el archivo se hace de la siguiente forma
"""
# Para abrirlo sólo en lectura se pone una "r"
open("Alumnos.txt","r")
# Para abrirlo sólo en escritura se pone una "w"
open("Alumnos.txt","w")
# Para abrirlo sólo en escritura se pone una "a"
open("Alumnos.txt","a")
# Para abrirlo en escritura y lectura se pone una "r+"
open("Alumnos.txt","r+")
"""
# Para abrirlo sólo en lectura se pone una "r"
archivo_alumnos = open("estu.txt", "r")
# Para saber si es un archivo que puedes leer se escribe .readable()
print(archivo_alumnos.readable())
# Para que se muestre el contenido del archivo se escribe .read()
#print(archivo_alumnos.read())
# Para imprimir la primer linea y asi sucesivamente se escribe .readline()
#print(archivo_alumnos.readline())
#print(archivo_alumnos.readline())
# Para acceder al archivo como si fuera una lista se usa .readlines() en plural
#print(archivo_alumnos.readlines())
# sólo puedes recorrer o leer el archivo una vez y desaparecen los datos no en el original
print(archivo_alumnos.readlines()[1])
# Para cerrar el archivo se hace de la siguiente forma, así debe ser la buena practica
archivo_alumnos.close()
# ^ Despues de cerrado el archivo ya no se puede hacer uso de él.


# 48 ESCRIBIR EN ARCHIVOS DE TEXTO

# Para crear y escribir en un archivo se pone una "w" de write
archivo_alumnos = open("estudiantes2.txt", "w")
# Para saber si es un archivo escribible
print(archivo_alumnos.writable())
# Para escribir en el archivo se hace de la siguiente forma
# Aunque cada modificación crea un archivo nuevo
print(archivo_alumnos.write("Es un texto nuevo que se crea cada vez\nY puedo dar saltos de linea"))
# Para agregar texto al que ya está en el archivo se usa la "a" de append
# Se agrega al final del texto original y hay que usar saltos de linea para evitar romper el programa
archivo_alumnos = open("estudiantes2.txt", "a")
print(archivo_alumnos.write("\nCaroline Masutti - ReactJS"))
# Cuando se usa r+ se puede leer y escribir pero sobre escribe en la primer parte del archivo
archivo_alumnos = open("estudiantes2.txt", "r+")
print(archivo_alumnos.write("Caroline Masutti2 - ReactJS"))
# Para cerrar el archivo se hace de la siguiente forma, así debe ser la buena practica
archivo_alumnos.close()
# ^ Despues de cerrado el archivo ya no se puede hacer uso de él.

# 49 ELIMINAR ARCHIVOS DE TEXTO

# Para abrir el archivo se hace de la siguiente forma

archivo_alumnos = open("estudiantes2.txt", "r")
print(archivo_alumnos)
archivo_alumnos.close()

# Para borrar un archivo se hace de la siguiente forma
# Primero importar una librería
import os
# Llamar la función de esa libreria con el archivo y lo borra
os.remove("estudiantes2.txt")

# 50 MODULOS
# Un módulo es un archivo que se puede importar dentro de otro en el cual
# podemos hacer uso de su contenido, como funciones y variables.

# Si estan en la misma carpeta los dos archivos sólo se pone el nombre, si no
# hay que especificar la ruta del archivo
import utilidades_extra
# de esta forma se manda a llamar una variable del módulo
print(utilidades_extra.metros_en_kilometros)
print(utilidades_extra.avengers[2])
# Para renombrar el modulo a uno más corto se usa AS seguido del nombre
#import utilidades_extra as ue
#print(ue.tirar_dado(6))

# Para no importar todo lo que viene en ese módulo y sólo lo que necesitamos
# Se hace de la siguiente forma
from utilidades_extra import tirar_dado
print(tirar_dado(6))
# y para renombrar la función o variable se hace también con AS
from utilidades_extra import tirar_dado as td
print(td(6))

# 51 MODULOS PROPIOS DE PYTHON
# 52 PIP
# 53 VIRTUALENV

# 54 CLASES Y OBJETOS

# Definimos una clase de la siguiente forma
# Si la clase tiene más de un nombre se usa CamelCase como a continuación
#class EstudiantesActivosAhora:

# Esta clase ya puede ser mandada a llamar en otro archivo como si fuera un módulo
class Estudiante:
    def __init__(self, nombre, edad, curso_inicial):         # <<< Aquí se ponen los atributos
        self.nombre = nombre
        self.edad = edad
        self.curso_inicial = curso_inicial
        self.esta_inscrito = True                          # puede ir un "si" o lo que se quiera
        self.cursos = [curso_inicial, "SQL"]

# el nombre que se le asigna al dato para acceder a él, es el que está después de .SELF
# Le asignamos los datos a un objeto para ser parte de la clase, no puede faltar ninguno
estudiante1 = Estudiante("Angelo", 24, "Python")

# De esta forma se accede a cada parte o dato, de la clase hecha
print(estudiante1.nombre)
print(estudiante1.edad)
print(estudiante1.cursos)
print(estudiante1.esta_inscrito)

# 55 MÉTODOS DE LAS CLASES

# Definimos una clase de la siguiente forma
# Si la clase tiene más de un nombre se usa CamelCase como a continuación
#class EstudiantesActivosAhora:

# Esta clase ya puede ser mandada a llamar en otro archivo como si fuera un módulo
class Estudiante:
    def __init__(self, nombre, edad, curso_inicial):         # <<< Aquí se ponen los atributos
        self.nombre = nombre
        self.edad = edad
        self.curso_inicial = curso_inicial
        self.esta_inscrito = True                          # puede ir un "si" o lo que se quiera
        self.cursos = [curso_inicial, "SQL"]
#
# Podemos definir más funciones y hacer uso de ellas
    def desactivar (self):
        self.esta_inscrito = False

    def anadir(self, agregar):

        self.cursos = self.cursos + [agregar]


estudiante1 = Estudiante("Angelo", 24, "Python")
print(estudiante1.esta_inscrito)
print(estudiante1.cursos)
# Hacemos uso de la función desactivar y al imprimir cambia de True a False
estudiante1.desactivar()
print(estudiante1.esta_inscrito)
estudiante1.anadir(agregar = input("añade un nuevo curso"))
print(estudiante1.cursos)

# TAREA CREAR DOS MÉTODOS
# 1 QUE PERMITA AÑADIR CURSOS AL ESTUDIANTE
# 2 OTRO QUE PERMITA ELIMINAR CURSOS DEL ESTUDIANTE

# 56, 57 BUSQUEDAS BINARIAS
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
        return f"El número {valor} está en el el lugar {res_busqueda} "

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

# 58, 59 JUEGO DE POKEMON
from utilidades_extra import tirar_dado

# Creamos la clase Pokemon
class Pokemon:
    def __init__(self, nombre, ataque):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = 100

    def personaje(self, numero_de_p):
        self.Pikachu = p1
        self.Bulbazur = p2
        self.Squirtle = p3


    def gano(self):
        print(f"{(self.nombre).upper()} GANÓ ESTA BATALLA!!!")

# Creamos nuestros pokemon
P1 = Pokemon("Pikachu", 59)
P2 = Pokemon("Bulbazur", 55)
p3 = Pokemon("Squirtle", 57)
p4 = Pokemon("Charmander", 60)
p5 = Pokemon("Meowth", 50)
p6 = Pokemon("Jigglypuff", 99)

# Inicializamos los valores y el turno

while True:
    P1.vida = 100
    P2.vida = 100

    turno = tirar_dado(2)
    print(f"{P1.nombre} se enfrenta a {P2.nombre}, veremos quien es más fuerte")
    print("HA INICIADO LA BATALLA!!!\n")
    # Inicia la batalla
    while P1.vida > 0 and P2.vida > 0:
        if turno == 1:
            P2.vida = P2.vida - P1.ataque
            turno = 2
            print(f"{P1.nombre} ataca, ahora {P2.nombre} tiene de vida {P2.vida}")
            print("\n----PRÓXIMA RONDA----")
        else:
            P1.vida -= P2.ataque
            turno = 1
            print(f"{P2.nombre} ataca, ahora {P1.nombre} tiene de vida {P1.vida}")
            print("\n----PRÓXIMA RONDA----")

        # consultamos que pokemon perdió
    if P1.vida <= 0:
        P2.gano()
    else:
        P1.gano()

    print("\nQuieres otra batalla? ")
    print("Presiona 1 para seguir con ellas, o presiona 2 para terminarlas")
    opc = input("> ")
    if opc == "1":
        print("¡¡¡CONTINUAN LAS BATALLAS!!!")
    if opc == "2":
        print("OK, Nos vemos pronto para la siguiente batalla.")
        break

# 60 EXPRESIONES REGULARES
# USAMOS EL MÓDULO DE PYTHON RE.la_funcion_a_utilizar

# CLASE 01
import re

# re.SEARCH este método nos ayudará a buscar la primer coincidencia de una cadena de caracteres
# dentro de un texto, devolverá un objeto si lo encuentra, o NONE si no lo encuentra

cadena = "Hola estudiantes de AcademiaCoder. En AcademiaCoder los estudiantes aprenderán programación"

# Si se usa triple comilla para poner una cadena en una variable, imprime tal cual se escriba en ellas
cadena2 = """
Hola estudiantes de AcademiaCoder. 
En AcademiaCoder los estudiantes aprenderán programación
se acabó el curso.
"""

a_buscar = "estudiantes"
print(re.search(a_buscar, cadena))

# Renombramos la coincidencia o match
buscado = re.search(a_buscar, cadena)

if re.search(a_buscar, cadena):
    print("Se ha encontrado")
else:
    print("No se ha encontrado")
# .START sirve para ver donde empieza el match o coincidencia
print(buscado.start())

# .END sirve para ver donde termina el match o coincidencia
print(buscado.end())

# .SPAN sirve para mostrar el intervalo donde está el match
print(buscado.span())

# CLASE 02 == re.FINDALL, re.SPLIT, re.SUB

# .FINDALL() Sirve para que devuelva todas las coincidencias que se hayan obtenido en la cadena
re_findall = re.findall(a_buscar, cadena)
print(re_findall)

# .SPLIT() Sirve para separar las palabras indicandole la letra o el simbolo donde quieres la separación
# por ejemplo separar las palabras por cada espacio que haya "\s"
re_split = re.split("\s", cadena)
print(re_split)

# .SUB() Sirve para sustituir palabras por las que nosotros querramos
re_sub = re.sub(a_buscar, "desarroladores", cadena)
print(re_sub)

print(cadena2)

# CLASE 03 == ANCLAS Y METACARACTERES sintaxis de RegEx

lista = [
    "Marcos - PYTHON",
    "Carlos - JavaScript",
    "Ana - JavaScript",
    "Marcos - PHP",
    "Natalia - VUE",
    "Valeria - PYHTON",
    "Ana - VUE",
    "Martha - Java",
    "Angelo - Programacion",
    "Paty - programación"
]

# De esta forma imprime las lineas que contengan la palabra buscada ""
for linea in lista:
    if re.findall("Marcos", linea):
        print(linea)
print()
# De esta forma imprime las que empiecen por lo que este despues del caret ^
for linea in lista:
    if re.findall("^Mar", linea):
        print(linea)
print()
# De esta forma imprime las que terminen por lo que este antes del símbolo $
for linea in lista:
    if re.findall("aScript$", linea):
        print(linea)
print()
# De la siguiente forma es muy útil para consultar en bases de datos externas
# y se usa como un comodín para buscar por ejemplo, palabras con o sin acento, mayúsculas y minúsculas
for linea in lista:
    if re.findall("[Pp]rogramaci[oó]n", linea):
        print(linea)
