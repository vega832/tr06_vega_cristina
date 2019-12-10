#progrma 07
import os
# Declaracion de variables
clase_de_arte,sueldo="",0
# INPUT via OS
clase_de_arte=os.sys.argv[1]
sueldo=int(os.sys.argv[2])

# PROCESSING
#Si el sueldo es mayor 100,
# mostrar "buen trabajo"
#si el sueldo es menor 70
#mostrar "no trabajo"
if ( sueldo> 100 ):
    print(sueldo, ",buen sueldo ")
if ( sueldo<70 ):
    print(sueldo,"no trabajo")
#fin_if
