# costo_camion.py

import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    costo_total=0
    for row in rows:
        try:
            print(row)
            cajones=int(row[1])
            precio=float(row[2])
            costo_total+=(cajones*precio)
        except ValueError:
            print('Warning: el archivo posee lineas que no pueden ser procesadas.\n La línea se salteará.')
    print(f'Costo total: {costo_total:.2f}')
    f.close()

costo_camion('../Data/camion.csv')
costo_camion('../Data/missing.csv')