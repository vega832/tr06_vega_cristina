# Programa 10
import os
#INPUT
altura=0
altura=int(os.sys.argv[1])

# PROCESSING
pulgada= altura/2.54

# OUTPUT
#si en pulgadas es mayor a 4 mostrar "pulgada esta en altura"
#si en pulgada es menor a 10 mostrar " no esta en pulgada la altura"
if(pulgada>4):
    print("la altura en pulgada es:",pulgada)
if(pulgada<10):
 print("no esta en pulgada la altura: ",pulgada)
#fin_if

