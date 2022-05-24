#se uso el metodo de newton para obtener la raiz
from math import exp

def f(x):# Función
    return exp(2-x)-7*x

def f2(x):# Derivada: 
    return -exp(2-x)-7

x0=1.5
x1=x0-f(x0)/f2(x0)#primera derivada

print('x1= ', x1)

x2=x1-f(x1)/f2(x1)#segunda derivada
print('x2= ', x2)

x3=x2-f(x2)/f2(x2)#tercera derivada
print('valor =',f(x3))
print('x3= ', x3)
print('La raiz es ',x3)