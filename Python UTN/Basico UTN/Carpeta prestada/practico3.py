#                                                FUNCIONES

#Ejercicio 1

def signo (a):
    if (a >= 0):
        return 1
    if (a < 0):
        return -1

# x = int(input("ingrese un numero: "))   #ESTAN COMENTADOS, YA QUE LOS USE PARA VERIFICAR LA FUNCION

# print(signo(x))

#Ejercicio 2

def enRango(n,a,b):
    if (a < n < b):
        return True
    else:
        return False

# a = int(input("ingrese un numero: ")) 
# b = int(input("ingrese un numero: "))   #ESTAN COMENTADOS, YA QUE LOS USE PARA VERIFICAR LA FUNCION
# c = int(input("ingrese un numero: "))

# print(enRango(a,b,c))

#Ejercicio 3

def FarenheitTOCelsius (tf):
    return (tf - 32)*5/9

# t = int(input("ingrese la temperatura en fahrenheit: "))

# print(FarenheitTOCelsius(t))            #ESTAN COMENTADOS, YA QUE LOS USE PARA VERIFICAR LA FUNCION

#Ejercicio 4

def suma (a,b):
    return (a + b)**2

# w = int(input("ingrese un numero: "))   #ESTAN COMENTADOS, YA QUE LOS USE PARA VERIFICAR LA FUNCION
# z = int(input("ingrese un numero: "))

# print(suma(w,z))

#Ejercicio 5

def palabrasfrase (frase):
    
    w = 0
    for space in range(len(frase)):
        if (frase[space] == " "): 
            w = w + 1
    
    print("la cantidad de palabras en la frase es de ",w + 1)
    
# frasesita = input("ingrese una frase: ")  #ESTAN COMENTADOS, YA QUE LOS USE PARA VERIFICAR LA FUNCION

# palabrasfrase(frasesita)

#Ejercicio 6

def listaprom (lista):  
    
    return sum(lista) / len(lista)

# listita = [5,2,6,9,11,2,45]
# print(listaprom(listita))

#Ejercicio 7

def frasecarac (frase, caracter):
    
    
    for s in range(len(frase)):
        if  (frase[s] == " "):
            nuevafrase = frase.replace(" ",caracter)
            return nuevafrase
      
# frasesita = input("ingrese una frase: ")
# caracter1 = input("ingrese un caracter: ")

# print(frasecarac(frasesita, caracter1))

#Ejercicio 8 

def HalfTriangle (long,caracter):
    
    i = ""
    for j in range(long):
        i = i + caracter
        print(i)
    return ("")
        
# n = int(input("ingrese una longitud: "))
# c = input("ingrese un caracter: ")

# print(HalfTriangle(n, c))

#Ejercicio 9 

def EliminarRepListas (lista): 
    lista1 = lista.split()     #pense que los elementos los introdujera el usuario y con el split, pasarlo a una lista
    return list(set(lista1))   #el comando lista(set(LISTA QUE USE)) se encarga de eliminar las repeticiones

# lista2 = input("ingrese los elementos que quire introducir a su lista: ")
# print(EliminarRepListas(lista2))

#                                                BUCLE WHILE

#Ejercicio 10 

N = int(input("ingrese un numero: "))
i = 0

while (i <= N): #Inclui al nro ingresado por el usuario, pero podria no haberlo hecho 
    print(i)
    i = i + 1 

#Ejercicio 11
    
nro = int(input("ingrese un numero: "))

i = nro
while (i >= 0):
    print("")               #este print me da un salto por cada fila
    for j in range(i,0,-1):
        print(j, end = "")
    i = i - 1               #cuando i=0, la condición deja de ser cierta, ya que el while se cumple si i>=0

#Ejercicio 12

listanros = []
numero = ""

while (numero != "s"):
    
    numero1 = input("Ingrese un número, o la letra -s- para salir: ")
    if (numero1 != "s"):
        
        nro = int(numero1)
        listanros.append(nro)
    
    else: 
        print("La lista de numeros ingresados es", listanros)
        break

#Ejercicio 13
        
print("Elija una opcion del siguiente menú")
    
print("1. Sumar dos numeros")
print("2. Restar dos numeros") #en valor absoluto SIEMPRE por criterio propio
print("3. Multiplicar dos numeros")
print("4. Dividir dos numeros")
print("5. Salir")

i = 0
while (i < 5):
    
    n = int(input("ingrese una opcion: "))
    
    if (n == 1):
    
        a = int(input("ingrese un numero: ")) 
        b = int(input("ingrese otro numero: ")) 
        
        print("la suma de sus numeros es: ",a + b)
        
    if (n == 2):
        
        a1 = int(input("ingrese un numero: ")) 
        b1 = int(input("ingrese otro numero: ")) 
        
        if (a1 < b1):        #Recurri a este IF para que la resta sea siempre positiva
            print("la resta de sus numeros es: ",b1 - a1)
        
        else:
            print("la resta de sus numeros es: ",a1 - b1)
            
    if (n == 3):
        
        a2 = int(input("ingrese un numero: ")) 
        b2 = int(input("ingrese otro numero: ")) 
        
        print("la multiplicacion de sus numeros es: ",a2 * b2)
        
    if (n == 4):
        
        a3 = int(input("ingrese un numero: ")) 
        b3 = int(input("ingrese otro numero: ")) 
        
        print("la division de sus numeros es: ",a3 / b3)  #Sin redondear, ni truncar, resultado con decimales
        
    if (n == 5):
        
        print("gracias por utilizar el menu")
        break        
        
#                                                VARIADO

#Ejercicio 14 DUDA
            
# def LetrasPar (texto):
#     par = ""
#     n = 0

#     for i in range(len(texto)):
    
#         n = n + 2
        
#         if (i == n):
        
#             par = par + texto[i]
            
#         return par

# textito = input("Ingrese una texto: ")
# print(LetrasPar(textito))     
    
#Ejercicio 15
    
def LongPalabraFrase (frase):
   
    listalongitudes = []

    longpal = 0

    for s in frase:
        
        if (s == " "):
        
            listalongitudes.append(longpal)
            longpal = 0
        else: 
            longpal = longpal + 1    
            if (longpal != 0):       
                listalongitudes.append(longpal)
    
    print("la longitud de la palabra más es de", max(listalongitudes), "letras") 

# frase1 = input("ingrese una frase: ")

# LongPalabraFrase(frase1)
    
#Ejercicio 16
    
def EqualElementosListas (lista1, lista2):
    
    for i in lista1:
    
        for j in lista2:
        
            if (i == j):
             
                return True
        
            else: 
                return False

# lista11 = ["a","b","c","d"]
# lista22 = ["z","w"]

# print(EqualElementosListas(lista11,lista22))







      