# Creamos nuestra primer clase en python
# creamos la clase perro

#  usamos la palabra reservada class
# todos los metodos de una clase arrancan con el argumento self

# un metodo sera ladrar, coorer, y un atributo puede ser el nombre, raza, color 

class Perro: 
    def ladrar (self):
        print("Guau")

mascota = Perro()   # defino una variable tipo perro, este es constructor
mascota.ladrar()
    
class Perro:
    def __init__(self,nombreperro):     # init es para iniciar un constructor
        self.nombre = nombreperro      #metodo constructuro, solohay uno 
    
    def ladrar (self):
        print("guau")

    def get_nombre (self):  # los metodos para obtener datos son get
        return self.nombre
miperrito = Perro("sultan")        
print (miperrito.get_nombre())



class Perro:
    # CONSTRUCTOR
    def __init__(self, nombre, edad = 1):
        # Defino los ATRIBUTOS nombre y edad
        self.__nombre = nombre
        self.__edad = edad
        # Obtengo los getters
    def get_nombre (self):
        return self.nombre
    def get_edad(self):
        return self.edad
    # Obtengo los setters 
    def set_nombre (self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    def set_edad (self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
            
    def ladrar (self):
        print("guau guau")


# 
miperro = Perro("coraje",2)
perro_vecinos = Perro ("Batata", 6)
miperro.ladrar()
print(perro_vecinos.get.edad()) 
            
            
            
            
            
            
            
            
            