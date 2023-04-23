import numpy as np 

ldl=[[1,2,-1],[-1,1,2],[2,-1,1]]
matriz= np.array(ldl)

print(matriz)

#Investigar metodos de sistemas de ecuaciones
#Tambien investigar inversa, traspuesta y determinante de una ecuación
det = int(np.linalg.det(matriz))
print(np.linalg.inv(matriz)*det)
print(det)