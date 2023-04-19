# arboles.py
import csv
from collections import Counter

#%%
# Ejercicio 4.13: Lectura de los árboles de un parque
def leer_parque(nombre_archivo, parque):
    arboles=[]
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i,row in enumerate(rows):
            record = dict(zip(headers,row))
            if record["espacio_ve"]==parque:
                altura=float(record['altura_tot'])
                record['altura_tot']=altura
                arboles.append(record)
    return arboles

# arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', "GENERAL PAZ")
#%%
# Ejercicio 4.14: Determinar las especies en un parque

def especies(lista_arboles):
    especies_total=[]
    for i,n in enumerate(lista_arboles):
        especie = lista_arboles[i]['nombre_com']
        especies_total.append(especie)
    unicos = set(especies_total)
    return unicos

# lista_de_especies = especies(arboles)

#%%
# Ejercicio 4.15: Contar ejemplares por especie

def contar_ejemplares(lista_arboles):
    contador = Counter()
    for a in lista_arboles:
        contador[a['nombre_com']] += 1
    return contador

# ejemplares1 = contar_ejemplares(leer_parque('../Data/arbolado-en-espacios-verdes.csv', "GENERAL PAZ"))
# ejemplares1.most_common(5)
# ejemplares2 = contar_ejemplares(leer_parque('../Data/arbolado-en-espacios-verdes.csv', "ANDES, LOS"))
# ejemplares2.most_common(5)
# ejemplares3 = contar_ejemplares(leer_parque('../Data/arbolado-en-espacios-verdes.csv', "CENTENARIO"))
# ejemplares3.most_common(5)

#%%
# Ejercicio 4.16: Alturas de una especie en una lista

def obtener_alturas(lista_arboles, especie):
    alturas=[]
    for i,n in enumerate(lista_arboles):
        if lista_arboles[i]['nombre_com'] == especie:
            alturas.append(lista_arboles[i]['altura_tot'])
    return alturas

def altura_promedio_y_max(lista_alturas):
    altura_acumulada=0
    altura_max=0
    for i,n in enumerate(lista_alturas):
        if lista_alturas[i] > altura_max:
            altura_max=lista_alturas[i]
        altura_acumulada+=lista_alturas[i]
    altura_promedio=round(altura_acumulada/len(lista_alturas),2)
    return (altura_max,altura_promedio)

# alturas1 = altura_promedio_y_max(obtener_alturas(leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ'),'Jacarandá'))
# alturas2 = altura_promedio_y_max(obtener_alturas(leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS'),'Jacarandá'))
# alturas3 = altura_promedio_y_max(obtener_alturas(leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO'),'Jacarandá'))

#%%
# Ejercicio 4.17: Inclinaciones por especie de una lista

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones=[]
    for i,n in enumerate(lista_arboles):
        if lista_arboles[i]['nombre_com'] == especie:
            inclinaciones.append(int(lista_arboles[i]['inclinacio']))
    return inclinaciones

# inclinacion = obtener_inclinaciones(leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ'), 'Jacarandá')

#%%
# Ejercicio 4.18: Especie con el ejemplar más inclinado

def especimen_mas_inclinado(lista_arboles):
    lista_especies = especies(lista_arboles)
    especie_mas_inclinada= ''
    parque = lista_arboles[1]['espacio_ve']
    inclinacion_especie_max=0
    for especie in lista_especies:
        inclinacion_especie = obtener_inclinaciones(lista_arboles,especie)
        for i,n in enumerate(inclinacion_especie):
            if inclinacion_especie[i] > inclinacion_especie_max:
                inclinacion_especie_max=inclinacion_especie[i]
                especie_mas_inclinada=especie
    return (f'El espécimen más inclinado del parque {parque} es: {especie_mas_inclinada}, con una inclinación de {inclinacion_especie_max} grados.')

especimen_mas_inclinado(leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ'))
especimen_mas_inclinado(leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS'))
especimen_mas_inclinado(leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO'))

#%%
# Ejercicio 4.19: Especie más inclinada en promedio

def especimen_promedio_mas_inclinado(lista_arboles):
    lista_especies = especies(lista_arboles)
    especie_promedio_mas_inclinada= ''
    parque = lista_arboles[1]['espacio_ve']
    inclinacion_promedio_especie_max=0
    for especie in lista_especies:
        if especie == 'No Determinable' or especie == 'No Determinado':
            continue
        inclinacion_promedio=0
        inclinacion_especie = obtener_inclinaciones(lista_arboles,especie)
        for i,n in enumerate(inclinacion_especie):
            inclinacion_promedio+=inclinacion_especie[i]
        inclinacion_promedio=inclinacion_promedio/len(inclinacion_especie)
        if inclinacion_promedio > inclinacion_promedio_especie_max:
            inclinacion_promedio_especie_max=int(round(inclinacion_promedio))
            especie_promedio_mas_inclinada=especie
    return (f'El espécimen más inclinado en promedio del parque {parque} es: {especie_promedio_mas_inclinada}, con una inclinación de {inclinacion_promedio_especie_max} grados.')

especimen_promedio_mas_inclinado(leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ'))
# especimen_promedio_mas_inclinado(leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS'))
# especimen_promedio_mas_inclinado(leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO'))

#%%
# Ejercicio 4.19 EXTRAS: Especie más inclinada de la ciudad

def leer_arbolado(nombre_archivo):
    arboles=[]
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i,row in enumerate(rows):
            record = dict(zip(headers,row))
            arboles.append(record)
    return arboles

def altura_max(lista_alturas):
    altura_max=0
    for i,n in enumerate(lista_alturas):
        if lista_alturas[i] > altura_max:
            altura_max=lista_alturas[i]
    return altura_max

def especimen_mas_inclinado(lista_arboles):
    lista_especies = especies(lista_arboles)
    especie_mas_inclinada= ''
    inclinacion_especie_max=0
    for especie in lista_especies:
        inclinacion_especie = obtener_inclinaciones(lista_arboles,especie)
        for i,n in enumerate(inclinacion_especie):
            if inclinacion_especie[i] > inclinacion_especie_max:
                inclinacion_especie_max=inclinacion_especie[i]
                especie_mas_inclinada=especie
    coords=()
    for i,n in enumerate(lista_arboles):
        if lista_arboles[i]['nombre_com'] == especie_mas_inclinada:
            coords=(lista_arboles[i]['lat'], lista_arboles[i]['long'])
    return (f'El espécimen más inclinado de la ciudad es: {especie_mas_inclinada}, con una inclinación de {inclinacion_especie_max} grados, y se encuentra en las coordenadas {coords}')

especimen_mas_inclinado(leer_arbolado('../Data/arbolado-en-espacios-verdes.csv'))

#%%
# Ejercicio 4.19 EXTRAS: Especie más alta de la ciudad