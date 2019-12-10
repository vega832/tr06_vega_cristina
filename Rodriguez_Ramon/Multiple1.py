#PROGRAMA_01
import os
cliente,costo_producto_1,cant_1,total="",0,0,0.0

#INPUT VIA OS
cliente=os.sys.argv[1]
costo_producto_1=int(os.sys.argv[2])
cant_1=int(os.sys.argv[3])

#PROCESSING
total=costo_producto_1*cant_1
#Condicion multiple
#Si su total >= 180 ("calidad de algodon")
if(total >= 180):
    print("calidad de algodon")
#Si su total <= 150 ("calidad media de algodon")
if(total <= 150):
    print("calidad media de algodon")
#Si su total <=80 ("mala calidad de algodon")
if(total <= 80):
    print("mala calidad de algodon")
#fin_if
