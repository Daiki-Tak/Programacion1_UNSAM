# tabla_informe.py

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

def hacer_informe(camion, precios):
    cambio=[]
    for i in range(len(camion)):
        k = camion[i]['nombre']
        if k in precios:
            cambio.append(precios[k]-camion[i]['precio'])
    record = []
    for i,n in enumerate(camion):
        record.append((n['nombre'], n['cajones'],n['precio'],cambio[i]))
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    f_headers = ''
    separator = ''
    a=''
    for n in headers:
        f_headers+=(f'{n:>10} ')
        separator+=(f'{a:->9}  ')
    print(f_headers,'\n',separator)

    for nombre, cajones, precio, cambio in record:
        print(f'{nombre:>10s} {cajones:>10d} {f"${precio:.2f}":>10s} {cambio:>10.2f}')
    return

#%%
camion = leer_camion('../Data/fecha_camion.csv')
precios = leer_precios('../Data/precios.csv')
hacer_informe(camion, precios)

#%%
total=0.0
total_vendido=0.0
for s in camion:
    total += s['cajones']*s['precio']

for i in range(len(camion)):
    key = camion[i]['nombre']
    if key in precios:
        total_vendido += camion[i]['cajones']*precios[key]
   
balance = total_vendido - total
print(f'Total gastado: {f"${total:.2f}":10s} | Total vendido: {f"${total_vendido:.2f}":10s} | Balance final: {f"${balance:.2f}":10s}')
