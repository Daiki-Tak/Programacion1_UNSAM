# camion_commandline.py
import csv
import sys

def costo_camion(nombre_archivo):
    '''
    Esta funcion calcula el costo total del cargamento de un camion, indicando en caso de haber un error en el archivo a leer.
    --------------------------------
    Argumentos:
        nombre_archivo: Direccion absoluta de la ubicacion del archivo .csv a leer.
    Retorno:
        costo_total: string que contiene el valor final del cargamento, redondeado a 2 decimales.    
    '''
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        costo_total=0
        i=1
        for row in rows:
            try:
                cajones=int(row[1])
                precio=float(row[2])
                costo_total+=(cajones*precio)
                i+=1
            except ValueError:
                print(f'Warning: el archivo posee lineas que no pueden ser procesadas.\n La línea {i} se salteará.')
                i+=1
        return (f'{costo_total:.2f}')

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)