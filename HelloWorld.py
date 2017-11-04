
print("hello world")
#Integer
intVal=5
#Float
floatVal=5.5
#potenica
powVal=3**3
#Divición
flowDiv1=16//3
flowDiv2=16//6
#Booleanos
boolVal=True
#Modular
modulo1=4%3

#Assigment Operators
addAssigment=3
addAssigment+=5 #addAssigment=8 concatenacion de numeros
#subAssing
subAssing=10
subAssing-=5 #subAssing=5
#multAssing
multAssing=10
multAssing*=5 #multAssing=50
#divAssing
divAssing=10
divAssing /=5 #divAssing=2.0

#Order of Operations
'''
Original: (9-7)*2**3+10%6//-1*2-1
step1:2*2**3+10%6//-1*2-1
step2:2*8+10%6//-1*2-1
step3:16+-8-1
step:7
'''

print(boolVal)
boolVal=False
print(intVal)
print(floatVal)
print(boolVal)
print("Potencia de 3 ^3=",powVal)
print("Divicion de 16,6 =",flowDiv2)
print("Modulo 4%3=",modulo1)
print("Concatenacion de numero",addAssigment)

#Escape Sequence
str1="The book\"A Feast for Crows\"was Written by george R.R Martin"
print(str1)

#Accessing by index
str="Example"
ex1=str[0]#assing the variable ex1 "e"
ex2="tape"[2]#assings variable ex2 "p"
print("Accessing by index",ex1)

#Slicing A string
example="apples"
ex3=example[:3]#assign the string "app" to the variable ex3
ex4=example[2:5]#assign the string "ple" to the variable ex4
ex5=example[3:]#assign the string "les" to the variable ex5

ex6="apples"[:3]#asssign the string "app" to the variable ex6
ex7="apples"[2:5]#assign the string "ple" to the variable ex7
ex8="apples"[3:]#assign the string "les" to the variable ex8

#Sentencia-If
z=1
if(z>5): print("z es mayor que 5")
print("fin")
#if y else
if(z!=10):
    print( "la variable es diferente de 10")
else:
    print ("la variables es igual a 10!")
print ("fin")

#For

#Recorrer cadena de texto
for letra in 'Hola':
    print('Estamos en la letra: ',letra)


#Interaciones con For
autos = ['mercedez','BMW','Toyota']
for indice in range(len(autos)): #range define un rango que es el tamaño de la lista
     print ('El auto es un ',autos[indice])

    #la equivalencia sin usar indice seria:
autos=['mercedez','BMW','Toyota']
for auto in autos:
        print("el auto es un",auto)

#Funcion  INPUT()
print("¿Como te llamas?")
nombre=input()
print("Me alegro de conocerte",nombre)

#Conversion de tipos:
cantidad =int(input("Cual es la cantidad en pesetas:"))
print(cantidad,"pesetas son",cantidad/166.386,"euros")

cantidad = float(input("Dígame una cantidad en euros (hasta con 2 decimales): "))
print(cantidad, "euros son", cantidad * 166.386, "pesetas")

#http://www.mclibre.org/consultar/python/lecciones/python-entrada-teclado.html
#http://recursospython.com/guias-y-manuales/colorama-texto-fondo-coloreados-la-consola/
