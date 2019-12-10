#Programa 05
import os
usuario,cant_de_horas_por_dia,cant_de_horas_por_semana="",0,0

#INPUT VIA OS
usuario=os.sys.argv[1]
cant_de_horas_por_dia=int(os.sys.argv[2])
cant_de_horas_por_semana=int(os.sys.argv[3])

#PROCESSING
cant_de_horas_por_semana=cant_de_horas_por_dia*cant_de_horas_por_semana
#Condicion multiple
#Si la cantidad de horas >= 15 ("adiccion a las redes sociales")
if(cant_de_horas_por_semana >= 15):
    print("adiccion a las redes sociales")
#Si la cantidad de horas <= 10 ("uso moderado de las redes sociales")
if(cant_de_horas_por_semana <= 10):
    print("uso moderado de las redes sociales")
#Si la cantidad de horas es <=5 ("uso normal de las redes sociales")
if(cant_de_horas_por_semana <= 5):
    print("uso normal de las redes sociales")
#fin_if
