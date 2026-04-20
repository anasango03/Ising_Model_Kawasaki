import matplotlib.pyplot as plt
import numpy as np


#Leo los datos del fichero de texto
file_in1 = 'C:/Users/Usuario/Desktop/UGR/COMPU/Kawasaki/resultados/cN_N32.txt'
datos1 = np.loadtxt(file_in1)

file_in2 = 'C:/Users/Usuario/Desktop/UGR/COMPU/Kawasaki/resultados/cN_N64.txt'
datos2 = np.loadtxt(file_in2)

file_in3 = 'C:/Users/Usuario/Desktop/UGR/COMPU/Kawasaki/resultados/cN_N128.txt'
datos3 = np.loadtxt(file_in3)


#Introduzco los datos en vectores
T = datos1[:, 0]
N32 = datos1[:, 1]
N64 = datos2[:, 1]
N128 = datos3[:, 1]


#Creo la figura 
fig = plt.figure(figsize=(10, 10))


#Gráfica grande
ax1 = fig.add_subplot(2, 1, 2)
ax1.plot(T, N32, 'ro-', label='N=32')
ax1.plot(T, N64, 'bo-', label='N=64')
ax1.plot(T, N128, 'go-', label='N=128')
ax1.set_xlabel('Temperatura')
ax1.set_ylabel('Energía')
ax1.grid(True)
ax1.legend()


#Posición y tamaño para las tres gráficas pequeñas
left, bottom, width, height = 0.1, 0.55, 0.22, 0.25

#Primera gráfica pequeña
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(T, N32, 'ro-', label='N=32')  # Ejemplo de datos
ax2.grid(True)
ax2.legend()

#Segunda gráfica pequeña
ax3 = fig.add_axes([left + width + 0.1, bottom, width, height])
ax3.plot(T, N64, 'bo-', label='N=64')  
ax3.grid(True)
ax3.legend()

#Tercera gráfica pequeña
ax4 = fig.add_axes([left + 2 * (width + 0.1), bottom, width, height])
ax4.plot(T, N128, 'go-', label='N=128') 
ax4.grid(True)
ax4.legend()


#Muestro la figura
plt.subplots_adjust(top=0.95, bottom=0.1, hspace=0.4)
plt.show()