#progrma 08
import os
# Declaracion de variables
empleado,sueldo="",0
# INPUT via OS
empleado=os.sys.argv[1]
sueldo=int(os.sys.argv[2])

# PROCESSING
#Si el sueldo es mayor 100,
# mostrar "calidad de trabajo"
#Si la cantidad del producto es menor 10,
# mostrar "no hay calidad de trabajo"

if ( sueldo> 100 ):
    print(sueldo, ",calidad de trabajo ")
if ( sueldo<100 ):
    print(sueldo,"no hay calidad de trabajo")
#fin_if

