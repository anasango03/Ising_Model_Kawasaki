import numpy as np
import matplotlib.pyplot as plt


#Leo los datos del fichero de texto
file_in = 'C:/Users/Usuario/Desktop/UGR/COMPU/Kawasaki/resultados/ener_N64_noNul.txt'
datos = np.loadtxt(file_in)


#Introduzco los datos en vectores
T = datos[:, 0]
energia_media = datos[:, 1]


#Graficamos los resultados
plt.figure(figsize=(7, 7), layout = 'tight')

plt.plot(T, energia_media) 
plt.scatter(T, energia_media, label = 'Energía media por partícula')

plt.xlabel('Temperatura') 
plt.ylabel('Energía')
plt.legend()
plt.grid()                                 

plt.show()
