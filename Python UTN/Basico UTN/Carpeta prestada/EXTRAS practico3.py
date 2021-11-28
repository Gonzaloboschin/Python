#                                                VARIADO

#Ejercicio 1

def SecuenciaNros (a,b):

    x = 0
    y = b + 1    #Hago que mi segundo contador, comience del valor mayor, para que vaya decreciendo
    for j in range(a, b + 1):
        x = x + 1
        y = y - 1
        
        print(x, y)
  
# a1 = int(input("ingrese un numero de inicio: "))
# b1 = int(input("ingrese un numero de fin: "))

# SecuenciaNros(a1,b1)
        
#Ejercicio 2
        
nrospares = []
nrosimpares = []
nro = ""
   
while (nro != "q"):
        
    numero = input("Ingrese un número, o la letra -q- para salir: ")
    
    if (numero != "q"):
        
        nros = int(numero)
        if (nros % 2 == 0):
            
            nrospares.append(nros)
            
        else:    
            
            nrosimpares.append(nros)   
            
    else:
        print("La lista de pares es", nrospares)
        print("La lista de impares es", nrosimpares)
        
#Ejercicio 3

lista1 = ["a","b","c","d"]
lista2 = ["a","c"]
lista3 = []

for i in lista1:
    
    for j in lista2:
        
        if (i == j):
            
            lista3.append(i)
            
print("las nueva lista con los elementos en comun es ",lista3)

#Ejercicio 4
        
import random

print("juguemos a -Adivina mi numero- ")

nr = random.randint(1,9)
i = ""

while (i != "s"):
    
    numero = input("Ingrese un número para jugar o la letra -s- para salir: ")
    
    if (numero != "s"):
        
        nro = int(numero)
        if (nro < nr): 
        
            print("su numero esta por debajo del numero RANDOM")
        
        if (nro > nr):
            print("su numero esta por encima del numero RANDOM")
        
        if (nro == nr):
            print("usted acerto. ENHORABUENA!")
            break
                
    else:
         print("gracias por jugar")
         break        
    
#Ejercicio 5 

def cuenta_digitos (numero):
    
    digito = 0
    for j in range(len(numero)):
                
        digito = digito + 1

    return digito

n1 = input("ingrese un numero: ")

print("el numero tiene",cuenta_digitos(n1),"digitos")

#Ejercicio 6

def cuantos_autos (personas):

#supongo que por auto, para que todos viajen comodos, se admiten 4 personas

    return personas//4 #al usar la doble barra, estoy redondeando al entero menor, lo cual es valido ya que se puede tolerar hasta 5 personas

# personas1 = int(input("ingrese cuantas personas viajaran numero: "))

# print("se necesitan",cuantos_autos(personas1),"autos")

#Ejercicio 7
    
def swap_name (nombre,apellido):
    print(apellido, nombre)

nombre1 = input("ingrese su nombre: ")
apellido1 = input("ingrese su apellido: ")

swap_name(nombre1,apellido1)   #me esmere poco en este, cuando lo hice no estaba tan FRESCO, prometo corregirlo a futuro

#Ejercicio 9

def pesada (palabra):

    w = ""
    for i in palabra: 
        w = w +2*i 
    return w
    
# palabrita = input("ingrese una palabra: ")    
# print(pesada(palabrita))

#Ejercicio 10
    
def pedacito (a,b,frase):
    
    subfrase = " "
    a = int(a)
    b = int(b)
    
    if ((a <= b) and (a >= 1) and (b <= int(len(frase)))):
        
        for i in range(a,b + 1):
            
            subfrase = subfrase + frase[i]
            
        return subfrase
            
# incio = int(input("ingrese un numero de inicio: "))
# fin = int(input("ingrese un numero de fin: "))
# frasesita = input("ingrese una frase: ")

# print(pedacito(incio,fin,frasesita))

#Ejercicio 11

def longPalabras (palabra1,palabra2):
    
    if (len(palabra1) == len(palabra2)):
        return True
    else:
        return False

# palabra = input("ingrese una palabra: ")
# palabrota = input("ingrese otra palabra: ")

# print(longPalabras(palabra, palabrota))