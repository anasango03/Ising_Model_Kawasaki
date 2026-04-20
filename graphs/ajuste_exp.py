import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#Función exponencial de exponente negativo
def exp(x, a, b):
    return a * np.exp(-b * x)


#Leo los fatos del fichero de texto
file_in = 'C:/Users/Usuario/Desktop/UGR/COMPU/Kawasaki/resultados/cN_N128.txt'
datos = np.loadtxt(file_in)
T = datos[:, 0]
cN = datos[:, 1]


#Realizamos el ajuste usando curve_fit
params, covariance = curve_fit(exp, T, cN)

#Extraemos los parámetros ajustados
a_fit, b_fit = params

#Generamos puntos para la curva ajustada
x_fit = np.linspace(0, 5, 100)
y_fit = exp(x_fit, a_fit, b_fit)


#Graficamos los datos originales y la curva del ajuste
plt.scatter(T, cN, label='N=128', color='red')
plt.plot(x_fit, y_fit, label=f'Ajuste: $c_N = {a_fit:.2f} \cdot e^{{-{b_fit:.2f} \cdot T}}$', color='blue')
plt.xlabel('$T$')
plt.ylabel('$c_N(T)$')
plt.legend(prop={'size': 20})
plt.grid()
plt.show()


#Imprimimos por pantalla los parámetros del ajuste
print(f'Parámetros del ajuste: a = {a_fit:.2f}, b = {b_fit:.2f}')
