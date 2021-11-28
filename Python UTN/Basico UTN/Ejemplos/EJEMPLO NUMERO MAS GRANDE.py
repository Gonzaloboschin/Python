# MAYOR DE TRES NUMEROS

a = int(input("ingrese numero a = "))
b = int(input("ingrese numero b = "))
c = int(input("ingrese numero c = "))

if(a >= b) and (a >= c):
    maximo = a
else:
    if(b >= a) and (b >= c):
        maximo = b
    else:
        maximo = c
    print("el numero mas grande es ", max(a,b,c))
    
    
        