# informe.py

import csv

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i,row in enumerate(rows):
            record = dict(zip(headers,row))
            try:
                lote = {'nombre': record['nombre'], 'cajones': int(record['cajones']), 'precio': float(record['precio'])}
                camion.append(lote)
            except ValueError:
                print(f'Fila {i}: No puede interpretar: {row}')
    return camion

def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precios[row[0]] = float(row[1])
            except:
                pass
    return precios

camion = leer_camion('../Data/fecha_camion.csv')
precios = leer_precios('../Data/precios.csv')

total=0.0
total_vendido=0.0
for s in camion:
    total += s['cajones']*s['precio']

for i in range(len(camion)):
    key = camion[i]['nombre']
    if key in precios:
        total_vendido += camion[i]['cajones']*precios[key]
   
balance = total_vendido - total
print(f'Total gastado: {total:.2f} | Total vendido: {total_vendido:.2f} | Balance final: {balance:.2f}')