#                                      EXPRESIONES REGULARES 

import re

#Ejercicio 1

def validarDNI (doc):
    
    regla = "^\d{7,9}$"

    if (re.search(regla,doc)):
        return True
    
    else:
        return False

# DNI = input("Ingrese su numero de documento: ")
# print(validarDNI(DNI))
    
#Ejercicio 2

def validarPATENTE (patente):
    
    regla1 = "^[A-Z]{3}\s\d{3}$"     #Modelo antiguo de patente 3 letras + 3 numeros

    if (re.search(regla1,patente)):  #Con ^ al inicio y $ al final, la regla es 100% estricta y no permite variaciones
        return True
    
    else:
        return False

# nropatente = input("Ingrese la patente de su vehiculo: ")
# print(validarPATENTE(nropatente))

#Ejercicio 3

def es_decimal (nrofloat):    #use ambas separaciones, con diferentes reglas, por las dudas, pero para mi es con coma
    
    regla2 = "^\d\.\d{1,2}$"    #separacion con punto
    regla2v = "^\d\,\d{1,2}$"   #separacion con coma
    
    if (re.search(regla2,nrofloat) or re.search(regla2v,nrofloat)):
        return True
    
    else:
        return False
    
# nrodecimal = input("Ingrese un numero decimal: ")
# print(es_decimal(nrodecimal))

#Ejercicio 4

def solo_letras(texto):
    
    if (re.search("^\D[a-zA-z]*$",texto)):
        return True
    else:
        return False
    
# palabra = input("Ingrese una palabra: ")

# print(solo_letras(palabra))

#Ejercicio 5

def celular_internacional(numero):
        
    reglanro = "\+549\d{2,4}\d+"
    
    while (numero != "q"):
        
        # numero = input("Ingrese un numero de celular: ")
        
        if (re.search(reglanro,numero)):
            return True
        
        else:
            return False
            break
    
numero = input("Ingrese un numero de celular: ")

print(celular_internacional(numero))    

#Ejercicio 6

frase = "Mis abuelos tenian 22 y 25 cuando se mudaron, y tuvieron casa propia 3 años despues"

nros = re.findall("\d+",frase)

print(nros)

#Ejercicio 7

def es_capital(texto):
    resultado = re.search("^[A-Z][a-z]+$",texto)
    return (bool(resultado))

palabra = input("Ingrese una palabra: ")
listapalabras = []

while (palabra != "s"):

    
    palabra = input("Ingrese una palabra: ")
    
    if (es_capital(palabra) == True):
        listapalabras.append(palabra)
            
    else:
        break
    
nombresarch = open("nombres.txt","w")

with nombresarch: 
    for elemento in listapalabras:
        
        nombresarch.write(elemento + "\n")


#Ejercicio 8    ¿¿¿¿FINDALL O SEARCH???? 

frase = input("Ingrese una frase: ")

solopalabras = re.findall("[^\d]*",frase) #Pido que tome todo, menos numeros. Si considera los caracteres
                                          #Imprime todo como una lista, pero sin los digitos del 0 al 9
print(solopalabras)

#Ejercicio 9

mails = open("utnba.txt","r",encoding = "utf8")

with mails:
    for linea in mails:
        
        reglamails1 = "([a-zA-z]{3,15}\@cedi.frba.utn.edu.ar)"
        reglamails2 = "([a-zA-z]{3,15}\@frba.utn.edu.ar)"
        
        if (re.search(reglamails1,linea)):
    
            print(linea)
        
        if (re.search(reglamails2,linea)):
            
            print(linea)

#Ejercicio 10

borges = open("borges.txt","r")
with borges:
    
    contenido = borges.read()
    
    links = re.findall("<https?://\S+",contenido)

linksborges = open("borgeslinks.txt","w")

with linksborges:
    
    for linea in links:
        
        linksborges.write(linea + "\n")

#Ejercicio 11
            
mails = open("emails.txt","r")

with mails:
    
    x = 0
    y = 0
    z = 0
    w = 0
    v = 0
    h = 0
    for elemento in mails:
        
        # for i in elemento:
            
        if (re.search("\@gmail",elemento)):
            x = x + 1
                
        if (re.search("\@uolsinectis",elemento)):
            y = y + 1
            
        if (re.search("\@hotmail",elemento)):
            z = z + 1 
            
        if (re.search("\@univision",elemento)):
            w = w + 1 
         
        if (re.search("\@altavista",elemento)):
            v = v + 1
      
        if (re.search("\@utn",elemento)):
            h = h + 1
            
            
print("El servidor de gmail se usa", x ,"veces")
print("El servidor de uolsinectis se usa", y ,"veces")
print("El servidor de hotmail se usa", z ,"veces")
print("El servidor de univision se usa", w ,"veces")
print("El servidor de altavista se usa", v ,"veces")
print("El servidor de utn se usa", h ,"veces")           