import numpy as np 
import sympy as sym
import matplotlib.pyplot as plt

xi=[-1,0,4,5]
fi=[3,-7,7,11]

xi = np.array(xi)
fi= np.array(fi)
B=np.copy(fi)

#Procedimiento
n = len(xi)
D=np.zeros((n,n), dtype=float)
ultima=n-1
i=0

for i in range(0,n,1):
    for j in range(0,n,1):
        potencia=ultima-j
        D[i,j]= xi[i]**potencia

#coeficientes
coeficientes=np.linalg.solve(D,B)

#polinomio interpolacion
x=sym.Symbol('x')
polinomio=0
for i in range(0,n,1):
    potencia=(n-1)-i
    termino=coeficientes[i]*(x**potencia)
    polinomio=polinomio+termino

px=sym.lambdify(x,polinomio) 
#evaluar polinomio
muestras=51
a=np.min(xi)
b=np.max(xi)
pxi=np.linspace(a,b,muestras)
pfi=px(pxi)

#salida
print('MAtriz vandermonde')
print(D)
print('Coeficientes: ')
print(coeficientes)
print('polinomio: ',polinomio)

#Grafica
plt.plot(xi,fi,'o',label='puntos')
plt.plot(pxi,pfi,label='polinomio')
plt.show()
