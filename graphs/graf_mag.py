import numpy as np
import matplotlib.pyplot as plt


#Leo los datos del fichero de texto
file_in = 'mag_N128.txt'
datos = np.loadtxt(file_in)


#Introduzco los datos en vectores
T = datos[:, 0]
mag_media_sup = datos[:, 1]
mag_media_inf = datos[:, 2]
mag_media = mag_media_sup + mag_media_inf


#Graficamos los resultados
plt.figure(figsize=(7, 7), layout = 'tight')

plt.plot(T, mag_media_sup, color='red') 
plt.scatter(T, mag_media_sup, color='red', label = 'Magnetización media mitad superior')

plt.plot(T, mag_media_inf, color='blue') 
plt.scatter(T, mag_media_inf, color='blue', label = 'Magnetización media mitad inferior')

plt.plot(T, mag_media, color='green') 
plt.scatter(T, mag_media, color='green', label = 'Magnetización media total')
 
plt.xlabel('Temperatura') 
plt.ylabel('Magnetización')
plt.legend(prop={'size': 15})                                 
plt.grid()

plt.show()
