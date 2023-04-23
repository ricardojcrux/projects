import numpy as np

def matriz(lista : list):
    matriz = np.array(lista)
    determ = np.linalg.det(matriz)
    return matriz, int(determ)

def inversa(matriz, determ):
    if determ == 0:
        return 'La matriz no tienen inversa'
    else:
        return (np.linalg.inv(matriz)*determ)

valor = [input('Ingrese la lista de elementos, separada por comas: ') for x in range(3)]
lista = [[int(y) for y in x.split(',')] for x in valor]

matriz, determ = matriz(lista)
print('La inversa de la matriz es:')
print(inversa(matriz,determ))
print('La determinante es: ',determ)