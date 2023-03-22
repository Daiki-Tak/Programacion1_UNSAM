# costo_camion.py
def costo_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt')
    next(f)
    costo_total=0
    for line in f:
        try:
            row = line.split(',')
            cajones=int(row[1])
            precio=float(row[2].strip('\n'))
            costo_total+=(cajones*precio)
        except:
            print('Warning: el archivo posee lineas que no pueden ser procesadas.\n La línea se salteará.')
            next(f)
    print(f'Costo total: {costo_total:.2f}')
    f.close()

costo = costo_camion('../Data/camion.csv')
costo = costo_camion('../Data/missing.csv')