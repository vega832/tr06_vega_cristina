# Programa 01
import os
producto, mensaje="",""

#INPUT VIA OS
producto=os.sys.argv[1]

# PROCESSING
# Si el producto es gloria, mostrar producto malo
#si el producto es ideal ,mostrar producto bueno
if ( producto== "gloria"):
    print("producto malo")
if(producto=="ideal"):
    print("producto bueno")
#fin_if
