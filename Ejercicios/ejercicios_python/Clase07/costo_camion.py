# costo_camion.py

import informe_funciones

def costo_camion(nombre_archivo):
    camion = informe_funciones.leer_camion(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    costo_total=0
    for row in camion:
        costo_total += row['cajones'] * row['precio']
    return costo_total

print(costo_camion('../Data/fecha_camion.csv'))