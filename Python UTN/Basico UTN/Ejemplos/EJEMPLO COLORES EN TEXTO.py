# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:25:23 2021

@author: Gonzalo
"""

# EJEMPLO de color
# Imprimo hola en verde
print("\033[32m")
print("hola")

# también puedo imprimir Zapatilla, cambiando su fondo y estilo, y poniendo
# la secuencia de escape dentro del mismo texto en el print:
print("\033[1;35;40m Zapatilla")

# Colores de letra:

# Negro: \u001b[30m
# Rojo: \u001b[31m
# Verde: \u001b[32m
# Amarillo: \u001b[33m
# Azul: \u001b[34m
# Magenta: \u001b[35m
# Cyan: \u001b[36m
# Blanco: \u001b[37m