#progrma 05
import os
# Declaracion de variables
cliente,costo_de_unidad="",0
# INPUT via OS
cliente=os.sys.argv[1]
costo_de_unidad=int(os.sys.argv[2])

# PROCESSING
#Si el costo de unidad es mayor 10,
# mostrar "no barato"
#Si el costo de unidad es menor 10,
# mostrar "barato"
if ( costo_de_unidad> 10 ):
    print(costo_de_unidad, ", no barato")
if ( costo_de_unidad< 10 ):
    print(costo_de_unidad,"barato")
#fin_if
