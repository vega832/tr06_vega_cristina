#PROGRAMA_02
import os
cliente,producto_1,cant_1="",0,0.0

#INPUT VIA OS
cliente=os.sys.argv[1]
producto_1=int(os.sys.argv[2])
cant_1=float(os.sys.argv[3])

#PROCESSING
total=producto_1*cant_1
#Condicion multiple
#Si su total >= 180 ("Marca")
if(total >= 250):
    print("Marca")
#Si su total <= 150 (Media Marca)
if(total <= 160):
    print("calidad media de algodon")
#Si su total <=80 ("Mala marca")
if(total <= 50):
    print("Mala marca")
#fin_if
