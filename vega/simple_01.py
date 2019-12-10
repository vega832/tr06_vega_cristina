# Programa 01
import os
producto, mensaje="",""

#INPUT VIA OS
producto=os.sys.argv[1]

# PROCESSING
# Si el producto es gloria, mostrar "producto malo"
if ( producto == "gloria"):
    mensaje="producto malo"

#OUTPUT
print(mensaje)
