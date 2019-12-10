#Programa 07
import os
paciente,medicamento_1,cantidad_de_medicamento_por_dia="","",0

#INPUT VIA OS
paciente=os.sys.argv[1]
medicamento_1=str(os.sys.argv[2])
cantidad_de_medicamento_por_dia=int(os.sys.argv[3])

#PROCESSING
total_medicamento=medicamento_1*cantidad_de_medicamento_por_dia
#Condicion multiple
#Si su medicacion >= 20 ("automedicacion")
if(cantidad_de_medicamento_por_dia >= 20 ):
    print("automedicacion")
#Si su medicacion <= 18 ("medicacion normal")
if(cantidad_de_medicamento_por_dia <= 18):
    print("medicacion normal")
#Si su medicacion es <=14 ("medicamento para dolor muscular")
if(cantidad_de_medicamento_por_dia <= 14):
    print("medicamento para dolor muscular")
#fin_if
