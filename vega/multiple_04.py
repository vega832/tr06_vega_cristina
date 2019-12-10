#progrma 04
import os
# Declaracion de variables
clase_de_trabajo,nro_empleados="",0
# INPUT via OS
clase_de_trabajo=os.sys.argv[1]
nro_empleados=int(os.sys.argv[2])

# PROCESSING
#Si el nro de empleados supera 10,
# mostrar "empresa laboral "
#si el nro de empleados no supera 10
#mostrar "nimgun trabajo"
if ( nro_empleados> 10 ):
    print(clase_de_trabajo, ", empresa laboral")
if(nro_empleados<10):
    print(clase_de_trabajo,"ningun trabajo")
#fin_if
