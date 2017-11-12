#se hace uso de def para definir una funcion
def ex():
    print("Esto es una funcion")
ex()

#funciones con un unico parametro
def single(a):
    print(a)

single(9)

#funcion con multiples parametros
def mult(a,b,c):
    d=a*b
    print(d+c)
mult(2,3,4)

#funciones que llaman otras funciones
def giver(a,b):
    c=a+b
    return c

def taker(d,e):
    output=giver(d,e)
    return output
print(taker(1,5))



#ejemplo:
def first():
    print("this is a function with multiple functions")

def intFun(intVal):
    return intVal*2

def takesTwo(int1, int2):
    return int1*int2

def functionInside(a,b,c):
    print(takesTwo(intFun(a),b)*c)

first()
functionInside(7,4,2)