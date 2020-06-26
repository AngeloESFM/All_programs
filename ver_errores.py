# 45 TRATAR CON ERRORES EN PYTHON
# TRY ... EXCEPT...ELSE...FINALLY

# TRY & EXCEPT, sirven para cuando haya un error lo brinque y siga ejecutando el programa
# Lo que está en el bloque de TRY, se ejecuta hasta que encuentra un error
try:
    num1 = int(input("Introduzca un número: "))
    num2 = 0
    print(num1)
    print(num1/num2)
# lo que está en el bloque de EXCEPT, se ejecuta cuando ocurre el error
# Para que escriba el error como python se hace de esta forma
except ZeroDivisionError as err:
    print(err)
# Puedes poner también tú propio mensaje
except ValueError:
    print("Ingresa un valor entero")
# lo que está en el bloque de ELSE, se ejecuta cuando no hay ninugún error
else:
    print("No hubo ningún error")
# Lo que está en el bloque de FINALLY, se ejecuta haya o no errores en el código
finally:
    print("Siempre se ejecuta el finally")
