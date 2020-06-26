# 60, 61, 62, 63 EXPRESIONES REGULARES
# USAMOS EL MÓDULO DE PYTHON RE.la_funcion_a_utilizar

# CLASE 01
import re

# re.SEARCH este método nos ayudará a buscar la primer coincidencia de una cadena de caracteres
# dentro de un texto, devolverá un objeto si lo encuentra, o NONE si no lo encuentra
# RE.SEARCH(match_a_buscar, cadena_en_la_que_busca)
print("Clase 1")
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

print("\nClase 2")
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

print("Clase 3")
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

# CLASE 04 == RANGOS, RANGO NEGADO, CLASES PREDEFINIDAS, CUANTIFICADORES Y OTROS METACARÁCTERES

print("\nClase 4")
cadena = "abcdef ghi_"\
    "0123456789-"

# RANGOS[] Se usa para buscar en un rango determinado por
# RE.FINDALL("[menor-mayor]", cadena_en_la_que_se_busca)
print(re.findall("[a-d]", cadena))

# Se pueden concatenar rangos de la siguiente forma poniendo rangos seguidos
print(re.findall("[a-d1-5]", cadena))

# RANGO NEGADO Si se le agrega un ^ (caret) previo al rango, busca todo lo contrario al rango
print(re.findall("[^a-d1-5]", cadena))

# CLASES PREDEFINIDAS
# \d muestra todos los números que existan
# \D lo contrario a d
# \w muestra las letras, minus, mayus, números, guiones bajos
# \W Lo contrario a \w
# \s muestra todos los espacios

print(re.findall("\d", cadena))
print(re.findall("\D", cadena))
print(re.findall("\w", cadena))
print(re.findall("\W", cadena))
print(re.findall("\s", cadena))
"""
CUANTIFICADORES
Son caracteres que multiplican el patrón que les precede.
Mientras que con las clases de caracteres podemos buscar un dígito, o una letra; 
con los cuantificadores podemos buscar cero o más letras, al menos 7 dígitos, o entre tres y 
cinco letras mayúsculas. Los cuantificadores son:
?: coincide con cero o una ocurrencia del patrón. Dicho de otra forma, hace que el patrón sea opcional
+: coincide con una o más ocurrencias del patrón
*: coincide con cero o más ocurrencias del patrón.
{x}: coincide con exactamente x ocurrencias del patrón
{x, y}: coincide con al menos x y no más de y ocurrencias. Si se omite x, el mínimo es cero, y si se omite y, no hay máximo. Esto permite especificar a los otros como casos particulares: ? es {0,1}, + es {1,} y * es {,} o {0,}.
Ejemplos:
.* : cualquier cadena, de cualquier largo (incluyendo una cadena vacía)
[a-z]{3,6}: entre 3 y 6 letras minúsculas
\d{4,}: al menos 4 dígitos
.*[hH]ola!?: una cadena cualquiera, seguida de hola, y terminando (o no) con un !
"Mi nombre es Marcos, hola!"
"Mi nombre es Marcos, hola"
OTROS METACARACTERES
Existen otros metacaracteres en el lenguaje de las expresiones regulares:
?: Además de servir como cuantificador, puede modificar el comportamiento de otro. 
De forma predeterminada, un cuantificador coincide con la mayor cadena posible. 
Cuando se le coloca un ?, se indica que se debe coincidir con la menor cadena posible. 
Esto es: dada la cadena bbbbb, b+ coincide con la cadena entera, mientras que b+? coincide solamente con b. 
Es decir, la menor cadena que cumple el patrón.
(): agrupan patrones. Sirven para que aquel pedazo de la cadena que coincida con el patrón sea capturado; 
o para delimitar el alcance de un cuantificador. Ejemplo: ab+ coincide con ab, abb, abbbbb, …, 
mientras que (ab)+ coincide con ab, abab, abab…
| : permite definir opciones para el patrón: perro|gato coincide con perro y con gato.
"""