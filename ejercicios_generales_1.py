# EJERCICIOS GENERALES 1
## DATOS SIMPLES
## CONDICIONALES
## BÚCLES
## LISTAS Y DÚPLAS

# EUP que lea un entero positivo, 𝑛, introducido por el usuario y después
# muestre en pantalla la suma de todos los enteros desde 1 hasta 𝑛.
# La suma de los 𝑛 primeros enteros positivos puede ser calculada de la siguiente forma: SUMA = (N(N+1))/2
"""
n = int(input("Ingresa un número para saber su sumatoria: "))
suma = (n*(n + 1)) / 2
print(f"La suma es: {suma}")
for i in range(1, n):
    print(f"{i} + ", end="")
print(str(n) + " =", str(suma))
"""
# EUP que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla:
# <NOMBRE> tiene <n> letras
"""
def letras_en_nombre(nombre):
    n = 0
    for i in nombre:
        n += 1
    return n


nombre = input("Introduzca un nombre: ")
l_e_n = letras_en_nombre(nombre)
print(f"{nombre.upper()} tiene {l_e_n} letras")

# En dos lineas ---
name = input("¿Cómo te llamas? ")
print(name.upper() + " tiene " + str(len(name)) + " letras")
"""

# EUP que pida al usuario su peso (en kg) y estatura (en metros),
# calcule el índice de masa corporal y lo almacene en una variable,
# y muestre por pantalla la frase Tu índice de masa corporal es <imc>

"""
def imc(peso, talla):
    imc = peso / talla**2
    if imc < 18.5:
        print("Tienes un peso inferior al normal")
    elif 18.5 < imc < 24.9:
        print("Tienes un peso normal")
    elif 25 < imc < 29.9:
        print("Tienes un peso superior al normal")
    else:
        print("Tienes obesidad")
    return imc
kg = float(input("Introduce tú peso en kg: "))
est = float(input("Introduce tú estatura en metros: "))
print(f"Tú índice de masa corporal es {round(imc(kg, est), 2)}")
"""
# EUP que pida al usuario dos números enteros
# y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r>
"""
n = int(input("Introduzca un número: "))
m = int(input("Introduzca un número diferente de cero: "))
c = n // m
r = n%m
print(f"Dividendo es {n}, divisor es {m}, cociente es {c} y residuo es {r}")

"""
# EUP que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
# y muestre por pantalla el capital obtenido en la inversión.

"""
def inversion(capital, interes, anios):
    capital_final = capital * ((interes/100 + 1)** anios)
    print("El capital final obtenido fué de:", str(round(capital_final, 2)))

inversion(capital= float(input("Cuánto invertirás? ")),
          interes= float(input("Cuánto es la tasa de interés anual en porcentaje? ")),
          anios= float(input("Cuánto años dejarás la inversión? ")))
"""

# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete,
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda.
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y
# muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""
def paquete(clown, doll):
    peso = (112* clown) + (75*doll)
    print("El peso total es", str(peso/1000) + " KG")


paquete(clown= int(input("Cuántos payasos se venderán? ")),
        doll=  int(input("Cuántos muñecas se venderán? ")))
"""

# Una panadería vende barras de pan a 3.49€ cada una.
# El pan que no es el día tiene un descuento del 60%.
# EUP que comience leyendo el número de barras vendidas que no son del día.
# Después el programa debe mostrar el precio habitual de una barra de pan,
# el descuento que se le hace por no ser fresca y el coste final total.
"""
precio_de_pan = 3.49
porc_de_descuento = 60/100
def descuento(sell):
    des = precio_de_pan * porc_de_descuento
    total_des = sell*(precio_de_pan - des)
    return des, total_des


precio_total = descuento(int(input("Cuántos panes que no son del día se vendieron? ")))
print(f"La barra de pan cuesta {precio_de_pan} ")
print(f"El descuento que se hace por pan es: {precio_total[0]}")
print(f"El costo final del pan vendido es: {round(precio_total[1], 2)}")
"""
# EUP que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario
# coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""
password = "password"
password1 = input("Introduce una contraseña: ")

if password == password1.lower():
    print("Es la contraseña")
else:
    print("No es la contraseña")
"""

# EUP que pida al usuario dos números y muestre por pantalla su división.
# Si el divisor es cero el programa debe mostrar un error.
"""
num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca otro número: "))
while num2 == 0:
    try:
        print(num1 / num2)
    except ZeroDivisionError as error:
        print(error)
        print("No se puede dividir entre 0")
    num2 = int(input("Introduzca otro número diferente a 0: "))

print(num1 / num2)
"""

# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A esta formado por las mujeres con un nombre anterior a la M
# y los hombres con un nombre posterior a la N y el grupo B por el resto.
# EUP que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

"""
def grupo(name, sex):
    abc = "abcdefghijklm"
    xyz = "nñopqrstuvwxyz"
    if (name[0].lower() in abc and sex.lower() == "f") or\
            (name[0].lower() in xyz and sex.lower() == "m"):
        print("Estás en el grupo A")
    else:
        print("Estás en el grupo B")


name = input("Ingresa tú nombre: ")
sex = input('Ingresa tú sexo: ')
grupo(name, sex)

"""
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 200000€ y 35000€	20%
# Entre 350000€ y 60000€	30%
# Más de 60000€	45%
# EUP que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""
renta = int(input("Cuál es tú renta anual? "))
if renta < 10000:
    print("Te corresponde 5%")
elif renta < 20000:
    print("Te corresponde 15%")
elif renta <35000:
    print("Te corresponde 20%")
elif renta <60000:
    print("Te corresponde 30%")
else:
    print("Te corresponde 45%")
"""


# En una determinada empresa, sus empleados son evaluados al final de cada año.
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
# traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más,
# pero no valores intermedios entre las cifras mencionadas.
# La cantidad de dinero conseguida en cada nivel es de 2.400 $ multiplicada por la puntuación del nivel.
# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más
# EUP que lea la puntuación del usuario e indique su nivel de rendimiento,
# así como la cantidad de dinero que recibirá el usuario.
"""
while True:
    score = float(input("Introduzca la puntuación del usuario: "))
    if score == 0.0:
        print('Tú rendimiento es "Inaceptable, "'
              'Tú bonificación es 0 $')
    elif score == 0.4:
        print('Tú rendimiento es "Aceptable", '
              f'Tú bonificación es {2400*score} $')
    elif score >= 0.6:
        print('Tú rendimiento es "Meritoria", '
              f'Tú bonificación es {2400*score} $')
    else:
        print("No existe esa puntuación")

    print("Presiona 1 para calificar a otro empleado, "
          "o presiona 2 para terminar el programa")
    try:
        opc = int(input())
        while opc != 1 and opc != 2:
            print("Elije 1 o 2")
            opc = int(input())
        if opc == 1:
            continue
        elif opc == 2:
            print("Bye")
            break
    except:
        print("Escribe un número, ya sea 1 o 2")
        pass
"""


# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
# Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

"""
def pizza(v):
    if v == "1":
        print("Los ingredientes disponibles son: Pimiento y tofu. Escribe uno.")
        ingr = input()
        print('Tú pizza es vegana con los ingredientes mozzarella, tomate y ', str(ingr))
    else:
        print("Los ingredientes disponibles son: Pepperoni, Jamón y salmón. Elige uno")
        ingr = input()
        print('Tú pizza no es vegetariana con los ingredientes mozzarella, tomate y', str(ingr))

pizza(input("Escribe si deseas una pizza\n1. vegana \n2. no vegana: "))

"""

# EUP que pida al usuario una palabra y la muestre por pantalla 10 veces
"""
pal = input('Introduce una palabra: ')

for i in range(1, 11):
    print(pal)
"""

# EUP que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
edad = int(input("cuántos años tienes? "))

print("Tú edad ha sido: ")
for i in range(1, edad):
    print(str(str(i) + ", "), end="")
print(str(edad) + " años")
"""

# EUP que pida al usuario un número entero positivo y
# muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
num = int(input("Escriba un número: "))

for i in range(1, num, 2):
    #if i%2 != 0:
        print(str(i) + ", ", end="")
print(num)
"""

# EUP que pida al usuario un número entero positivo y
# muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
num = int(input("EScriba un número: "))

print("Los valores son: ", end="")
for i in range(num, -1, -1):
    print(str(i) + ", ", end="")
"""

# EUP que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

"""
def inversion(capital, interes, anios):
    capital_final = capital * ((interes/100 + 1)** anios)
    return capital_final


capital=float(input("Cuánto invertirás? "))
interes=float(input("Cuánto es la tasa de interés anual en porcentaje? "))
anios=float(input("Cuánto años dejarás la inversión? "))


for i in range(1, int(anios)):
    inv_anu = inversion(capital, interes, i)
    print(str(round(inv_anu, 2)) + ", ", end="")
print(inversion(capital, interes, anios))
"""
# otra forma
"""
amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años? "))
for i in range(years):
    amount *= 1 + interest / 100
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))
"""

