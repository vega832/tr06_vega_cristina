#PROGRAMA_10
import os
cliente,producto_1="",0

#INPUT VIA OS
cliente=os.sys.argv[1]
producto_1=int(os.sys.argv[2])

#PROCESSING
#Si el numero de producto supera 15, mostrar "Comprador pasivo"
if(producto_1 > 15):
    print(cliente, "Comprador pasivo")
#fin_if
