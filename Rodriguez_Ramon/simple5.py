#PROGRAMA_05
import os
usuario,cant_de_hora_diarias="",0

#INPUT VIA OS
usuario=os.sys.argv[1]
cant_de_hora_diarias=int(os.sys.argv[2])

#PROCESSING
#Si el numero de horas supera 15, mostrar "Adiccion de las redes sociales"
if(cant_de_hora_diarias > 15):
    print(usuario , "Adiccion de las redes sociales")
#fin_if
