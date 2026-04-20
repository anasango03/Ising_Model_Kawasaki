import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec


#Leo los datos de los ficheros de texto
file_in1 = 'C:/Users/Usuario/Desktop/UGR/COMPU/Kawasaki/resultados/dens_N32_T05.txt'
datos1 = np.loadtxt(file_in1)
file_in2 = 'C:/Users/Usuario/Desktop/UGR/COMPU/Kawasaki/resultados/dens_N64_T05.txt'
datos2 = np.loadtxt(file_in2)
file_in3 = 'C:/Users/Usuario/Desktop/UGR/COMPU/Kawasaki/resultados/dens_N128_T05.txt'
datos3 = np.loadtxt(file_in3)
file_in4 = 'C:/Users/Usuario/Desktop/UGR/COMPU/Kawasaki/resultados/dens_N64_T1.txt'
datos4 = np.loadtxt(file_in4)
file_in5 = 'C:/Users/Usuario/Desktop/UGR/COMPU/Kawasaki/resultados/dens_N64_T2.txt'
datos5 = np.loadtxt(file_in5)
file_in6 = 'C:/Users/Usuario/Desktop/UGR/COMPU/Kawasaki/resultados/dens_N64_T3.txt'
datos6 = np.loadtxt(file_in6)
file_in7 = 'C:/Users/Usuario/Desktop/UGR/COMPU/Kawasaki/resultados/dens_N64_T4.txt'
datos7 = np.loadtxt(file_in7)


#Creo la figura
fig = plt.figure(figsize=(10, 15))
gs = GridSpec(5, 2, figure=fig)


#Creo los subplots
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[2, 0])
ax4 = fig.add_subplot(gs[3, 0])
ax5 = fig.add_subplot(gs[4, 0])
ax6 = fig.add_subplot(gs[1, 1])
ax7 = fig.add_subplot(gs[2, 1])
ax8 = fig.add_subplot(gs[3, 1])


#Graficas de la columna izquierda
ax1.plot(datos2[:,0], datos2[:,1])
ax1.set_title('N=64  T=0.5')
ax2.plot(datos4[:,0], datos4[:,1])
ax2.set_title('N=64  T=1.0')
ax3.plot(datos5[:,0], datos5[:,1])
ax3.set_title('N=64  T=2.0')
ax4.plot(datos6[:,0], datos6[:,1])
ax4.set_title('N=64  T=3.0')
ax5.plot(datos7[:,0], datos7[:,1])
ax5.set_title('N=64  T=4.0')

#Graficas de la columna derecha
ax6.plot(datos1[:,0], datos1[:,1])
ax6.set_title('N=32  T=0.5')
ax7.plot(datos2[:,0], datos2[:,1])
ax7.set_title('N=64  T=0.5')
ax8.plot(datos3[:,0], datos3[:,1])
ax8.set_title('N=128  T=0.5')


#Muestro la figura
plt.tight_layout()
plt.show()



