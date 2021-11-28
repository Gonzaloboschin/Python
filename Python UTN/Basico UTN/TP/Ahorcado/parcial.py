lista = ["4.76", "9.12", "3.12", "6.44", "5.82", "3.41", "7.21"]
n = 0
for i in lista:
    i = float(i)
    n = n + i 
print("el resultado de la suma es: ", n)




# EJERCICIO 2

palabras = []
palabra = ""
frase = ""   

while (frase != "s"):
    contador = 0
    frase = input("Ingrese una frase: ")
    frase = frase + " "
    for i in frase:
        if i != " ":
            palabra = palabra + i
        else:
            palabras.append(palabra)
            palabra = ""
    for i in palabras:
        for j in i:
            if j != "d":
                break
            else:
                contador = contador + 1
                break
    print("La cantidad de palabras que empiezan con d son:",contador)
    print()
    palabras = []
            
print("Muchas gracias!")


# EJERCICIO 3



lista1 = [2,5,4,7]
lista2 = [4,4,9,4,7,58,2.58]
lista3 = [6,7,4,7]

def calcular_promedio(lista):
    n = 0 
    for i in lista:
        n = n + i
    promedio = n/len(lista)
    return promedio

print("El promedio de la lista es: ", calcular_promedio(lista1))
print("El promedio de la lista es: ", calcular_promedio(lista2))
print("El promedio de la lista es: ", calcular_promedio(lista3))


# EJERCICIO 4
import re

def validad_email(email):
    # email= input("A continuacion ingrese su email: ")
    regla = "[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}"
    re.fullmatch(regla,email)
    if re.fullmatch(regla,email):
            return " - MAIL INGRESADO CON EXITO - "
    else:
            return " - MAIL INCORRECTO - "
            
print(validad_email(input("Ingrese su email: ")))


# EJERCICIO 5 


numeros = ["5","2","8","12","1","4"]
datos= open("datos.txt","w")
with datos:
    for i in numeros:
        datos.write(i + "\n")
        
    
data = open("datos.txt","r")
with data:
        i = 0
        for l in data:
            l = int(l)
            i = i + l
        print("La suma de los valores de la lista es: ",i)
        
        

# EJERCICIO 6

 # Crear la clase Ciudad, con los siguientes atributos nombre,
 # es_capital, cantidad_habitantes, lengua, zona_horaria. 
 # Crear su constructor, sus métodos get y set. De métodos
 # interesantes, crear un método to_str que devuelva un 
 # solo str con toda la información del objeto ciudad. 
 # De un ejemplo de uso. *
        
class Ciudad:
     
    def __init__(self, nombre, es_capital, cantidad_habitantes, lengua, zona_horaria ):
        
        self.__nombre = nombre
        self.__es_capital = es_capital
        self.__cantidad_habitantes = cantidad_habitantes
        self.__lengua = lengua
        self.__zona_horaria = zona_horaria
            
    def get_nombre (self):
        return self.__nombre 
    def get_es_capital (self):
        return self.__es_capital
    def get_cantidad_habitantes (self):
        return self.__cantidad_habitantes
    def get_lengua (self):
        return self.__lengua
    def get_zona_horaria(self):
        return self.__zona_horaria
    
    
    def set_nombre (self, nuevo_nombre):
        self.__nombre = nuevo_nombre 
    def set_es_capital (self, nuevo_es_capital):
        self.__es_capital = nuevo_es_capital 
    def set_cantidad_habitantes (self, nuevo_cantidad_habitantes):
        self.__cantidad_habitantes = nuevo_cantidad_habitantes 
    def set_lengua (self, nuevo_lengua):
        self.__lengua = nuevo_lengua 
    def set_zona_horaria (self, nuevo_zona_horaria):
        self.__zona_horaria = nuevo_zona_horaria

    
    def to_str (self):
        city_data = "DATOS DE CIUDAD: " "\n"\
        + " - NOMBRE: " + self.__nombre + "\n"\
        + " - Es capital?: " + self.__es_capital + "\n"\
        + " - Cantidad de habitantes: " + self.__cantidad_habitantes + "\n"\
        + " - Lengua: "+ self.__lengua + "\n"\
        + " - Zona horaria: " + self.__zona_horaria 
        return city_data
    
    
ciudad1 = Ciudad("Cordoba", "Si", "250000", "Castellano", "UTC-3")
ciudad2 = Ciudad("Mendoza", "Si", "450250", "castellano", "UTC-3")
ciudad3 = Ciudad("Bordeux", "No", "258000", "Frances", "UTC-6")

print(ciudad1.to_str())
print(ciudad2.to_str())
print(ciudad3.to_str())



#  EJERCICIO 7

# 7. Crear una variable de diccionario y llenarla con algunos datos inventados 
# por usted. Describa cómo se puede acceder a un valor de una clave? Describa 
# como puedo utilizar los bucles for para recorrer un diccionario, todos los
#  modos que usted conoce. ¿Para qué le parece que sirve un diccionario? Cómo 
#  obtengo sus valores? Y sus claves? *

vehiculos = [
{"Tipo": "Auto","Color": "Rojo" ,"Kilometros": 35700},
{"Tipo": "Camioneta","Color": "Blanco","Kilometros": 58210},
{"Tipo": "Auto", "Color": "Blanco","Kilometros": 23804},
{"Tipo": "Auto", "Color": "Gris","Kilometros": 72500},
{"Tipo": "Auto", "Color": "Blanco", "Kilometros": 12500}]

autosrojos = 0
autosblancos = 0
autosgrises = 0

for i in vehiculos:
    autosrojos
    
for i in vehiculos:
    if i["Color"] == "Rojo":
        autosrojos  += 1
    if i["Color"] == "Blanco":
        autosblancos  += 1
    if i["Color"] == "Gris":
        autosgrises  += 1
        
print("Hay ", autosrojos, "autos rojos")
print("")
print("Hay ", autosblancos, "autos blancos")
print("")
print("Hay ", autosgrises, "autos grises")


# EJERCCIO 8

# 8. Generar una lista de números pares del 2 al 42, utilizando 
# listas por comprensión. Mostrar en pantalla el resultado.

numeros = [n for n in range(2,42) if n % 2 == 0]
print("Los numeros son: ")
print("")
print(numeros)


