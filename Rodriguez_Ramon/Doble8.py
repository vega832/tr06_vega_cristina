#PROGRAMA_08
import os
alumno,horas_dedicadas_al_estudio_por_dia="",0

#INPUT VIA OS
alumno=os.sys.argv[1]
horas_dedicadas_al_estudio_por_dia=int(os.sys.argv[2])

#PROCESSING
#Si el numero de horas dedicadas supera 35, mostrar "Buen rendimiento academico"
#Caso contrario mostar "Bajo rendimiento academico"
if(horas_dedicadas_al_estudio_por_dia > 35 ):
    print(alumno, "Buen rendimiento academico")
else:
    print(alumno,"Bajo rendimiento academico")
#fin_if
