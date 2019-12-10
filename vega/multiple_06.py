#progrma 06
import os
# Declaracion de variables
cliente,costo_de_unidad="",0
# INPUT via OS
cliente=os.sys.argv[1]
cantidad_producto=int(os.sys.argv[2])

# PROCESSING
#Si la cantidad del producto es mayor 10,
# mostrar "comprador impulsivo"
#Si la cantidad del producto es menor 10,
# mostrar "comprador no impulsivo"

if ( cantidad_producto> 10 ):
    print(cantidad_producto, ",comprador impulsivo ")
if ( cantidad_producto<10 ):
    print(cantidad_producto,"comprador no impulsivo")
#fin_if


