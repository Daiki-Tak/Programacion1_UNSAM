# arboles.py
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

#%%
# Ejercicio 5.15: Lectura de los árboles de un parque
def leer_arboles(nombre_archivo):
    types=[float,float,int,int,int,int,int,str,str,str,str,str,str,str,str,float,float] 
    # PD: los tipos de dato los saque de la documentacion oficial.
    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        arboleda=[{nombre: func(val) for nombre, func, val in zip(headers,types,row)} for i, row in enumerate(rows)]
    return arboleda

#%%
# Ejercicio 5.16: Lista de altos de Jacarandá

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
def H(lista):
    return [arbol['altura_tot'] for arbol in lista if arbol['nombre_com'] == 'Jacarandá']

#%%
# Ejercicio 5.17: Lista de altos y diámetros de Jacarandá

def H_D(lista):
    return [(arbol['altura_tot'],arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

#%%
# Ejercicio 5.18: Diccionario con medidas

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies, arboleda):
    return {especie: [(arbol['altura_tot'],arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}

#%%
# Ejercicio 6.10: Histograma de altos de Jacarandás

nombre_archivo = os.path.join('..','Data','arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
altos = H(arboleda)
plt.hist(altos, bins=50)

#%%
# Ejercicio 6.11: Scatterplot (diámetro vs alto) de Jacarandás
# Esta linea define en pulgadas el tamaño del gráfico en una tupla (largo, alto), 
# AJUSTAR SEGUN SEA NECESARIO.
plt.rcParams["figure.figsize"] = (10,6)

def scatter_hd(lista_de_pares, especie):
    lista_de_pares = np.array(lista_de_pares)
    h=lista_de_pares[:,0]
    d=lista_de_pares[:,1]
    plt.scatter(h,d, s=10, c=np.random.random(len(lista_de_pares)), alpha=0.25) 
    #
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.xlim(0,30)
    plt.ylim(0,100)
    plt.title(f"Relación diámetro-alto para {especie}")

# Los Jacarandás parecen mantener una relacion lineal o ajustable a una cuadrática.

#%%
# Ejercicio 6.12: Scatterplot para diferentes especies

arboleda = leer_arboles(nombre_archivo)
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)
eucalipto = np.array(medidas['Eucalipto'])
P_B_R = np.array(medidas['Palo borracho rosado'])
jacaranda = np.array(medidas['Jacarandá'])

def scatter_hd_multispecies(medidas, especies):
    arrays_especies=[]
    h_per_species=[]
    d_per_species=[]
    for i, especie in enumerate(especies):
        arrays_especies.append(np.array(medidas[especie]))
        h_per_species.append(arrays_especies[i][:,0].copy())
        d_per_species.append(arrays_especies[i][:,1].copy())
    colors = ['red', 'green', 'blue']
    for i,array in enumerate(zip(h_per_species,d_per_species)):
        plt.scatter(array[0], array[1], s=10, c=colors[i], label=f'{especies[i]}', alpha=0.1)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.xlim(0,30)
    plt.ylim(0,100)
    plt.title("Relación diámetro-alto para las especies indicadas")
    plt.legend()
    
#para 2 especies:
# scatter_hd_multispecies(medidas, especies[0:2])
#para las 3:
# scatter_hd_multispecies(medidas, especies)
# honestamente ninguno de los 2 se entiende mucho pero los hice con el unico proposito de responder a la pregunta extra