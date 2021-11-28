#Ejercicio 1 TEÓRICO

#a = input( ̈Ingrese un numero:”)
#b = input(’Ingrese otro numero:”)
#if (b - a = 0):
#print(’a y b son distintos’)

#El código tiene dos errores principales, que son pedir 2 datos numéricos siendo que no estan especificadas 
#ambas variables (a y b) como INT, ya que el input devolverá un dato STR. Además no respeta la comilla doble
#por lo que tampoco podrá emitir el mensaje de lo que se quiere pedir al usuario.
#La segunda observación del código es que si b - a = 0, va a imprimir (tampoco ya que no respete la doble comilla)
#un texto que dice que a y b son distintos, lo cual no es correcto ya que dos números diferentes que se restan dan cero
#Finalmente, el bloque debajo del IF no esta TABULADO (le falta el TAB). 

#MI CORRECCIÓN DEL CÓDIGO SERÍA: 

#a = int(input("Ingrese un numero: "))
#b = int(input("Ingrese otro numero: "))

#if  (b - a != 0):
#   print("a y b son distintos)

#else: #condición opuesta, en el caso de que la resta si sea cero
#   print("a y b son iguales")

#Ejercicio 2 TEÓRICO

#¿Que imprimira en pantalla el siguiente codigo?
#n = 5
#m = 1
#o = 8
#if ((n != m) and (o > m)) or (m == 1):
#if (n + m == o + 2):
#   print(”)
#else:
#   print(”listo”)
#   print(”tal vez”)

#El código no imprime nada en pantalla, ya que cumple el primer IF, entonces
#se dirigue a la primera respuesta en caso de cumplir que es PRINT("")
#el cual no posee ningun tipo de texto de retroalimentación.

#Ejercicio 3

m = input("ingrese su mes de nacimiento: ") #m de mes 
d = int(input("ingrese su dí­a de nacimiento: ")) #d de día

#pude solucionar este ejercicio con 3 paréntesis al inicioy final de cada IF

if  (d <= 0 or d >= 32):
    print("el dato ingresado no es válido")
    
else: 
    
#Acuario--------------------------------------------
    if  (((m == "enero") and (d >= 21)) or ((m == "febrero") and (d <= 18))):
        print("su signo zodiacal es ACUARIO")

#Piscis--------------------------------------------
    if  (((m == "febrero") and (d >= 19)) or ((m == "marzo") and (d <= 20))): 
        print("su signo zodiacal es PISCIS")  

#Aries------------------------------------------
    if  (((m == "marzo") and (d >= 21)) or ((m == "abril") and (d <= 20))): 
        print("su signo zodiacal es ARIES")
        
#Tauro------------------------------------------    
    if  (((m == "abril") and (d >= 21)) or ((m == "mayo") and (d <= 20))): 
        print("su signo zodiacal es TAURO")

#Géminis----------------------------------------         
    if  (((m == "mayo") and (d >= 21)) or ((m == "junio") and (d <= 21))): 
        print("su signo zodiacal es GÉMINIS")

#Cáncer------------------------------------------
    if  (((m == "junio") and (d >= 22)) or ((m == "julio") and (d <= 22))): 
        print("su signo zodiacal es CÁNCER")

#Leo-------------------------------------------
    if  (((m == "julio") and (d >= 23)) or ((m == "agosto") and (d <= 22))): 
        print("su signo zodiacal es LEO")
        
#Virgo-------------------------------------------
    if  (((m == "agosto") and (d >= 23)) or ((m == "septiembre") and (d <= 22))): 
        print("su signo zodiacal es VIRGO")

#Libra-------------------------------------------
    if  (((m == "septiembre") and (d >= 23)) or ((m == "octubre") and (d <= 22))): 
        print("su signo zodiacal es LIBRA")

#Escorpio-------------------------------------------
    if  (((m == "octubre") and (d >= 23)) or ((m == "noviembre") and (d <= 22))): 
        print("su signo zodiacal es ESCORPIO")
    
#Sagitario----------------------------------------
    if  (((m == "noviembre") and (d >= 23)) or ((m == "diciembre") and (d <= 21))): 
        print("su signo zodiacal es SAGITARIO")

#Capricornio--------------------------------------------
    if  (((m == "diciembre") and (d >= 22)) or ((m == "enero") and (d <= 20))): 
        print("su signo zodiacal es CAPRICORNIO")

#Ejercicio 4

#Este ejercicio tiene 24 combinaciones posibles, lo cual lo supe mediante la 
#cantidad de permutaciones posibles que permite el ejercicio con el elemento n!
#de las cuales, cada número tiene 6 permutaciones posibles, lo que da 6*4=24