# EUP que pida al usuario un número entero y muestre por pantalla un triángulo
# rectángulo como el de más abajo, de altura el número introducido.
"""
altura = int(input("Que altura de triángulo quieres? "))

for i in range(1, altura + 1):
    for j in range(i):
        print("* ", end="")
    print()
"""
# EUP que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1
"""
altura = int(input("Que altura de triángulo quieres? "))
for i in range(1, altura + 1, 2):
    for j in range(i, 0, -2):
        print(str(j) + " ", end="")
    print()
"""

# EUP que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""
num = int(input("Inserte un número: "))

for i in range(1, 11):
    tabla = num * i
    print(f"{i} x {num} = {tabla}")
"""
# EUP ue almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""
password = "contraseña"
usuario = input("Introduzca la contraseña: ")

while usuario != password:
    print("no es la contraseña")
    usuario = input("Introduzca la contraseña: ")

print("si es la contraseña")
"""
# EUP que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""
from math import sqrt
num = int(input("Introduce un número: "))
c= 0
for i in range(1, round(sqrt(num)+1)):
    primo = num%i
    if primo == 0:
        c += 1
print(sqrt(num))
print(round(sqrt(num)+1))
if c == 1:
    print("es primo")
else:
    print("no es primo")
    """
# Tambien se puede
"""
n = int(input("Introduce un número entero positivo mayor que 2: "))
for i in range(2, n):
    if n % i == 0:
        break
if (i + 1)  == n:
    print(str(n) + " es primo")
else: 
    print(str(n) + " no es primo")
"""

# EUP que pida al usuario una palabra y
# luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""
palabra = input("introduzca una palabra: ")
for i in range(len(palabra)-1, -1, -1):
    print(str(palabra[i]), end="")
"""
# EUP  en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.
"""
palabra = input("Introduzca una palabra: ")
letra = input("Introduzca una letra: ")
c = 0
for i in palabra:
    if i == letra:
        c += 1
# Esta notación se usa para poder ponerle comillas a una variable
print("La letra '%s' aparece %s veces en la frase '%s'." % (letra, c, palabra))
"""

# EUP que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

"""
pal = input("INtroduce palabras, hasta que quieras salir, ingresa 'salir'")
while pal != "salir":
    print(pal)
    pal = input()

print("aguafiestas")
"""
# LISTAS Y TUPLAS
# EUP que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista y la muestre por pantalla.
"""
lista = []
c = 1
num = int(input("Cuántas materias agregará? "))
while c <= num:
    mat = input("Escribe la materia: ")
    lista.append(mat)
#    lista += [mat]  también se puede de esta forma
    c += 1
print(lista)
"""

# TAMBIEN EN FUNCIÓN  en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>,
# donde <asignatura> es cada una de las asignaturas de la lista.

"""
def asignaturas(num):
    lista = []
    for i in range(num):
        mat = input("Escribe la materia: ")
        lista.append(mat)
    for j in lista:
        print(f"Yo estudio {j}")
    return lista


num = int(input("Cuántas materias ingresaras? "))
print(f"Las materias son: {asignaturas(num)}")
"""

# EUP que almacene las asignaturas de un curso ( Matemáticas, Física, Química, Historia y Lengua) en una lista,
# pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje
# En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota>
# cada una de las correspondientes notas introducidas por el usuario.

"""
subjects = ["Math", "Spanish", "Physics", "Geo", "History"]
for i in range(len(subjects)):
    score = float(input(f"ingresa la calificación para {subjects[i]}: "))

    print(f"En {subjects[i]} has sacado {score}")
"""
# Otra forma de resolverlo
"""
subjects = ["Math", "Spanish", "Physics", "Geo", "History"]
score = []
for j in subjects:
    nota = float(input(f"ingresa la calificación para {j}: "))
    score.append(nota)
for i in range(len(subjects)):
    print(f"En {subjects[i]} has sacado {score[i]}")
"""
# EUP que pregunte al usuario los números ganadores de la lotería primitiva,
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
# si tiene 10 números
"""c = 1
loteria = []
while c <= 6:
    num = int(input("Introduzca los números de la loteria: "))
    loteria.append(num)
    c += 1

print("los números ganadores son: ", end="")
loteria.sort()
print(loteria)
loteria.reverse()
print(loteria)
"""

# EUP que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""
lista = []
for i in range(1, 11):
    lista.append(i)

lista.reverse()
print("Los números son: ")
print(lista)

# Otra forma de resolverlo

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 10):
    print(numbers[-i], end=", ")
print("1")
print("")

# Otra forma más

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
for number in numbers:
    print(str(number) + ", ", end="")
