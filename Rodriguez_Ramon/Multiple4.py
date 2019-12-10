#Programa 04
import os
cliente,visita_por_semana,cant_visita,total="",0,0,0

#INPUT VIA OS
cliente=os.sys.argv[1]
visita_por_semana=int(os.sys.argv[2])
cant_visita=int(os.sys.argv[3])
total=int(os.sys.argv[4])

#PROCESSING
total=cant_visita*visita_por_semana
#Condicion multiple
#Si la visita_por_semana  >= 20 ("Visita pasiva a una libreria")
if(visita_por_semana > 20):
    print("Visita pasiva a una libreria")
#Si la visita_por_semana  <= 15 ("Visita media pasiva a una libreria")
if(visita_por_semana  <= 15):
    print("Visita media pasiva a una libreria")
#Si la visita_por_semana  >= 8 ("Baja visita compulsiva a una libreria")
if(visita_por_semana <= 8):
    print("Baja visita compulsiva a una libreria")
#fin_if
