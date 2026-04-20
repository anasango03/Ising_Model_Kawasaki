import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


#Función para leer la matriz desde un archivo de texto
def leer_matriz_desde_txt(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    matriz = [list(map(float, linea.strip().split())) for linea in lineas]
    return np.array(matriz)


#Leo la matriz desde el archivo de texto
ruta_archivo = 'C:/Users/Usuario/Desktop/UGR/COMPU/Kawasaki/resultados/matriz_N64_T4_noNul.txt'
matriz = leer_matriz_desde_txt(ruta_archivo)


#Mapa de colores
#Azul para -1 y rojo para 1
cmap = mcolors.ListedColormap(['blue', 'red'])  


#Creo la figura 
fig, ax = plt.subplots()

cax = ax.matshow(matriz, cmap=cmap)

ax.set_xticks([])
ax.set_yticks([])

ax.axis('off')


# Muestro la imagen
plt.show()
