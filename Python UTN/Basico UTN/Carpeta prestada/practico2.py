#                                          MANEJO DE STRINGS

#Ejercicio 1

frase = input("ingrese una frase: ")

print(frase.upper())
print(frase.lower())

#Ejercicio 2

frase1 = input("ingrese una frase: ") 

if  (frase1 == frase1.lower()):
    print(frase1.upper())
    
else:
    print(frase1.lower())
    
#Ejercicio 3

frase = input("ingrese una frase: ")
palabra = input("ingrese una palabra: ")

if  (palabra in frase):
    print("la palabra está en la frase")

else:
    print("la palabra no está en la frase")

#Ejercicio 4
    
palabra = input("ingrese una palabra: ")
todosnumeros = True

for letra in palabra:
    if  (letra not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]):
        todosnumeros = False

if  (todosnumeros == True):
    print("la palabra tiene números")

else:
    print("la palabra no tiene números")

#Ejercicio 5
    
frase = input("ingrese una frase: ")
palabra = input("ingrese una palabra: ")

if  (frase.startswith(palabra)):
    print("la frase comienza con la palabra", palabra)

if  (frase.endswith(palabra)):
    print("la frase termina con la palabra", palabra)  

#Ejercicio 6
    
frase = input("ingrese una frase: ")
letra = input("ingrese una letra: ")

cant = 0

for letrita in frase:
    if  (letrita == letra):
        cant = cant + 1

print("la cantidad de ocurrencias de la letra en la frase es:", cant)

#Ejercicio 7

frase = input("ingrese una frase o palabra: ")

print("-".join(frase)) #Pude haber utilizado un separador diferente, como una coma o un punto. 
    
#Ejercicio 8

frasenro = "23,6,82,5,123,65"

print(frasenro.split())

#                                              LISTAS
    
#Ejercicio 9

#Para conocer el último elemento de una lista, sin utilizar len() o conociendo su cantidad de elementos,
#es utilizando el comando lista(-1), donde lista tiene almacenado los datos de mi lista y el "-1" indica
#el último elemento (sea numérico o una palabra). 
    
#Ejercicio 10

frutas = ["durazno","cereza","manzana","melon","sandia","banana","pera","frambuesa","naranja","mandarina"]

#a

if  ("cereza" in frutas):
    print("hay cerezas en la lista")

#b

fruta1 = input("ingrese una fruta: ")
frutas.append(fruta1)
print("se añadió la fruta a la lista",frutas)


#c

if  ("durazno" in frutas):
    frutas.remove("durazno")
    print(frutas)
else: 
    print("la fruta durazno no se encuentra en la lista")

#d

print("las primeras 5 frutas de la lista son: ",frutas[:5])

#e

print("la cantidad de frutas disponibles son", frutas)

#f

ver1 = input("ingrese una verdura: ")
ver2 = input("ingrese una verdura: ")
ver3 = input("ingrese una verdura: ")
ver4 = input("ingrese una verdura: ")
ver5 = input("ingrese una verdura: ")

verduras = [ver1,ver2,ver3,ver4,ver5]
print(frutas)

#g

frutasalfabeticas = frutas.sort()

print(frutas)

#                                        BUCLES: FOR

#Ejercicio 11

#a

palabra = input("ingrese una palabra: ")

for l in palabra:
     print(l)
     
#b

palabra = input("ingrese una palabra: ")

for l2 in palabra[::-1]: #comando extraído de google algo[::-1] me da 'algo' al revés
     print(l2)

#c

cuenta = 0
for i in range(1,51):
    cuenta = cuenta + (i**2 + 3*i)

print(cuenta)

#d

a = int(input("ingrese un número entero: "))
b = int(input("ingrese otro número entero: "))

sumita = 0
for j in range(1,46):
    sumita = sumita + (j + (b - a)/(a**2 + b**2 + j**2))

print(sumita)

#Ejercicio 12

