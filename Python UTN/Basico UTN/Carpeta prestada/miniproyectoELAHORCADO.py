#                                 MINIPROYECTO: EL AHORCADO

import random

palabras = ["dinosaurio","celular","cuenta","universidad","pesca","gato"]

palabra = random.choice(palabras)

palabrag = ""

for g in palabra:
    if (g != "-"):
        palabrag = palabrag + "-"  #ALTERNATIVA: palabrag = "-"*len(palabra)

listapalabra = list(palabra)

listaguion = list(palabrag)

intentos = int(input("ingrese con cuantos intentos quiere jugar: "))
aciertos = 0
n = 0

while (n < intentos):
    
    letra = input("Ingrese una letra: ")
    
    listaletra = list(letra)
    
    n = n + 1

    print("Le quedan ",intentos - n," intentos")    
        
    if (listaletra == listapalabra[:]):
            
        break
        
    else:
            
        if (letra in listapalabra):
          
            for l in range(len(listapalabra)):
            
                 if (letra == listapalabra[l]):
                     
                     listaguion.insert(l,letra)
                     
                     del listaguion[1 + l]
                     
                     aciertos = aciertos + 1
                     
                 if (aciertos + 1 == len(listapalabra)):
                     
                    adivinar = "".join(listaguion)
                    
                    print("¡Felicidades, usted ha adivinado la palabra!", adivinar)
                    
                    break
        else:
            
            print("La letra ingresada no es válida")
    
    adivinar = "".join(listaguion)
       
    print(adivinar)
            