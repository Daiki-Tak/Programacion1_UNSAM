# ej_2_miercoles.py

import csv

#%%
# =============================================================================
# Una función leer estudiantes(archivo) que lee un archivo como el del ejemplo y que devuelve una lista de diccionarios donde las columnas del encabezado son las claves, y los valores son los datos de cada fila del csv.
# =============================================================================

def leer_estudiantes(archivo):
    '''
    Recibe un nombre de archivo, lo abre, lee fila por fila y lo va almacenando
    en una lista de diccionarios. Devuelve dicha lista.
    '''
    estudiantes=[] # Inicializo la lista vacía
    with open(archivo, mode='rt', encoding='utf-8') as f: # Abro el archivo, cierro al final del ciclo
        rows = csv.reader(f) # Cargo las filas con csv.reader
        headers = next(rows) # Cargo la primera fila en headers
        estudiantes = [{nombre: val for nombre,val in zip(headers,row)} for i, row in enumerate(rows)] 
        # Con una comprension de listas, creo un diccionario por alumno con las claves siendo lo que fue leido en headers y los valores lo leido en rows.
    return estudiantes

#%%
# =============================================================================
# Una función promediar_regulares(lista estudiantes) que toma una lista como la que genera leer_estudiantes() y devuelve una lista conteniendo sólo los diccionarios de les estudiantes que tengan condición REGULAR, junto con un nueva clave “promedio” por estudiante cuyo valor sea el promedio de sus tres notas.
# =============================================================================

def promediar_estudiantes(lista_estudiantes):
    '''
    Recibe una lista de diccionarios, lee los diccionarios para ver que alumnos 
    cumplen con la condición de 'REGULAR', calcula el promedio de sus notas, lo
    agrega a su diccionario y lo inserta en nuestra otra lista. Devuelve dicha
    lista.
    '''
    # Utilizando .keys() cargo las claves de los diccionarios en una lista.
    keys = list(lista_estudiantes[0].keys()) 
    estudiantes_regulares = [] # Inicializo mi nueva lista vacía
    for row in lista_estudiantes: # Por cada diccionario en nuestra lista_estudiantes:
        # Si el valor de la clave 3 ('condicion') es 'REGULAR', calculo el promedio y lo cargo en una nueva clave llamada 'promedio'.
        if row[keys[2]] == 'REGULAR': 
            row['promedio'] = float((int(row['nota_1']) + int(row['nota_2']) + int(row['nota_3'])) / 3)
            estudiantes_regulares.append(row) # Luego cargo el diccionario a nuestra otra lista.
    return estudiantes_regulares

#%%
# =============================================================================
# Una función imprimir notas(lista estudiantes) que toma un diccionario de notas como el que sale de (cualquiera de) las funciones anteriores e imprime en pantalla (de manera bonita) las notas de les estudiantes junto con su nombre y apellido.
# =============================================================================

def imprimir_notas(lista_estudiantes):
    '''
    Recibe una lista de diccionarios e imprime en una tabla los datos de le estudiante y sus 3 notas. 
    Acotación: La función se ve bastante desorganizada pero en esencia el
    código esta repetido de manera tal que si la lista que recibe es la de
    los estudiantes regulares, imprima sus promedios.
    '''
    # Utilizando .keys() cargo las claves de los diccionarios en una lista.
    header = list(lista_estudiantes[0].keys())
    a='' # Inicializo mi valor pivote para imprimir el separador
    if len(header) == 6:
        print(f'{header[0]:>10} {header[1]:>10} | {header[3]:^9} {header[4]:^9} {header[5]:^9}') # Imprimo el encabezado primero
        print(f' {a:->20} | {a:->28}') # Luego imprimo el separador (el número fue arbitrario, calculado a mano)
        for row in lista_estudiantes: 
        # Por cada estudiante en lista_estudiantes, imprimo sus datos.
            print(f'{row[header[0]]:>10} {row[header[1]]:>10} | {row[header[3]]:^9} {row[header[4]]:^9} {row[header[5]]:^9}')
    else: # Mismo procedimiento pero asumiendo que son los estudiantes regulares.
        print(f'{header[0]:>10} {header[1]:>10} | {header[3]:^9} {header[4]:^9} {header[5]:^9} {header[6]:^10}')
        print(f' {a:->20} | {a:->40}') 
        for row in lista_estudiantes: 
            print(f'{row[header[0]]:>10} {row[header[1]]:>10} | {row[header[3]]:^9} {row[header[4]]:^9} {row[header[5]]:^9} {row[header[6]]:^10.2f}')

#%%

archivo = 'alumnos.csv'
imprimir_notas(promediar_estudiantes(leer_estudiantes(archivo)))