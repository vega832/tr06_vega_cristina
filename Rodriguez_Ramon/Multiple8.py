#Programa 08
import os
alumno,horas_dedicadas_al_estudio_por_dia,horas_dedicadas_al_estudio_por_semana="",0,0

#INPUT VIA OS
alumno=os.sys.argv[1]
horas_dedicadas_al_estudio_por_dia=int(os.sys.argv[2])
horas_dedicadas_al_estudio_por_semana=int(os.sys.argv[3])

#PROCESSING
horas_dedicadas_al_estudio_por_semana=horas_dedicadas_al_estudio_por_dia*horas_dedicadas_al_estudio_por_semana
#Condicion multiple
#Si la cantidad de horas >= 35 ("buen rendimiento academico")
if(horas_dedicadas_al_estudio_por_semana >= 35):
    print("buen rendimiento academico")
#Si la cantidad de horas <= 30 ("regular rendimiento academico")
if(horas_dedicadas_al_estudio_por_semana <= 30):
    print("regular rendimiento academico")
#Si la cantidad de horas <= 20 ("bajo rendimiento academico")
if(horas_dedicadas_al_estudio_por_semana <= 20):
    print("bajo rendimiento academico")
#fin_if
