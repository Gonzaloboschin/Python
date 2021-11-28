# =============================================================================
# PROYECTO - Ahorcado
# Autor: Gonzalo Boschin
# ============================================================================

import random


#  ====================    BASE DE DATOS DE PALABRAS   =======================      


listapalabras = ["televisor","guitarra", "botella", "bicicleta", "mesa", "maceta", "carpeta"
                 "teclado","planta","calculadora","telefono", "sillon","armario","heladera",
                 "gorro", "barbijo"]   

palabras = open ("palabras.txt", "w")
with palabras:
    for k in listapalabras:
        palabras.write(k + "\n")
            

listacolores = ["rojo","azul","verde","amarillo","naranja", "marron", "negro", 
                "blanco", "dorado", "rosa", "violeta"]

colores = open ("colores.txt","w")
with colores:
    for k in listacolores:
        colores.write(k + "\n")

listaanimales = ["perro", "gato", "raton", "jirafa", "elefante", "tigre", "ballena"
                 "vaca", "caballo","cerdo", "gallina", "pollo"]
    
animales = open("animales.txt", "w")
with animales:
    for k in listaanimales:
        animales.write(k + "\n")
    
    
#  ====================    PRESENTACION DEL AHORCADO   =======================

print("")
print("BIENVENIDO AL AHORCADO!")
print("")
print("Tienes 10 intentos para adivinar la palabra, si no, estas ahorcado!")
print("")
print(""" Con que deseas jugar: 
          1- Palabras aleatoreas
          2- Colores
          3- Animales       """)
sel = int(input("Opcion: "))

if sel == 1:
    # open("palabras.txt", "r")
    palabra = random.choice(listapalabras)
    word = palabra
    print("la palabra tiene ", len(palabra), "digitos!")

if sel == 2:
    # open ("colores.txt", "r")
    palabra = random.choice(listacolores)
    word = palabra
    print("la palabra tiene ", len(palabra), "digitos!")
    print("")
    print("Comencemos!")


if sel == 3:
    # open ("animales.txt", "r")
    palabra = random.choice(listaanimales)
    word = palabra
    print("la palabra tiene ", len(palabra), "digitos!")

palabra1 = ""

for k in palabra:
    if (k != "-"):
        palabra1 = palabra1 + "-"

listapalabra = list(palabra) 
palabraguion = list(palabra1)

intentos = 0
aciertos = 0

while intentos < 10:
    
    intentos += 1
    letra = input("Ingrese una letra: ")
    listaletra = list(letra)
    print("Todavia te quedan ", 10 - intentos, "intentos")
    
    if letra in listapalabra[:]:
        
        for l in range(len(listapalabra)):
            
            if letra == listapalabra[l]:
                palabraguion.insert(l,letra)
                del palabraguion[1 + l]
                aciertos += 1
                
            if aciertos == len (listapalabra):
                adivinar = "".join(palabraguion)
                print("HAS GANADO!")
                print("")
                print("la palabra es ", word)
                break
                # intentos = 10
                
    else:
        
        print("Incorrecto!")
    adivinar = "".join(palabraguion)
    print(adivinar)
print("")
print("PERDISTE!")
print("")
print("""  
            +------H
            [      H
            O      H
           /|\     H
            |      H 
           /\      H
                   H   
 __________________H    """) 
print("")
print("La palabra era ", word)
                   
#  no corta cuando adivinaste la palabra
#  cuando adivinas la palabra, deja un guion en la ultima letra adivinada



