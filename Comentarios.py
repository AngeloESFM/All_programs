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
