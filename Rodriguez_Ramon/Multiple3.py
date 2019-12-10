#PROGRAMA_03
import os
nombre_alumno,nota_1,nota_2,nota_3,promedio="",0,0,0,0

#INPUT VIA OS
nombre_alumno=os.sys.argv[1]
nota_1=int(os.sys.argv[2])
nota_2=int(os.sys.argv[3])
nota_3=int(os.sys.argv[4])

#PROCESSING
promedio=nota_1+nota_2+nota_3/3
#Condicion multiple
#Si el promedio >= 12 ("nota aprobatoria")
if(promedio >= 12):
    print("nota aprobatoria")
#Si el promedio <= 11 ("nota aprobatoria baja")
if(promedio <= 11):
    print("nota aprobatoria baja")
#Si el promedio <=10 ("nota desaprobatoria)
if(promedio <= 10):
    print("nota desaprobtoria")
#fin_if
