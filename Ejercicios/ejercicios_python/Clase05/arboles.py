# arboles.py
import csv

#%%
# Ejercicio 5.15: Lectura de los árboles de un parque
def leer_arboles(nombre_archivo):
    types=[float,float,int,int,int,int,int,str,str,str,str,str,str,str,str,float,float]
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        arboleda=[{nombre: func(val) for nombre, func, val in zip(headers,types,row)} for i, row in enumerate(rows)]
    return arboleda

#%%
# Ejercicio 5.16: Lista de altos de Jacarandá

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
H = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

#%%
# Ejercicio 5.17: Lista de altos y diámetros de Jacarandá

H_D= [(arbol['altura_tot'],arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

#%%
# Ejercicio 5.18: Diccionario con medidas

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies, arboleda):
    return {especie: [(arbol['altura_tot'],arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
