import numpy as np
import matplotlib.pyplot as plt


#Leo los datos del fichero de texto
file_in = 'C:/Users/Usuario/Desktop/UGR/COMPU/Kawasaki/resultados/cN_N32_noNul.txt'
datos = np.loadtxt(file_in)


#Introduzco los datos en vectores
T = datos[:, 0]
calor_especifico = datos[:, 1]


#Graficamos los resultados
plt.figure(figsize=(7, 7), layout = 'tight')

plt.plot(T, calor_especifico) 
plt.scatter(T, calor_especifico, label = 'Calor específico')

plt.xlabel('Temperatura') 
plt.ylabel('Calor Específico')
plt.legend()   
plt.grid()                              

plt.show()

