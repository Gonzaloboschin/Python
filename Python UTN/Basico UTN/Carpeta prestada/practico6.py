#                                 Introducción a Objetos

import math

#Ejercicio 1

class Gato:
    
    #Atributos o propiedades de la clase
    def __init__(self,nombre,color,raza):
        self.__nombre = nombre
        self.__color = color 
        self.__raza = raza
        
    #GET
    def get_nombre (self):
        return self.__nombre
    def get_color (self):
        return self.__color
    def get_raza (self):
        return self.__raza
      
    #SET
    def set_nombre (self, newnombre):
        self.__nombre = newnombre
    def set_color (self, newcolor):
        self.__color = newcolor
    def set_nombre (self, newraza):
        self.__raza = newraza
    
    #Acciones o métodos de la clase Gato
    def mauyar (self):
        print ("Miau miau")
        
    #Para verificar la clase
        
# migato = Gato("Leo","naranja","siames")
        
# migato.mauyar()
# print(migato.get_nombre())
# print(migato.get_raza())
# print(migato.get_color())
        
#Ejercicio 2

class Circulo:
    #Atributos
    def __init__(self,radio,color):
        self.__radio = radio
        self.__color = color 
        
    #GET
    def get_radio (self):
        return self.__radio
    def get_color (self):
        return self.__color
    def get_area (self):
        return math.pi*(self.__radio)**2
    
    #SET
    def set_radio (self, nuevoradio):
        self.__radio = nuevoradio
    def set_color (self, nuevocolor):
        self.__color = nuevocolor
        
    #Para verificar la clase
        
# micirculo = Circulo(5,"rojo")

# print(micirculo.get_radio())
# print(micirculo.get_area())      
# print(micirculo.get_color())   
        
#Ejercicio 3
        
class Rectangulo:
    
    #Atributos o propiedades de la clase
    def __init__(self,ancho,alto,color = "blanco"):
        self.__ancho = ancho
        self.__alto = alto
        self.__color = color 
        
    #GET
    def get_ancho (self):
        return self.__ancho
    def get_alto (self):
        return self.__alto
    def get_color (self):
        return self.__color
    
    #SET
    def set_ancho (self, nuevoancho):
        self.__ancho = nuevoancho
    def set_alto (self,nuevoalto):
        self.__alto = nuevoalto
    def set_color (self, nuevocolor):
        self.__color = nuevocolor
    
    #GET extras
    def get_area (self):
        return self.__ancho*self.__alto
    def get_perimetro (self):
        return 2*(self.__ancho + self.__alto)

rectangulito = Rectangulo(5,6,"azul")
rectangulote = Rectangulo(4.5,6,"negro")
rectangulox = Rectangulo(7,8)

# print(rectangulito.get_area())
# print(rectangulito.get_perimetro())      
# print(rectangulito.get_color())

#Ejercicio 4
        
listarectangulos = []    #lista vacía para cargarle datos

listarectangulos.append(rectangulito)
listarectangulos.append(rectangulote)
listarectangulos.append(rectangulox)

print(listarectangulos)  
#al realizar este PRINT, me devuelve la lista, con los objetos que posee y su ubicación en la memoria RAM
#En otras palabras, este print no muestra los datos de cada rectangulo en la lista, sino en donde encontrarlos. 

#Ejercicio 5

class Cuenta: 
    def __init__ (self,titular,balance,dni,nro_cuenta):
        self.__titular = titular
        self.__balance = balance
        self.__dni = dni
        self.__nro_cuenta = nro_cuenta
    
    #GET
    def get_titular (self):
        return self.__titular
    def get_balance (self):
        return self.__balance
    def get_dni (self):
        return self.__dni
    def get_nro_cuenta (self):
        return self.__nro_cuenta
    
    #SET
    def set_titular (self,nuevotitular):
        self.__titular = nuevotitular
    def set_balance (self,nuevobalance):
        self.__balance = nuevobalance
    def set_dni (self,nuevodni):
        self.__dni = nuevodni
    def set_nro_cuenta (self,nuevonro_cuenta):
        self.__nro_cuenta = nuevonro_cuenta
    
    #GET extras
    def get_depositar (self,deposito):
        balance_deposito = Cuenta.get_balance(self) + float(deposito)
        Cuenta.set_balance(self,balance_deposito)
        return balance_deposito
    def get_retirar (self,retiro):
        balance_retiro = Cuenta.get_balance(self) - float(retiro)
        Cuenta.set_balance(self,balance_retiro)
        return balance_retiro

#Ejercicio 6

