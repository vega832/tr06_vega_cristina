#PROGRAMA_04
import os
cliente,visita_por_semana="",0

#INPUT VIA OS
cliente=os.sys.argv[1]
visita_por_semana=int(os.sys.argv[2])

#PROCESSING
#Si el numero de visita supera 20, mostrar "Visita compulsiva a una libreria"
if(visita_por_semana > 20):
    print(cliente , "Visita compulsiva a una libreria")
#fin_if
