# costo_camion.py

import informe_final

def costo_camion(nombre_archivo):
    camion = informe_final.leer_camion(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    costo_total=0
    for row in camion:
        costo_total += row['cajones'] * row['precio']
    return costo_total

def f_principal(parametros):
    print('Costo total:', costo_camion(parametros[1]))

if __name__ == "__main__":
    import sys
    f_principal(sys.argv)