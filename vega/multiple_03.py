#progrma 03
import os
# Declaracion de variables
nombre,nro_venta="",0
# INPUT via OS
nombre=os.sys.argv[1]
nro_venta=int(os.sys.argv[2])

# PROCESSING
#Si el nro de venta supera 100,
# mostrar "Gano canasta !"
#Si el nro de venta no supera 100,
#  mostrar "Sigue intentado"
if ( nro_venta > 100 ):
    print(nombre, ", Gano canasta !")
if(nro_venta<100):
    print(nombre, ", Sigue intentando!")
#fin_if