n1 = int(input("ingrese un número entero: "))
n2 = int(input("ingrese un número entero: "))
n3 = int(input("ingrese un número entero: "))
n4 = int(input("ingrese un número entero: "))
n5 = int(input("ingrese un número entero: "))
n6 = int(input("ingrese un número entero: "))
n7 = int(input("ingrese un número entero: "))
n8 = int(input("ingrese un número entero: "))
n9 = int(input("ingrese un número entero: "))
n10 = int(input("ingrese un número entero: "))

nros = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]

print("la lista de números es:", nros)

print("el mayor número de la lista es: ", max(nros))
print("el mayor número de la lista es: ", min(nros))

#Ejercicio 13

n = int(input("ingrese longitud: "))

borde = ""
for i in range(n):
     borde = borde + "#"

medio = "#"
for i in range(n - 2):
    medio = medio + " "

medio = medio + "#"  

#CONDICIÓN DE DIBUJO   
print(borde)

for i in range(n - 2):
    print(medio)

print(borde)

#                                     NÚMEROS ALEATORIOS

import random 

#Ejercicio 14

#a

frase = input("ingrese una frase: ")

print(random.choice(frase))

#b

nro = int(input("ingrese un número: "))
otronro = random.randint(1,100)

print("número aleatorio", otronro)

if  (nro > otronro):
    print("el número ingresado es mayor que el número aleatorio")
    
else: 
    print("el número ingresado es menor que el número aleatorio")

#Ejercicio 15
    
colores = ["azul", "verde", "anaranjado", "rojo", "violeta", "topacio"]

print("un color al azar de la lista es, ",random.choice(colores))

#Ejercicio 16

nrosx = [] #lista vacía a llenar

for t in range(50): #el 50 representa la cantidad de nros que quiero ingresar a la lista
    nrosx.append(random.randint(1,10)) #este rango representa los nros que que se verán en la lista, incluidos los extremos

print(nrosx) 
    
#Ejercicio 17

nrosz = [] #lista vacía a llenar

for n in range(10): 
    nrosz.append(random.random()) 

print(nrosz)    
    
#                                             VARIADOS   

#Ejercicio 18

# frase = input("Ingrese una frase: ")
# frase = frase.strip()
# c = 0
# for i in range(len(frase)):
#     if (frase[i] == ' '):
#         c = c + 1

# print(c + 1)    
    
#El programita seleccionado, comienza pidiendo una frase al usuario, a la cual le elimina los espacios 
#que sobran, tanto al inicio como al final. Luego en el FOR, declara una variable "i", que va a dar "n"
#vueltas. Lo que hace el if, es que si es igual a un espacio vacío, que lo sume en la variable contador "c".
#Entonces, luego de terminar de dar las vueltas, imprime la cantidad de espacios que contó.
#Básicamente cuenta la cantidad de sílabas que tiene la frase ingresada por el usuario.  
    
#Ejercicio 19    
    
frase = input("Ingrese una frase: ")

for r in frase:
    if  (r == "a" or r == "e" or r == "i" or r == "o" or r == "u"):
      print(r)     
    
#Ejercicio 20

#Igual al ejercicio 5    
    
#Ejercicio 21
      
frase1 = input("Ingrese una frase: ")

w = 0
for s in range(len(frase1)):
    if (frase1[s] == ' '): #el único error es que si el usuario tipea un espacio al final, lo cuenta como palabra
        w = w + 1

print("la cantidad de palabras que hay en la frase son: ",w + 1)  
    
#Ejercicio 22   
 
palabra2 = input("Ingrese una palabra: ")
vocales = ("aeiou")

sinvocal = ""

for letras in palabra2:
    if(letras not in vocales):
        sinvocal = sinvocal + letras

print(sinvocal)    
    
#Ejercicio 23    
  
palabra3 = input("introduzca una palabra: ")
palabra4 = input("introduzca otra palabra: ")

if  ((palabra3[::-1] == palabra4) or (palabra4[::-1] == palabra3)):
    print("las palabras ingresadas son inversas una de la otra")

else: 
    print("las palabras ingresadas no son inversas entre sí")    
    
#Ejercicio 24   

palabra5 = input("Ingrese una palabra: ")

if  (palabra5 == palabra5[::-1]):
    print("la palabra es palíndrome")

else: 
    print("la palabra no es palíndrome ")   