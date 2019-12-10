#programa 09
import os
# Declaracion de variables
trabajador,renumeracion_neta_anual="",0
# INPUT via OS
trabajador=os.sys.argv[1]
renumeracion_neta_anual=int(os.sys.argv[2])

# PROCESSING
#Si la renumeracion neta anual es mayor 200
# mostrar "impuesto mensual"
#Si la renumeracion neta anual es maenor200
# mostrar " no hay impuesto mensual"

if ( renumeracion_neta_anual> 200 ):
    print(renumeracion_neta_anual, ",impueto mensual")
if( renumeracion_neta_anual< 100 ):
    print(renumeracion_neta_anual,"no hay impuesto mensual")
#fin_if
