#PROGRAMA_06
import os
nombre,deporte="",0

#INPUT VIA OS
nombre=os.sys.argv[1]
deporte=int(os.sys.argv[2])

#PROCESSING
#Si el numero de deporte supera 6, mostrar "Gusto por el deporte"
if(deporte > 6):
    print(nombre, "Gusto por el deporte")
#fin_if
