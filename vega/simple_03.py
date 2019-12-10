#progrma 03
import os
# Declaracion de variables
nombre,nro_venta="",0
# INPUT via OS
nombre=os.sys.argv[1]
nro_venta=int(os.sys.argv[2])

# PROCESSING
#Si el nro de venta supera 100,
# mostrar "Gano canasta"
if ( nro_venta > 100 ):
    print(nombre, ", Gano canasta ")
#fin_if