class Persona: 
    def __init__ (self,nombre,apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = 0
        self.__tel = 0
        self.__dni = 0
        self.__email = ""
        
    #GET nombre y apellido
    def get_nombre (self):
        return self.__nombre
    def get_apellido (self):
        return self.__apellido
    #SET nombre y apellido
    def set_nombre (self,nuevonombre):
        self.__nombre = nuevonombre
    def set_apellido (self,nuevoapellido):
        self.__apellido = nuevoapellido
        
    #GET y SET para los demás parámetros
    def get_edad (self):
        return self.__edad
    def set_edad (self,nuevaedad):
        if (0 <= nuevaedad) and (nuevaedad <= 110):
            self.__edad = nuevaedad
    
    def get_tel (self):
        return self.__tel
    def set_tel (self,nuevotel):
        self.__tel = nuevotel
    
    def get_dni (self):
        return self.__dni
    def set_dni (self,nuevodni):
        if (0 <= nuevodni <= 15):   #tome este criterio sobre cantidad de cifras de DNI según población
            self.__dni = nuevodni
    
    def get_email (self):
        return self.__email
    def set_email (self,nuevoemail):
        self.__email = nuevoemail       
        
    #GET Extra
        
    def to_str (self):
        cadenastr = " Nombre: " + self.__nombre + "\n"\
        + " Apellido: " + self.__apellido + "\n"\
        + " Edad: " + str(self.__edad) + "\n"\
        + " Teléfono: " + str(self.__tel) + "\n"\
        + " Dni: " + str(self.__dni) + "\n"\
        + " Email: " + self.__email
        return cadenastr
        
# fullname = Persona("Agustin","Vazquez") 
# print(fullname.to_str())
         
#Ejercicio 7

listapersonas = [] 

for persona in range(5):
    nombre = input("Ingrese un nombre: ")
    apellido = input("Ingrese un apellido: ")
    personita = Persona(nombre,apellido)
    edad = int(input("ingrese su edad: "))
    personita.set_edad(edad)
    dni = int(input("Ingrese el DNI: "))
    personita.set_dni(dni)
    
    listapersonas.append(personita)

for pna in listapersonas:
    print(pna.to_str())

#Ejercicio 8
    
class Vehiculo:
    def __init__ (self,tipo,cant_ruedas,marca,color,modelo,patente,dueño):
        self.__tipo = tipo
        self.__cant_ruedas = cant_ruedas
        self.__marca = marca
        self.__color = color
        self.__modelo = modelo
        self.__patente = patente
        self.__dueño = dueño
        self.__velocidad = 0
        
    #GET
    def get_tipo (self):
        return self.__tipo
    def get_cant_ruedas (self):
        return self.__cant_ruedas
    def get_marca (self):
        return self.__marca
    def get_color (self):
        return self.__color
    def get_modelo (self):
        return self.__modelo
    def get_patente (self):
        return self.__patente
    def get_dueño (self):
        return self.__dueño
    
    #SET
    def set_tipo (self,nuevotipo):
        self.__tipo = nuevotipo
    def set_cant_ruedas (self,nuevacant_ruedas):
        self.__cant_ruedas = nuevacant_ruedas
    def set_marca (self,nuevamarca):
        self.__marca = nuevamarca
    def set_color (self, nuevocolor):
        self.__color = nuevocolor
    def set_modelo (self,nuevomodelo):
        self.__modelo = nuevomodelo
    def set_patente (self,nuevapatente):
        self.__patente = nuevapatente
    def set_dueño (self,nuevodueño):
        self.__dueño = nuevodueño
    
    #GET Extras
    def to_str (self):
        vehiculostr = " -Tipo: " + self.__tipo + "\n"\
        + " -Nro de ruedas: " + self.__cant_ruedas + "\n"\
        + " -Marca: " + self.__marca + "\n"\
        + " -Color: " + self.__color + "\n"\
        + " -Modelo: " + self.__modelo + "\n"\
        + " -Patente: " + self.__patente + "\n"\
        + " -Dueño: " + self.__dueño + "\n"\
        + " -Velocidad: " + str(self.__velocidad)
        return vehiculostr
    
    def avanzar (self):
        if (self.__velocidad > 0):
            self.__velocidad += 5
        else:
            self.__velocidad = 10
            
    def retroceder (self):
        self.__velocidad = -5
        
    def frenar (self):
        self.__velocidad = 0
    
# vehiculo1 = Vehiculo("bicicleta","2","Venzo","rojo","2015","","agustin")
# print(vehiculo1.to_str())

# vehiculo1.avanzar()
# print(vehiculo1.to_str())

# vehiculo1.avanzar()
# print(vehiculo1.to_str())

# vehiculo1.avanzar()
# print(vehiculo1.to_str())

# vehiculo1.frenar()
# print(vehiculo1.to_str())
        
        
#Ejercicio 9
        
def quitar_repetidos(lista):     #función auxiliar, en caso de necesitar la lista sin repeticiones
    lista1 = []
    
    for item in lista: 
        if item not in lista1:
            lista1.append(item)
    return lista1
        
#Vehiculos de prueba para realizar el programa

vehiculo1 = Vehiculo("auto","4","Ford","rojo","2015","ABC 123","Agustin")
vehiculo2 = Vehiculo("auto","4","Honda","blanco","2020","ASC 456","Javier")
vehiculo3 = Vehiculo("auto","4","Ferrari","rojo","2012","GFC 128","Gustavo")
vehiculo4 = Vehiculo("moto","4","Ford","naranja","2015","ASE 892","Micaela")
vehiculo5 = Vehiculo("auto","2","Yamaha","negro","2013","DFS 562","Gabriel")

listautos = [vehiculo1,vehiculo2,vehiculo3,vehiculo4,vehiculo5]
marcasautos =  []

for auto in listautos:
    marcasautos.append(auto.get_marca())
# print(marcasautos)

ocurrencias = []
chequeadas = []
   
for m in marcasautos:
    cant = 0
    if m not in chequeadas:
        
        for fav in marcasautos:
            if (m == fav):
                cant = cant + 1
        ocurrencias.append(cant)
        chequeadas.append(m)

marcafav = quitar_repetidos(marcasautos)
# print(ocurrencias)
# print(chequeadas)
# print(marcafav)

maxi = max(ocurrencias)  #Con este comando, calculo el numero maximo o de mayor repetición
for rep in range(len(ocurrencias)):
    
    if (ocurrencias[rep] == maxi):
        
        favorita = marcafav[rep]

print("La lista de marcas de vehiculos de la familia es: ",marcasautos)
print("La marca favorita de la familia es: ",favorita)

    