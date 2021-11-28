#                                                   Diccionarios

#Ejercicio 1

caminatas = [
        {"dia": "Lunes", "distancia": 7000},
        {"dia": "Martes", "distancia": 4010},
        {"dia": "Miercoles", "distancia": 1500},
        {"dia": "Jueves", "distancia": 6450},
        {"dia": "Viernes", "distancia": 2571},
        {"dia": "Sabado", "distancia": 3000},
        {"dia": "Domingo", "distancia": 5200}]

# Usaré dos contadores, uno para la distancia total, otro para los dias de caminata

sumadist = 0
cantdias = 0

for dist in caminatas: 
    
    cantdias = cantdias + 1           #contador de dias
    
    sumadist = sumadist + dist["distancia"]   #contador de distancia
    
    # for valor in dias.values():
          
print("En total, usted caminó",sumadist ,"metros en",cantdias, "días")

print("Su promedio semanal es: ",sumadist/cantdias ,"metros por día")

#Ejercicio 2

dic = {"hola": 3, "que": 340, "para": 120}

valores = list(dic.values())  #Lista que guarda los valores de cada clave

maximo = max(valores)  #Valor maximo de la lista

minimo = min(valores)  #Valor minimo de la lista

for clave,valor in dic.items():   #Recorro el diccionario
    
    if (dic.get(clave) == maximo): #Si la clave del diccionario es igual a "maximo"
        
        palabramax = clave  #pido la clave (el STR o palabra que mas se repite)
    
    if (dic.get(clave) == minimo):
        
        palabramin = clave
        
print("La clave con menos ocurrencias es: ",palabramin)
print("La clave con más ocurrencias es: ",palabramax)

    
#Ejercicio 3 

empleados = {
"empleado01": {"nombre": "Juan", "salario": 7500},
"empleado02": {"nombre": "Pedrito", "salario": 6320},
"empleado03": {"nombre": "Ema", "salario": 7200},
"empleado04": {"nombre": "Lucila", "salario": 8500}
}

for empleado in empleados:
    
    if empleado == "empleado02" in empleados:
        
        emp2 = empleados.get("empleado02")
                
        emp2["salario"] = emp2["salario"] + 2180
        
print("El nuevo salario de Pedrito es: ",emp2["salario"])


print(empleados) #Con esto verifico que el valor se cambió en el diccionario

#Ejercicio 4 

apariciones = {}   #diccionario vacío para guardar los datos

frase = input("Ingrese una frase: ")

lista = (frase.lower()).split()

for palabra in lista:
    
    contador = apariciones.get(palabra,0)
    
    apariciones[palabra] = contador + 1

for palabra in apariciones:
    
    print(palabra, apariciones[palabra])

#Ejercicio 5

mazocartas = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8,
              "9" : 9, "10" : 10, "As" : 11, "Zota" : 12, "Reina" : 13, "Rey" : 14}

suma = 0

for cartita in range(6): 
    
    carta = input("Ingrese una carta: ")
    
    suma = suma + mazocartas[carta]
    
print("el promedio de cartas es: ",suma/6)

#Ejercicio 6

posibles_citas = [{"nombre": "Julia", "sexo": "femenino", "edad": 29,

"hobbies": ["correr", "musica", "leer"], "ciudad": "Cordoba"},
{"nombre": "Camila", "sexo": "femenino", "edad": 18,
"hobbies": ["escribir", "arte"], "ciudad": "Mendoza"},
{"nombre": "Lucia", "sexo": "femenino", "edad": 35,
"hobbies": ["arte"], "ciudad": "Mendoza"},
{"nombre": "Daniel", "sexo": "masculino", "edad": 50,
"hobbies": ["boxeo", "leer", "arte"], "ciudad": "Mendoza"},
{"nombre": "Pepe", "sexo": "masculino", "edad": 32,
"hobbies": ["correr", "leer"], "ciudad": "Cordoba"},
{"nombre": "Juan", "sexo": "masculino", "edad": 41,
"hobbies": ["leer", "alpinismo", "juegos de mesa"],
"ciudad": "Cordoba"}]

citas = ""

for cita in posibles_citas:
    
    requisito = True
    
    if (cita["edad"] <= 30):
        requisito = False
        
    if (cita["sexo"] != "femenino"):
        requisito = False
        
    if (cita["ciudad"] != "Mendoza"):
        requisito = False
        
    if (cita["hobbies"] == "arte"):
        requisito = True
    
    if (requisito == True):
        citas = citas + cita["nombre"]
        
print("La posible cita para Wally es: ",citas)

