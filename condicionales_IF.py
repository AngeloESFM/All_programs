# 32 CONDICIONALES
# Sirve para comprobar si algo es cierto o falso y ejecutar una acción
"""
IF sentencia_a_comprobar:
ELIF sentencia_2_a_comprobar:
ELSE:

"""
eres_hombre = False
eres_alto = False

print("Antes del if")

if eres_hombre and eres_alto:
    print("Eres un hombre alto ")
elif eres_hombre and not eres_alto:
    print("Eres un hombre bajo")
elif not eres_hombre and eres_alto:
    print("No eres hombre, pero eres alto")
else:
    print("No eres hombre, ni alto")

print("Despues del if")

if eres_hombre or eres_alto:
    print("Eres hombre o eres alto")
else:
    print("No eres hombre o no eres alto")