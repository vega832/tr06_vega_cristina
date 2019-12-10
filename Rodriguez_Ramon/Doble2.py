#PROGRAMA_02
import os
cliente,producto_1="",0

#INPUT VIA OS
cliente=os.sys.argv[1]
producto_1=int(os.sys.argv[2])

#PROCESSING
#Si el numero de producto supera 250, mostrar "Marca"
#Caso contrario mostar "Mala marca"
if(producto_1 > 250 ):
    print(cliente, "Marca")
else:
    print(cliente,"Mala marca")
#fin_if
