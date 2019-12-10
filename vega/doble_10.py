# Programa 10
import os
#INPUT
altura=0.0
altura=float(os.sys.argv[1])

# PROCESSING
pulgada= altura/2.54

# OUTPUT
#si en pulgadas es mayor a 4 mostrar pulgada
#si no  de lo contrario mostrar que no esta en pulgada
if(pulgada>4):
    print("la altura en pulgada es:",pulgada)
else:
    print("no esta en pulgada la altura: ",pulgada)
#fin_if

