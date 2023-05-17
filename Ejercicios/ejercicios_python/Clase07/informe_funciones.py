# informe_funciones.py
import fileparse

def leer_camion(nombre_archivo, select = None, types = None, has_headers = True):
    camion = fileparse.parse_csv(nombre_archivo, select, types, has_headers)
    return camion

def leer_precios(nombre_archivo, select = None, types = None, has_headers = False):
    precios = dict(fileparse.parse_csv(nombre_archivo, select, types, has_headers))
    return precios    

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    precios = leer_precios(nombre_archivo_precios, types = [str, float])
    cambio=[]
    for i in range(len(camion)):
        k = camion[i]['nombre']
        cambio.append(precios[k]-camion[i]['precio'])
    informe = []
    for i,n in enumerate(camion):
        informe.append((n['nombre'], n['cajones'],n['precio'],cambio[i]))
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    f_headers = ''
    separator = ''
    a=''
    for header in headers:
        f_headers+=(f'{header:>10} ')
        separator+=(f'{a:->9}  ')
    print(f_headers,'\n',separator)
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {f"${precio:.2f}":>10s} {cambio:>10.2f}')

# informe_camion('../Data/camion.csv', '../Data/precios.csv')