print("se le pedirán 4 números enteros, para ordenarlos decreciente")

n1 = int(input("ingrese el primer número entero: "))
n2 = int(input("ingrese el segundo número entero: "))
n3 = int(input("ingrese el tercer número entero: "))
n4 = int(input("ingrese el cuarto número entero: "))

#combinaciones con n1 como más chico de todos
    
if (n1 < n2 < n3 < n4):
    print(n4, n3, n2, n1)
    
if (n1 < n2 < n4 < n3):
    print(n3, n4, n2, n1)
    
if (n1 < n3 < n2 < n4):
    print(n4, n2, n3, n1)

if (n1 < n3 < n4 < n2):
    print(n2, n4, n3, n1)    
    
if (n1 < n4 < n3 < n2):
    print(n2, n3, n4, n1)    
    
if (n1 < n4 < n2 < n3):
    print(n3, n2, n4, n1)     
    
#combinaciones con n2 como más chico de todos
    
if (n2 < n1 < n3 < n4):
    print(n4, n3, n1, n2)
    
if (n2 < n1 < n4 < n3):
    print(n3, n4, n1, n2)
    
if (n2 < n3 < n1 < n4):
    print(n4, n1, n3, n2)

if (n2 < n3 < n4 < n1):
    print(n1, n4, n3, n2)    
    
if (n2 < n4 < n3 < n1):
    print(n1, n3 , n4, n2)    
    
if (n2 < n4 < n1 < n3):
    print(n3, n1, n4, n2)      
    
#combinaciones con n3 como más chico de todos
    
if (n3 < n1 < n2 < n4):
    print(n4, n2, n1, n3)
    
if (n3 < n1 < n4 < n2):
    print(n2, n4, n1, n3)
    
if (n3 < n2 < n1 < n4):
    print(n4, n1, n2, n3)

if (n3 < n2 < n4 < n1):
    print(n1, n4, n2, n3)    
    
if (n3 < n4 < n1 < n2):
    print(n2, n1, n4, n3)    
    
if (n3 < n4 < n2 < n1):
    print(n1, n2, n4, n3)         

#combinaciones con n4 como más chico de todos
    
if (n4 < n1 < n2 < n3):
    print(n3, n2, n1, n4)
    
if (n4 < n1 < n3 < n2):
    print(n2, n3, n1, n4)
    
if (n4 < n2 < n1 < n3):
    print(n3, n1, n2, n4)

if (n4 < n2 < n3 < n1):
    print(n1, n3, n2, n4)        
    
if (n4 < n3 < n1 < n2):
    print(n2, n1, n3, n4)    
    
if (n4 < n3 < n2 < n1):
    print(n1, n2, n3, n4)

#Ejercicio 5
    
print("se le pediran tres números enteros, que representarán la longitud de los lados de un triángulo")

n1 = int(input("ingrese la longitud del primer lado: "))
n2 = int(input("ingrese la longitud del segundo lado: "))
n3 = int(input("ingrese la longitud del tercer lado: "))

if  (n1 == n2 == n3):
   print("el triángulo es equilátero")

if ((n1 == n2 != n3) or (n1 == n3 != n2) or (n2 == n3 != n1)):
   print("el triángulo es isóceles")

else:
    if  (n1 != n2 != n3):
        print("el triángulo es escaleno")

#Ejercicio 6       

a = int(input("ingrese la edad de su mascota: "))

print("teniendo en cuenta que los primeros 2 años equivalen a 10,5 años humanos, entonces..")

if  (a >= 1 or a <= 2):
    print("la edad de su mascota, en años de humano, es: ", a*10.5)
    
if  (a > 2):
    print("luego de los 2 años, cada año equivale a 4 años de un humano")
    print("la edad de su mascota, equivalente en años de humano, es: ", 2*10.5 + 4*a)
    
#CREO HABER COMPRENDIDO QUE DESPUES DE LOS 2 AÑOS, LOS 10,5 SE CONSERVAN   
    
#Ejercicio 7
    
l = input("ingrese una letra cualquiera: ")

#Las VOCALES son las letras a, e, i, o y u
#Las CONSONANTES son las demás letras del abecedario

if  ((l == "a") or (l == "e") or (l == "i") or (l == "o") or (l == "u")):
    print("la letra ingresada es una VOCAL")

#este código discrimina entre una a y una A, lo cual decidí no solucionar por creer que es un tema futuro    
#podría haber hecho 5 IF, pero era innecesario un código tan largo

else: 
    print("la letra ingresada es una CONSONANTE")