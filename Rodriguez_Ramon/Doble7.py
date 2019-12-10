#PROGRAMA_07
import os
paciente,medicamento_1="",0

#INPUT VIA OS
paciente=os.sys.argv[1]
medicamento_1=int(os.sys.argv[2])

#PROCESSING
#Si el numero de medicamento supera 20, mostrar "Automedicacion"
#Caso contrario mostar "Mala automedicacion"
if(medicamento_1 > 20 ):
    print(paciente, "Automedicacion")
else:
    print(paciente,"Mala automedicacion")
#fin_if