print(numbers[9])
"""
# EUP que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
# pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""
materias = ["MAth", "Phys", "Chemis", "His", "Leng"]
reprobadas = []
for j in materias:
    cal = float(input("Introuce calificación para " + str(j) + ": "))
    if cal <= 5.5:
        reprobadas.append(j)

print("Las materias que repetirá son : ", end="")
for i in range(0, len(reprobadas)-1):
    print(str(reprobadas[i]), end=", ")
print(reprobadas[-1])
"""
# EUP que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3,
# y muestre por pantalla la lista resultante.
"""
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o"]
mul3 = []
for i in range(1, len(abc) + 1):
    if (i%3 == 0):
        mul3.append(abc[i-1])
for j in mul3:
    abc.remove(j)

print("La lista que quedó es: ", end="")
for k in abc:
    print(str(k), end=" ")
print("")
# También se puede
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(alphabet), 1, -1):
    if i % 3 == 0:
        alphabet.pop(i-1)
print(alphabet)
"""
# EUP que lea una palabra y diga si es un palíndromo
"""
pal = input("Escriba una palabra: ")
palind = ""
pal = pal.lower()
for i in range(len(pal)-1, -1, -1 ):
    palind += pal[i]

if pal== palind:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
    print("La palabra inversa es: ", end="")
    print(palind.capitalize())

# Otra forma convirtiendo en lista cada de letra de una palabra con el comando LIST(palabra_introducida)
word = input("Introduce una palabra: ").lower()
reversed_word = word
word = list(word)
print(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
print(reversed_word)
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
"""
# para imprimir el abecedario se usa ASCII_LOWERCASE
"""
from string import ascii_lowercase
print(ascii_lowercase)
for i in ascii_lowercase:
    if i < 'p':
        print(i, end='')
"""

# EUP que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""
pal = input("ingresa una palabra: ")
voc = [""]
ca, ce, ci, co, cu = 0, 0, 0, 0, 0
for i in pal.lower():
    if i == 'a':
        ca += 1
    elif i =='e':
        ce += 1
    elif i == 'i':
        ci += 1
    elif i == 'o':
        co += 1
    elif i == 'u':
        cu += 1
print("Las veces que apareció 'a' fué: " + str(ca))
print("Las veces que apareció 'e' fué: " + str(ce))
print("Las veces que apareció 'i' fué: " + str(ci))
print("Las veces que apareció 'o' fué: " + str(co))
print("Las veces que apareció 'u' fué: " + str(cu))
"""
# OTRA FORMA
"""
word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals:
    times = 0
    for letter in word:
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")
"""
# EUP que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8,
# y muestre por pantalla el menor y el mayor de los precios.
"""
precios = [50, 75, 46, 22, 80, 8, 97, 32, 100]
may = men = precios[0]

for i in range(len(precios)):
    if precios[i] < men:
        men = precios[i]
    if precios[i] > may:
        may = precios[i]
print("El mayor es: " + str(may))
print("El menor es: " + str(men))
"""
# EUP que almacene los vectores (1,2,3) y (-1,0,2) en dos tuplas y muestre por pantalla su producto escalar.
"""
a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores " + str(a) + " y " + str(b) + " es " + str(product))
"""

# EUP que pregunte por una muestra de números, separados por comas, los guarde en una tupla
# y muestre por pantalla su media y desviación típica.
"""
from math import sqrt
sample = input("Introduce una muestra de números separados por comas: ")
sample = sample.split(',')
n = len(sample)
suma = 0
for i in range(n):
    suma += float(sample[i])
media = suma/n
sumavar = 0
for i in range(n):
    sumavar += (float(sample[i]) - media)**2
var = sumavar/n
sd = sqrt(var)
sd2 = var**(1/2)
print(media)
print(var)
print(sd)
print(sd2)
"""
## OTRA FORMA
"""
sample = input("Introduce una muestra de números separados por comas: ")
sample = sample.split(',')
n = len(sample)
for i in range(n):
    sample[i] = int(sample[i])
sample = tuple(sample)
sum = 0
sumsq = 0
for i in sample:
    sum += i
    sumsq += i**2
mean = sum/n
stdev = (sumsq/n-mean**2)**(1/2)
print('La media es', mean, ', y la desviación típica es', stdev)
"""
# EUP que almacene las matrices en una lista y muestre por pantalla su producto.
# Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
# Con NUMPY multiplicando las matrices
"""
import numpy as np
a = ([1, 2, 3],
     [4, 5, 6])
b = ([-1, 0], [0, 1], [1, 1])
np.dot(a,b)
array([[2,  5],
       [2, 11]])
"""
# SIN NUMPY
"""
a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
result = [[0,0],
          [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])"""