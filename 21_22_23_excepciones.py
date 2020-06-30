# 21, 22, 23 EXCEPCIONES I, II, III
""" 
Estas se usan para que el programa siga corriendo y no se frene por errores
TRY:
    código_que_debe_intentar
EXCEPT nombre_del_error:
    código_que_dice_que_hacer_si_produce_un_error
"""
"""
def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multiplica(num1, num2):
    return num1*num2

def divide(num1,num2): 
    # intenta TRY hacer la operación y si hay error hace lo que esta en EXCEPT
    try: 
        return num1/num2
    except ZeroDivisionError:
        print("no se puede dividir entre 0")
        return "Operacion erronea"

while True:

    try:
    op1=(int(input("Introduce el primer número: ")))

    op2=(int(input("Introduce el segundo número: "))) 

    except ValueError:
        print("escribe números") 
    
    operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

    if operacion=="suma":
        print(suma(op1,op2))

    elif operacion=="resta":
        print(resta(op1,op2))

    elif operacion=="multiplica":
        print(multiplica(op1,op2))

    elif operacion=="divide":
        print(divide(op1,op2))

    else:
        print ("Operación no contemplada")


    print("Operación ejecutada. Continuación de ejecúción del programa ")

    dec = input("Elige 1 para  seguir, 2 para cerrar: ")
    if dec == "1":
        print("Seguimos...")
    else: 
        print("Adios.")
        break
"""
def div():
    
    try:
        n1 = float(input("introduce un número: "))
        n2 = float(input("introduce un número: "))
        print("El resultado es" +  str(n1/n2))
    # se pueden poner todos los EXCEPT consecutivamente, unos tras otro
    except ZeroDivisionError:
        print("no se puede dividir entre 0")
    except ValueError:
        print("Escriba números, no otra cosa")
    # Lo que está dentro de FINALLY, se ejecuta siempre, tenga errores o no el programa
    finally:
        print("Se ha hecho el cálculo")

div()

def evaEdad(edad):

    if edad<0:
        #se puede definir tú propio error pero hay que crear una clase o usar las existentes
        # se define con la instrucción RAISE tipo_del_error("mensaje para el usuario")
        raise TypeError("No puede haber edades negativas")
    if edad<20:
        print("Eres muy jóven")
    elif edad<50:
        print("Eres adulto")

evaEdad(-15)