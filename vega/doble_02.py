#ejercicio 02
import os
#delclarion de variables
trabajador,renumeracion_mensual="",0
#INPUT VIA OS

trabajador=os.sys.argv[1]
renumeracion_mensual=int(os.sys.argv[2])
#PROCESSING
#si el la renumeracion mensual es mayor 100
#mostrar tiene renumeracion anual
#caso contrario se muestra "no tiene renumeracion anual"
if (renumeracion_mensual>100):
    print(trabajador,"tiene reunmeracion anual")
else:
    print(trabajador,"no tiene renumeracion anual")
#fin_if
