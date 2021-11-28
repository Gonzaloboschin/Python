#                                      VARIADO Y ARCHIVOS DE TEXTO 

import random

#Ejercicio 1

blocnombres = open("nombres.txt","r")

with blocnombres:
    for linea in blocnombres:
        print(linea)
        
#Ejercicio 2      

numeros = open("nros.txt","w")

with numeros:
    for linea in range(1,51):
           
        i = random.randint(1,50)
       
        i = str(i)
              
        numeros.write(i + "\n") 
       
#Ejercicio 3
       
coloritos = ["rojo","azul","naranja","blanco","marron","violeta","negro"]   #lista propia supuse

coloretes = open("colores.txt","w")   #Use "a", para practicar, en si es igual que "w", pero agrega todo al final si tengo algo escrito 

with coloretes:
    for clr in coloritos:
               
        coloretes.write(clr + "\n") 
       
#Ejercicio 4
       
coloretes = open("colores.txt","r")   #Use "a", para practicar, en si es igual que "w", pero agrega todo al final si tengo algo escrito 

with coloretes:
        
    linea = coloretes.readlines()     
    
    print(random.choice(linea))      
       
#Ejercicio 5       

datosnricos = open("datos.txt","r")

with datosnricos:
       
    i = 0
    for linea in datosnricos:
        
        
        linea = int(linea)
        
        i = i + linea
        
    print(i)

#Ejercicio 6

promedionros = open("datos.txt","r")

with promedionros:
       
    i = 0       #Primer contador, para realizar la suma
    cant = 0    #Segundo contador, para contar cada línea del archivo ".txt" con que promediaré
    for numerito in promedionros:
        
        
        numerito = int(numerito)
        
        i = i + numerito
        cant = cant + 1
        
    print(i/cant)

#Ejercicio 7

damigos = open("amigos.csv","w")
lista = []

with damigos:
   
    i = ""   
    
    while (i != "q"):
        
        datos = input("Ingrese el nombre de un amigo y su numero de celular: ")
        # damigos.write(datos + "\n")
        
        if (datos != "q"):
            
            damigos.write(datos + "\n")
            datosl = datos.split()
            datos2 = ",".join(datosl)
            lista.append(datos2)
    
        else:
            # damigos.close()
            print("se guardaron sus entradas")
            print(lista)
            break       
  
#Ejercicio 8     
            
cantamigos = open("amigos.csv","r")

with cantamigos:
    
    x = 0
    for i in cantamigos: 

        x = x + 1

    print(x)
    
    
    
    
    
    