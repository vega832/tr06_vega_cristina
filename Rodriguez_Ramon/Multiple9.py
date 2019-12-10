#Programa 09
import os
cliente,costo_producto,cant_producto,costo_total="",0.0,0,0.0

#INPUT VIA OS
cliente=os.sys.argv[1]
costo_producto=float(os.sys.argv[2])
cant_producto=int(os.sys.argv[3])
costo_total=float(os.sys.argv[4])

#PROCESSING
costo_total=cant_producto*costo_producto
#Condicion multiple
#Si el costo total >= 260 ("comprador compulsivo")
if(costo_total >= 260):
    print("comprador compulsivo")
#Si el costo total <= 200 ("comprador pasivo")
if(costo_total <= 200):
    print("comprador pasivo")
#Si el costo total >= 150 ("comprador cauteloso")
if(costo_total <= 150):
    print("comprador cauteloso")
#fin_if
