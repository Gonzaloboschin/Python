#Trabajo Practico 1

import math

#Ejercicio 1

x = math.sqrt(458)  #la variable x va a almacenar el resultado de la raíz cuadrada de 458

print("el resultado de la raíz cuadrada de x es: ")
print(x)

print("el resultado de la raíz cuadrada de x, trucado, es: ")
print(math.trunc(x)) #también se puede truncar con la doble barra '//'
print(x//1) #divido por 1 ya que me daría como resultado el mismo número


#Ejercicio 2

#a

print((3+8)*(2-26))

#b

print(34**3)

#c

print(int((2*(10-2)/-(8-12)))) #use el 'int' para que no sea un resultado con decimales

#d

x = math.sqrt(9)

print(int(3*x)) 
print(3*math.sqrt(9)) #es posible realizar el calculo dentro del 'print' sin definir antes la raíz

#e (sumatoria desde i=1 hasta i=10, el término es 'i')

print(1 + 2 + 3 + 4 + 5 + 6 + 7+ 8 + 9 + 10)
 
#f (productoria desde j=2 hasta j=8, el término es 'j+1')

print((2 + 1)*(3 + 1)*(4 + 1)*(5 + 1)*(6 + 1)*(7 + 1)*(8 + 1))

#g (suma de fracciones)

print("el resultado decimal es: ")
print(1/2 + 2/3 + 3/4 + 4/5)

print("el resultado truncado es: ")
print(math.trunc(1/2 + 2/3 + 3/4 + 4/5))

#h (está ecuación corresponde a una de las raíces de una cuadrática)

x = math.sqrt(8**2 - 4*3*2) #es más comodo almacenar el resultado de la raíz y utilizar la variable luego

print((-8 + x)/(2*3))

#Ejercicio 3 

tf = input("ingrese la temperatura en Fahrenheit: ")
tf = int(tf) #otra forma de hacer y simplificar este paso es hacer un 'int(input("ACÁ INGRESAR TEXTO"))'

print("la temperatura equivalente en Celsius es: ")
print((5/9)*(tf - 32))
         
#Ejercicio 4 

unidad = int(input("ingrese la medición en pulgadas: "))

print("su medición equivalente en metros son: ")
print(unidad*0.0254)

#Ejercicio 5

nombre = input("ingrese su nombre: ")
print("hola")
print(nombre)

#Ejercicio 6

n = int(input("ingrese un número: "))

if  (n % 2 == 0 ): #el resto de un la división de un número par es cero
    print("el número es par")   

else: 
    print("el número es impar")   

#Ejercicio 7 

n = int(input("ingrese un número entre 1 y 10: "))

if  (n >= 5 and n < 10):
    print("el número ingresado es mayor a 5 y menor que 10")

if (n < 5):
    print("el número ingresado es menor a 5")
    
#Ejercicio 8

n1 = int(input("ingrese un número real: "))

if (n1 > 0):
    print("+1")

else:
    print("-1")
    
#Ejercicio 9
    
n2 = int(input("ingrese un número real: "))

if (n2 > 0):       
    print("+1")

if (n2 < 0): #no use un else, porque abarco otra condición, que no es la opuesta a la inicial
    print("0")
    
 #Ejercicio 10
    
n3 = int(input("ingrese un número entero: "))
n4 = int(input("ingrese un número otro entero: "))
    
if (n3 == n4):
    print("1")

else:
    print("0")
    
#Ejercicio 11
    
n5 = int(input("ingrese un número entero: "))
n6 = int(input("ingrese un número otro entero: "))
    
if (n5 == n6):
    print("true")

else:
    print("false")
    
#Ejercicio 12
    
n7 = input("ingrese una palabra: ")
n8 = input("ingrese otra palabra: ")
    
if (n7 == n8):
    print("true")

else:
    print("false")
    
#Ejercicio 13
    
n = input("ingrese una palabra: ")
n1 = input("ingrese otra palabra: ")

print(n + n1)

#Ejercicio 14 (contraseña sólo numérica)
 
n3 = int(input("ingrese la contraseña: "))
    
if (n3 == 2020):
    print("contraseña correcta")

else:
    print("contraseña incorrecta")

#Ejercicio 14 (contraseña con letras)
    
n3 = str(input("ingrese la contraseña: "))
n3 = str("python2020")
    
if (n3 == "python2020"):
    print("contraseña correcta")

else:
    print("contraseña incorrecta")

#Ejercicio 15
    
print("se le pedirán 3 números enteros, para ordenarlos de menor a mayor")

n1 = int(input("ingrese el primer número entero: "))
n2 = int(input("ingrese el segundo número entero: "))
n3 = int(input("ingrese el tercer número entero: "))
    
if (n1 < n2 < n3):
    print(n1, n2, n3)
    
if (n1 < n3 < n2):
    print(n1, n3, n2)
    
if (n2 < n1 < n3):
    print(n2, n1, n3)
        
if (n2 < n3 < n1):
    print(n1, n3, n2)
    
if (n3 < n1 < n2):
    print(n3, n1, n2)
        
if (n3 < n2 < n1):
    print(n3, n2, n1)
    
#Ejercicio 16

print("conversión de pesos a dólares")

n1 = int(input("ingrese el valor del dólar actual: "))
n2 = int(input("ingrese el valor de su cantidad en pesos: "))

print("usted tiene, en dólares, la cantidad de:")
print(n2/n1)

#Ejercicio 17

print("conversión de dólares a pesos")

n1 = int(input("ingrese el valor del dólar actual: "))
n2 = int(input("ingrese el valor de un producto en dólares: "))


print("el precio de producto en pesos es:")
print(n1*n2)


#Ejercicio 18

n = int(input("ingrese la nota del alumno: "))

if  (n < 1 or n > 10):
    print("la nota ingresada no es válida")
        
else:
    if  (n >= 9 and n <= 10):
        print("PROMOCIONA")
    
    if  (n >= 6 and n <= 8):
        print("APROBADO")
    
    if  (n < 6):
        print("DESAPROBADO")

#COMENTARIO: Me hubiese gustado hacer una sentencia que si al ingresar la nota mal, pida volver a intentar y continuar la clasificación