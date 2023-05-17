# ej_3_miercoles.py

import csv
import sys

#%%

def leer_estudiantes(archivo):
    estudiantes=[]
    with open(archivo, mode='rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        estudiantes = [{nombre: val for nombre,val in zip(headers,row)} for i, row in enumerate(rows)]
    return estudiantes

#%%

def promediar_estudiantes(lista_estudiantes):
    keys = list(lista_estudiantes[0].keys())
    estudiantes_regulares = []
    for row in lista_estudiantes:
        if row[keys[2]] == 'REGULAR':
            row['promedio'] = (int(row['nota_1']) + int(row['nota_2']) + int(row['nota_3'])) / 3
            estudiantes_regulares.append(row)
    return estudiantes_regulares

#%%

def imprimir_notas(lista_estudiantes):
    header = list(lista_estudiantes[0].keys())
    a=''
    if len(header) == 6:
        print(f'{header[0]:>10} {header[1]:>10} | {header[3]:^9} {header[4]:^9} {header[5]:^9}')
        print(f' {a:->20} | {a:->28}')
        for row in lista_estudiantes:
            print(f'{row[header[0]]:>10} {row[header[1]]:>10} | {row[header[3]]:^9} {row[header[4]]:^9} {row[header[5]]:^9}')
    else:
        print(f'{header[0]:>10} {header[1]:>10} | {header[3]:^9} {header[4]:^9} {header[5]:^9} {header[6]:^10}')
        print(f' {a:->20} | {a:->40}') 
        for row in lista_estudiantes: 
            print(f'{row[header[0]]:>10} {row[header[1]]:>10} | {row[header[3]]:^9} {row[header[4]]:^9} {row[header[5]]:^9} {row[header[6]]:^10.2f}')

#%%

if len(sys.argv) == 2:
    archivo = sys.argv[1]
else:
    archivo = 'alumnos.csv'

imprimir_notas(leer_estudiantes(archivo))