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
#Si el costo total >= 15 ("comprador pasivo")
if(costo_total >= 15):
    print("comprador pasivo")
#Si el costo total <= 12 ("comprador medio pasivo")
if(costo_total <= 12):
    print("comprador medio pasivo")
#Si el costo total >= 10 ("comprador cauteloso")
if(costo_total <= 10):
    print("comprador cauteloso")
#fin_if
