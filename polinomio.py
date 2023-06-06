from sympy import symbols, Poly, lambdify
from matplotlib import pyplot as plt
import numpy as np

print('Bienvenido a la calculadora de polinomios')
grado = [x for x in reversed(range(int(input('De que grado será el polinomio: '))+1))]
coeficientes = [int(input(f'Ingrese el coeficiente {i}: ')) for i in grado]
rango = sorted([int(input(f'Ingrese el rango {i}: ')) for i in ['inicial','final']])
x_list = np.linspace(rango[0],rango[1],100)

x = symbols('x')
polinomio = Poly(coeficientes, x)
derivada = polinomio.diff(x)
p_lambda = lambdify(x,polinomio.as_expr())
d_lambda = lambdify(x,derivada.as_expr())

plt.plot(x_list,p_lambda(x_list),label='Función')
plt.plot(x_list,d_lambda(x_list),label='Derivada')
plt.title(f'Gráfico de: {polinomio.as_expr()}')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()