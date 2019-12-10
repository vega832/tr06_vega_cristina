#PROGRAMA_03
import os
nombre_del_alumno,nota_1="",0

#INPUT VIA OS
nombre_del_alumno=os.sys.argv[1]
nota_1=int(os.sys.argv[2])

#PROCESSING
#Si el numero de nota supera 11, mostrar "Nota aprobatoria"
if(nota_1 > 11):
    print(nombre_del_alumno, "Nota aprobatoria")
#fin_if
