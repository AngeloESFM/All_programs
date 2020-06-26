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