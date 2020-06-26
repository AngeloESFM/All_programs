# OPERADORES MATEMATICOS
"""
+ SUMA
- RESTA
* MULTIPLICACIÓN
** EXPONENTE
/ DIVISIÓN
// DIVISIÓN QUE DEVUELVE SOLO ENTEROS
% MODULO O RESTO
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

#OPERADORES DE CADENAS

cadena1 = "Hola "
cadena2 = "mundo"
cadenas_unidas= cadena1 + cadena2
#print(cadenas_unidas)

cadenas_repetidas = cadena1 * 3
#print(cadenas_repetidas)

#OPERADORES DE RELACIÓN
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
#OPERADORES DE ASIGNACIÓN= Para asignar valores a una variable
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

#OPERADORES LÓGICOS
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

#OPERADORES DE PERTENENCIA
# Los operadores de pertenencia evaluan si un objeto se encuentra dentro de otro
"""
in -> se encuentra en
not in -> no se encuentra en
"""
cadena = "Angelo"
#print('An' in cadena)
#print('Z' not in cadena)

#FUNCIONES IDENTIDAD
# Los operadores comprueban si un objeto es igual a otro
# is & is not
a = 10
b = 10
print(a is float)
print(a is not int)

# la diferencia entre mutable en inmutable es que los vectores son mutables osea que no cambian su lugar en memoria
# inmutable es que se modifica su lugar en memoria, osea que se borra y se reescribe de nuevo
