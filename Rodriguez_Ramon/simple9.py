#PROGRAMA_09
import os
cliente,producto_1="",0

#INPUT VIA OS
cliente=os.sys.argv[1]
producto_1=int(os.sys.argv[2])

#PROCESSING
#Si el numero de producto supera 260, mostrar "Comprador compulsivo"
if(producto_1 > 260):
    print(cliente, "Comprador compulsivo")
#fin_if
