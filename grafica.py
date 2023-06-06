import matplotlib.pyplot as plt
import numpy as np

a=int(input('Inserte el valor de a: '))
b=int(input('Inserte el valor de b: '))
rang=int(input('Inserte el rango: '))
rango = np.linspace(0,rang+1,100)

y=[]
for i in rango:
	x=a*np.exp(b*i)	
	y.append(x)

name= f'gráfico de f(x) = {a}^({b}x)'
plt.title(name)
plt.plot(rango, y)
plt.grid()
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.show()