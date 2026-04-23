import numpy as np
import matplotlib.pyplot as plt


#Leo los datos del fichero de texto
file_in = 'suscep_N128.txt'
datos = np.loadtxt(file_in)


#Introduzco los datos en vectores
T = datos[:, 0]
suscep_media_sup = datos[:, 1]
suscep_media_inf = datos[:, 2]


#Graficamos los resultados
plt.figure(figsize=(7, 7), layout = 'tight')

plt.plot(T, suscep_media_sup, color='red') 
plt.scatter(T, suscep_media_sup, color='red', label = 'Susceptibilidad media mitad superior')

plt.plot(T, suscep_media_inf, color='blue') 
plt.scatter(T, suscep_media_inf, color='blue', label = 'Susceptibilidad media mitad inferior')
 
plt.xlabel('Temperatura') 
plt.ylabel('Susceptibilidad')
plt.legend()                                 
plt.grid()

plt.show()
