import numpy as np
import random
from numba import set_num_threads
from numba import jit
set_num_threads(4)



####################################################################
####################################################################


#Función que intercambia la posición de dos elementos de una matriz
@jit(nopython=True)
def intercambio(S, N, m, n, pos):
    #pos es un número entero entre 0 y 3
    #0 arriba, 1 abajo, 2 derecha, 3 izquierda
    
    aux = S[m,n]
    
    if pos==0: #Arriba
        S[m,n]=S[(m-1)%N,n]
        S[(m-1)%N,n]=aux
    if pos==1: #Abajo
        S[m,n]=S[(m+1)%N,n]
        S[(m+1)%N,n]=aux
    if pos==2: #Izquierda
        S[m,n]=S[m,(n-1)%N]
        S[m,(n-1)%N]=aux
    if pos==3: #Derecha
        S[m,n]=S[m,(n+1)%N]
        S[m,(n+1)%N]=aux        
    return S


####################################################################
####################################################################


#Función que calcula la energía de la matriz
@jit(nopython=True)
def energia(S, N):
    
    E = 0.0
    for i in range(1, N-1, 1): #No tengo en cuenta la primera y la última fila
        for j in range(N):                
            E = E - 0.5*S[i,j]*(S[(i+1)%N,j] + S[i,(j+1)%N] + S[(i-1)%N,j] + S[i,(j-1)%N])
      
    return E


####################################################################
####################################################################


# Defino parámetros iniciales
N = 64  # Tamaño de la matriz
l = (N*N)*10**5  # Número de iteraciones
T = 2.0  # Temperatura


#Rellenamos la matriz con 1 y -1 de forma aleatoria, 
#de manera que la magnetización inicial sea nula 
#while True:
    #S = 2*np.random.randint(2, size=(N, N)) - 1
    #S[0, :] = -1  # Fijamos la primera fila con espines negativos
    #S[N-1, :] = 1  # Fijamos la última fila con espines positivos
    #if np.sum(S)==0:
        #break


#Para comenzar con una magnetización no nula:
S = 2*np.random.randint(2, size=(N, N)) - 1
S[0, :] = -1  # Fijamos la primera fila con espines negativos
S[N-1, :] = 1  # Fijamos la última fila con espines positivos


####################################################################
####################################################################


#Calculo la energía de la configuración inicial
E1 = energia(S, N)

for k in range(l):
                  
    #Escojo una posición aleatoria de la matriz
    m = np.random.randint(1, N-1) #No elijo ni la primera ni la última fila
    n = np.random.randint(0, N)
                
    #Escojo aleatoriamente una posición adyacente
    if m == 1: #si estamos en la segunda fila no tenemos en cuenta la posición de arriba
        pos = random.choice([1,2,3])
    elif m == (N-2): #si estamos en la penúltima fila no tenemos en cuenta la posición de abajo
        pos = random.choice([0,2,3])
    else:    
        pos = random.choice([0,1,2,3])
        
    #Intercambio las posiciones
    intercambio(S, N, m, n, pos)
        
    #Calculo la energía de la nueva configuración
    E2 = energia(S, N)
        
    #Calculo la variación de energía
    AE = E2-E1
        
    #Llevo a cabo el cambio si se cumple:
    if (AE<0) or (random.random()<np.exp(-AE/T)):
        E1 = E2
    #Si no se cumple, revierto el cambio   
    else:
        intercambio(S, N, m, n, pos)   



#Guardo la matriz de la configuración final 

#Con Joel
np.savetxt('/home/cphys-ana.sanchezgonzalez/COMPU2024/matriz_N64_T2_noNul.txt', S)

#Con el PC
#np.savetxt('C:/Users/Usuario/Desktop/UGR/COMPU/Kawasaki/resultados/matriz_N16_T05.txt', S)