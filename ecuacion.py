import numpy as np

def lineal(lista):
	a,b,c,d,e,f = lista
	matriz = np.array([[a,b],[d,e]])
	result = np.array([c,f])
	det = np.linalg.det(matriz)

	if det == 0:
		return 'El sistema no tiene soluciones'
	else:
		y= (d*c - a*f)/(d*b - a*e)
		x= (c - (b*y)) / a
		return x, y

print('Sistemas de ecuaciones 2x2\n\nax+by=c\ndx+ey=f\n')

lista = [int(input(f'Inserte valor n°{i+1}: ')) for i in range(6)]

print(lineal(lista))