#ejercicio 02
import os
#delclarion de variables
trabajador,renumeracion_mensual="",0
#INPUT VIA OS

trabajador=os.sys.argv[1]
renumeracion_mensual=int(os.sys.argv[2])
#PROCESSING
#si el la renumeracion mensual es mayor 100
#mostrar "tiene renumeracion anual"
#si el la renumeracion mensual es menor 50
#mostrar "no tiene renumeracion anual"
if (renumeracion_mensual>100):
    print(trabajador,"tiene reunmeracion anual")
if(renumeracion_mensual<50):
    print(trabajador,"no tiene renumeracion anual")

#fin_if
