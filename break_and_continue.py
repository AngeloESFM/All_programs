# 40 BREAK AND CONTINUE
# Sirve para manejar el flujo de información en un búcle
# el comando BREAK, sirve para cuando queremos que pare el código y lo corta
"""
# Esto recorre e imprime del 0 al 10 y al llegar al 4 para el programa
# si ponemos el print después del break, no imprime el 4
for indice in range(10):
    if indice == 4:
        break
    print(indice)

# Si ponemos el print antes del break, sí imprime el 4
for indice in range(10):
    print(indice)
    if indice == 4:
        break
"""
# el comando CONTINUE, sirve para prevenir o quitar un dato, pero sigue ejecutando lo demás
# Si ponemos el print despues del continue, salta el que es igual a 4
for indice in range(10):
    if indice == 4:
        continue
    print(indice)

# Si ponemos el print antes del continue, no realiza ningún cambio y no funcionaria correctamente
for indice in range(10):
    print(indice)
    if indice == 4:
        continue

# BREAK Y CONTINUE, también funcionan con listas

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

for dia in dias:
    print(dia)
    if dia == "Jueves":
        break


for dia in dias:
    if dia == "Jueves":
        continue
    print(dia)




