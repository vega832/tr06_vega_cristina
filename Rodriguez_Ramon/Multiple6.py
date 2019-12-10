#Programa 06
import os
deporte,cant_horas_diarias,cant_horas_semanales="",0,0

#INPUT VIA OS
deporte=os.sys.argv[1]
cant_horas_diarias=int(os.sys.argv[2])
cant_horas_semanales=int(os.sys.argv[3])

#PROCESSING
total=cant_horas_diarias*cant_horas_semanales
#Condicion multiple
#Si el total de horas >= 6 ("Inclinacion al deporte")
if(total >= 6):
    print("inclinacion al deporte")
#Si el total de horas <= 5 ("disgusto por el deporte")
if(total <= 5):
    print("disgusto por el deporte")
#Si el total de horas <= 4 ("no le gusta practicar deporte")
if(total <= 4):
    print("no le gusta practicar deporte")
#fin_if
