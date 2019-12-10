# Programa 01
import os
producto, mensaje="",""

#INPUT VIA OS
producto=os.sys.argv[1]

# PROCESSING
# Si el producto es gloria mostrar que es producto malo
#si no al contrario sera producto bueno
if ( producto== "gloria"):
    print("producto malo")
else:
    print("producto bueno")
#fin_if
