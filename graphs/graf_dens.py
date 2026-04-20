import numpy as np
import matplotlib.pyplot as plt


#Leo los datos del fichero de texto
file_in = 'C:/Users/Usuario/Desktop/UGR/COMPU/Kawasaki/resultados/dens_N64_T4.txt'
datos = np.loadtxt(file_in)


#Introduzco los datos en vectores
x = datos[:, 0]
dens = datos[:, 1]


#Graficamos los resultados
plt.figure(figsize=(7, 7), layout = 'tight')

plt.plot(x, dens) 
plt.scatter(x, dens, label = 'N=64  T=4.0')

plt.xlabel('x') 
plt.ylabel('Densidad de partículas media en la dirección $y$')
plt.legend()                                 
plt.grid()

plt.show()

