numero = int(input("introduce un numero "))
 
resultado={}
for i in range(1,numero+1):
	resultado[i]=(i*(i+1)/2)
 
for i in resultado:
	print(int(resultado[i])) 